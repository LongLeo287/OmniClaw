---
id: pixl-server-storage-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:30:59.333439
---

# KNOWLEDGE EXTRACT: pixl-server-storage
> **Extracted on:** 2026-03-30 13:15:55
> **Source:** pixl-server-storage

---

## File: `.npmignore`
```
.gitignore
node_modules/
work/
*.log
```

## File: `hash.js`
```javascript
// PixlServer Storage System - Hash Mixin
// Copyright (c) 2016 Joseph Huckaby
// Released under the MIT License

var util = require("util");
var async = require('async');
var Class = require("pixl-class");
var Tools = require("pixl-tools");

module.exports = Class.create({
	
	hashCreate: function(path, opts, callback) {
		// Create new hash table
		var self = this;
		
		if (!opts) opts = {};
		if (!opts.page_size) opts.page_size = this.hashItemsPerPage;
		opts.length = 0;
		opts.type = 'hash';
		
		this.logDebug(9, "Creating new hash: " + path, opts);
		
		this.get(path, function(err, hash) {
			if (hash) {
				// hash already exists
				self.logDebug(9, "Hash already exists: " + path, hash);
				return callback(null, hash);
			}
			self.put( path, opts, function(err) {
				if (err) return callback(err);
				
				// create first page
				self.put( path + '/data', { type: 'hash_page', length: 0, items: {} }, function(err) {
					if (err) return callback(err);
					else callback(null, opts);
				} ); // put
			} ); // header created
		} ); // get check
	},
	
	_hashLoad: function(path, create_opts, callback) {
		// Internal method, load hash root, possibly create if doesn't exist
		var self = this;
		if (create_opts && (typeof(create_opts) != 'object')) create_opts = {};
		this.logDebug(9, "Loading hash: " + path);
		
		this.get(path, function(err, hash) {
			if (hash) {
				// hash already exists
				callback(null, hash);
			}
			else if (create_opts && err && (err.code == "NoSuchKey")) {
				// create new hash, ONLY if record was not found (and not some other error)
				self.logDebug(9, "Hash not found, creating it: " + path);
				self.hashCreate(path, create_opts, function(err, hash) {
					if (err) callback(err);
					else callback( null, hash );
				} );
			}
			else {
				// no exist and no create, or some other error
				self.logDebug(9, "Hash could not be loaded: " + path + ": " + err);
				callback(err);
			}
		} ); // get
	},
	
	_hashLock: function(key, wait, callback) {
		// internal hash lock wrapper
		// uses unique key prefix so won't deadlock with user locks
		this.lock( '|'+key, wait, callback );
	},
	
	_hashUnlock: function(key) {
		// internal hash unlock wrapper
		this.unlock( '|'+key );
	},
	
	_hashShareLock: function(key, wait, callback) {
		// internal hash shared lock wrapper
		// uses unique key prefix so won't deadlock with user locks
		this.shareLock( 'C|'+key, wait, callback );
	},
	
	_hashShareUnlock: function(key) {
		// internal hash shared unlock wrapper
		this.shareUnlock( 'C|'+key );
	},
	
	hashPut: function(path, hkey, hvalue, create_opts, callback) {
		// store key/value pair into hash table
		var self = this;
		if (!callback && (typeof(create_opts) == 'function')) {
			callback = create_opts;
			create_opts = {};
		}
		if (!path) return callback(new Error("Hash path must be a valid string."));
		if (!hkey) return callback(new Error("Hash key must be a valid string."));
		if (typeof(hvalue) == 'undefined') return callback(new Error("Hash value must not be undefined."));
		
		this.logDebug(9, "Storing hash key: " + path + ": " + hkey, this.debugLevel(10) ? hvalue : null);
		
		// lock hash for this
		this._hashLock(path, true, function() {
			
			// load header
			self._hashLoad(path, create_opts, function(err, hash) {
				if (err) {
					self._hashUnlock(path);
					return callback(err);
				}
				
				var state = {
					path: path,
					data_path: path + '/data',
					hkey: ''+hkey,
					hvalue: hvalue,
					hash: hash,
					index_depth: -1,
					key_digest: Tools.digestHex(hkey, 'md5')
				};
				
				self._hashPutKey(state, function(err) {
					// done
					self._hashUnlock(path);
					return callback(err);
				}); // _hashPutKey
			}); // load
		}); // lock
	},
	
	_hashPutKey: function(state, callback) {
		// internal hash put method, store at one hashing level
		// recurse for deeper indexes
		var self = this;
		
		self.get(state.data_path, function(err, data) {
			if (err) data = { type: 'hash_page', length: 0, items: {} };
			
			if (data.type == 'hash_index') {
				// recurse for deeper level
				state.index_depth++;
				state.data_path += '/' + state.key_digest.substring(state.index_depth, state.index_depth + 1);
				return self._hashPutKey(state, callback);
			}
			else {
				// got page, store at this level
				var new_key = false;
				data.items = Tools.copyHashRemoveProto( data.items );
				
				if (!(state.hkey in data.items)) {
					data.length++;
					state.hash.length++;
					new_key = true;
				}
				
				data.items[state.hkey] = state.hvalue;
				
				var finish = function(err) {
					if (err) return callback(err);
					
					if (data.length > state.hash.page_size) {
						// enqueue page reindex task
						self.logDebug(9, "Hash page has grown beyond max keys, running index split: " + state.data_path, {
							num_keys: data.length,
							page_size: state.hash.page_size
						});
						self._hashSplitIndex(state, callback);
					} // reindex
					else {
						// no reindex needed
						callback();
					}
				}; // finish
				
				// save page and possibly hash header
				self.put(state.data_path, data, function(err) {
					if (err) return callback(err);
					
					if (new_key) self.put(state.path, state.hash, finish);
					else finish();
				}); // put
			} // hash_page
		}); // get
	},
	
	_hashSplitIndex: function(state, callback) {
		// hash split index
		// split hash level into 16 new index buckets
		var self = this;
		state.index_depth++;
		
		this.logDebug(9, "Splitting hash data into new index: " + state.data_path + " (" + state.index_depth + ")");
		
		// load data page which will be converted to a hash index
		self.get(state.data_path, function(err, data) {
			// check for error or if someone stepped on our toes
			if (err) {
				// normal, hash may have been deleted
				self.logError('hash', "Failed to fetch data record for hash split: " + state.data_path + ": " + err);
				return callback();
			}
			if (data.type == 'hash_index') {
				// normal, hash may already have been indexed
				self.logDebug(9, "Data page has been reindexed already, skipping: " + state.data_path, data);
				return callback();
			}
			
			// rehash keys at new index depth
			var pages = {};
			data.items = Tools.copyHashRemoveProto( data.items );
			
			for (var hkey in data.items) {
				var key_digest = Tools.digestHex(hkey, 'md5');
				var ch = key_digest.substring(state.index_depth, state.index_depth + 1);
				
				if (!pages[ch]) pages[ch] = { type: 'hash_page', length: 0, items: {} };
				pages[ch].items[hkey] = data.items[hkey];
				pages[ch].length++;
				
				// Note: In the very rare case where a subpage also overflows,
				// the next hashPut will take care of the nested reindex.
			} // foreach key
			
			// save all pages in parallel, then rewrite data page as an index
			async.forEachOfLimit(pages, self.concurrency, 
				function (page, ch, callback) {
					self.put( state.data_path + '/' + ch, page, callback );
				},
				function(err) {
					if (err) {
						return callback( new Error("Failed to write data records for hash split: " + state.data_path + "/*: " + err.message) );
					}
					
					// final conversion of original data path
					self.put( state.data_path, { type: 'hash_index' }, function(err) {
						if (err) {
							return callback( new Error("Failed to write data record for hash split: " + state.data_path + ": " + err.message) );
						}
						
						self.logDebug(9, "Hash split complete: " + state.data_path);
						callback();
					}); // final put
				} // complete
			); // forEachOf
		}); // get
	},
	
	hashPutMulti: function(path, records, create_opts, callback) {
		// put multiple hash records at once, given object of keys and values
		// need concurrency limit of 1 because hashPut locks
		var self = this;
		if (!callback && (typeof(create_opts) == 'function')) {
			callback = create_opts;
			create_opts = {};
		}
		
		async.eachLimit(Object.keys(records), 1, 
			function(hkey, callback) {
				// iterator for each key
				self.hashPut(path, hkey, records[hkey], create_opts, function(err) {
					callback(err);
				} );
			}, 
			function(err) {
				// all keys stored
				callback(err);
			}
		);
	},
	
	hashGet: function(path, hkey, callback) {
		// fetch key/value pair from hash table
		var self = this;
		var state = {
			path: path,
			data_path: path + '/data',
			hkey: hkey,
			index_depth: -1,
			key_digest: Tools.digestHex(hkey, 'md5')
		};
		this.logDebug(9, "Fetching hash key: " + path + ": " + hkey);
		
		this._hashShareLock(path, true, function() {
			// share locked
			self._hashGetKey(state, function(err, value) {
				// done
				self._hashShareUnlock(path);
				callback(err, value);
			}); // _hashGetKey
		} ); // _hashShareLock
	},
	
	_hashGetKey: function(state, callback) {
		// internal hash get method, fetch at one hashing level
		// recurse for deeper indexes
		var self = this;
		
		self.get(state.data_path, function(err, data) {
			if (err) return callback(err);
			
			if (data.type == 'hash_index') {
				// recurse for deeper level
				state.index_depth++;
				state.data_path += '/' + state.key_digest.substring(state.index_depth, state.index_depth + 1);
				return self._hashGetKey(state, callback);
			}
			else {
				// got page, fetch at this level
				data.items = Tools.copyHashRemoveProto( data.items );
				
				if (!(state.hkey in data.items)) {
					// key not found
					var err = new Error("Failed to fetch hash key: " + state.path + ": " + state.hkey + ": Not found");
					err.code = "NoSuchKey";
					return callback(err);
				}
				
				callback(null, data.items[state.hkey]);
			} // hash_page
		}); // get
	},
	
	hashGetMulti: function(path, hkeys, callback) {
		// fetch multiple hash records at once, given array of keys
		// callback is provided an array of values in matching order to keys
		var self = this;
		var records = Object.create(null);
		
		async.eachLimit(hkeys, this.concurrency, 
			function(hkey, callback) {
				// iterator for each key
				self.hashGet(path, hkey, function(err, value) {
					if (err) return callback(err);
					records[hkey] = value;
					callback();
				} );
			}, 
			function(err) {
				if (err) return callback(err);
				
				// sort records into array of values ordered by keys
				var values = [];
				for (var idx = 0, len = hkeys.length; idx < len; idx++) {
					values.push( records[hkeys[idx]] );
				}
				
				callback(null, values);
			}
		);
	},
	
	hashUpdate: function(path, hkey, updates, callback) {
		// update existing key/value pair in hash table
		var self = this;
		if (!path) return callback(new Error("Hash path must be a valid string."));
		if (!hkey) return callback(new Error("Hash key must be a valid string."));
		if (!Tools.isaHash(updates)) return callback(new Error("Hash updates must be an object."));
		
		this.logDebug(9, "Updating hash key: " + path + ": " + hkey, this.debugLevel(10) ? updates : null);
		
		// lock hash for this
		this._hashLock(path, true, function() {
			
			// load header, do not create new
			self._hashLoad(path, false, function(err, hash) {
				if (err) {
					self._hashUnlock(path);
					return callback(err);
				}
				
				var state = {
					path: path,
					data_path: path + '/data',
					hkey: ''+hkey,
					updates: updates,
					hash: hash,
					index_depth: -1,
					key_digest: Tools.digestHex(hkey, 'md5')
				};
				
				self._hashUpdateKey(state, function(err) {
					// done
					self._hashUnlock(path);
					return callback(err);
				}); // _hashPutKey
			}); // load
		}); // lock
	},
	
	_hashUpdateKey: function(state, callback) {
		// internal hash update method, store at one hashing level
		// recurse for deeper indexes
		var self = this;
		
		self.get(state.data_path, function(err, data) {
			if (err) data = { type: 'hash_page', length: 0, items: {} };
			
			if (data.type == 'hash_index') {
				// recurse for deeper level
				state.index_depth++;
				state.data_path += '/' + state.key_digest.substring(state.index_depth, state.index_depth + 1);
				return self._hashUpdateKey(state, callback);
			}
			else {
				// got page, our key should be at this level
				data.items = Tools.copyHashRemoveProto( data.items );
				
				if (!(state.hkey in data.items)) {
					// key not found
					var err = new Error("Failed to fetch hash key: " + state.path + ": " + state.hkey + ": Not found");
					err.code = "NoSuchKey";
					return callback(err);
				}
				
				var hvalue = data.items[state.hkey];
				
				// apply updates directly to forehead
				for (var key in state.updates) {
					Tools.setPath( hvalue, key, state.updates[key] );
				}
				
				// save page
				self.put(state.data_path, data, callback);
			} // hash_page
		}); // get
	},
	
	hashUpdateMulti: function(path, records, callback) {
		// update multiple hash records at once, given object of keys and values
		// need concurrency limit of 1 because hashUpdate locks
		var self = this;
		
		async.eachLimit(Object.keys(records), 1, 
			function(hkey, callback) {
				// iterator for each key
				self.hashUpdate(path, hkey, records[hkey], function(err) {
					callback(err);
				} );
			}, 
			function(err) {
				// all keys updated
				callback(err);
			}
		);
	},
	
	hashEachPage: function(path, iterator, callback) {
		// call user iterator for each populated hash page, data only
		// iterator will be passed page items hash object
		var self = this;
		
		this._hashShareLock(path, true, function() {
			// share locked
			self._hashEachPage(path + '/data', 
				function(data, callback) {
					if ((data.type == 'hash_page') && (data.length > 0)) {
						data.items = Tools.copyHashRemoveProto( data.items );
						iterator(data.items, callback);
					}
					else callback();
				}, 
				function(err) {
					self._hashShareUnlock(path);
					callback(err);
				}
			); // _hashEachPage
		} ); // _hashShareLock
	},
	
	_hashEachPage: function(data_path, iterator, callback) {
		// internal method for iterating over hash pages
		// invokes interator for both index and data pages
		var self = this;
		
		self.get(data_path, function(err, data) {
			if (err) return callback(); // normal, page may not exist
			data.path = data_path;
			
			iterator(data, function(err) {
				if (err) return callback(err); // abnormal
				
				if (data.type == 'hash_index') {
					// recurse for deeper level
					async.eachSeries( [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f'],
						function(ch, callback) {
							self._hashEachPage( data_path + '/' + ch, iterator, callback );
						},
						callback
					);
				}
				else callback();
			}); // complete
		}); // get
	},
	
	hashGetAll: function(path, callback) {
		// return ALL keys/values as a single, in-memory hash
		var self = this;
		var everything = Object.create(null);
		
		this._hashShareLock(path, true, function() {
			// share locked
			self._hashEachPage( path + '/data',
				function(page, callback) {
					// called for each hash page (index or data)
					if (page.type == 'hash_page') {
						page.items = Tools.copyHashRemoveProto( page.items );
						Tools.mergeHashInto( everything, page.items );
					}
					callback();
				},
				function(err) {
					self._hashShareUnlock(path);
					callback(err, err ? null : everything);
				} // done
			); // _hashEachPage
		} ); // _hashShareLock
	},
	
	hashEach: function(path, iterator, callback) {
		// iterate over hash and invoke function for every key/value
		// iterator function is asynchronous (callback), like async.forEachOfSeries
		var self = this;
		
		this._hashShareLock(path, true, function() {
			// share locked
			self._hashEachPage( path + '/data',
				function(page, callback) {
					// called for each hash page (index or data)
					if (page.type == 'hash_page') {
						page.items = Tools.copyHashRemoveProto( page.items );
						async.forEachOfSeries( page.items,
							function(hvalue, hkey, callback) {
								// swap places of hkey,hvalue in iterator args because I HATE how async does it
								iterator(hkey, hvalue, callback);
							},
							callback
						); // forEachOfSeries
					} // hash_page
					else callback();
				}, // page
				function(err) {
					self._hashShareUnlock(path);
					callback(err);
				}
			); // _hashEachPage
		} ); // _hashShareLock
	},
	
	hashEachSync: function(path, iterator, callback) {
		// iterate over hash and invoke function for every key/value
		// iterator function is synchronous (no callback), like Array.forEach()
		var self = this;
		
		this._hashShareLock(path, true, function() {
			// share locked
			self._hashEachPage( path + '/data',
				function(page, callback) {
					// called for each hash page (index or data)
					if (page.type == 'hash_page') {
						page.items = Tools.copyHashRemoveProto( page.items );
						for (var hkey in page.items) {
							if (iterator( hkey, page.items[hkey] ) === false) {
								// user abort
								return callback( new Error("User Abort") );
							}
						}
					} // hash_page
					callback();
				}, // page
				function(err) {
					self._hashShareUnlock(path);
					callback(err);
				}
			); // _hashEachPage
		} ); // _hashShareLock
	},
	
	hashCopy: function(old_path, new_path, callback) {
		// copy entire hash to new location
		var self = this;
		this.logDebug(9, "Copying hash: " + old_path + " to " + new_path);
		
		this._hashLock( new_path, true, function() {
			// copy header
			self.copy( old_path, new_path, function(err) {
				if (err) {
					self._hashUnlock(new_path);
					return callback(err);
				}
				
				// iterate over each page
				self._hashEachPage( old_path + '/data',
					function(page, callback) {
						// called for each hash page (index or data)
						var new_page_path = page.path.replace( old_path, new_path );
						
						// copy page
						self.copy(page.path, new_page_path, callback);
					}, // page
					function(err) {
						// all pages copied
						self._hashUnlock(new_path);
						callback(err);
					}
				); // _hashEachPage
			} ); // copy header
		}); // lock
	},
	
	hashRename: function(old_path, new_path, callback) {
		// Copy, then delete hash (and all keys)
		var self = this;
		this.logDebug(9, "Renaming hash: " + old_path + " to " + new_path);
		
		this.hashCopy( old_path, new_path, function(err) {
			// copy complete, now delete old hash
			if (err) return callback(err);
			
			self.hashDeleteAll( old_path, true, callback );
		} ); // copied
	},
	
	hashDeleteAll: function(path, entire, callback) {
		// delete entire hash
		var self = this;
		
		// support 2-arg calling convention (no entire)
		if (!callback && (typeof(entire) == 'function')) {
			callback = entire;
			entire = false;
		}
		
		this.logDebug(9, "Deleting hash: " + path);
		
		this._hashLock( path, true, function() {
			// load header
			self._hashLoad(path, false, function(err, hash) {
				if (err) {
					self._hashUnlock(path);
					return callback(err);
				}
				
				// iterate over each page
				self._hashEachPage( path + '/data',
					function(page, callback) {
						// called for each hash page (index or data)
						self.delete(page.path, callback);
					}, // page
					function(err) {
						// all pages deleted
						if (err) {
							self._hashUnlock(path);
							return callback(err);
						}
						
						if (entire) {
							// delete hash header as well
							self.delete( path, function(err) {
								self._hashUnlock(path);
								callback(err);
							} ); // delete
						}
						else {
							// reset hash for future use
							hash.length = 0;
							self.put( path, hash, function(err) {
								self._hashUnlock(path);
								callback(err);
							} ); // put
						}
					} // complete
				); // _hashEachPage
			}); // _hashLoad
		}); // lock
	},
	
	hashDelete: function(path, hkey, entire, callback) {
		// delete single key from hash
		var self = this;
		
		// support 3-arg calling convention (no entire)
		if (!callback && (typeof(entire) == 'function')) {
			callback = entire;
			entire = false;
		}
		
		this.logDebug(9, "Deleting hash key: " + path + ": " + hkey);
		
		// lock hash for this
		this._hashLock(path, true, function() {
			
			// load header
			self._hashLoad(path, false, function(err, hash) {
				if (err) {
					self._hashUnlock(path);
					return callback(err);
				}
				
				var state = {
					path: path,
					data_path: path + '/data',
					hkey: hkey,
					hash: hash,
					index_depth: -1,
					key_digest: Tools.digestHex(hkey, 'md5'),
					entire: entire
				};
				
				self._hashDeleteKey(state, function(err) {
					// done
					self._hashUnlock(path);
					return callback(err);
				}); // _hashDeleteKey
			}); // load
		}); // lock
	},
	
	_hashDeleteKey: function(state, callback) {
		// internal hash delete method, delete from one hashing level
		// recurse for deeper indexes
		var self = this;
		
		self.get(state.data_path, function(err, data) {
			if (err) return callback(err);
			
			if (data.type == 'hash_index') {
				// recurse for deeper level
				state.index_depth++;
				state.data_path += '/' + state.key_digest.substring(state.index_depth, state.index_depth + 1);
				return self._hashDeleteKey(state, callback);
			}
			else {
				// got page, delete from this level
				data.items = Tools.copyHashRemoveProto( data.items );
				
				if (!(state.hkey in data.items)) {
					var err = new Error("Failed to delete hash key: " + state.path + ": " + state.hkey + ": Not found");
					err.code = 'NoSuchKey';
					self.logError('hash', err.message);
					return callback(err);
				}
				
				data.length--;
				state.hash.length--;
				
				delete data.items[state.hkey];
				
				// check for delete entire on empty
				if (!state.hash.length && state.entire) {
					self.delete(state.data_path, function(err) {
						if (err) return callback(err);
						self.delete(state.path, callback);
					}); // put
					return;
				}
				
				// save page and hash header
				self.put(state.data_path, data, function(err) {
					if (err) return callback(err);
					
					self.put(state.path, state.hash, function(err) {
						if (err) return callback(err);
						
						// index unsplit time?
						if (!data.length && (state.index_depth > -1)) {
							// index unsplit task
							self.logDebug(9, "Hash page has no more keys, running unsplit check: " + state.data_path);
							self._hashUnsplitIndexCheck(state, callback);
						} // unsplit
						else {
							// no unsplit check needed
							callback();
						}
						
					}); // put
				}); // put
			} // hash_page
		}); // get
	},
	
	_hashUnsplitIndexCheck: function(state, callback) {
		// unsplit hash index
		// check if all sub-pages are empty, and if so, delete all and convert index back into page
		var self = this;
		var data_path = state.data_path.replace(/\/\w+$/, '');
		var found_keys = false;
		var sub_pages = [];
		
		this.logDebug(9, "Checking all hash index sub-pages for unsplit: " + data_path + "/*");
		
		// make sure page is still an index
		self.get(data_path, function(err, data) {
			if (err) {
				self.logDebug(9, "Hash page could not be loaded, aborting unsplit: " + data_path);
				return callback();
			}
			
			if (data.type != 'hash_index') {
				self.logDebug(9, "Hash page is no longer an index, aborting unsplit: " + data_path);
				return callback();
			}
			
			// test each sub-page, counting keys
			// abort on first key (i.e. no need to load all pages in that case)
			async.eachLimit( [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f'], self.concurrency,
				function(ch, callback) {
					self.get( data_path + '/' + ch, function(err, data) {
						if (data) sub_pages.push( ch );
						if (data && ((data.type != 'hash_page') || data.length)) {
							self.logDebug(9, "Index page still has keys: " + data_path + '/' + ch);
							found_keys = true;
							callback( new Error("ABORT") );
						}
						else callback();
					} );
				},
				function(err) {
					// scanned all pages
					if (found_keys || !sub_pages.length) {
						// nothing to be done
						self.logDebug(9, "Nothing to do, aborting unsplit: " + data_path);
						return callback();
					}
					
					self.logDebug(9, "Proceeding with unsplit: " + data_path);
					
					// proceed with unsplit
					async.eachLimit( sub_pages, self.concurrency,
						function(ch, callback) {
							self.delete( data_path + '/' + ch, callback );
						},
						function(err) {
							// all pages deleted, now rewrite index
							if (err) {
								// this should never happen, but we must continue the op.
								// we cannot leave the index in a partially unsplit state.
								self.logError('hash', "Failed to delete index sub-pages: " + data_path + "/*: " + err);
							}
							
							self.put( data_path, { type: 'hash_page', length: 0, items: {} }, function(err) {
								// all done
								if (err) {
									self.logError('hash', "Failed to put index page: " + data_path + ": " + err);
								}
								else {
									self.logDebug(9, "Unsplit operation complete: " + data_path);
								}
								callback();
							} ); // put
						} // pages deleted
					); // eachLimit
				} // key check
			); // eachLimit
		} ); // load
	},
	
	hashDeleteMulti: function(path, hkeys, callback) {
		// delete multiple hash records at once, given array of keys
		// need concurrency limit of 1 because hashDelete locks
		var self = this;
		
		async.eachLimit(hkeys, 1, 
			function(hkey, callback) {
				// iterator for each key
				self.hashDelete(path, hkey, function(err) {
					callback(err);
				} );
			}, 
			function(err) {
				// all keys deleted
				callback(err);
			}
		);
	},
	
	hashGetInfo: function(path, callback) {
		// Return info about hash (number of items, etc.)
		this._hashLoad( path, false, callback );
	}
	
});
```

## File: `indexer-single.js`
```javascript
// PixlServer Storage System - Indexer Single Search Mixin
// Copyright (c) 2018 Joseph Huckaby
// Released under the MIT License

// These methods implement a searchRecords-like API, but only run a query on a single record at a time.
// This is used for things like real-time searches (views), where a single updated record is 
// re-evaluated to see if it should be added/removed to a live search result set.

var Class = require("pixl-class");
var Tools = require("pixl-tools");

module.exports = Class.create({
	
	searchSingle: function(query, record_id, config, callback) {
		// run search query on single record
		// load record idx_data
		var self = this;
		
		// parse search string if required
		if (typeof(query) == 'string') {
			query = query.trim();
			
			if (query == '*') {
				// search wildcard -- special instant result of always true
				return callback(null, true);
			}
			else if (query.match(/^\([\s\S]+\)$/)) {
				// PxQL syntax, parse grammar
				query = this.parseGrammar(query, config);
				if (query.err) {
					this.logError('index', "Invalid search query: " + query.err, query);
					return callback(query.err, false);
				}
			}
			else {
				// simple query syntax
				query = this.parseSearchQuery(query, config);
			}
		}
		
		if (!query.criteria || !query.criteria.length) {
			this.logError('index', "Invalid search query", query);
			return callback(null, false);
		}
		
		this.get( config.base_path + '/_data/' + record_id, function(err, idx_data) {
			if (err) return callback(err);
			
			var results = self._searchSingle(query, record_id, idx_data, config);
			callback( null, !!results[record_id] );
		});
	},
	
	_searchSingle: function(query, record_id, idx_data, config) {
		// execute single search on idx_data (sync)
		// query must be pre-compiled and idx_data must be pre-loaded
		var self = this;
		
		// prep idx_data, but only once
		if (!idx_data.hashed) {
			for (var def_id in idx_data) {
				var data = idx_data[def_id];
				data.word_hash = this.getWordHashFromList( data.words || [] );
			}
			idx_data.hashed = true;
		}
		
		var state = query;
		state.config = config;
		state.record_ids = Object.create(null);
		state.first = true;
		
		// first, split criteria into subs (sub-queries), 
		// stds (standard queries) and negs (negative queries)
		var subs = [], stds = [], negs = [];
		for (var idx = 0, len = query.criteria.length; idx < len; idx++) {
			var crit = query.criteria[idx];
			if (crit.criteria) subs.push( crit );
			else {
				var def = Tools.findObject( config.fields, { id: crit.index } );
				if (!def) {
					this.logError('index', "Invalid search query: Index not found: " + crit.index, query);
					return {};
				}
				crit.def = def;
				
				if (crit.negative) negs.push( crit );
				else stds.push( crit );
			}
		}
		
		// generate series of tasks, starting with any sub-queries,
		// then standard positive criteria, then negative criteria
		var tasks = [].concat( subs, stds, negs );
		
		tasks.forEach( function(task) {
			if (task.criteria) {
				// sub-query
				var records = self._searchSingle( task, record_id, idx_data, config );
				self.mergeIndex( state.record_ids, records, state.first ? 'or' : state.mode );
				state.first = false;
			}
			else if (task.skip) {
				// skip this task (all words removed)
			}
			else if (task.def.type) {
				// custom index type, e.g. date, time, number
				var func = 'searchSingle_' + task.def.type;
				if (self[func]) self[func]( task, record_id, idx_data, state );
				else self.logError('index', "Unknown index type: " + task.def.type);
			}
			else if (task.literal) {
				self._searchSingleWordIndexLiteral(task, record_id, idx_data, state);
			}
			else {
				self._searchSingleWordIndex(task, record_id, idx_data, state);
			}
		} ); // foreach task
		
		return state.record_ids;
	},
	
	_searchSingleWordIndex: function(query, record_id, idx_data, state) {
		// run one search query (list of words against one index)
		var self = this;
		var config = state.config;
		var def = query.def;
		
		var mode = state.first ? 'or' : state.mode;
		if (query.negative) mode = 'not';
		state.first = false;
		
		var cur_items = state.record_ids;
		var new_items = Object.create(null);
		
		// create "fake" hash index for word, containing only our one record
		var items = Object.create(null);
		if (idx_data[def.id] && idx_data[def.id].word_hash && idx_data[def.id].word_hash[query.word]) {
			items[ record_id ] = idx_data[def.id].word_hash[query.word];
		}
		
		switch (mode) {
			case 'and':
				for (var key in items) {
					if (key in cur_items) new_items[key] = 1;
				}
			break;
			
			case 'or':
				for (var key in items) {
					cur_items[key] = 1;
				}
			break;
			
			case 'not':
				for (var key in items) {
					delete cur_items[key];
				}
			break;
		}
		
		if (mode == 'and') state.record_ids = new_items;
	},
	
	_searchSingleWordIndexLiteral: function(query, record_id, idx_data, state) {
		// run literal search query (list of words which must be in sequence)
		var self = this;
		var def = query.def;
		
		var mode = state.first ? 'or' : state.mode;
		if (query.negative) mode = 'not';
		state.first = false;
		
		var record_ids = state.record_ids;
		var temp_results = Object.create(null);
		var temp_idx = 0;
		
		query.words.forEach( function(word) {
			// for each word, iterate over record ids
			var keepers = Object.create(null);
			
			// create "fake" hash index for word, containing only our one record
			var items = Object.create(null);
			if (idx_data[def.id] && idx_data[def.id].word_hash && idx_data[def.id].word_hash[word]) {
				items[ record_id ] = idx_data[def.id].word_hash[word];
			}
			
			Object.keys(items).forEach( function(record_id) {
				var raw_value = items[record_id];
				
				// instant rejection if temp_idx and record_id isn't already present
				if (temp_idx && !(record_id in temp_results)) return;
				
				var offset_list = raw_value.split(/\,/);
				var still_good = 0;
				
				for (var idx = offset_list.length - 1; idx >= 0; idx--) {
					var word_idx = parseInt( offset_list[idx] );
					
					if (temp_idx) {
						// Subsequent pass -- make sure offsets are +1
						var arr = temp_results[record_id];
						for (var idy = 0, ley = arr.length; idy < ley; idy++) {
							var elem = arr[idy];
							if (word_idx == elem + 1) {
								arr[idy]++;
								still_good = 1;
							}
						}
					} // temp_idx
					else {
						// First pass -- get word idx into temp_results
						if (!temp_results[record_id]) temp_results[record_id] = [];
						temp_results[record_id].push( word_idx );
						still_good = 1;
					}
				} // foreach word_idx
				
				if (!still_good) delete temp_results[record_id];
				else keepers[record_id] = 1;
			} ); // foreach fake hash key
			
			// If in a subsequent word pass, make sure all temp_results
			// ids are still matched in the latest word
			if (temp_idx > 0) self.mergeIndex( temp_results, keepers, 'and' );
			temp_idx++;
		} ); // foreach word
		
		// all done, now merge data into record ids
		for (var record_id in temp_results) {
			temp_results[record_id] = 1; // cleanup values
		}
		
		this.mergeIndex( record_ids, temp_results, mode );
	}
	
});
```

## File: `indexer.js`
```javascript
// PixlServer Storage System - Indexer Mixin
// Copyright (c) 2016 - 2020 Joseph Huckaby
// Released under the MIT License

var async = require('async');
var Class = require("pixl-class");
var Tools = require("pixl-tools");
var Perf = require("pixl-perf");
var nearley = require("nearley");
var pxql_grammar = require("./pxql.js");
var stemmer = require('porter-stemmer').stemmer;
var unidecode = require('unidecode');
var he = require('he');

var IndexerSingle = require("./indexer-single.js");
var DateIndexType = require("./index_types/Date.js");
var NumberIndexType = require("./index_types/Number.js");

module.exports = Class.create({
	
	__mixins: [ IndexerSingle, DateIndexType, NumberIndexType ],
	
	removeWordCache: null,
	
	indexRecord: function(id, record, config, callback) {
		// index record (transaction version)
		var self = this;
		
		// if no transactions, or transaction already in progress, jump to original func
		if (!this.transactions || this.currentTransactionPath) {
			return this._indexRecord(id, record, config, function(err, state) {
				if (err) self.logError('index', "Indexing failed on record: " + id + ": " + err);
				callback(err, state);
			});
		}
		
		// use base path for transaction lock
		var path = config.base_path;
		
		// here we go
		this.beginTransaction(path, function(err, clone) {
			// transaction has begun
			// call _indexRecord on CLONE (transaction-aware storage instance)
			clone._indexRecord(id, record, config, function(err, state) {
				if (err) {
					// index generated an error
					self.logError('index', "Indexing failed on record: " + id + ": " + err);
					
					// emergency abort, rollback
					self.abortTransaction(path, function() {
						// call original callback with error that triggered rollback
						if (callback) callback( err );
					}); // abort
				}
				else {
					// no error, commit transaction
					self.commitTransaction(path, function(err) {
						if (err) {
							// commit failed, trigger automatic rollback
							self.abortTransaction(path, function() {
								// call original callback with commit error
								if (callback) callback( err );
							}); // abort
						} // commit error
						else {
							// success!  call original callback
							if (callback) callback(null, state);
						}
					}); // commit
				} // no error
			}); // _indexRecord
		}); // beginTransaction
	},
	
	validateIndexConfig: function(config) {
		// make sure index config is kosher
		// return false for success, or error on failure
		if (!config || !config.fields || !Tools.isaArray(config.fields)) {
			return( new Error("Invalid index configuration object.") );
		}
		if (Tools.findObject(config.fields, { _primary: 1 })) {
			return( new Error("Invalid index configuration key: _primary") );
		}
		
		// validate each field def
		for (var idx = 0, len = config.fields.length; idx < len; idx++) {
			var def = config.fields[idx];
			
			if (!def.id || !def.id.match(/^\w+$/)) {
				return( new Error("Invalid index field ID: " + def.id) );
			}
			if (def.id.match(/^(_id|_data|_sorters|constructor|__defineGetter__|__defineSetter__|hasOwnProperty|__lookupGetter__|__lookupSetter__|isPrototypeOf|propertyIsEnumerable|toString|valueOf|__proto__|toLocaleString)$/)) {
				return( new Error("Invalid index field ID: " + def.id) );
			}
			
			if (def.type && !this['prepIndex_' + def.type]) {
				return( new Error("Invalid index type: " + def.type) );
			}
			
			if (def.filter && !this['filterWords_' + def.filter]) {
				return( new Error("Invalid index filter: " + def.filter) );
			}
		} // foreach def
		
		// validate each sorter def
		if (config.sorters) {
			if (!Tools.isaArray(config.sorters)) {
				return( new Error("Invalid index sorters array.") );
			}
			
			for (var idx = 0, len = config.sorters.length; idx < len; idx++) {
				var sorter = config.sorters[idx];
				
				if (!sorter.id || !sorter.id.match(/^\w+$/)) {
					return( new Error("Invalid index sorter ID: " + sorter.id) );
				}
				if (sorter.id.match(/^(_id|_data|_sorters|constructor|__defineGetter__|__defineSetter__|hasOwnProperty|__lookupGetter__|__lookupSetter__|isPrototypeOf|propertyIsEnumerable|toString|valueOf|__proto__|toLocaleString)$/)) {
					return( new Error("Invalid index sorter ID: " + sorter.id) );
				}
				if (sorter.type && !sorter.type.match(/^(string|number)$/)) {
					return( new Error("Invalid index sorter type: " + sorter.type) );
				}
			} // foreach sorter
		} // config.sorters
		
		return false; // no error
	},
	
	_indexRecord: function(id, record, config, callback) {
		// index record (internal)
		var self = this;
		this.logDebug(8, "Indexing record: " + id);
		
		var state = {
			id: id,
			config: config
		};
		
		// sanity checks
		if (!id) {
			if (callback) callback( new Error("Missing Record ID for indexing.") );
			return;
		}
		
		// make sure ID is a string, and has some alphanumeric portion
		id = '' + id;
		var normal_id = this.normalizeKey(id);
		if (!normal_id || !normal_id.match(/^\w/)) {
			if (callback) callback( new Error("Invalid Record ID for indexing: " + id) );
			return;
		}
		
		if (!record || !Tools.isaHash(record)) {
			if (callback) callback( new Error("Invalid record object for index.") );
			return;
		}
		
		// make sure we have a good config
		var err = this.validateIndexConfig(config);
		if (err) {
			if (callback) callback(err);
			return;
		}
		
		// generate list of fields based on available values in record
		// i.e. support partial updates by only passing in those fields
		var fields = [];
		
		config.fields.forEach( function(def) {
			var value = def.source.match(/\[.+\]/) ? Tools.sub(def.source, record, true) : Tools.getPath(record, def.source);
			if (value === undefined) value = null;
			if ((value === null) && ("default_value" in def)) value = def.default_value;
			if (value !== null) fields.push(def);
		} );
		
		// start index and track perf
		var pf = this.perf.begin('index');
		
		// lock record (non-existent key, but it's record specific for the lock)
		this.lock( config.base_path + '/' + id, true, function() {
			
			// see if we've already indexed this record before
			self.get( config.base_path + '/_data/' + id, function(err, idx_data) {
				// check for fatal I/O error
				if (err && (err.code != 'NoSuchKey')) {
					self.unlock( config.base_path + '/' + id );
					pf.end();
					return callback(err);
				}
				
				if (!idx_data) {
					idx_data = {};
					state.new_record = true;
					
					// add special index for primary ID (just a hash -- new records only)
					fields.push({ _primary: 1 });
				}
				state.idx_data = idx_data;
				state.changed = {};
				
				// walk all fields in parallel (everything gets enqueued anyway)
				async.each( fields,
					function(def, callback) {
						// process each index
						if (def._primary) {
							// primary id hash
							var opts = { page_size: config.hash_page_size || 1000 };
							self.hashPut( config.base_path + '/_id', id, 1, opts, callback );
							return;
						}
						
						var value = def.source.match(/\[.+\]/) ? Tools.sub(def.source, record, true) : Tools.getPath(record, def.source);
						if (value === undefined) value = null;
						if ((value === null) && ("default_value" in def)) value = def.default_value;
						if (typeof(value) == 'object') value = JSON.stringify(value);
						
						var words = self.getWordList( ''+value, def, config );
						var checksum = Tools.digestHex( words.join(' '), 'md5' );
						var data = { words: words, checksum: checksum };
						var old_data = idx_data[ def.id ];
						
						self.logDebug(9, "Preparing data for index: " + def.id, {
							value: value,
							words: words,
							checksum: checksum
						});
						
						if (def.delete) {
							// special mode: delete index data
							if (old_data) {
								state.changed[ def.id ] = 1;
								self.deleteIndex( old_data, def, state, callback );
							}
							else callback();
						}
						else if (old_data) {
							// index exists, check if data has changed
							if (checksum != old_data.checksum) {
								// must reindex
								state.changed[ def.id ] = 1;
								self.updateIndex( old_data, data, ''+value, def, state, callback );
							}
							else {
								// data not changed, no action required
								self.logDebug(9, "Index value unchanged, skipping: " + def.id);
								callback();
							}
						}
						else {
							// index doesn't exist for this record, create immediately
							state.changed[ def.id ] = 1;
							self.writeIndex( data, ''+value, def, state, callback );
						}
					}, // iterator
					function(err) {
						// everything indexed
						if (err) {
							self.unlock( config.base_path + '/' + id );
							pf.end();
							if (callback) callback(err);
							return;
						}
						
						// now handle the sorters
						async.eachLimit( config.sorters || [], self.concurrency,
							function(sorter, callback) {
								if (sorter.delete) self.deleteSorter( id, sorter, state, callback );
								else self.updateSorter( record, sorter, state, callback );
							},
							function(err) {
								// all sorters sorted
								// save idx data for record
								self.put( config.base_path + '/_data/' + id, idx_data, function(err) {
									if (err) {
										self.unlock( config.base_path + '/' + id );
										pf.end();
										if (callback) callback(err);
										return;
									}
									
									var elapsed = pf.end();
									
									if (!err) self.logTransaction('index', config.base_path, {
										id: id,
										elapsed_ms: elapsed
									});
									
									self.unlock( config.base_path + '/' + id );
									if (callback) callback(err, state);
								} ); // put (_data)
							}
						); // eachLimit (sorters)
					} // done with fields
				); // each (fields)
			} ); // get (_data)
		} ); // lock
	},
	
	unindexRecord: function(id, config, callback) {
		// unindex record (transaction version)
		var self = this;
		
		// if no transactions, or transaction already in progress, jump to original func
		if (!this.transactions || this.currentTransactionPath) {
			return this._unindexRecord(id, config, callback);
		}
		
		// use base path for transaction lock
		var path = config.base_path;
		
		// here we go
		this.beginTransaction(path, function(err, clone) {
			// transaction has begun
			// call _unindexRecord on CLONE (transaction-aware storage instance)
			clone._unindexRecord(id, config, function(err, state) {
				if (err) {
					// index generated an error
					// emergency abort, rollback
					self.abortTransaction(path, function() {
						// call original callback with error that triggered rollback
						if (callback) callback( err );
					}); // abort
				}
				else {
					// no error, commit transaction
					self.commitTransaction(path, function(err) {
						if (err) {
							// commit failed, trigger automatic rollback
							self.abortTransaction(path, function() {
								// call original callback with commit error
								if (callback) callback( err );
							}); // abort
						} // commit error
						else {
							// success!  call original callback
							if (callback) callback(null, state);
						}
					}); // commit
				} // no error
			}); // _unindexRecord
		}); // beginTransaction
	},
	
	_unindexRecord: function(id, config, callback) {
		// unindex record (internal)
		var self = this;
		this.logDebug(8, "Unindexing record: " + id);
		
		var state = {
			id: id,
			config: config
		};
		
		// sanity checks
		if (!id) {
			if (callback) callback( new Error("Invalid ID for record index.") );
			return;
		}
		
		// make sure we have a good config
		var err = this.validateIndexConfig(config);
		if (err) {
			if (callback) callback(err);
			return;
		}
		
		// copy fields so we can add the special primary one
		var fields = [];
		for (var idx = 0, len = config.fields.length; idx < len; idx++) {
			fields.push( config.fields[idx] );
		}
		
		// add special index for primary ID (just a hash)
		fields.push({ _primary: 1 });
		
		// start unindex and track perf
		var pf = this.perf.begin('unindex');
		
		// lock record (non-existent key, but it's record specific for the lock)
		this.lock( config.base_path + '/' + id, true, function() {
			
			// see if we've indexed this record before
			self.get( config.base_path + '/_data/' + id, function(err, idx_data) {
				// check for error
				if (err) {
					self.unlock( config.base_path + '/' + id );
					pf.end();
					return callback(err);
				}
				
				state.idx_data = idx_data;
				state.changed = {};
				
				// walk all fields in parallel (everything gets enqueued anyway)
				async.each( fields,
					function(def, callback) {
						// primary id hash
						if (def._primary) {
							self.hashDelete( config.base_path + '/_id', id, callback );
							return;
						}
						
						// check if index exists
						var data = idx_data[ def.id ];
						
						if (data) {
							// index exists, proceed with delete
							state.changed[ def.id ] = 1;
							self.deleteIndex( data, def, state, callback );
						}
						else callback();
					},
					function(err) {
						// everything unindexed
						if (err) {
							self.unlock( config.base_path + '/' + id );
							pf.end();
							if (callback) callback(err);
							return;
						}
						
						// delete main idx data record
						self.delete( config.base_path + '/_data/' + id, function(err) {
							if (err) {
								self.unlock( config.base_path + '/' + id );
								pf.end();
								if (callback) callback(err);
								return;
							}
							
							// now handle the sorters
							async.eachLimit( config.sorters || [], self.concurrency,
								function(sorter, callback) {
									self.deleteSorter( id, sorter, state, callback );
								},
								function(err) {
									// all sorters sorted
									var elapsed = pf.end();
									
									if (!err) self.logTransaction('unindex', config.base_path, {
										id: id,
										elapsed_ms: elapsed
									});
									
									self.unlock( config.base_path + '/' + id );
									if (callback) callback(err, state);
								}
							); // eachLimit (sorters)
						} ); // delete (_data)
					} // done (fields)
				); // each (fields)
			} ); // get (_data)
		} ); // lock
	},
	
	writeIndex: function(data, raw_value, def, state, callback) {
		// create or update single field index
		var self = this;
		var words = data.words;
		
		// check for custom index prep function
		if (def.type) {
			var func = 'prepIndex_' + def.type;
			if (self[func]) {
				var result = self[func]( words, def, state );
				if (result === false) {
					if (callback) {
						callback( new Error("Invalid data for index: " + def.id + ": " + words.join(' ')) );
					}
					return;
				}
				data.words = words = result;
			}
		}
		
		this.logDebug(9, "Indexing field: " + def.id + " for record: " + state.id, words);
		
		var base_path = state.config.base_path + '/' + def.id;
		var word_hash = this.getWordHashFromList( words );
		
		// first, save idx record (word list and checksum)
		state.idx_data[ def.id ] = data;
		
		// word list may be empty
		if (!words.length && !def.master_list) {
			self.logDebug(9, "Word list is empty, skipping " + def.id + " for record: " + state.id);
			if (callback) callback();
			return;
		}
		
		// now index each unique word
		var group = {
			count: Tools.numKeys(word_hash),
			callback: callback || null
		};
		
		// lock index for this
		self.lock( base_path, true, function() {
			// update master list if applicable
			if (def.master_list) {
				group.count++;
				self.indexEnqueue({
					action: 'custom', 
					label: 'writeIndexSummary',
					handler: self.writeIndexSummary.bind(self),
					def: def,
					group: group,
					base_path: base_path,
					word_hash: word_hash,
					raw_value: raw_value
				});
			} // master_list
			
			for (var word in word_hash) {
				var value = word_hash[word];
				var path = base_path + '/word/' + word;
				
				self.indexEnqueue({
					action: 'custom', 
					label: 'writeIndexWord',
					handler: self.writeIndexWord.bind(self),
					hash_page_size: state.config.hash_page_size || 1000,
					// config: state.config,
					group: group,
					word: word,
					id: state.id,
					base_path: base_path,
					path: path,
					value: value
				});
			} // foreach word
			
		} ); // lock
	},
	
	writeIndexWord: function(task, callback) {
		// index single word, invoked from storage queue
		var self = this;
		var opts = { page_size: task.hash_page_size || 1000, word: task.word };
		
		this.logDebug(10, "Indexing word: " + task.path + " for record: " + task.id);
		
		this.hashPut( task.path, task.id, task.value, opts, function(err) {
			if (err) {
				// this will bubble up at the end of the group
				task.group.error = "Failed to write index data: " + task.path + ": " + err.message;
				self.logError('index', task.group.error);
			}
			
			// check to see if we are the last task in the group
			task.group.count--;
			if (!task.group.count) {
				// group is complete, unlock and fire secondary callback if applicable
				self.unlock(task.base_path);
				if (task.group.callback) task.group.callback(task.group.error);
			} // last item in group
			
			// queue callback
			callback();
		} ); // hashPut
	},
	
	writeIndexSummary: function(task, callback) {
		// index summary of words (record counts per word), invoked from storage queue
		var self = this;
		this.logDebug(10, "Updating summary index: " + task.base_path);
		
		var path = task.base_path + '/summary';
		var word_hash = task.word_hash;
		
		this.lock( path, true, function() {
			// locked
			self.get( path, function(err, summary) {
				if (err && (err.code != 'NoSuchKey')) {
					// serious I/O error, need to bubble this up
					task.group.error = "Failed to get index summary data: " + path + ": " + err.message;
					self.logError('index', task.group.error);
				}
				if (err || !summary) {
					summary = { id: task.def.id, values: {} };
				}
				summary.values = Tools.copyHashRemoveProto( summary.values );
				summary.modified = Tools.timeNow(true);
				
				for (var word in word_hash) {
					if (!summary.values[word]) summary.values[word] = 0;
					summary.values[word]++;
					
					if (task.def.master_labels) {
						if (!summary.labels) summary.labels = {};
						summary.labels[word] = task.raw_value;
					}
				} // foreach word
				
				// save summary back to storage
				self.put( path, summary, function(err) {
					self.unlock( path );
					if (err) {
						// this will bubble up at the end of the group
						task.group.error = "Failed to write index summary data: " + path + ": " + err.message;
						self.logError('index', task.group.error);
					}
					
					// check to see if we are the last task in the group
					task.group.count--;
					if (!task.group.count) {
						// group is complete, unlock and fire secondary callback if applicable
						self.unlock(task.base_path);
						if (task.group.callback) task.group.callback(task.group.error);
					} // last item in group
					
					// queue callback
					callback();
					
				} ); // put
			} ); // get
		} ); // lock
	},
	
	deleteIndex: function(data, def, state, callback) {
		// delete index
		// this must be sequenced before a reindex
		var self = this;
		var words = data.words;
		
		// check for custom index prep delete function
		if (def.type) {
			var func = 'prepDeleteIndex_' + def.type;
			if (self[func]) {
				self[func]( words, def, state );
			}
		}
		
		this.logDebug(9, "Unindexing field: " + def.id + " for record: " + state.id, words);
		
		var base_path = state.config.base_path + '/' + def.id;
		var word_hash = this.getWordHashFromList( words );
		
		// first, delete idx record (word list and checksum)
		delete state.idx_data[ def.id ];
		
		// word list may be empty
		if (!words.length && !def.master_list) {
			self.logDebug(9, "Word list is empty, skipping " + def.id + " for record: " + state.id);
			if (callback) callback();
			return;
		}
		
		// now unindex each unique word
		var group = {
			count: Tools.numKeys(word_hash),
			callback: callback || null
		};
		
		// lock index for this
		self.lock( base_path, true, function() {
			// update master list if applicable
			if (def.master_list) {
				group.count++;
				self.indexEnqueue({
					action: 'custom', 
					label: 'deleteIndexSummary',
					handler: self.deleteIndexSummary.bind(self),
					def: def,
					group: group,
					base_path: base_path,
					word_hash: word_hash
				});
			} // master_list
			
			for (var word in word_hash) {
				var path = base_path + '/word/' + word;
				
				self.indexEnqueue({
					action: 'custom', 
					label: 'deleteIndexWord',
					handler: self.deleteIndexWord.bind(self),
					group: group,
					word: word,
					id: state.id,
					base_path: base_path,
					path: path
				});
			} // foreach word
			
		} ); // lock
	},
	
	deleteIndexWord: function(task, callback) {
		// delete single word, invoked from storage queue
		var self = this;
		this.logDebug(10, "Unindexing word: " + task.path + " for record: " + task.id);
		
		this.hashDelete( task.path, task.id, true, function(err) {
			if (err) {
				var err_msg = "Failed to write index data: " + task.path + ": " + err.message;
				self.logError('index', err_msg);
				
				// check for fatal I/O
				if (err.code != 'NoSuchKey') {
					// this will bubble up at end
					task.group.error = err_msg;
				}
			}
			
			// check to see if we are the last task in the group
			task.group.count--;
			if (!task.group.count) {
				// group is complete, unlock and fire secondary callback if applicable
				self.unlock(task.base_path);
				if (task.group.callback) task.group.callback(task.group.error);
			} // last item in group
			
			// queue callback
			callback();
		} ); // hashDelete
	},
	
	deleteIndexSummary: function(task, callback) {
		// delete summary of words (record counts per word), invoked from storage queue
		var self = this;
		this.logDebug(10, "Removing words from summary index: " + task.base_path, task.word_hash);
		
		var path = task.base_path + '/summary';
		var word_hash = task.word_hash;
		
		this.lock( path, true, function() {
			// locked
			self.get( path, function(err, summary) {
				if (err && (err.code != 'NoSuchKey')) {
					// serious I/O error, need to bubble this up
					task.group.error = "Failed to get index summary data: " + path + ": " + err.message;
					self.logError('index', task.group.error);
				}
				if (err || !summary) {
					// index summary doesn't exist, huh
					self.logDebug(5, "Index summary doesn't exist: " + path);
					summary = { id: task.def.id, values: {} };
				}
				summary.values = Tools.copyHashRemoveProto( summary.values );
				summary.modified = Tools.timeNow(true);
				
				for (var word in word_hash) {
					if (summary.values[word]) summary.values[word]--;
					if (!summary.values[word]) {
						delete summary.values[word];
						if (task.def.master_labels && summary.labels) delete summary.labels[word];
					}
				} // foreach word
				
				// save summary back to storage
				self.put( path, summary, function(err) {
					self.unlock( path );
					if (err) {
						// this will bubble up at the end of the group
						task.group.error = "Failed to write index summary data: " + path + ": " + err.message;
						self.logError('index', task.group.error);
					}
					
					// check to see if we are the last task in the group
					task.group.count--;
					if (!task.group.count) {
						// group is complete, unlock and fire secondary callback if applicable
						self.unlock(task.base_path);
						if (task.group.callback) task.group.callback(task.group.error);
					} // last item in group
					
					// queue callback
					callback();
					
				} ); // put
			} ); // get
		} ); // lock
	},
	
	updateIndex: function(old_data, new_data, raw_value, def, state, callback) {
		// efficiently update single field index
		var self = this;
		var old_words = old_data.words;
		var new_words = new_data.words;
		
		// check for custom index prep function
		// we only need this on the new words
		if (def.type) {
			var func = 'prepIndex_' + def.type;
			if (self[func]) {
				var result = self[func]( new_words, def, state );
				if (result === false) {
					if (callback) {
						callback( new Error("Invalid data for index: " + def.id + ": " + new_words.join(' ')) );
					}
					return;
				}
				new_data.words = new_words = result;
			}
		}
		
		this.logDebug(9, "Updating Index: " + def.id + " for record: " + state.id, new_words);
		
		var base_path = state.config.base_path + '/' + def.id;
		var old_word_hash = this.getWordHashFromList( old_words );
		var new_word_hash = this.getWordHashFromList( new_words );
		
		// calculate added, changed and removed words
		var added_words = Object.create(null);
		var changed_words = Object.create(null);
		var removed_words = Object.create(null);
		
		for (var new_word in new_word_hash) {
			var new_value = new_word_hash[new_word];
			if (!(new_word in old_word_hash)) {
				// added new word
				added_words[new_word] = new_value;
			}
			if (new_value != old_word_hash[new_word]) {
				// also includes added, which is fine
				changed_words[new_word] = new_value;
			}
		}
		for (var old_word in old_word_hash) {
			if (!(old_word in new_word_hash)) {
				// word removed
				removed_words[old_word] = 1;
			}
		}
		
		// write idx record (word list and checksum)
		state.idx_data[ def.id ] = new_data;
		
		// now index each unique word
		var group = {
			count: Tools.numKeys(changed_words) + Tools.numKeys(removed_words),
			callback: callback || null
		};
		
		if (!group.count) {
			this.logDebug(9, "Actually, nothing changed in index: " + def.id + " for record: " + state.id + ", skipping updateIndex");
			if (callback) callback();
			return;
		}
		
		// lock index for this
		self.lock( base_path, true, function() {
			// update master list if applicable
			if (def.master_list) {
				if (Tools.numKeys(added_words) > 0) {
					group.count++;
					self.indexEnqueue({
						action: 'custom', 
						label: 'writeIndexSummary',
						handler: self.writeIndexSummary.bind(self),
						def: def,
						group: group,
						base_path: base_path,
						word_hash: added_words,
						raw_value: raw_value
					});
				}
				if (Tools.numKeys(removed_words) > 0) {
					group.count++;
					self.indexEnqueue({
						action: 'custom', 
						label: 'deleteIndexSummary',
						handler: self.deleteIndexSummary.bind(self),
						def: def,
						group: group,
						base_path: base_path,
						word_hash: removed_words
					});
				}
			} // master_list
			
			for (var word in changed_words) {
				var value = changed_words[word];
				var path = base_path + '/word/' + word;
				
				self.indexEnqueue({
					action: 'custom', 
					label: 'writeIndexWord',
					handler: self.writeIndexWord.bind(self),
					hash_page_size: state.config.hash_page_size || 1000,
					// config: state.config,
					group: group,
					word: word,
					id: state.id,
					base_path: base_path,
					path: path,
					value: value
				});
			} // foreach changed word
			
			for (var word in removed_words) {
				var path = base_path + '/word/' + word;
				
				self.indexEnqueue({
					action: 'custom', 
					label: 'deleteIndexWord',
					handler: self.deleteIndexWord.bind(self),
					group: group,
					word: word,
					id: state.id,
					base_path: base_path,
					path: path
				});
			} // foreach removed word
			
		} ); // lock
	},
	
	indexEnqueue: function(task) {
		// special index version of enqueue()
		// if we're in a transaction, call ORIGINAL enqueue() from parent
		// this is because index queue items must execute right away -- they CANNOT wait until commit()
		if (this.rawStorage) this.rawStorage.enqueue(task);
		else this.enqueue(task);
	},
	
	updateSorter: function(record, sorter, state, callback) {
		// add record to sorter index
		var config = state.config;
		
		var value = Tools.getPath(record, sorter.source);
		if (value === undefined) value = null;
		if ((value === null) && ("default_value" in sorter)) value = sorter.default_value;
		if (value === null) {
			if (state.new_record) value = ((sorter.type == 'number') ? 0 : '');
			else return callback();
		}
		
		// store value in idx_data as well
		if (!state.idx_data._sorters) state.idx_data._sorters = {};
		else if ((sorter.id in state.idx_data._sorters) && (value == state.idx_data._sorters[sorter.id])) {
			// sorter value unchanged, return immediately
			this.logDebug(10, "Sorter value unchanged, skipping write: " + sorter.id + ": " + state.id + ": " + value);
			return callback();
		}
		
		state.idx_data._sorters[sorter.id] = value;
		
		var path = config.base_path + '/' + sorter.id + '/sort';
		var opts = { page_size: config.sorter_page_size || 1000 };
		
		this.logDebug(10, "Setting value in sorter: " + sorter.id + ": " + state.id + ": " + value);
		this.hashPut( path, state.id, value, opts, callback );
	},
	
	deleteSorter: function(id, sorter, state, callback) {
		// remove record from sorter index
		var config = state.config;
		var path = config.base_path + '/' + sorter.id + '/sort';
		
		this.logDebug(10, "Removing record from sorter: " + sorter.id + ": " + id);
		this.hashDelete( path, id, function(err) {
			// only report actual I/O errors
			if (err && (err.code != 'NoSuchKey')) {
				return callback(err);
			}
			callback();
		} );
	},
	
	filterWords_markdown: function(value) {
		// filter out markdown syntax and html tags, entities
		value = value.replace(/```[\s\S]*?```/g, ''); // fenced code
		return this.filterWords_html(value);
	},
	
	filterWords_html: function(value) {
		// filter out html tags, entities
		return he.decode( value.replace(/<[^>]*>/g, '') );
	},
	
	filterWords_alphanum: function(value) {
		// filter out everything except alphanum + underscore
		return value.replace(/\W+/g, '_').replace(/_+/g, '_');
	},
	
	filterWords_alphanum_array: function(value) {
		// filter out everything except alphanum + underscore + comma, suitable for JSON arrays
		return value.replace(/[\[\]\"\']+/g, '').replace(/[^\w\,]+/g, '_').replace(/_+/g, '_');
	},
	
	getWordList: function(value, def, config) {
		// clean and filter text down to list of alphanumeric words
		// return array of clean words
		if (def.filter && this['filterWords_' + def.filter]) {
			value = this['filterWords_' + def.filter]( value );
		}
		if (def.type && this['filterWords_' + def.type]) {
			value = this['filterWords_' + def.type]( value );
		}
		
		// more text cleanup
		if (!def.no_cleanup) {
			value = unidecode( value ); // convert unicode to ascii
			value = value.replace(/\w+\:\/\/([\w\-\.]+)\S*/g, '$1'); // index domains, not full urls
			value = value.replace(/\'/g, ''); // index nancy's as nancys
			value = value.replace(/\d+\.\d[\d\.]*/g, function(m) { return m.replace(/\./g, '_').replace(/_+$/, ''); }); // 2.5 --> 2_5
		}
		
		// special filter for firstname.lastname usernames
		if (def.username_join) {
			value = value.replace(/\w+\.\w[\w\.]*/g, function(m) { return m.replace(/\./g, '_').replace(/_+$/, ''); });
		}
		
		value = value.toLowerCase();
		
		var min_len = def.min_word_length || 1;
		var max_len = def.max_word_length || 255;
		var items = value.split(/\b/);
		var words = [];
		
		var remove_words = Object.create(null);
		if (def.use_remove_words && config.remove_words) {
			remove_words = this.cacheRemoveWords(config);
		}
		
		for (var idx = 0, len = items.length; idx < len; idx++) {
			var word = items[idx];
			if (word.match(/^\w+$/) && (word.length >= min_len) && (word.length <= max_len) && !remove_words[word]) {
				if (def.use_stemmer) word = stemmer(word);
				words.push( word );
			}
		}
		
		if (def.max_words && (words.length > def.max_words)) {
			words.splice( def.max_words );
		}
		
		return words;
	},
	
	getWordHashFromList: function(words) {
		// convert word list to hash of unique words and offset CSV
		var hash = Object.create(null);
		var word = '';
		
		for (var idx = 0, len = words.length; idx < len; idx++) {
			word = words[idx];
			if (word in hash) hash[word] += ','; else hash[word] = '';
			hash[word] += '' + Math.floor(idx + 1);
		} // foreach word
		
		return hash;
	},
	
	parseSearchQuery: function(value, config) {
		// parse search query string into array of criteria
		var criteria = [];
		var cur_index = config.default_search_field || '';
		
		this.logDebug(9, "Parsing simple search query: " + value);
		
		// basic pre-cleanup
		value = value.replace(/\s*\:\s*/g, ':');
		value = value.replace(/\s*\|\s*/g, '|');
		
		// escape literals (they will be re-unescaped below after splitting)
		value = value.replace(/\"(.+?)\"/g, function(m_all, m_g1) { return '"' + escape(m_g1) + '"'; } );
		
		var parts = value.split(/\s+/);
		
		for (var idx = 0, len = parts.length; idx < len; idx++) {
			var part = parts[idx];
			var crit = {};
			if (part.match(/^(\w+)\:(.+)$/)) {
				cur_index = RegExp.$1;
				part = RegExp.$2;
			}
			var def = Tools.findObject( config.fields, { id: cur_index || '_NOPE_' } );
			if (def) {
				if (part.match(/\|/)) {
					// piped OR list of values, must create sub-query
					crit.mode = 'or';
					crit.criteria = [];
					
					var pipes = part.split(/\|/);
					for (var idy = 0, ley = pipes.length; idy < ley; idy++) {
						var pipe = pipes[idy];
						
						var sub_words = this.getWordList(pipe, def, config);
						for (var idz = 0, lez = sub_words.length; idz < lez; idz++) {
							crit.criteria.push({ index: cur_index, word: sub_words[idz] });
						}
					}
					
					if (crit.criteria.length) criteria.push( crit );
				}
				else {
					crit.index = cur_index;
					
					part = part.replace(/^\+/, '');
					if (part.match(/^\-/)) {
						crit.negative = 1;
						part = part.replace(/^\-/, '');
					}
					if (part.match(/^\"(.+)\"$/)) {
						crit.literal = 1;
						part = unescape( RegExp.$1 );
						crit.words = this.getWordList(part, def, config);
					}
					else if (def.type) {
						// all defs with a 'type' are assumed to support ranges and lt/gt
						if (part.match(/^(.+)\.\.(.+)$/)) {
							// range between two values (inclusive)
							var low = RegExp.$1;
							var high = RegExp.$2;
							
							var lwords = this.getWordList(low, def, config);
							if (lwords.length) low = lwords[0];
							
							var hwords = this.getWordList(high, def, config);
							if (hwords.length) high = hwords[0];
							
							crit = {
								mode: 'and', 
								criteria: [
									{ index: cur_index, operator: ">=", word: low },
									{ index: cur_index, operator: "<=", word: high }
								]
							};
							criteria.push( crit );
						}
						else {
							// exact match or open-ended range
							var op = '=';
							if (part.match(/^(=|>=|>|<=|<)(.+)$/)) {
								op = RegExp.$1;
								part = RegExp.$2;
							}
							crit.operator = op;
							// crit.word = part;
							var words = this.getWordList(part, def, config);
							if (words.length) crit.word = words[0];
						}
					}
					else {
						var words = this.getWordList(part, def, config);
						if (words.length > 1) {
							crit.literal = 1;
							crit.words = words;
						}
						else if (words.length) crit.word = words[0];
					}
					
					if (crit.word || (crit.words && crit.words.length)) criteria.push( crit );
				}
			} // cur_index
		} // foreach part
		
		var query = { mode: 'and', criteria: criteria };
		
		this.logDebug(10, "Compiled search query:", query);
		return query;
	},
	
	parseGrammar: function(value, config) {
		// parse PxQL syntax, convert to native format
		var self = this;
		var parser = new nearley.Parser( nearley.Grammar.fromCompiled(pxql_grammar) );
		
		// pre-cleanup, normalize whitespace
		value = value.replace(/\s+/g, " ");
		
		this.logDebug(9, "Parsing PxQL search query: " + value);
		
		try {
			parser.feed( value );
		}
		catch (err) {
			return { err: err };
		}
		
		var query = parser.results[0];
		if (!query) {
			return { err: new Error("Failed to parse") };
		}
		if (!query.criteria && query.index) {
			// single criteria collapsed into parent
			query = { mode: 'and', criteria: [ query ] };
		}
		if (!query.criteria || !query.criteria.length) {
			return { err: new Error("Failed to parse") };
		}
		delete query.err;
		
		// apply post-processing for exact phrases, remove words
		var processCriteria = function(criteria) {
			// walk array, recurse for inner sub-queries
			criteria.forEach( function(crit) {
				if (query.err) return;
				
				if (crit.word) {
					// standard word query
					var def = Tools.findObject( config.fields, { id: crit.index || '_NOPE_' } );
					if (def) {
						var words = self.getWordList(crit.word, def, config);
						if (words.length > 1) {
							// literal multi-word phrase
							crit.words = words;
							crit.literal = 1;
							delete crit.word;
						}
						else if (words.length == 1) {
							// single word match
							crit.word = words[0];
						}
						else {
							// all words were removed
							// not technically an error, but this clause needs to be skipped
							self.logDebug(9, "All words removed from criteron: " + crit.word, crit);
							crit.skip = 1;
						}
					}
					else {
						query.err = new Error("Index not found: " + crit.index);
						return;
					}
				}
				if (crit.criteria && !query.err) processCriteria( crit.criteria );
			} );
		};
		
		processCriteria( query.criteria );
		return query;
	},
	
	weighCriterion: function(crit, config, callback) {
		// weigh single criterion for estimated memory usage
		var base_path = config.base_path + '/' + crit.index;
		var word = crit.word || crit.words[0];
		var path = base_path + '/word/' + word;
		
		// this doesn't work on ranged queries with typed columns, e.g. dates and numbers
		// as those use a master index for searching
		var def = Tools.findObject( config.fields, { id: crit.index } );
		if (def && def.type && crit.operator && crit.operator.match(/<|>/)) {
			crit.weight = 0;
			process.nextTick( function() { callback(); } );
			return;
		}
		
		this.hashGetInfo(path, function(err, hash) {
			if (hash && hash.length) crit.weight = hash.length;
			else crit.weight = 0;
			callback();
		});
	},
	
	searchRecords: function(query, config, callback) {
		// search fields (public API with shared lock on trans commit key)
		// this will block only if a transaction is currently committing
		var self = this;
		var path = config.base_path;
		var pf = this.perf.begin('search');
		
		var orig_query = query;
		if (typeof(query) == 'object') query = Tools.copyHash(query, true);
		
		this.shareLock( 'C|'+path, true, function(err, lock) {
			// got shared lock
			self._searchRecords( query, config, function(err, results, state) {
				// search complete
				if (!err) self.logTransaction('search', path, {
					query: orig_query,
					perf: state.perf ? state.perf.metrics() : {},
					results: (self.logEventTypes.search || self.logEventTypes.all) ? Tools.numKeys(results) : 0
				});
				
				self.shareUnlock( 'C|'+path );
				callback( err, results, state );
			} ); // search
		} ); // lock
	},
	
	_searchRecords: function(query, config, callback) {
		// search index for criteria, e.g. status:bug|enhancement assigned:jhuckaby created:2016-05-08
		// or main_text:google +style "query here" -yay status:open
		// return hash of matching record ids
		var self = this;
		
		// parse search string if required
		if (typeof(query) == 'string') {
			query = query.trim();
			
			if (query == '*') {
				// fetch all records
				this.logDebug(8, "Fetching all records: " + config.base_path);
				var apf = new Perf();
				apf.begin();
				apf.begin('all');
				
				return this.hashGetAll( config.base_path + '/_id', function(err, results) {
					// ignore error, just return empty hash
					apf.end('all');
					apf.end();
					callback( null, results || {}, { perf: apf } );
				} );
			}
			else if (query.match(/^\([\s\S]+\)$/)) {
				// PxQL syntax, parse grammar
				query = this.parseGrammar(query, config);
				if (query.err) {
					this.logError('index', "Invalid search query: " + query.err, query);
					return callback(query.err, null);
				}
			}
			else {
				// simple query syntax
				query = this.parseSearchQuery(query, config);
			}
		}
		
		if (!query.criteria || !query.criteria.length) {
			this.logError('index', "Invalid search query", query);
			return callback(null, {}, {});
		}
		
		this.logDebug(8, "Performing index search", query);
		
		var state = query;
		state.config = config;
		state.record_ids = Object.create(null);
		state.first = true;
		
		// track detailed perf of search operations
		if (!state.perf) {
			state.perf = new Perf();
			state.perf.begin();
		}
		
		// first, split criteria into subs (sub-queries), 
		// stds (standard queries) and negs (negative queries)
		var subs = [], stds = [], negs = [];
		for (var idx = 0, len = query.criteria.length; idx < len; idx++) {
			var crit = query.criteria[idx];
			if (crit.criteria) subs.push( crit );
			else {
				var def = Tools.findObject( config.fields, { id: crit.index } );
				if (!def) {
					this.logError('index', "Invalid search query: Index not found: " + crit.index, query);
					return callback(null, {}, state);
				}
				crit.def = def;
				
				if (crit.negative) negs.push( crit );
				else stds.push( crit );
			}
		}
		
		// stds need to be weighed and sorted by weight ascending
		var wpf = state.perf.begin('weigh');
		async.eachLimit( (query.mode == 'and') ? stds : [], this.concurrency,
			function(crit, callback) {
				self.weighCriterion(crit, config, callback);
			},
			function(err) {
				wpf.end();
				
				// sort stds by weight ascending (only needed in AND mode)
				if (query.mode == 'and') {
					stds = stds.sort( function(a, b) { return a.weight - b.weight; } );
				}
				
				// generate series of tasks, starting with any sub-queries,
				// then sorted weighed criteria, then negative criteria
				var tasks = [].concat( subs, stds, negs );
				async.eachSeries( tasks,
					function(task, callback) {
						task.perf = state.perf;
						
						if (task.criteria) {
							// sub-query	
							self._searchRecords( task, config, function(err, records) {
								state.perf.count('subs', 1);
								self.mergeIndex( state.record_ids, records, state.first ? 'or' : state.mode );
								state.first = false;
								callback();
							} );
						}
						else if (task.skip) {
							// skip this task (all words removed)
							process.nextTick( function() { callback(); } );
						}
						else if (task.def.type) {
							// custom index type, e.g. date, time, number
							var func = 'searchIndex_' + task.def.type;
							if (!self[func]) return callback( new Error("Unknown index type: " + task.def.type) );
							
							var cpf = state.perf.begin('search_' + task.def.id + '_' + task.def.type);
							self[func]( task, state, function(err) {
								cpf.end();
								state.perf.count(task.def.type + 's', 1);
								callback(err);
							} );
						}
						else if (task.literal) {
							// literal multi-word phrase
							var spf = state.perf.begin('search_' + task.def.id + '_literal');
							self.searchWordIndexLiteral(task, state, function(err) {
								spf.end();
								state.perf.count('literals', 1);
								callback(err);
							});
						}
						else {
							// single word search
							var spf = state.perf.begin('search_' + task.def.id + '_word');
							self.searchWordIndex(task, state, function(err) {
								spf.end();
								state.perf.count('words', 1);
								callback(err);
							});
						}
					},
					function(err) {
						// complete
						if (err) {
							self.logError('index', "Index search failed: " + err);
							state.record_ids = {};
							state.err = err;
						}
						self.logDebug(10, "Search complete", state.record_ids);
						callback(null, state.record_ids, Tools.copyHashRemoveKeys(state, { config:1, record_ids:1, first:1 }));
					}
				); // eachSeries (tasks)
			} // weigh done
		); // eachLimit (weigh)
	},
	
	searchWordIndex: function(query, state, callback) {
		// run one word query (single word against one index)
		var self = this;
		var config = state.config;
		var def = query.def;
		this.logDebug(10, "Running word query", query);
		
		var mode = state.first ? 'or' : state.mode;
		if (query.negative) mode = 'not';
		state.first = false;
		
		var path = config.base_path + '/' + def.id + '/word/' + query.word;
		var cur_items = state.record_ids;
		var new_items = Object.create(null);
		
		// query optimizations
		var num_cur_items = Tools.numKeys(cur_items);
		
		// if current items is empty and mode = and|not, we can exit early
		if (!num_cur_items && ((mode == 'and') || (mode == 'not'))) {
			process.nextTick( callback );
			return;
		}
		
		// Decide on row scan or hash merge:
		// If query weight (hash length) divided by page size is greater than num_cur_items
		// then it would probably be faster to apply the logic using _data getMulti (a.k.a row scan).
		// Otherwise, perform a normal hash merge (which has to read every hash page).
		var hash_page_size = config.hash_page_size || 1000;
		var wpf = state.perf.begin('word_' + query.word);
		
		if ((mode == 'and') && query.weight && (query.weight / hash_page_size > num_cur_items)) {
			this.logDebug(10, "Performing row scan on " + num_cur_items + " items", query);
			
			var record_ids = Object.keys( cur_items );
			var data_paths = record_ids.map( function(record_id) {
				return config.base_path + '/_data/' + record_id;
			} );
			
			var rspf = state.perf.begin('row_scan');
			this.getMulti( data_paths, function(err, datas) {
				rspf.end();
				if (err) return callback(err);
				
				datas.forEach( function(data, idx) {
					var record_id = record_ids[idx];
					if (!data || !data[def.id] || !data[def.id].words || (data[def.id].words.indexOf(query.word) == -1)) {
						delete cur_items[record_id];
					}
				} );
				
				state.perf.count('rows_scanned', datas.length);
				wpf.end();
				callback();
			} ); // getMulti
		} // row scan
		else {
			this.logDebug(10, "Performing '" + mode + "' hash merge on " + num_cur_items + " items", query);
			
			var hmpf = state.perf.begin('hash_merge');
			this.hashEachPage( path,
				function(items, callback) {
					switch (mode) {
						case 'and':
							for (var key in items) {
								if (key in cur_items) new_items[key] = 1;
							}
						break;
						
						case 'or':
							for (var key in items) {
								cur_items[key] = 1;
							}
						break;
						
						case 'not':
							for (var key in items) {
								delete cur_items[key];
							}
						break;
					}
					state.perf.count('hash_pages', 1);
					callback();
				},
				function(err) {
					hmpf.end();
					wpf.end();
					if (mode == 'and') state.record_ids = new_items;
					callback(err);
				}
			);
		} // hash merge
	},
	
	searchWordIndexLiteral: function(query, state, callback) {
		// run literal search query (list of words which must be in sequence)
		var self = this;
		var def = query.def;
		this.logDebug(10, "Running literal word query", query);
		
		var mode = state.first ? 'or' : state.mode;
		if (query.negative) mode = 'not';
		state.first = false;
		
		var path_prefix = state.config.base_path + '/' + def.id + '/word/';
		var record_ids = state.record_ids;
		
		var temp_results = Object.create(null);
		var temp_idx = 0;
		
		async.eachSeries( query.words,
			function(word, callback) {
				// for each word, iterate over record ids
				var keepers = Object.create(null);
				var wpf = state.perf.begin('literal_' + word);
				
				self.hashEachSync( path_prefix + word,
					function(record_id, raw_value) {
						// instant rejection if temp_idx and record_id isn't already present
						if (temp_idx && !(record_id in temp_results)) return;
						
						var offset_list = raw_value.split(/\,/);
						var still_good = 0;
						
						for (var idx = offset_list.length - 1; idx >= 0; idx--) {
							var word_idx = parseInt( offset_list[idx] );
							
							if (temp_idx) {
								// Subsequent pass -- make sure offsets are +1
								var arr = temp_results[record_id];
								for (var idy = 0, ley = arr.length; idy < ley; idy++) {
									var elem = arr[idy];
									if (word_idx == elem + 1) {
										arr[idy]++;
										still_good = 1;
									}
								}
							} // temp_idx
							else {
								// First pass -- get word idx into temp_results
								if (!temp_results[record_id]) temp_results[record_id] = [];
								temp_results[record_id].push( word_idx );
								still_good = 1;
							}
						} // foreach word_idx
						
						if (!still_good) delete temp_results[record_id];
						else keepers[record_id] = 1;
					},
					function(err) {
						wpf.end();
						// If in a subsequent word pass, make sure all temp_results
						// ids are still matched in the latest word
						if (temp_idx > 0) self.mergeIndex( temp_results, keepers, 'and' );
						temp_idx++;
						
						callback();
					}
				); // hashEachSync (word)
			},
			function(err) {
				// all done, now merge data into record ids
				for (var record_id in temp_results) {
					temp_results[record_id] = 1; // cleanup values
				}
				
				self.mergeIndex( record_ids, temp_results, mode );
				callback(err);
			}
		);
	},
	
	mergeIndex: function(record_ids, dbh, mode) {
		// Merge record ID keys from index subnode into hash
		switch (mode || 'or') {
			case 'and':
				for (var key in record_ids) {
					if (!(key in dbh)) delete record_ids[key];
				}
			break;
			
			case 'not':
				for (var key in dbh) {
					delete record_ids[key];
				}
			break;
			
			case 'or':
				for (var key in dbh) {
					record_ids[key] = dbh[key];
				}
			break;
		}
	},
	
	sortRecords: function(record_hash, sorter_id, sort_dir, config, callback) {
		// sort records by sorter index
		var self = this;
		if (!sort_dir) sort_dir = 1;
		
		if (self.debugLevel(8)) {
			self.logDebug(8, "Sorting " + Tools.numKeys(record_hash) + " records by " + sorter_id + " (" + sort_dir + ")", {
				path: config.base_path
			});
		}
		
		var sorter = Tools.findObject( config.sorters, { id: sorter_id } );
		if (!sorter) return callback( new Error("Cannot find sorter: " + sorter_id) );
		
		// apply sort values to record hash
		var path = config.base_path + '/' + sorter.id + '/sort';
		var sort_pairs = [];
		var pf = this.perf.begin('sort');
		
		this.hashEachPage( path, 
			function(items, callback) {
				for (var key in items) {
					if (key in record_hash) {
						sort_pairs.push([ key, items[key] ]);
					}
				}
				callback();
			},
			function() {
				// setup comparator function
				var comparator = (sorter.type == 'number') ?
					function(a, b) { return (a[1] - b[1]) * sort_dir; } :
					function(a, b) { return a[1].toString().localeCompare( b[1] ) * sort_dir; };
				
				// now we can sort
				sort_pairs.sort( comparator );
				
				// copy ids back to simple array
				var record_ids = [];
				for (var idx = 0, len = sort_pairs.length; idx < len; idx++) {
					record_ids.push( sort_pairs[idx][0] );
				}
				
				var elapsed = pf.end();
				self.logTransaction('sort', config.base_path, {
					sorter_id: sorter_id,
					sorter_type: sorter.type || 'string',
					sort_dir: sort_dir,
					elapsed_ms: elapsed,
					records: record_ids.length
				});
				
				self.logDebug(8, "Sort complete, returning results");
				callback( null, record_ids, sort_pairs, comparator );
			}
		); // hashEachPage
	},
	
	getFieldSummary: function(id, config, callback) {
		// get field summary for specified field
		this.get( config.base_path + '/' + id + '/summary', function(err, data) {
			if (err) return callback(err);
			if (!data) return callback( new Error("Index field not found: " + config.base_path + '/' + id) );
			if (!data.values) data.values = {};
			data.values = Tools.copyHashRemoveProto( data.values );
			callback( null, data.values );
		} );
	},
	
	cacheRemoveWords: function(config) {
		// cache remove words in hash for speed
		if (!this.removeWordCache) this.removeWordCache = {};
		
		if (this.removeWordCache[config.base_path]) {
			return this.removeWordCache[config.base_path];
		}
		
		// build cache
		var cache = Object.create(null);
		this.removeWordCache[config.base_path] = cache;
		
		for (var idx = 0, len = config.remove_words.length; idx < len; idx++) {
			cache[ config.remove_words[idx] ] = 1;
		}
		
		return cache;
	}
	
});
```

## File: `list-splice.js`
```javascript
// PixlServer Storage System - List Splice Mixin
// Copyright (c) 2017 Joseph Huckaby
// Released under the MIT License

var util = require("util");
var async = require('async');
var Class = require("pixl-class");
var Tools = require("pixl-tools");

// support for older node versions
var isArray = Array.isArray || util.isArray;

module.exports = Class.create({
	
	listSplice: function(key, idx, len, new_items, callback) {
		// Cut any size chunk out of list, optionally replacing it with a new chunk of any size
		var self = this;
		if (!new_items) new_items = [];
		if (!isArray(new_items)) new_items = [new_items];
		var num_new = new_items.length;
		
		idx = parseInt( idx || 0 );
		if (isNaN(idx)) return callback( new Error("Position must be an integer.") );
		
		len = parseInt( len || 0 );
		if (isNaN(len)) return callback( new Error("Length must be an integer.") );
		
		this.logDebug(9, "Splicing " + len + " items at position " + idx + " in list: " + key, this.debugLevel(10) ? new_items : null);
		
		this._listLock( key, true, function() {
			// locked
			self._listLoad(key, false, function(err, list) {
				// check for error
				if (err) {
					self._listUnlock(key);
					return callback(err);
				}
				
				// Manage bounds, allow negative
				if (idx < 0) { idx += list.length; }
				// if (!len) { len = list.length - idx; }
				if (idx + len > list.length) { len = list.length - idx; }
				
				// bounds check
				if ((idx < 0) || (idx > list.length)) {
					self._listUnlock(key);
					return callback( new Error("List index out of bounds.") );
				}
				
				if (!len && !num_new) {
					// nothing to cut, nothing to insert, so we're already done
					self._listUnlock(key);
					return callback(null, []);
				}
				if (!len && (idx == list.length)) {
					// nothing to cut and idx is at the list end, so push instead
					self._listUnlock(key);
					return self.listPush( key, new_items, function(err) { callback(err, []); } );
				}
				if (!len && !idx) {
					// nothing to cut and idx is at the list beginning, so unshift instead
					self._listUnlock(key);
					return self.listUnshift( key, new_items, function(err) { callback(err, []); } );
				}
				
				if (!idx && list.length && (len == list.length) && !num_new) {
					// special case: cutting ALL items from list, and not replacing any
					// need to create a proper empty list, and return the items
					self._listUnlock(key);
					self.listGet( key, idx, len, function(err, items) {
						if (err) return callback(err);
						
						self.listDelete( key, false, function(err) {
							if (err) return callback(err);
							callback(null, items);
						} );
					} );
					return;
				}
				
				var complete = function(err, cut_items) {
					// finally, save list metadata
					if (err) {
						self._listUnlock(key);
						return callback(err, null);
					}
					
					self.put( key, list, function(err, data) {
						self._listUnlock(key);
						if (err) return callback(err, null);
						
						// success, return spliced items
						callback(null, cut_items);
					} );
				};
				
				// jump to specialized method for splice type
				var right_side = !!(idx + (len / 2) >= list.length / 2);
				var cut_func = right_side ? "_listCutRight" : "_listCutLeft";
				var ins_func = right_side ? "_listInsertRight" : "_listInsertLeft";
				
				if (num_new == len) {
					// simple replace
					self._listSpliceSimple( list, key, idx, len, new_items, complete );
				}
				else if (len) {
					// cut first, then maybe insert
					self[cut_func]( list, key, idx, len, function(err, cut_items) {
						if (err) return complete(err);
						
						// done with cut, now insert?
						if (num_new) {
							self[ins_func]( list, key, idx, new_items, function(err) {
								// insert complete
								return complete(err, cut_items);
							} ); // ins_func
						} // num_new
						else {
							// no insert needed, cut only
							complete(err, cut_items);
						}
					} ); // cut_func
				}
				else {
					// insert only
					self[ins_func]( list, key, idx, new_items, function(err) {
						// insert complete
						return complete(err, []);
					} ); // ins_func
				}
				
			} ); // loaded
		} ); // locked
	},
	
	_listSpliceSimple: function(list, key, idx, len, new_items, callback) {
		// perform simple list splice where replacement is the same length as the cut
		// i.e. list doesn't have to grow or shrink
		var self = this;
		var page_idx = list.first_page;
		var chunk_size = list.page_size;
		var num_fp_items = 0;
		var cut_items = [];
		
		this.logDebug(9, "Performing simple splice", { key: key, idx: idx, cut: len, add: new_items.length, list: list });
		
		async.whilst(
			function() { return page_idx <= list.last_page; },
			function(callback) {
				self._listLoadPage(key, page_idx, false, function(err, page) {
					if (err) return callback(err);
					
					var page_key = key + '/' + page_idx;
					var page_start_idx = 0;
					
					if (page_idx == list.first_page) {
						num_fp_items = page.items.length;
						if (idx >= num_fp_items) {
							// find page we need to jump to
							page_idx = list.first_page + 1 + Math.floor((idx - num_fp_items) / chunk_size);
							return callback(null);
						}
					} // first page
					else {
						page_start_idx = num_fp_items + ((page_idx - list.first_page - 1) * chunk_size);
					}
					
					var local_idx = idx - page_start_idx;
					
					while (len && (local_idx >= 0) && (local_idx < page.items.length)) {
						cut_items.push( page.items[local_idx] );
						page.items[local_idx++] = new_items.shift();
						idx++;
						len--;
					}
					
					if (!len) page_idx = list.last_page;
					page_idx++;
					
					self.put( page_key, page, callback );
				} );
			},
			function(err) {
				// all pages updated
				if (err) return callback(err, null);
				callback( null, cut_items );
			}
		); // pages loaded
	},
	
	_listCutRight: function(list, key, idx, len, callback) {
		// perform list cut on the "right" side (from last_page inward)
		var self = this;
		var page_idx = list.first_page;
		var chunk_size = list.page_size;
		var delta = 0 - len; // will be negative
		var num_fp_items = 0;
		var cut_items = [];
		var page_cache = [];
		
		this.logDebug(9, "Performing right-side cut", { key: key, idx: idx, cut: len, list: list });
		
		async.whilst(
			function() { return page_idx <= list.last_page; },
			function(callback) {
				self._listLoadPage(key, page_idx, true, function(err, page) {
					if (err) return callback(err);
					
					var page_key = key + '/' + page_idx;
					var page_start_idx = 0;
					
					if (page_idx == list.first_page) {
						num_fp_items = page.items.length;
						if (idx >= num_fp_items) {
							// find page we need to jump to
							page_idx = list.first_page + 1 + Math.floor((idx - num_fp_items) / chunk_size);
							return callback(null);
						}
					} // first page
					else {
						page_start_idx = num_fp_items + ((page_idx - list.first_page - 1) * chunk_size);
					}
					
					var local_idx = idx - page_start_idx;
					
					// cut mode
					while (len && (local_idx >= 0) && (local_idx < page.items.length)) {
						cut_items.push( page.items[local_idx] );
						page.items.splice( local_idx, 1 );
						idx++;
						len--;
					}
					
					// fill gaps
					var cidx = 0;
					while (!len && page.items.length && (cidx < page_cache.length)) {
						while (!len && page.items.length && (page_cache[cidx].page.items.length < chunk_size)) {
							page_cache[cidx].page.items.push( page.items.shift() );
						}
						cidx++;
					}
					
					// add current page to write cache
					page_cache.push({
						page_idx: page_idx,
						page_key: page_key,
						page: page
					});
					
					// advance page
					page_idx++;
					
					// eject page from cache if full and ready to write
					if (page_cache.length && (page_cache[0].page.items.length == chunk_size)) {
						var cpage = page_cache.shift();
						self.put( cpage.page_key, cpage.page, callback );
					}
					else callback();
				} );
			},
			function(err) {
				// all pages updated
				if (err) return callback(err, null);
				
				// write all remaining cache entries
				async.eachLimit(page_cache, self.concurrency, 
					function(cpage, callback) {
						// iterator for each page
						if (cpage.page.items.length || (list.first_page == list.last_page)) {
							self.put( cpage.page_key, cpage.page, callback );
						}
						else {
							// delete page
							list.last_page--;
							self.delete( cpage.page_key, callback );
						}
					}, 
					function(err) {
						// all pages stored
						list.length += delta; // will be negative
						callback( null, cut_items );
					}
				); // eachLimit
			} // all pages complete
		); // pages loaded
	},
	
	_listCutLeft: function(list, key, idx, len, callback) {
		// perform list cut on the "left" side (from first_page inward)
		var self = this;
		var page_idx = list.last_page;
		var chunk_size = list.page_size;
		var delta = 0 - len; // will be negative
		var num_fp_items = 0;
		var num_lp_items = 0;
		var cut_items = [];
		var page_cache = [];
		
		this.logDebug(9, "Performing left-side cut", { key: key, idx: idx, cut: len, list: list });
		
		idx += (len - 1);
		var ridx = (list.length - 1) - idx;
		
		async.whilst(
			function() { return page_idx >= list.first_page; },
			function(callback) {
				self._listLoadPage(key, page_idx, true, function(err, page) {
					if (err) return callback(err);
					
					var page_key = key + '/' + page_idx;
					var page_start_idx = 0;
					
					if (page_idx == list.last_page) {
						num_lp_items = page.items.length;
						if (list.last_page == list.first_page) num_fp_items = num_lp_items;
						else {
							num_fp_items = ((list.length - num_lp_items) % chunk_size) || chunk_size;
						}
						if (ridx >= num_lp_items) {
							// find page we need to jump to
							page_idx = (list.last_page - 1) - Math.floor((ridx - num_lp_items) / chunk_size);
							return callback(null);
						}
					} // last page
					
					if (page_idx != list.first_page) {
						page_start_idx = num_fp_items + ((page_idx - list.first_page - 1) * chunk_size);
					}
					
					var local_idx = idx - page_start_idx;
					
					// cut mode
					while (len && (local_idx >= 0) && (local_idx < page.items.length)) {
						cut_items.unshift( page.items[local_idx] );
						page.items.splice( local_idx--, 1 );
						idx--;
						len--;
					}
					
					// fill gaps
					var cidx = 0;
					while (!len && page.items.length && (cidx < page_cache.length)) {
						while (!len && page.items.length && (page_cache[cidx].page.items.length < chunk_size)) {
							page_cache[cidx].page.items.unshift( page.items.pop() );
						}
						cidx++;
					}
					
					// add current page to write cache
					page_cache.push({
						page_idx: page_idx,
						page_key: page_key,
						page: page
					});

					// advance page
					page_idx--;
					
					// eject page from cache if full and ready to write
					if (page_cache.length && (page_cache[0].page.items.length == chunk_size)) {
						var cpage = page_cache.shift();
						self.put( cpage.page_key, cpage.page, callback );
					}
					else callback();
				} );
			},
			function(err) {
				// all pages updated
				if (err) return callback(err, null);
				
				// write all remaining cache entries
				async.eachLimit(page_cache, self.concurrency, 
					function(cpage, callback) {
						// iterator for each page
						if (cpage.page.items.length || (list.first_page == list.last_page)) {
							self.put( cpage.page_key, cpage.page, callback );
						}
						else {
							// delete page
							list.first_page++;
							self.delete( cpage.page_key, callback );
						}
					}, 
					function(err) {
						// all pages stored
						list.length += delta; // will be negative
						callback( null, cut_items );
					}
				); // eachLimit
			} // all pages complete
		); // pages loaded
	},
	
	_listInsertRight: function(list, key, idx, new_items, callback) {
		// perform list insert on the "right" side (expand towards last_page)
		var self = this;
		var page_idx = list.first_page;
		var chunk_size = list.page_size;
		var delta = new_items.length;
		var num_fp_items = 0;
		var buffer = [];
		
		this.logDebug(9, "Performing right-side insert", { key: key, idx: idx, add: delta, list: list });
		
		async.whilst(
			function() { return page_idx <= list.last_page; },
			function(callback) {
				self._listLoadPage(key, page_idx, true, function(err, page) {
					if (err) return callback(err);
					
					var page_key = key + '/' + page_idx;
					var page_start_idx = 0;
					
					if (page_idx == list.first_page) {
						num_fp_items = page.items.length;
						if (num_fp_items && (idx >= num_fp_items)) {
							// find page we need to jump to
							page_idx = list.first_page + 1 + Math.floor((idx - num_fp_items) / chunk_size);
							
							// this may be an end-of-list insert, in which case we have to short circuit the page jump
							if (page_idx > list.last_page) page_idx = list.last_page;
							if (page_idx != list.first_page) return callback(null);
						}
					} // first page
					else {
						page_start_idx = num_fp_items + ((page_idx - list.first_page - 1) * chunk_size);
					}
					
					var local_idx = idx - page_start_idx;
					
					if (new_items.length) {
						// insert mode
						var orig_items_len = page.items.length;
						while (new_items.length && (local_idx >= 0) && (local_idx < chunk_size)) {
							if (local_idx < orig_items_len) buffer.push( page.items[local_idx] );
							page.items[local_idx++] = new_items.shift();
							idx++;
						}
					}
					
					// cleanup mode
					if (!new_items.length && buffer.length && (local_idx >= 0) && (local_idx < chunk_size)) {
						
						// page.items.splice( local_idx, 0, buffer );
						buffer.unshift( local_idx, 0 );
						[].splice.apply( page.items, buffer );
						
						if (page.items.length > chunk_size) buffer = page.items.splice(chunk_size);
						else buffer = [];
						idx = page_start_idx + page.items.length;
					}
					
					if (page_idx == list.first_page) num_fp_items = page.items.length;
					
					page_idx++;
					if ((page_idx > list.last_page) && (new_items.length || buffer.length)) {
						// extend list by a page
						list.last_page = page_idx;
					}
					
					self.put( page_key, page, callback );
				} );
			},
			function(err) {
				// all pages updated
				if (err) return callback(err, null);
				list.length += delta;
				callback( null );
			}
		); // pages loaded
	},
	
	_listInsertLeft: function(list, key, idx, new_items, callback) {
		// perform list insert on the "left" side (expand towards first_page)
		var self = this;
		var page_idx = list.last_page;
		var chunk_size = list.page_size;
		var delta = new_items.length;
		var num_fp_items = 0;
		var num_lp_items = 0;
		var num_new_pages = 0;
		var buffer = [];
		
		this.logDebug(9, "Performing left-side insert", { key: key, idx: idx, add: delta, list: list });
		
		idx--;
		var ridx = (list.length - 1) - idx;
		
		async.whilst(
			function() { 
				return( (page_idx >= list.first_page) || new_items.length || buffer.length ); 
			},
			function(callback) {
				self._listLoadPage(key, page_idx, true, function(err, page) {
					if (err) return callback(err);
					
					var page_key = key + '/' + page_idx;
					var page_start_idx = 0;
					
					if (page_idx == list.last_page) {
						num_lp_items = page.items.length;
						if (list.last_page == list.first_page) num_fp_items = num_lp_items;
						else {
							num_fp_items = ((list.length - num_lp_items) % chunk_size) || chunk_size;
						}
						if (num_lp_items && (ridx >= num_lp_items)) {
							// find page we need to jump to
							page_idx = (list.last_page - 1) - Math.floor((ridx - num_lp_items) / chunk_size);
							
							// this may be an start-of-list insert, in which case we have to short circuit the page jump
							if (page_idx < list.first_page) page_idx = list.first_page;
							if (page_idx != list.last_page) return callback(null);
						}
					} // last page
					
					if (page_idx != list.first_page) {
						page_start_idx = num_fp_items + ((page_idx - list.first_page - 1) * chunk_size);
					}
					
					var local_idx = idx - page_start_idx;
					if (local_idx >= page.items.length) local_idx = page.items.length - 1;
					
					if (new_items.length) {
						// insert mode
						while (new_items.length) {
							if (local_idx >= 0) {
								buffer.unshift( page.items[local_idx] );
								page.items[local_idx--] = new_items.pop();
							}
							else if (page.items.length < chunk_size) {
								page.items.unshift( new_items.pop() );
							}
							else break;
							idx--;
						}
					}
					
					// cleanup mode
					if (!new_items.length && buffer.length && (local_idx >= -1) && (local_idx < chunk_size)) {
						
						// page.items.splice( local_idx + 1, 0, buffer );
						buffer.unshift( local_idx + 1, 0 );
						[].splice.apply( page.items, buffer );
						
						if (page.items.length > chunk_size) buffer = page.items.splice( 0, page.items.length - chunk_size );
						else buffer = [];
						// idx = page_start_idx - 1;
					}
					idx = page_start_idx - 1;
					
					if (page_idx == list.first_page) num_fp_items = page.items.length;
					if (page_idx == list.last_page) num_lp_items = page.items.length;
					
					page_idx--;
					if ((page_idx < list.first_page) && (new_items.length || buffer.length)) {
						// extend list by a page
						num_new_pages++;
					}
					
					self.put( page_key, page, callback );
				} );
			},
			function(err) {
				// all pages updated
				if (err) return callback(err, null);
				list.first_page -= num_new_pages;
				list.length += delta;
				callback( null );
			}
		); // pages loaded
	}
	
});
```

## File: `list.js`
```javascript
// PixlServer Storage System - List Mixin
// Copyright (c) 2015 Joseph Huckaby
// Released under the MIT License

var util = require("util");
var async = require('async');
var Class = require("pixl-class");
var Tools = require("pixl-tools");

var ListSplice = require("./list-splice.js");

// support for older node versions
var isArray = Array.isArray || util.isArray;

module.exports = Class.create({
	
	__mixins: [ ListSplice ],
	
	listCreate: function(key, opts, callback) {
		// Create new list
		var self = this;
		
		if (!opts) opts = {};
		if (!opts.page_size) opts.page_size = this.listItemsPerPage;
		opts.first_page = 0;
		opts.last_page = 0;
		opts.length = 0;
		opts.type = 'list';
		
		this.logDebug(9, "Creating new list: " + key, opts);
		
		this.get(key, function(err, list) {
			if (list) {
				// list already exists
				return callback(null, list);
			}
			self.put( key, opts, function(err) {
				if (err) return callback(err);
				
				// create first page
				self.put( key + '/0', { type: 'list_page', items: [] }, function(err) {
					if (err) return callback(err);
					else callback(null, opts);
				} );
			} ); // header created
		} ); // get check
	},
	
	_listLoad: function(key, create_opts, callback) {
		// Internal method, load list root, create if doesn't exist
		var self = this;
		if (create_opts && (typeof(create_opts) != 'object')) create_opts = {};
		this.logDebug(9, "Loading list: " + key);
		
		this.get(key, function(err, data) {
			if (data) {
				// list already exists
				callback(null, data);
			}
			else if (create_opts && err && (err.code == "NoSuchKey")) {
				// create new list, ONLY if record was not found (and not some other error)
				self.logDebug(9, "List not found, creating it: " + key, create_opts);
				self.listCreate(key, create_opts, function(err, data) {
					if (err) callback(err, null);
					else callback( null, data );
				} );
			}
			else {
				// no exist and no create, or some other error
				self.logDebug(9, "List could not be loaded: " + key + ": " + err);
				callback(err, null);
			}
		} ); // get
	},
	
	_listLoadPage: function(key, idx, create, callback) {
		// Internal method, load page from list, create if doesn't exist
		var self = this;
		var page_key = key + '/' + idx;
		this.logDebug(9, "Loading list page: " + page_key);
		
		this.get(page_key, function(err, data) {
			if (data) {
				// list page already exists
				callback(null, data);
			}
			else if (create && err && (err.code == "NoSuchKey")) {
				// create new list page, ONLY if record was not found (and not some other error)
				self.logDebug(9, "List page not found, creating it: " + page_key);
				callback( null, { type: 'list_page', items: [] } );
			}
			else {
				// no exist and no create
				self.logDebug(9, "List page could not be loaded: " + page_key + ": " + err);
				callback(err, null);
			}
		} ); // get
	},
	
	_listLock: function(key, wait, callback) {
		// internal list lock wrapper
		// uses unique key prefix so won't deadlock with user locks
		this.lock( '|'+key, wait, callback );
	},
	
	_listUnlock: function(key) {
		// internal list unlock wrapper
		this.unlock( '|'+key );
	},
	
	_listShareLock: function(key, wait, callback) {
		// internal list shared lock wrapper
		// uses unique key prefix so won't deadlock with user locks
		this.shareLock( 'C|'+key, wait, callback );
	},
	
	_listShareUnlock: function(key) {
		// internal list shared unlock wrapper
		this.shareUnlock( 'C|'+key );
	},
	
	listPush: function(key, items, create_opts, callback) {
		// Push new items onto end of list
		var self = this;
		if (!callback && (typeof(create_opts) == 'function')) {
			callback = create_opts;
			create_opts = {};
		}
		var list = null;
		var page = null;
		if (!isArray(items)) items = [items];
		this.logDebug(9, "Pushing " + items.length + " items onto end of list: " + key, this.debugLevel(10) ? items : null);
		
		this._listLock(key, true, function() {
			async.series([
				function(callback) {
					// first load list header
					self._listLoad(key, create_opts, function(err, data) {
						list = data; 
						callback(err, data);
					} );
				},
				function(callback) {
					// now load last page in list
					self._listLoadPage(key, list.last_page, 'create', function(err, data) {
						page = data;
						callback(err, data);
					} );
				}
			],
			function(err, results) {
				// list and page loaded, proceed with push
				if (err) {
					self._listUnlock(key);
					return callback(err, null);
				}
				
				// populate tasks array with records to save
				var tasks = [];
				
				// split items into pages
				var item = null;
				var count = 0;
				while (item = items.shift()) {
					// make sure item is an object
					if (typeof(item) != 'object') continue;
					
					// if last page is full, we need to create a new one
					if (page.items.length >= list.page_size) {
						// complete current page, queue for save
						if (count) tasks.push({ key: key + '/' + list.last_page, data: page });
						
						// add new page
						list.last_page++;
						page = { type: 'list_page', items: [] };
					}
					
					// push item onto list
					page.items.push( item );
					list.length++;
					count++;
				} // foreach item
				
				if (!count) {
					self._listUnlock(key);
					return callback(new Error("No valid objects found to add."), null);
				}
				
				// add current page, and main list record
				tasks.push({ key: key + '/' + list.last_page, data: page });
				tasks.push({ key: key, data: list });
				
				// save all pages and main list
				var lastErr = null;
				var q = async.queue(function (task, callback) {
					self.put( task.key, task.data, callback );
				}, self.concurrency );
				
				q.drain = function() {
					// all pages saved, complete
					self._listUnlock(key);
					callback(lastErr, list);
				};
				
				q.push( tasks, function(err) {
					lastErr = err;
				} );
				
			} ); // loaded
		} ); // locked
	},
	
	listUnshift: function(key, items, create_opts, callback) {
		// Unshift new items onto beginning of list
		var self = this;
		if (!callback && (typeof(create_opts) == 'function')) {
			callback = create_opts;
			create_opts = {};
		}
		var list = null;
		var page = null;
		if (!isArray(items)) items = [items];
		this.logDebug(9, "Unshifting " + items.length + " items onto beginning of list: " + key, this.debugLevel(10) ? items : null);
		
		this._listLock( key, true, function() {
			async.series([
				function(callback) {
					// first load list header
					self._listLoad(key, create_opts, function(err, data) {
						list = data; 
						callback(err, data);
					} );
				},
				function(callback) {
					// now load first page in list
					self._listLoadPage(key, list.first_page, 'create', function(err, data) {
						page = data;
						callback(err, data);
					} );
				}
			],
			function(err, results) {
				// list and page loaded, proceed with unshift
				if (err) {
					self._listUnlock(key);
					return callback(err, null);
				}
				
				// populate tasks array with records to save
				var tasks = [];
				
				// split items into pages
				var item = null;
				var count = 0;
				while (item = items.pop()) {
					// make sure item is an object
					if (typeof(item) != 'object') continue;
					
					// if last page is full, we need to create a new one
					if (page.items.length >= list.page_size) {
						// complete current page, queue for save
						if (count) tasks.push({ key: key + '/' + list.first_page, data: page });
						
						// add new page
						list.first_page--;
						page = { type: 'list_page', items: [] };
					}
					
					// push item onto list
					page.items.unshift( item );
					list.length++;
					count++;
				} // foreach item
				
				if (!count) {
					self._listUnlock(key);
					return callback(new Error("No valid objects found to add."), null);
				}
				
				// add current page, and main list record
				tasks.push({ key: key + '/' + list.first_page, data: page });
				tasks.push({ key: key, data: list });
				
				// save all pages and main list
				var lastErr = null;
				var q = async.queue(function (task, callback) {
					self.put( task.key, task.data, callback );
				}, self.concurrency );
				
				q.drain = function() {
					// all pages saved, complete
					self._listUnlock(key);
					callback(lastErr, list);
				};
				
				q.push( tasks, function(err) {
					lastErr = err;
				} );
				
			} ); // loaded
		} ); // locked
	},
	
	listPop: function(key, callback) {
		// Pop last item off end of list, shrink as necessary, return item
		var self = this;
		var list = null;
		var page = null;
		this.logDebug(9, "Popping item off end of list: " + key);
		
		this._listLock( key, true, function() {
			async.series([
				function(callback) {
					// first load list header
					self._listLoad(key, false, function(err, data) {
						list = data; 
						callback(err, data);
					} );
				},
				function(callback) {
					// now load last page in list
					self._listLoadPage(key, list.last_page, false, function(err, data) {
						page = data;
						callback(err, data);
					} );
				}
			],
			function(err, results) {
				// list and page loaded, proceed with pop
				if (err) {
					self._listUnlock(key);
					return callback(err, null);
				}
				if (!page.items.length) {
					self._listUnlock(key);
					return callback( null, null );
				}
				
				var actions = [];
				var item = page.items.pop();
				var old_last_page = list.last_page;
				
				if (!page.items.length) {
					// out of items in this page, delete page, adjust list
					if (list.last_page > list.first_page) {
						list.last_page--;
						
						actions.push( 
							function(callback) { self.delete( key + '/' + old_last_page, callback ); } 
						);
					}
					else {
						// list is empty, create new first page
						actions.push( 
							function(callback) { self.put( key + '/' + old_last_page, { type: 'list_page', items: [] }, callback ); } 
						);
					}
				}
				else {
					// still have items left, save page
					actions.push( 
						function(callback) { self.put( key + '/' + list.last_page, page, callback ); } 
					);
				}
				
				// shrink list
				list.length--;
				actions.push( 
					function(callback) { self.put( key, list, callback ); } 
				);
				
				// save everything in parallel
				async.parallel( actions, function(err, results) {
					// success, fire user callback
					self._listUnlock(key);
					callback(err, err ? null : item);
				} ); // save complete
				
			} ); // loaded
		} ); // locked
	},
	
	listShift: function(key, callback) {
		// Shift first item off beginning of list, shrink as necessary, return item
		var self = this;
		var list = null;
		var page = null;
		this.logDebug(9, "Shifting item off beginning of list: " + key);
		
		this._listLock( key, true, function() {
			async.series([
				function(callback) {
					// first load list header
					self._listLoad(key, false, function(err, data) {
						list = data; 
						callback(err, data);
					} );
				},
				function(callback) {
					// now load first page in list
					self._listLoadPage(key, list.first_page, false, function(err, data) {
						page = data;
						callback(err, data);
					} );
				}
			],
			function(err, results) {
				// list and page loaded, proceed with shift
				if (err) {
					self._listUnlock(key);
					return callback(err, null);
				}
				if (!page.items.length) {
					self._listUnlock(key);
					return callback( null, null );
				}
				
				var actions = [];
				var item = page.items.shift();
				var old_first_page = list.first_page;
				
				if (!page.items.length) {
					// out of items in this page, delete page, adjust list
					if (list.first_page < list.last_page) {
						list.first_page++;
						
						actions.push( 
							function(callback) { self.delete( key + '/' + old_first_page, callback ); } 
						);
					}
					else {
						// list is empty, create new first page
						actions.push( 
							function(callback) { self.put( key + '/' + old_first_page, { type: 'list_page', items: [] }, callback ); } 
						);
					}
				}
				else {
					// still have items left, save page
					actions.push( 
						function(callback) { self.put( key + '/' + list.first_page, page, callback ); } 
					);
				}
				
				// shrink list
				list.length--;
				actions.push( 
					function(callback) { self.put( key, list, callback ); } 
				);
				
				// save everything in parallel
				async.parallel( actions, function(err, results) {
					// success, fire user callback
					self._listUnlock(key);
					callback(err, err ? null : item);
				} ); // save complete
				
			} ); // loaded
		} ); // locked
	},
	
	listGet: function(key, idx, len, callback) {
		// Fetch chunk from list of any size, in any location
		// Use negative idx to fetch from end of list
		var self = this;
		var list = null;
		var page = null;
		var items = [];
		if (!this.started) return callback( new Error("Storage has not completed startup.") );
		
		idx = parseInt( idx || 0 );
		if (isNaN(idx)) return callback( new Error("Position must be an integer.") );
		
		len = parseInt( len || 0 );
		if (isNaN(len)) return callback( new Error("Length must be an integer.") );
		
		this.logDebug(9, "Fetching " + len + " items at position " + idx + " from list: " + key);
		
		async.series([
			function(callback) {
				// first we share lock
				self._listShareLock(key, true, callback);
			},
			function(callback) {
				// next load list header
				self._listLoad(key, false, function(err, data) {
					list = data; 
					callback(err, data);
				} );
			},
			function(callback) {
				// now load first page in list
				self._listLoadPage(key, list.first_page, false, function(err, data) {
					page = data;
					callback(err, data);
				} );
			}
		],
		function(err, results) {
			// list and page loaded, proceed with get
			if (err) {
				self._listShareUnlock(key);
				return callback(err, null, list);
			}
			
			// apply defaults if applicable
			if (!idx) idx = 0;
			if (!len) len = list.length;
			
			// range check
			if (list.length && (idx >= list.length)) {
				self._listShareUnlock(key);
				return callback( new Error("Index out of range"), null, list );
			}
			
			// Allow user to get items from end of list
			if (idx < 0) { idx += list.length; }
			if (idx < 0) { idx = 0; }
			
			if (idx + len > list.length) { len = list.length - idx; }
			
			// First page is special, as it is variably sized
			// and shifts the paging algorithm
			while (idx < page.items.length) {
				items.push( page.items[idx++] );
				len--;
				if (!len) break;
			}
			if (!len || (idx >= list.length)) {
				// all items were on first page, return now
				self._listShareUnlock(key);
				return callback( null, items, list );
			}
			
			// we need items from other pages
			var num_fp_items = page.items.length;
			var chunk_size = list.page_size;
			
			var first_page_needed = list.first_page + 1 + Math.floor((idx - num_fp_items) / chunk_size);
			var last_page_needed = list.first_page + 1 + Math.floor(((idx - num_fp_items) + len - 1) / chunk_size);
			var page_idx = first_page_needed;
			
			async.whilst(
				function() { return page_idx <= last_page_needed; },
				function(callback) {
					self._listLoadPage(key, page_idx, false, function(err, data) {
						if (err) return callback(err);
						var page = data;
						
						var page_start_idx = num_fp_items + ((page_idx - list.first_page - 1) * chunk_size);
						var local_idx = idx - page_start_idx;
						
						while ((local_idx >= 0) && (local_idx < page.items.length)) {
							items.push( page.items[local_idx++] );
							idx++;
							len--;
							if (!len) break;
						}
						
						if (!len) page_idx = last_page_needed;
						page_idx++;
						callback();
					} );
				},
				function(err) {
					// all pages loaded
					self._listShareUnlock(key);
					if (err) return callback(err, null);
					callback( null, items, list );
				}
			); // pages loaded
		} ); // list loaded
	},
	
	listFind: function(key, criteria, callback) {
		// Find single item in list given criteria -- WARNING: this can be slow with long lists
		var self = this;
		var num_crit = Tools.numKeys(criteria);
		this.logDebug(9, "Locating item in list: " + key, criteria);
		
		this._listShareLock(key, true, function() {
			// share locked
			self._listLoad(key, false, function(err, list) {
				// list loaded, proceed
				if (err) {
					self._listShareUnlock(key);
					return callback(err, null);
				}
				
				var item = null;
				var item_idx = 0;
				var page_idx = list.first_page;
				if (!list.length) {
					self._listShareUnlock(key);
					return callback(null, null);
				}
				
				async.whilst(
					function() { return page_idx <= list.last_page; },
					function(callback) {
						self._listLoadPage(key, page_idx, false, function(err, page) {
							if (err) return callback(err, null);
							// now scan page's items
							for (var idx = 0, len = page.items.length; idx < len; idx++) {
								var matches = 0;
								for (var k in criteria) {
									if (criteria[k].test) {
										if (criteria[k].test(page.items[idx][k])) { matches++; }
									}
									else if (criteria[k] == page.items[idx][k]) { matches++; }
								}
								if (matches == num_crit) {
									// we found our item!
									item = page.items[idx];
									idx = len;
									page_idx = list.last_page;
								}
								else item_idx++;
							} // foreach item
							
							page_idx++;
							callback();
						} ); // page loaded
					},
					function(err) {
						// all pages loaded
						self._listShareUnlock(key);
						if (err) return callback(err, null);
						if (!item) item_idx = -1;
						callback( null, item, item_idx );
					}
				); // whilst
			} ); // loaded
		} ); // _listShareLock
	},
	
	listFindCut: function(key, criteria, callback) {
		// Find single object by criteria, and if found, delete it -- WARNING: this can be slow with long lists
		var self = this;
		
		// This is a two-part macro function, which performs a find followed by a splice,
		// so we need an outer lock that lasts the entire duration of both ops, but we can't collide
		// with the natural lock that splice invokes, so we must add an additional '|' lock prefix.
		
		this._listLock( '|'+key, true, function() {	
			self.listFind(key, criteria, function(err, item, idx) {
				if (err) {
					self._listUnlock( '|'+key );
					return callback(err, null);
				}
				if (!item) {
					self._listUnlock( '|'+key );
					return callback(new Error("Item not found"), null);
				}
				
				self.listSplice(key, idx, 1, null, function(err, items) {
					self._listUnlock( '|'+key );
					callback(err, items ? items[0] : null);
				}); // splice
			} ); // find
		} ); // locked
	},
	
	listFindDelete: function(key, criteria, callback) {
		// alias for listFindCut
		return this.listFindCut(key, criteria, callback);
	},
	
	listFindReplace: function(key, criteria, new_item, callback) {
		// Find single object by criteria, and if found, replace it -- WARNING: this can be slow with long lists
		var self = this;
		
		// This is a two-part macro function, which performs a find followed by a splice,
		// so we need an outer lock that lasts the entire duration of both ops, but we can't collide
		// with the natural lock that splice invokes, so we must add an additional '|' lock prefix.
		
		this._listLock( '|'+key, true, function() {	
			self.listFind(key, criteria, function(err, item, idx) {
				if (err) {
					self._listUnlock( '|'+key );
					return callback(err, null);
				}
				if (!item) {
					self._listUnlock( '|'+key );
					return callback(new Error("Item not found"), null);
				}
				
				self.listSplice(key, idx, 1, [new_item], function(err, items) {
					self._listUnlock( '|'+key );
					callback(err);
				}); // splice
			} ); // find
		} ); // locked
	},
	
	listFindUpdate: function(key, criteria, updates, callback) {
		// Find single object by criteria, and if found, update it -- WARNING: this can be slow with long lists
		// Updates are merged into original item, with numerical increments starting with "+" or "-"
		var self = this;
		
		// This is a two-part macro function, which performs a find followed by a splice,
		// so we need an outer lock that lasts the entire duration of both ops, but we can't collide
		// with the natural lock that splice invokes, so we must add an additional '|' lock prefix.
		
		this._listLock( '|'+key, true, function() {	
			self.listFind(key, criteria, function(err, item, idx) {
				if (err) {
					self._listUnlock( '|'+key );
					return callback(err, null);
				}
				if (!item) {
					self._listUnlock( '|'+key );
					return callback(new Error("Item not found"), null);
				}
				
				// apply updates
				for (var ukey in updates) {
					var uvalue = updates[ukey];
					if ((typeof(uvalue) == 'string') && (typeof(item[ukey]) == 'number') && uvalue.match(/^(\+|\-)([\d\.]+)$/)) {
						var op = RegExp.$1;
						var amt = parseFloat(RegExp.$2);
						if (op == '+') item[ukey] += amt;
						else item[ukey] -= amt;
					}
					else item[ukey] = uvalue;
				}
				
				self.listSplice(key, idx, 1, [item], function(err, items) {
					self._listUnlock( '|'+key );
					callback(err, item);
				}); // splice
			} ); // find
		} ); // locked
	},
	
	listFindEach: function(key, criteria, iterator, callback) {
		// fire iterator for every matching element in list, only load one page at a time
		var self = this;
		var num_crit = Tools.numKeys(criteria);
		this.logDebug(9, "Locating items in list: " + key, criteria);
		
		this._listShareLock(key, true, function() {
			// share locked
			self._listLoad(key, false, function(err, list) {
				// list loaded, proceed
				if (err) {
					self._listShareUnlock(key);
					callback(err);
					return;
				}
				var page_idx = list.first_page;
				var item_idx = 0;
				
				async.whilst(
					function() { return page_idx <= list.last_page; },
					function(callback) {
						// load each page
						self._listLoadPage(key, page_idx++, false, function(err, page) {
							if (err) return callback(err);
							
							// iterate over page items
							if (page && page.items && page.items.length) {
								async.eachSeries( page.items, function(item, callback) {
									// for each item, check against criteria
									var matches = 0;
									for (var k in criteria) {
										if (criteria[k].test) {
											if (criteria[k].test(item[k])) { matches++; }
										}
										else if (criteria[k] == item[k]) { matches++; }
									}
									if (matches == num_crit) {
										iterator(item, item_idx++, callback);
									}
									else {
										item_idx++;
										callback();
									}
								}, callback );
							}
							else callback();
						} ); // page loaded
					},
					function(err) {
						// all pages iterated
						self._listShareUnlock(key);
						if (err) return callback(err);
						else callback(null);
					} // pages complete
				); // whilst
			} ); // loaded
		} ); // _listShareLock
	},
	
	listDelete: function(key, entire, callback) {
		// Delete entire list and all pages
		var self = this;
		this.logDebug(9, "Deleting list: " + key);
		
		this._listLock( key, true, function() {
			// locked
			self._listLoad(key, false, function(err, list) {
				// list loaded, proceed
				if (err) {
					self._listUnlock(key);
					return callback(err, null);
				}
				
				var page_idx = list.first_page;
				if (!entire) page_idx++; // skip first page, will be rewritten
				
				async.whilst(
					function() { return page_idx <= list.last_page; },
					function(callback) {
						// delete each page
						self.delete( key + '/' + page_idx, function(err, data) {
							page_idx++;
							return callback(err);
						} ); // delete
					},
					function(err) {
						// all pages deleted
						if (err) {
							self._listUnlock(key);
							return callback(err, null);
						}
						
						// delete list itself, or just clear it?
						if (entire) {
							// delete entire list
							self.delete(key, function(err, data) {
								// final delete complete
								self._listUnlock(key);
								callback(err);
							} ); // deleted
						} // entire
						else {
							// zero list for reuse
							list.length = 0;
							list.first_page = 0;
							list.last_page = 0;
							
							self.put( key, list, function(err, data) {
								// finished saving list header
								if (err) {
									self._listUnlock(key);
									return callback(err);
								}
								
								// now save a blank first page
								self.put( key + '/0', { type: 'list_page', items: [] }, function(err, data) {
									// save complete
									self._listUnlock(key);
									callback(err);
								} ); // saved
							} ); // saved header
						} // reuse
					} // pages deleted
				); // whilst
			} ); // loaded
		} ); // locked
	},
	
	listGetInfo: function(key, callback) {
		// Return info about list (number of items, etc.)
		this._listLoad( key, false, callback );
	},
	
	listCopy: function(old_key, new_key, callback) {
		// Copy list to new path (and all pages)
		var self = this;
		this.logDebug(9, "Copying list: " + old_key + " to " + new_key);
		
		this._listLoad(old_key, false, function(err, list) {
			// list loaded, proceed
			if (err) {
				callback(err);
				return;
			}
			var page_idx = list.first_page;
			
			async.whilst(
				function() { return page_idx <= list.last_page; },
				function(callback) {
					// load each page
					self._listLoadPage(old_key, page_idx, false, function(err, page) {
						if (err) return callback(err);
						
						// and copy it
						self.copy( old_key + '/' + page_idx, new_key + '/' + page_idx, function(err, data) {
							page_idx++;
							return callback(err);
						} ); // copy
					} ); // page loaded
				},
				function(err) {
					// all pages copied
					if (err) return callback(err);
					
					// now copy list header
					self.copy(old_key, new_key, function(err, data) {
						// final copy complete
						callback(err);
					} ); // deleted
				} // pages copied
			); // whilst
		} ); // loaded
	},
	
	listRename: function(old_key, new_key, callback) {
		// Copy, then delete list (and all pages)
		var self = this;
		this.logDebug(9, "Renaming list: " + old_key + " to " + new_key);
		
		this.listCopy( old_key, new_key, function(err) {
			// copy complete, now delete old list
			if (err) return callback(err);
			
			self.listDelete( old_key, true, callback );
		} ); // copied
	},
	
	listEach: function(key, iterator, callback) {
		// fire iterator for every element in list, only load one page at a time
		var self = this;
		
		this._listShareLock(key, true, function() {
			// share locked
			self._listLoad(key, false, function(err, list) {
				// list loaded, proceed
				if (err) {
					self._listShareUnlock(key);
					callback(err);
					return;
				}
				var page_idx = list.first_page;
				var item_idx = 0;
				
				async.whilst(
					function() { return page_idx <= list.last_page; },
					function(callback) {
						// load each page
						self._listLoadPage(key, page_idx++, false, function(err, page) {
							if (err) return callback(err);
							
							// iterate over page items
							if (page && page.items && page.items.length) {
								async.eachSeries( page.items, function(item, callback) {
									iterator(item, item_idx++, callback);
								}, callback );
							}
							else callback();
						} ); // page loaded
					},
					function(err) {
						// all pages iterated
						self._listShareUnlock(key);
						if (err) return callback(err);
						else callback(null);
					} // pages complete
				); // whilst
			} ); // loaded
		} ); // _listShareLock
	},
	
	listEachPage: function(key, iterator, callback) {
		// fire iterator for every page in list
		var self = this;
		
		this._listShareLock(key, true, function() {
			// share locked
			self._listLoad(key, false, function(err, list) {
				// list loaded, proceed
				if (err) {
					self._listShareUnlock(key);
					callback(err);
					return;
				}
				var page_idx = list.first_page;
				var item_idx = 0;
				
				async.whilst(
					function() { return page_idx <= list.last_page; },
					function(callback) {
						// load each page
						self._listLoadPage(key, page_idx++, false, function(err, page) {
							if (err) return callback(err);
							
							// call iterator for page items
							if (page && page.items && page.items.length) {
								iterator(page.items, callback);
							}
							else callback();
						} ); // page loaded
					},
					function(err) {
						// all pages iterated
						self._listShareUnlock(key);
						callback( err || null );
					} // pages complete
				); // whilst
			} ); // loaded
		} ); // _listShareLock
	},
	
	listEachUpdate: function(key, iterator, callback) {
		// fire iterator for every element in list, only load one page at a time
		// iterator can signal that a change was made to any items, triggering an update
		var self = this;
		
		this._listLock(key, true, function() {
			// exclusively locked
			self._listLoad(key, false, function(err, list) {
				// list loaded, proceed
				if (err) {
					self._listUnlock(key);
					callback(err);
					return;
				}
				var page_idx = list.first_page;
				var item_idx = 0;
				
				async.whilst(
					function() { return page_idx <= list.last_page; },
					function(callback) {
						// load each page
						var page_key = key + '/' + page_idx;
						
						self._listLoadPage(key, page_idx++, false, function(err, page) {
							if (err) return callback(err);
							
							// iterate over page items
							if (page && page.items && page.items.length) {
								var num_updated = 0;
								
								async.eachSeries( page.items, 
									function(item, callback) {
										iterator(item, item_idx++, function(err, updated) {
											if (updated) num_updated++;
											callback(err);
										});
									}, 
									function(err) {
										if (err) return callback(err);
										if (num_updated) self.put( page_key, page, callback );
										else callback();
									}
								); // async.eachSeries
							}
							else callback();
						} ); // page loaded
					},
					function(err) {
						// all pages iterated
						self._listUnlock(key);
						callback( err || null );
					} // pages complete
				); // whilst
			} ); // loaded
		} ); // _listLock
	},
	
	listEachPageUpdate: function(key, iterator, callback) {
		// fire iterator for every page in list
		// iterator can signal that a change was made to any page, triggering an update
		var self = this;
		
		this._listLock(key, true, function() {
			// exclusively locked
			self._listLoad(key, false, function(err, list) {
				// list loaded, proceed
				if (err) {
					self._listUnlock(key);
					callback(err);
					return;
				}
				var page_idx = list.first_page;
				var item_idx = 0;
				
				async.whilst(
					function() { return page_idx <= list.last_page; },
					function(callback) {
						// load each page
						var page_key = key + '/' + page_idx;
						
						self._listLoadPage(key, page_idx++, false, function(err, page) {
							if (err) return callback(err);
							
							// call iterator for page items
							if (page && page.items && page.items.length) {
								iterator(page.items, function(err, updated) {
									if (!err && updated) self.put( page_key, page, callback );
									else callback(err);
								});
							}
							else callback();
						} ); // page loaded
					},
					function(err) {
						// all pages iterated
						self._listUnlock(key);
						callback( err || null );
					} // pages complete
				); // whilst
			} ); // loaded
		} ); // _listLock
	},
	
	listInsertSorted: function(key, insert_item, comparator, callback) {
		// insert item into list while keeping it sorted
		var self = this;
		var loc = false;
		
		if (isArray(comparator)) {
			// convert to closure
			var sort_key = comparator[0];
			var sort_dir = comparator[1] || 1;
			comparator = function(a, b) {
				return( ((a[sort_key] < b[sort_key]) ? -1 : 1) * sort_dir );
			};
		}
		
		// This is a two-part macro function, which performs a find followed by a splice,
		// so we need an outer lock that lasts the entire duration of both ops, but we can't collide
		// with the natural lock that splice invokes, so we must add an additional '|' lock prefix.
		
		this._listLock( '|'+key, true, function() {	
			// list is locked
			self.listEach( key, 
				function(item, idx, callback) {
					// listEach iterator
					var result = comparator(insert_item, item);
					if (result < 0) {
						// our item should come before compared item, so splice here!
						loc = idx;
						callback("break");
					}
					else callback();
				}, // listEach iterator
				function(err) {
					// listEach complete
					// Ignoring error here, as we'll just create a new list
					
					if (loc !== false) {
						// found location, so perform non-removal splice
						self.listSplice( key, loc, 0, [insert_item], function(err) {
							self._listUnlock( '|'+key );
							callback(err);
						} );
					}
					else {
						// no suitable location found, so add to end of list
						self.listPush( key, insert_item, function(err) {
							self._listUnlock( '|'+key );
							callback(err);
						} );
					}
				} // listEach complete
			); // listEach
		} ); // list locked
	}
	
});
```

## File: `package.json`
```json
{
	"name": "pixl-server-storage",
	"version": "4.0.3",
	"description": "A key/value/list storage component for the pixl-server framework.",
	"author": "Joseph Huckaby <jhuckaby@gmail.com>",
	"homepage": "https://github.com/jhuckaby/pixl-server-storage",
	"license": "MIT",
	"main": "storage.js",
	"repository": {
		"type": "git",
		"url": "https://github.com/jhuckaby/pixl-server-storage"
	},
	"bugs": {
		"url": "https://github.com/jhuckaby/pixl-server-storage/issues"
	},
	"keywords": [
		"storage",
		"nosql",
		"s3",
		"couchbase",
		"redis",
		"sqlite"
	],
	"dependencies": {
		"@aws-sdk/client-s3": "3.995.0",
		"@aws-sdk/lib-storage": "3.995.0",
		"@smithy/node-http-handler": "3.3.3",
		"async": "2.6.4",
		"fast-stream-to-buffer": "1.0.0",
		"he": "1.1.1",
		"moo": "0.4.3",
		"nearley": "2.20.1",
		"pixl-cache": "^1.0.6",
		"pixl-class": "^1.0.3",
		"pixl-perf": "^1.0.9",
		"pixl-server": "^1.0.39",
		"pixl-tools": "^2.0.2",
		"porter-stemmer": "0.9.1",
		"stream-meter": "1.0.4",
		"unidecode": "0.1.8"
	},
	"devDependencies": {
		"pixl-unit": "^1.0.14"
	},
	"scripts": {
		"test": "pixl-unit test/test.js",
		"build": "nearleyc pxql.ne > pxql.js"
	}
}
```

## File: `pxql.js`
```javascript
// Generated automatically by nearley
// http://github.com/Hardmath123/nearley
(function () {
function id(x) {return x[0]; }


// PxQL (pixl-query-language)
// Copyright (c) 2017 PixlCore.com and Joseph Huckaby
// MIT Licensed

const moo = require('moo');

let lexer = moo.compile({
	space: {match: /\s+/, lineBreaks: true},
	column: {match: /[A-Za-z]\w*/, lineBreaks: false},
	operator: {match: /=~|\!~|<=|<|>=|>|==|=/, lineBreaks: false},
	separator: {match: /\&\&?|\|\|?/, lineBreaks: false},
	number: /-?(?:[0-9]|[1-9][0-9]+)(?:\.[0-9]+)?(?:[eE][-+]?[0-9]+)?\b/,
	string: /"(?:\\["bfnrt\/\\]|\\u[a-fA-F0-9]{4}|[^"\\])*"/,
	'(': '(',
	')': ')',
	true: 'true',
	false: 'false',
	null: 'null',
});




function extractGroup(d) {
	let output = [d[2][0]];
	let mode = '';
	
	for (let i in d[3]) {
		if (d[3][i][1].type == 'separator') {
			if (mode && (d[3][i][1].value != mode)) throw new Error("Ambiguous logic operator: " + d[3][i][1].value + " (use parenthesis to group)");
			mode = d[3][i][1].value;
		}
		output.push(d[3][i][3][0]);
	}
	
	if (mode.match(/\|/)) mode = 'or';
	else mode = 'and';
	
	if (output.length == 1) return output[0];
	else return { mode: mode, criteria: output };
}

function extractExpression(d) {
	var obj = { index: d[0].value, operator: d[2].value, word: ''+d[4].value };
	
	if ((obj.operator == '=~') || (obj.operator == '==') || (obj.operator == '=')) {
		// default operator
		delete obj.operator;
	}
	else if (obj.operator == '!~') {
		// negative word match
		obj.negative = 1;
		delete obj.operator;
	}
	
	return obj;
}

var grammar = {
    Lexer: lexer,
    ParserRules: [
    {"name": "main$subexpression$1", "symbols": ["expression"]},
    {"name": "main$subexpression$1", "symbols": ["group"]},
    {"name": "main", "symbols": ["_", "main$subexpression$1", "_"], "postprocess": function(d) { return d[1][0]; }},
    {"name": "group$subexpression$1", "symbols": ["expression"]},
    {"name": "group$subexpression$1", "symbols": ["group"]},
    {"name": "group$ebnf$1", "symbols": []},
    {"name": "group$ebnf$1$subexpression$1$subexpression$1", "symbols": ["expression"]},
    {"name": "group$ebnf$1$subexpression$1$subexpression$1", "symbols": ["group"]},
    {"name": "group$ebnf$1$subexpression$1", "symbols": ["_", (lexer.has("separator") ? {type: "separator"} : separator), "_", "group$ebnf$1$subexpression$1$subexpression$1"]},
    {"name": "group$ebnf$1", "symbols": ["group$ebnf$1", "group$ebnf$1$subexpression$1"], "postprocess": function arrpush(d) {return d[0].concat([d[1]]);}},
    {"name": "group", "symbols": [{"literal":"("}, "_", "group$subexpression$1", "group$ebnf$1", "_", {"literal":")"}], "postprocess": extractGroup},
    {"name": "expression", "symbols": [(lexer.has("column") ? {type: "column"} : column), "_", (lexer.has("operator") ? {type: "operator"} : operator), "_", "value"], "postprocess": extractExpression},
    {"name": "value", "symbols": ["number"], "postprocess": id},
    {"name": "value", "symbols": ["string"], "postprocess": id},
    {"name": "number", "symbols": [(lexer.has("number") ? {type: "number"} : number)], "postprocess": function(d) { return { type: 'number', value: parseFloat(d[0].value) }; }},
    {"name": "string", "symbols": [(lexer.has("string") ? {type: "string"} : string)], "postprocess": function(d) { return { type: 'string', value: JSON.parse(d[0].value) }; }},
    {"name": "_", "symbols": []},
    {"name": "_", "symbols": [(lexer.has("space") ? {type: "space"} : space)], "postprocess": function(d) { return null; }}
]
  , ParserStart: "main"
}
if (typeof module !== 'undefined'&& typeof module.exports !== 'undefined') {
   module.exports = grammar;
} else {
   window.grammar = grammar;
}
})();
```

## File: `pxql.ne`
```
# PxQL (pixl-query-language)
# Grammar Source for Nearley
# Compile: nearleyc pxql.ne > pxql.js
# Copyright (c) 2017 PixlCore.com and Joseph Huckaby
# MIT Licensed

@{%

// PxQL (pixl-query-language)
// Copyright (c) 2017 PixlCore.com and Joseph Huckaby
// MIT Licensed

const moo = require('moo');

let lexer = moo.compile({
	space: {match: /\s+/, lineBreaks: true},
	column: {match: /[A-Za-z]\w*/, lineBreaks: false},
	operator: {match: /=~|\!~|<=|<|>=|>|==|=/, lineBreaks: false},
	separator: {match: /\&\&?|\|\|?/, lineBreaks: false},
	number: /-?(?:[0-9]|[1-9][0-9]+)(?:\.[0-9]+)?(?:[eE][-+]?[0-9]+)?\b/,
	string: /"(?:\\["bfnrt\/\\]|\\u[a-fA-F0-9]{4}|[^"\\])*"/,
	'(': '(',
	')': ')',
	true: 'true',
	false: 'false',
	null: 'null',
});

%}

@lexer lexer

main -> _ (expression | group) _ {% function(d) { return d[1][0]; } %}

group -> "(" _ (expression | group) (_ %separator _ (expression | group)):* _ ")" {% extractGroup %}

expression -> %column _ %operator _ value {% extractExpression %}

value ->
	number {% id %}
	| string {% id %}

number -> %number {% function(d) { return { type: 'number', value: parseFloat(d[0].value) }; } %}

string -> %string {% function(d) { return { type: 'string', value: JSON.parse(d[0].value) }; } %}

_ -> null | %space {% function(d) { return null; } %}

@{%

function extractGroup(d) {
	let output = [d[2][0]];
	let mode = '';
	
	for (let i in d[3]) {
		if (d[3][i][1].type == 'separator') {
			if (mode && (d[3][i][1].value != mode)) throw new Error("Ambiguous logic operator: " + d[3][i][1].value + " (use parenthesis to group)");
			mode = d[3][i][1].value;
		}
		output.push(d[3][i][3][0]);
	}
	
	if (mode.match(/\|/)) mode = 'or';
	else mode = 'and';
	
	if (output.length == 1) return output[0];
	else return { mode: mode, criteria: output };
}

function extractExpression(d) {
	var obj = { index: d[0].value, operator: d[2].value, word: ''+d[4].value };
	
	if ((obj.operator == '=~') || (obj.operator == '==') || (obj.operator == '=')) {
		// default operator
		delete obj.operator;
	}
	else if (obj.operator == '!~') {
		// negative word match
		obj.negative = 1;
		delete obj.operator;
	}
	
	return obj;
}

%}

```

## File: `README.md`
```markdown
# Overview

This module is a component for use in [pixl-server](https://www.github.com/jhuckaby/pixl-server).  It implements a simple key/value storage system that can use multiple back-ends, such as [Amazon S3](https://aws.amazon.com/s3/), [Redis](https://redis.io/), or a local filesystem.  It introduces the concept of a "chunked linked list", which supports extremely fast push, pop, shift, unshift, and random reads/writes.  Also provided is a fast hash table implementation with key iteration, a transaction system, and an indexing and search system.

## Features at a Glance

* Uses very little memory in most cases.
* Store JSON or binary (raw) data records.
* Supports multiple back-ends including Amazon S3, Redis, and local filesystem.
* Linked lists with very fast push, pop, shift, unshift, and random reads/writes.
* Hash tables with key iterators, and very fast reads / writes.
* Advisory locking system with shared and exclusive locks.
* Variable expiration dates per key and automatic deletion.
* Transaction system for isolated compound operations and atomic commits, rollbacks.
* Indexing system for searches across collections of JSON records.
* Supports Google-style full-text search queries.

## Table of Contents

The documentation is split up across six files:

- &rarr; **[Main Docs](https://github.com/jhuckaby/pixl-server-storage/blob/master/README.md)** *(You are here)*
- &rarr; **[Lists](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Lists.md)**
- &rarr; **[Hashes](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Hashes.md)**
- &rarr; **[Transactions](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Transactions.md)**
- &rarr; **[Indexer](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Indexer.md)**
- &rarr; **[API Reference](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/API.md)**

Here is the table of contents for this current document:

<!-- toc -->
- [Usage](#usage)
	* [Standalone Mode](#standalone-mode)
- [Configuration](#configuration)
	* [engine](#engine)
	* [engine_path](#engine_path)
	* [list_page_size](#list_page_size)
	* [hash_page_size](#hash_page_size)
	* [concurrency](#concurrency)
	* [maintenance](#maintenance)
	* [log_event_types](#log_event_types)
	* [max_recent_events](#max_recent_events)
	* [expiration_updates](#expiration_updates)
	* [lower_case_keys](#lower_case_keys)
	* [debug (standalone)](#debug-standalone)
- [Engines](#engines)
	* [Local Filesystem](#local-filesystem)
		+ [Key Namespaces](#key-namespaces)
		+ [Raw File Paths](#raw-file-paths)
		+ [Key Template](#key-template)
		+ [Filesystem Cache](#filesystem-cache)
	* [Amazon S3](#amazon-s3)
		+ [S3 File Extensions](#s3-file-extensions)
		+ [S3 Key Prefix](#s3-key-prefix)
		+ [S3 Key Template](#s3-key-template)
		+ [S3 Cache](#s3-cache)
		+ [S3 Compatible Services](#s3-compatible-services)
	* [Redis](#redis)
		+ [RedisCluster](#rediscluster)
	* [SQLite](#sqlite)
	* [Hybrid](#hybrid)
- [Key Normalization](#key-normalization)
- [Basic Functions](#basic-functions)
	* [Storing Records](#storing-records)
	* [Fetching Records](#fetching-records)
	* [Copying Records](#copying-records)
	* [Renaming Records](#renaming-records)
	* [Deleting Records](#deleting-records)
- [Storing Binary Blobs](#storing-binary-blobs)
- [Using Streams](#using-streams)
- [Expiring Data](#expiring-data)
	* [Custom Record Types](#custom-record-types)
- [Advisory Locking](#advisory-locking)
- [Logging](#logging)
	* [Debug Logging](#debug-logging)
	* [Error Logging](#error-logging)
	* [Transaction Logging](#transaction-logging)
	* [Performance Logs](#performance-logs)
- [Performance Metrics](#performance-metrics)
- [Daily Maintenance](#daily-maintenance)
- [Plugin Development](#plugin-development)
- [Unit Tests](#unit-tests)
- [License](#license)

# Usage

Use [npm](https://www.npmjs.com/) to install the module:

```sh
npm install pixl-server pixl-server-storage
```

Here is a simple usage example.  Note that the component's official name is `Storage`, so that is what you should use for the configuration key, and for gaining access to the component via your server object.

```js
const PixlServer = require('pixl-server');
let server = new PixlServer({
	
	__name: 'MyServer',
	__version: "1.0",
	
	config: {
		"log_dir": "/let/log",
		"debug_level": 9,
		
		"Storage": {
			"engine": "Filesystem",
			"Filesystem": {
				"base_dir": "/let/data/myserver",
			}
		}
	},
	
	components: [
		require('pixl-server-storage')
	]
	
});

server.startup( function() {
	// server startup complete
	let storage = server.Storage;
	
	// store key
	storage.put( 'test-key', { foo:"hello", bar:42 }, function(err) {
		if (err) throw err;
		
		// fetch key
		storage.get( 'test-key', function(err, data) {
			if (err) throw err;
			console.log(data);
		} );
	} );
} );
```

Notice how we are loading the [pixl-server](https://www.github.com/jhuckaby/pixl-server) parent module, and then specifying [pixl-server-storage](https://www.github.com/jhuckaby/pixl-server-storage) as a component:

```js
components: [
	require('pixl-server-storage')
]
```

This example is a very simple server configuration, which will start a local filesystem storage instance pointed at `/let/data/myserver` as a base directory.  It then simply stores a test key, then fetches it back.

## Standalone Mode

If you want to access the storage component as a standalone class (i.e. not part of a [pixl-server](https://www.github.com/jhuckaby/pixl-server) server daemon), you can require the `pixl-server-storage/standalone` path and invoke it directly.  This can be useful for things like simple CLI scripts.  Example usage:

```js
const StandaloneStorage = require('pixl-server-storage/standalone');

const config = {
	"engine": "Filesystem",
	"Filesystem": {
		"base_dir": "/let/data/myserver"
	}
};

let storage = new StandaloneStorage(config, function(err) {
	if (err) throw err;
	// storage system has started up and is ready to go
	
	storage.put( 'test-key', { foo:"hello", bar:42 }, function(err) {
		if (err) throw err;
		
		// fetch key
		storage.get( 'test-key', function(err, data) {
			if (err) throw err;
			console.log(data);
			
			// we have to shutdown manually
			storage.shutdown( function() { 
				process.exit(0); 
			} );
		} );
	} );
});
```

Please note that standalone mode does not perform standard [pixl-server](https://www.github.com/jhuckaby/pixl-server) timer operations like emit `tick` and `minute` events, so things like performance metrics collection and [Daily Maintenance](#daily-maintenance) do not run.  It also doesn't register standard [SIGINT / SIGTERM](https://nodejs.org/api/process.html#process_signal_events) signal listeners for handing shutdown, so these must be handled by your code.

# Configuration

The configuration for this component is set by passing in a `Storage` key in the `config` element when constructing the `PixlServer` object, or, if a JSON configuration file is used, a `Storage` object at the outermost level of the file structure.  It can contain the following keys:

## engine

The `engine` property is used to declare the name of the back-end storage engine to use.  Specifically, this is for using one of the built-in engine modules located in the `pixl-server-storage/engines/` directory.  See [Engines](#engines) below for details.  Example:

```json
{
	"engine": "Filesystem",
	"Filesystem": {
		"base_dir": "/let/data/myserver"
	}
}
```

Note that the engine's own configuration should always go into a property named the same as the engine itself, in this case `Filesystem`.

## engine_path

The `engine_path` property can be used to load your own custom engine in any location.  The path should be either absolute, or relative to the location of the `pixl-server-storage/` directory.  Example:

```json
{
	"engine": "MyCustomEngine",
	"engine_path": "../../my_custom_storage_engine.js",
	"MyCustomEngine": {
		"something": "foo"
	}
}
```

All engines must have a name, so you always need to declare a `engine` property with a string, and that should always match a property containing engine-specific configuration directives.  See [Plugin Development](#plugin-development) for more details.

## list_page_size

The `list_page_size` property specifies the default page size (number of items per page) for new lists.  However, you can override this per each list when creating them.  See [Lists](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Lists.md) for details.

## hash_page_size

The `hash_page_size` property specifies the default page size (number of items per page) for new hashes.  However, you can override this per each hash when creating them.  See [Hashes](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Hashes.md) for details.

## concurrency

The `concurrency` property allows some operations to be parallelized in the storage engine.  This is mainly used for list and maintenance operations, which may involve loading and saving multiple records.  The default value is `1`.  Increase this number for potentially faster operations in some cases.

## maintenance

The `maintenance` property allows the storage system to run routine maintenance, and is highly recommended for daemons that run 24x7.  This is typically enabled to run nightly, and performs tasks such as deleting expired records.  To enable it, set this to any `HH:MM` string where `HH` is the hour in 24-hour time and `MM` is the minute.  Pad with a zero if either value is under 10.  Example:

```js
{
	"maintenance": "04:30" // run daily at 4:30 AM
}
```

Make sure your server's clock and timezone are correct.  The values are always assumed to be in the current timezone.

## log_event_types

The `log_event_types` property allows you to configure exactly which transaction event types are logged.  By default, none of them are. For details, see the [Transaction Logging](#transaction-logging) section below.

## max_recent_events

The `max_recent_events` property allows the storage system to track the latest N events in memory, which are then provided in the call to [getStats()](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/API.md#getstats).  For details, see the [Performance Metrics](#performance-metrics) section below.

## expiration_updates

The `expiration_updates` property activates additional features in the [expiration system](#expiring-data).  Namely, setting this property to `true` allows you to update expiration dates of existing records.  Otherwise only a single expiration date may be set once per each record.

Note that this feature incurs additional overhead, because the expiration date of every record needs to be stored in a global [Hash](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Hashes.md).  This slows down both the expiration set operation, and the nightly maintenance sweep to delete expired records.  For this reason, the `expiration_dates` property defaults to `false` (disabled).

## lower_case_keys

The `lower_case_keys` property causes all storage keys to be internally lower-cased, effectively making all storage paths case-insensitive.  This is the default (`true`).  If you set this property to `false`, then all storage keys retain their natural casing, effectively making them case-sensitive.

Please note that if you use the [Local Filesystem](#local-filesystem) engine, then the filesystem itself may be case-insensitive (e.g. legacy macOS HFS).

## debug (standalone)

The `debug` property is only used when using [Standalone Mode](#standalone-mode).  Setting this to `true` will cause the engine to emit debugging messages to the console.

# Engines

The storage system can be backed by a number of different "engines", which actually perform the reads and writes.  A simple local filesystem implementation is included, as well as modules for Amazon S3 and Redis.  Each one requires a bit of extra configuration.

## Local Filesystem

The local filesystem engine is called `Filesystem`, and reads/writes files to local disk.  It distributes files by hashing their keys using [MD5](https://en.wikipedia.org/wiki/MD5), and splitting up the path into several subdirectories.  So even with tens of millions of records, no one single directory will ever have more than 256 files.  For example:

```
Plain Key:
test1

MD5 Hash:
5a105e8b9d40e1329780d62ea2265d8a

Partial Filesystem Path:
/5a/10/5e/5a105e8b9d40e1329780d62ea2265d8a.json
```

The partial path is then combined with a base directory, which is configurable.  Here is an example configuration:

```json
{
	"engine": "Filesystem",
	"Filesystem": {
		"base_dir": "/let/data/myserver"
	}
}
```

So, putting all this together, the `test1` key would be stored on disk at this location:

```
/let/data/myserver/5a/10/5e/5a105e8b9d40e1329780d62ea2265d8a.json
```

For binary records, the file extension will match whatever was in the key.

### Key Namespaces

To help segment your application data into categories on the filesystem, an optional `key_namespaces` configuration parameter can be specified, and set to a true value.  This will modify the key hashing algorithm to include a "prefix" directory, extracted from the plain key itself.  Example configuration:

```json
{
	"engine": "Filesystem",
	"Filesystem": {
		"base_dir": "/let/data/myserver",
		"key_namespaces": true
	}
}
```

Here is an example storage key and how to gets translated to the a filesystem path:

```
Plain Key:
users/jhuckaby

MD5 Hash:
019aaa6887e5ce3533dcc691b05e69e4

Partial Filesystem Path:
/users/01/9a/aa/019aaa6887e5ce3533dcc691b05e69e4.json
```

So in this case the `users` prefix is extracted from the plain key, and then inserted at the beginning of the hash directories.  Here is the full filesystem path, assuming a base directory of `/let/data/myserver`:

```
/let/data/myserver/users/01/9a/aa/019aaa6887e5ce3533dcc691b05e69e4.json
```

In order to use key namespaces effectively, you need to make sure that *all* your plain keys contain some kind of namespace prefix, followed by a slash.  The idea is, you can then store your app's data in different physical locations using symlinks.  You can also determine how much disk space is taken up by each of your app's data categories, without having to walk all the hash directories.

### Raw File Paths

For testing purposes, or for small datasets, you can optionally set the `raw_file_paths` Filesystem configuration parameter to any true value.  This will skip the MD5 hashing of all filesystem paths, and literally write them to the filesystem verbatim, as they come in (well, after [Key Normalization](#key-normalization) of course).  Example configuration:

```json
{
	"engine": "Filesystem",
	"Filesystem": {
		"base_dir": "/let/data/myserver",
		"raw_file_paths": true
	}
}
```

So with raw file paths enabled our example key (`users/jhuckaby`) would literally end up on the filesystem right here:

```
/let/data/myserver/users/jhuckaby.json
```

Using this mode you can easily overwhelm a filesystem with too many files in a single directory, depending on how you format your keys.  It is really only meant for testing purposes.

Note that if `raw_file_paths` is enabled, `key_namespaces` has no effect.

### Key Template

For complete, low-level control over the key hashing and directory layout, you can specify a key "template" via the `key_template` configuration property.  This allows you to specify exactly how the directories are laid out, and whether the full plain key is part of the directory path, or just the MD5 hash.  For example, consider this configuration:

```json
{
	"engine": "Filesystem",
	"Filesystem": {
		"base_dir": "/let/data/myserver",
		"key_template": "##/##/##/[md5]"
	}
}
```

If your `key_template` property contains any hash marks (`#`), they will be dynamically replaced with characters from an [MD5 hash](https://en.wikipedia.org/wiki/MD5) of the key.  Also, `[md5]` will be substituted for the full MD5 hash, and `[key]` will be substituted with the full key itself.  So for another example:

```js
"key_template": "##/##/[key]"
```

This would replace the 4 hash marks with the first 4 characters from the key's MD5, followed by the full key itself e.g. `a5/47/users/jhuckaby`.  Note that this all happens behind the scenes and transparently, so you never have to specify the prefix or hash characters when fetching keys.

### Filesystem Cache

You can optionally enable caching for the filesystem, which keeps a copy of the most recently used JSON records in RAM.  This can increase performance if you have a small set of popular keys that are frequently accessed.  Note that the cache does *not* defer writes -- it only passively holds copies in memory, to intercept and accelerate repeat reads.

To enable the filesystem cache, include a `cache` object in your `Filesystem` configuration with the following properties:

```json
{
	"engine": "Filesystem",
	"Filesystem": {
		"base_dir": "/let/data/myserver",
		"cache": {
			"enabled": true,
			"maxItems": 1000,
			"maxBytes": 10485760
		}
	}
}
```

The properties are as follows:

| Property Name | Type | Description |
|---------------|------|-------------|
| `enabled` | Boolean | Set this to `true` to enable the filesystem caching system. |
| `maxItems` | Integer | This is the maximum number of objects to allow in the cache. |
| `maxBytes` | Integer | This is the maximum number of bytes to allow in the cache. |

The cache will automatically expire objects in LRU fashion when either of the limits are exceeded (whichever is hit first).  Set the properties to `0` for no limit.

Note that binary records are **not** cached.  This system is for JSON records only.

## Amazon S3

If you want to use [Amazon S3](http://aws.amazon.com/s3/) as a backing store, configure your storage thusly:

```json
{
	"engine": "S3",
	"AWS": {
		"region": "us-west-1",
		"credentials": {
			"accessKeyId": "YOUR_AMAZON_ACCESS_KEY", 
			"secretAccessKey": "YOUR_AMAZON_SECRET_KEY"
		}
	},
	"S3": {
		"connectTimeout": 5000,
		"socketTimeout": 5000,
		"maxAttempts": 50,
		"keyPrefix": "",
		"fileExtensions": true,
		"params": {
			"Bucket": "MY_S3_BUCKET_ID"
		},
		"cache": {
			"enabled": true,
			"maxItems": 1000,
			"maxBytes": 10485760
		}
	}
}
```

Replace `YOUR_AMAZON_ACCESS_KEY` and `YOUR_AMAZON_SECRET_KEY` with your Amazon Access Key and Secret Key, respectively.  These can be generated on the Security Credentials page.  Replace `MY_S3_BUCKET_ID` with the ID if your own S3 bucket.  Make sure you match up the region too.

If you plan on using Amazon AWS in other parts of your application, you can actually move the `AWS` config object into your outer server configuration.  The storage module will look for it there.

### S3 File Extensions

It is highly recommended that you set the S3 `fileExtensions` property to `true`, as shown in the example above.  This causes pixl-server-storage to append a file extension to all JSON S3 records when storing them.  For example, a key like `users/jhuckaby` would be stored in S3 as `users/jhuckaby.json`.  The benefit of this is that it plays nice with tools that copy or sync S3 data, including the popular [Rclone](https://rclone.org/) application.

This all happens behind the scenes, and is invisible to the pixl-server-storage APIs.  So you do not have to add any JSON record file extensions yourself, when storing, fetching or deleting your records.

Note that [binary keys](#storing-binary-blobs) already have file extensions, so they are excluded from this feature.  This only affects JSON records.

### S3 Key Prefix

The S3 engine supports an optional key prefix, in case you are sharing a bucket with other applications, and want to keep all your app related records separate.  To specify this, include a `keyPrefix` property in your `S3` object (this goes alongside the `params`, but not inside of it).  Example:

```json
{
	"S3": {
		"keyPrefix": "myapp",
		"params": {
			"Bucket": "MY_S3_BUCKET_ID"
		}
	}
}
```

This would prefix the string `myapp` before all your application keys (a trailing slash will be added after the prefix if needed).  For example, if your app tried to write a record with key `users/jhuckaby`, the actual S3 key would end up as `myapp/users/jhuckaby`.

### S3 Key Template

Note that Amazon [recommends adding a hash prefix](https://docs.aws.amazon.com/AmazonS3/latest/dev/request-rate-perf-considerations.html) to all your S3 keys, for performance reasons.  To that end, if you specify a `keyTemplate` property, and it contains any hash marks (`#`), they will be dynamically replaced with characters from an [MD5 hash](https://en.wikipedia.org/wiki/MD5) of the key.  So for example:

```js
"keyTemplate": "##/##/[key]"
```

This would replace the 4 hash marks with the first 4 characters from the key's MD5 digest, followed by the full key itself, e.g. `a5/47/users/jhuckaby`.  Note that this all happens behind the scenes and transparently, so you never have to specify the prefix or hash characters when fetching keys.

Besides hash marks, the special macro `[key]` will be substituted with the full key, and `[md5]` will be substituted with a full MD5 hash of the key.  These can be used anywhere in the template string.

### S3 Cache

It is *highly* recommended that you enable caching for S3, which keeps a copy of the most recently used JSON records in RAM.  Not only will this increase overall performance, but it is especially important if you use any of the advanced storage features like [Lists](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Lists.md), [Hashes](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Hashes.md), [Transactions](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Transactions.md) or the [Indexer](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Indexer.md).

To enable the S3 cache, include a `cache` object in your `S3` configuration with the following properties:

```json
{
	"cache": {
		"enabled": true,
		"maxItems": 1000,
		"maxBytes": 10485760
	}
}
```

The properties are as follows:

| Property Name | Type | Description |
|---------------|------|-------------|
| `enabled` | Boolean | Set this to `true` to enable the S3 caching system. |
| `maxItems` | Integer | This is the maximum number of objects to allow in the cache. |
| `maxBytes` | Integer | This is the maximum number of bytes to allow in the cache. |

The cache will automatically expire objects in LRU fashion when either of the limits are met (whichever is reached first).  Set the properties to `0` for no limit.

It is recommended that you set the `maxItems` and `maxBytes` high enough to allow new data written to live for *at least* several seconds before getting expired out of the cache.  This depends on the overall storage throughput of your application, but 1,000 max items and 10 MB max bytes is probably fine for most use cases.

Note that binary records are **not** cached, as they are generally large.  Only JSON records are cached, as they are usually much smaller and used in [Lists](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Lists.md), [Hashes](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Hashes.md), [Transactions](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Transactions.md) and the [Indexer](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Indexer.md).

### S3 Compatible Services

To use an S3 compatible service such as [MinIO](https://github.com/minio/minio), you'll need to add a few extra parameters to the `AWS` section:

```js
{
	"endpoint": "http://minio:9000",
	"endpointPrefix": false,
	"forcePathStyle": true,
	"hostPrefixEnabled": false
}
```

Replace `minio:9000` with your MinIO hostname or IP address, and port number (9000 is the default).

Here is a complete example with the new parameters added:

```js
{
	"Storage": {
		"transactions": true,
		"trans_auto_recover": true,
		
		"engine": "S3",
		"AWS": {
			"endpoint": "http://minio:9000",
			"endpointPrefix": false,
			"forcePathStyle": true,
			"hostPrefixEnabled": false,
			"region": "us-west-1",
			"credentials": {
				"accessKeyId": "YOUR_MINIO_ACCESS_KEY", 
				"secretAccessKey": "YOUR_MINIO_SECRET_KEY"
			}
		},
		"S3": {
			"connectTimeout": 5000,
			"socketTimeout": 5000,
			"maxAttempts": 50,
			"keyPrefix": "",
			"fileExtensions": true,
			"params": {
				"Bucket": "YOUR_MINIO_BUCKET_ID"
			},
			"cache": {
				"enabled": true,
				"maxItems": 1000,
				"maxBytes": 10485760
			}
		}
	}
}
```

## Redis

If you want to use [Redis](https://redis.io/) as a backing store, here is how to do so.  First, you need to manually install the [ioredis](https://www.npmjs.com/package/ioredis) module into your app:

```sh
npm install --save ioredis
```

Then configure your storage thusly:

```json
{
	"engine": "Redis",
	"Redis": {
		"host": "127.0.0.1",
		"port": 6379,
		"keyPrefix": "",
		"keyTemplate": ""
	}
}
```

Set the `host` and `port` for your own Redis server setup.  Please see [Common Redis Options](https://redis.github.io/ioredis/interfaces/CommonRedisOptions.html) for other things you can include here, such as timeouts, authentication and database selection.

The optional `keyPrefix` property works similarly to the [S3 Key Prefix](#s3-key-prefix) feature.  It allows you to prefix all the Redis keys with a common string, to separate your application's data in a shared database situation.

The optional `keyTemplate` property works similarly to the [S3 Key Template](#s3-key-template) feature.  It allows you to specify an exact layout of MD5 hash characters, which can be prefixed, mixed in with or postfixed after the key.

### RedisCluster

If you want to use a Redis cluster (e.g. [AWS ElastiCache](https://aws.amazon.com/elasticache/)), then here is how to do that.  First, you will need to manually install the following module into your app:

```sh
npm install --save ioredis
```

Then configure your storage thusly:

```json
{
	"engine": "RedisCluster",
	"RedisCluster": {
		"host": "127.0.0.1",
		"port": 6379,
		"connectRetries": 5,
		"clusterOpts": {
			"scaleReads": "master",
			"redisOptions": {
				"commandTimeout": 5000,
				"connectTimeout": 5000
			}
		},
		"keyPrefix": "",
		"keyTemplate": ""
	}
}
```

Set the `host` and `port` for your own Redis cluster setup.  The `host` should point to the cluster endpoint, **not** an individual Redis server.  The `connectRetries` sets the number of retries on the initial socket connect operation (it defaults to `5`).

The `clusterOpts` property can hold several different cluster configuration options.  Please see [Cluster Options](https://redis.github.io/ioredis/interfaces/ClusterOptions.html) for other things you can include here, such as `scaleReads` and `redisOptions`.  For the `redisOptions` object, please see [Common Redis Options](https://redis.github.io/ioredis/interfaces/CommonRedisOptions.html) for other things you can include, such as timeouts, authentication and database selection.

It is **highly recommended** that you keep the `scaleReads` property set to `"master"`, for immediate consistency (required for [Lists](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Lists.md), [Hashes](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Hashes.md), [Transactions](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Transactions.md) and the [Indexer](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Indexer.md)).

The optional `keyPrefix` property works similarly to the [S3 Key Prefix](#s3-key-prefix) feature.  It allows you to prefix all the Redis keys with a common string, to separate your application's data in a shared database situation.

The optional `keyTemplate` property works similarly to the [S3 Key Template](#s3-key-template) feature.  It allows you to specify an exact layout of MD5 hash characters, which can be prefixed, mixed in with or postfixed after the key.

## SQLite

If you want to use [SQLite](https://sqlite.com/) as a backing store, here is how to do so.  First, you need to manually install the [better-sqlite3](https://www.npmjs.com/package/better-sqlite3) module into your app:

```sh
npm install --save better-sqlite3
```

Then configure your storage thusly:

```json
{
	"engine": "SQLite",
	"SQLite": {
		"base_dir": "data",
		"filename": "sqlite.db",
		"pragmas": {
			"auto_vacuum": 0,
			"cache_size": -100000,
			"journal_mode": "WAL"
		},
		"backups": {
			"enabled": false,
			"dir": "data/backups",
			"filename": "backup-[yyyy]-[mm]-[dd].db",
			"compress": true,
			"keep": 7
		},
		"keyPrefix": "",
		"keyTemplate": ""
	}
}
```

The `base_dir` defaults to the current working directory, and will be created on startup if necessary.  The `filename` is the name of the SQLite DB file on disk (also created if necessary).

The optional `pragmas` object allows you set one or more [SQLite Pragmas](https://www.sqlite.org/pragma.html#toc) (configuration settings) on the database at startup.  Here you can specify things such as [auto_vacuum](https://www.sqlite.org/pragma.html#pragma_auto_vacuum), [cache_size](https://www.sqlite.org/pragma.html#pragma_cache_size) and [journal_mode](https://www.sqlite.org/pragma.html#pragma_journal_mode), among many others.

The optional `backups` object allows you to configure daily backups of the SQLite database file, which happens during the [daily maintenance](#daily-maintenance) event.  Set `enabled` to `true` to enable backups, then set `dir` to the directory to hold the backups, `filename` to the destination filename (you can use date/time placeholders here), `compress` to compress the backups with gzip, and `keep` to keep the latest N backups in the dir (i.e. auto-delete the oldest ones).  Please note that the backup operation locks the database, so it will cause other storage operations to hang while it is writing to the file.

The optional `keyPrefix` property works similarly to the [S3 Key Prefix](#s3-key-prefix) feature.  It allows you to prefix all the SQLite keys with a common string, to separate your application's data in a shared database situation.

The optional `keyTemplate` property works similarly to the [S3 Key Template](#s3-key-template) feature.  It allows you to specify an exact layout of MD5 hash characters, which can be prefixed, mixed in with or postfixed after the key.

## Hybrid

Your application may need the features of multiple engines.  Specifically, you may want JSON (document) records to use one engine, and binary records to use another.  Binary records are specified with keys that end in a file extension, e.g. `.jpg`.  To facilitate this, there is a `Hybrid` engine available, which can load multiple sub-engines, one for JSON keys and one for binary keys.  Example use:

```json
{
	"engine": "Hybrid",
	"Hybrid": {
		"docEngine": "Filesystem",
		"binaryEngine": "S3"
	}
}
```

The `Hybrid` engine only has two properties, `docEngine` and `binaryEngine`.  These should be set to the names of sub-engines to load and use for JSON (document) records and binary records respectively.  In this example we're using the `Filesystem` engine for JSON (document) records, and the `S3` engine for binary records.  The idea is that you also include configuration objects for each of the sub-engines:

```json
{
	"engine": "Hybrid",
	"Hybrid": {
		"docEngine": "Filesystem",
		"binaryEngine": "S3"
	},
	"Filesystem": {
		"base_dir": "/let/data/myserver"
	},
	"AWS": {
		"accessKeyId": "YOUR_AMAZON_ACCESS_KEY", 
		"secretAccessKey": "YOUR_AMAZON_SECRET_KEY", 
		"region": "us-west-1"
	},
	"S3": {
		"fileExtensions": true,
		"params": {
			"Bucket": "MY_S3_BUCKET_ID"
		}
	}
}
```

Note that all of the engine configuration objects are on the same level as the `Hybrid` object.

# Key Normalization

In order to maintain compatibility with all the various engines, keys are "normalized" on all entry points.  Specifically, they undergo the following transformations before being passed along to the engine:

* Unicode characters are down-converted to ASCII (via [unidecode](https://github.com/FGRibreau/node-unidecode)).
	* Those that do not have ASCII equivalents are stripped off (e.g. Emoji).
* Only the following characters are allowed (everything else is stripped):
	* Alphanumerics
	* Dashes (hyphens)
	* Dots (periods)
	* Forward-slashes
* All alphanumeric characters are converted to lower-case.
* Duplicate adjacent slashes (i.e. "//") are converted to a single slash.
* Leading and trailing slashes are stripped.

So for example, this crazy key:

```
" / / / // HELLO-KEY @*#&^$*@/#&^$(*@#&^$ 😃  tést   / "
```

...is normalized to this:

```
"hello-key/test"
```

The same key normalization filter is applied when both storing and fetching records.

# Basic Functions

The storage module supports the following basic methods for typical operations.  Upon error, all callback methods are passed an `Error` object as the first argument.  If not, the first argument will be falsey (i.e. `false`, `0`, `null` or `undefined`), and the second argument will contain any requested data, if applicable.

The code examples all assume you have your preloaded `Storage` component instance in a local variable named `storage`.  The component instance can be retrieved from a running server like this:

```js
let storage = server.Storage;
```

## Storing Records

To store a record, call the [put()](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/API.md#put) method.  Pass in a key, a value, and a callback.  The value may be an Object (which is automatically serialized to JSON), or a `Buffer` for a binary blob (see [Storing Binary Blobs](#storing-binary-blobs) below).  If the record doesn't exist, it is created, otherwise it is replaced.

```js
storage.put( 'test1', { foo: 'bar1' }, function(err) {
	if (err) throw err;
} );
```

## Fetching Records

To fetch a record, call the [get()](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/API.md#get) method.  Pass in a key, and a callback.  The data returned will be parsed back into an Object if JSON, or a raw `Buffer` object will be returned for binary records.

```js
storage.get( 'test1', function(err, data) {
	if (err) throw err;
} );
```

If you try to fetch a nonexistent record, a special error object will be passed to your callback with its `code` property set to `NoSuchKey`.  This is a special case allowing you to easily differentiate a "record not found" error from another, more severe I/O error.  Example:

```js
storage.get( 'this_key_does_not_exist', function(err, data) {
	if (err) {
		if (err.code == 'NoSuchKey') {
			// record not found
		}
		else {
			// some other error
		}
	}
	else {
		// success, data will contain the record
	}
} );
```

Some engines also allow you to "head" (i.e. ping) an object to retrieve some metadata about it, without fetching the value.  To do this, call the [head()](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/API.md#head) method, and pass in the key.  The metadata usually consists of the size (`len`) and last modification date (`mod`).  Example:

```js
storage.head( 'test1', function(err, data) {
	if (err) throw err;
	// data.mod
	// data.len
} );
```

You can fetch multiple records at once by calling `getMulti()` and passing in array of keys.  Example:

```js
storage.getMulti( ['test1', 'test2', 'test3'], function(err, values) {
	if (err) throw err;
	// values[0] will be the test1 record.
	// values[1] will be the test2 record.
	// values[2] will be the test3 record.
} );
```

## Copying Records

To make a copy of a record and store it under a new key, call the [copy()](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/API.md#copy) method.  Pass in the old key, new key, and a callback.

```js
storage.copy( 'test1', 'test2', function(err) {
	if (err) throw err;
} );
```

**Note:** This is a compound function containing multiple sequential engine operations.  You may require locking depending on your application.  See [Advisory Locking](#advisory-locking) below.

## Renaming Records

To rename a record, call the [rename()](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/API.md#rename) method.  Pass in the old key, new key, and a callback.

```js
storage.rename( 'test1', 'test2', function(err) {
	if (err) throw err;
} );
```

**Note:** This is a compound function containing multiple sequential engine operations.  You may require locking depending on your application.  See [Advisory Locking](#advisory-locking) below.

## Deleting Records

To delete a record, call the [delete()](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/API.md#delete) method.  This is immediate and permanent.  Pass in the key, and a callback.

```js
storage.delete( 'test1', function(err) {
	if (err) throw err;
} );
```

# Storing Binary Blobs

To store a binary value, pass a filled `Buffer` object as the value, and specify a key ending in a "file extension", e.g. `.gif`.  The latter requirement is so the engine can detect which records are binary and which are JSON, just by looking at the key.  Example:

```js
const fs = require('fs');
let buffer = fs.readFileSync('picture.gif');
storage.put( 'test1.gif', buffer, function(err) {
	if (err) throw err;
} );
```

When fetching a binary record, a `Buffer` object will be passed to your callback:

```js
const fs = require('fs');
storage.get( 'test1.gif', function(err, buffer) {
	if (err) throw err;
	fs.writeFileSync('picture.gif', buffer);
} );
```

# Using Streams

You can store and fetch binary records using [streams](https://nodejs.org/api/stream.html), so as to not load any content into memory.  This can be used to manage extremely large files in a memory-limited environment.  Note that the record content is treated as binary, so the keys *must* contain file extensions.  To store an object using a readable stream, call the [putStream()](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/API.md#putstream) method.  Similarly, to fetch a readable stream to a record, call the [getStream()](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/API.md#getstream) method.

Example of storing a record by spooling the data from a file:

```js
const fs = require('fs');
let stream = fs.createReadStream('picture.gif');

storage.putStream( 'test1.gif', stream, function(err) {
	if (err) throw err;
} );
```

Example of fetching a read stream and spooling it to a file:

```js
const fs = require('fs');
let writeStream = fs.createWriteStream('/let/tmp/downloaded.gif');

storage.getStream( 'test1.gif', function(err, readStream) {
	if (err) throw err;
	writeStream.on('finish', function() {
		// data is completely written
	} );
	readStream.pipe( writeStream );
} );
```

Please note that not all the storage engines support streams natively, so the content may actually be loaded into RAM in the background.  Namely, as of this writing, the Redis APIs do not support streams, so they are currently simulated in those engines.  Streams *are* supported natively in both the Filesystem and Amazon S3 engines.

# Expiring Data

By default all records live indefinitely, and have no predetermined lifespan.  However, you can set an expiration date on any record, and it will be deleted on that day by the daily maintenance job (see [Daily Maintenance](#daily-maintenance) below).  Note that there is no support for an expiration *time*, but rather only a date.

To set the expiration date for a record, call the [expire()](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/API.md#expire) method, passing in the key and the desired expiration date.  This function completes instantly and requires no callback.  The date argument can be a JavaScript `Date` object, any supported date string (e.g. `YYYY-MM-DD`), or Epoch seconds.  Example:

```js
storage.expire( 'test1', '2015-05-12' );
```

It is wasteful to call this multiple times for the same record and the same date.  It adds extra work for the maintenance job, as each call adds an event in a list that must be iterated over.  It should only be called once per record, or when extending the expiration date to a future day.

Please note that if you require the ability to update expiration dates on existing records, you must explicitly set the [expiration_updates](#expiration_updates) configuration property to `true`.  This activates additional internal bookkeeping, which keeps track of all current record expiration dates, so they can be efficiently updated.  Note that this does incur some additional overhead.

## Custom Record Types

You can register custom record types if they require special handling for deletion.  For example, your application may define its own record type that has other related records which must also be deleted.  Instead of setting separate expiration dates for all your related records, you can set one single expiration date on the primary record, and register it as a custom type.  Then, when the [daily maintenance](#daily-maintenance) runs, your custom handler function will be called for your custom records, and you can delete the all related records yourself.

Your custom records are identified by a special top-level `type` property in their JSON.  This property must be set to a unique string that you pre-register with the storage system at startup.  Note that only JSON records are supported for custom deletion -- binary records are not.

To register a custom record type, call the [addRecordType()](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/API.md#addrecordtype) method, and pass in a custom type key (string), and an object containing key/value pairs for actions and handlers.  Currently only the `delete` action is defined, for handling maintenance (expiration) of your custom record type.  Example use:

```js
storage.addRecordType( 'my_custom_type', {
	delete: function(key, value, callback) {
		// custom handler function, called from daily maint for expired records
		// execute my own custom deletion routine here, then fire the callback
		callback();
	}
});
```

So the idea here is whenever the [daily maintenance](#daily-maintenance) job runs, and encounters JSON records with a `type` property set to `my_custom_type`, your custom handler function would be called to handle the deletes for the expired records.  This would happen instead of a typical call to [delete()](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/API.md#delete), which is the default behavior.

# Advisory Locking

The storage system provides a simple, in-memory advisory locking mechanism.  All locks are based on a specified key, and can be exclusive or shared.  You can also choose to wait for a lock to be released by passing `true` as the 2nd argument, or fail immediately if the key is already locked by passing `false`.  To lock a key in exclusive mode, call [lock()](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/API.md#lock), and to unlock it call [unlock()](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/API.md#unlock).

Here is a simple use case:

```js
storage.lock( 'test1', true, function() {
	// key is locked, now we can fetch
	storage.get( key, function(err, data) {
		if (err) {
			storage.unlock('test1');
			throw err;
		}
		
		// increment counter
		data.counter++;
		
		// save back to storage
		storage.put( 'test1', data, function(err) {
			if (err) {
				storage.unlock('test1');
				throw err;
			}
			
			// and finally unlock
			storage.unlock('test1');
		} ); // put
	} ); // get
} ); // lock
```

The above example is a typical counter increment pattern using advisory locks.  The `test1` record is locked, fetched, its counter incremented, written back to disk, then finally unlocked.  The idea is, even though all the storage operations are async, all other requests for this record will block until the lock is released.  Remember that you always need to call `unlock()`, even if throwing an error.

In addition to exclusive locks, you can request a "shared" lock.  Shared locking allows multiple clients to access the key simultaneously.  For example, one could lock a key for reading using shared locks, but lock it for writing using an exclusive lock.  To lock a key in shared mode, call [shareLock()](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/API.md#sharelock), and to unlock it call [shareUnlock()](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/API.md#shareunlock).  Example:

```js
storage.shareLock( 'test1', true, function() {
	// key is locked, now we can fetch data safely
	storage.get( key, function(err, data) {
		storage.shareUnlock('test1');
		if (err) {
			throw err;
		}
	} ); // get
} ); // lock
```

Shared locks obey the following rules:

- If a key is already locked in exclusive mode, the shared lock waits for the exclusive lock to clear.
- If a key is already locked in shared mode, multiple clients are allowed to lock it simultaneously.
- If an exclusive lock is requested on a key that is locked in shared mode, the following occurs:
	- The exclusive lock must wait for all current shared clients to unlock.
	- Additional shared clients must wait until after the exclusive lock is acquired, and released.

Shared locks are used internally for accessing complex structures like lists, hashes and searching records in an index.

Please note that all locks are implemented in RAM, so they only exist in the current Node.js process.  This is really only designed for single-process daemons, and clusters with one master server doing writes.

# Logging

The storage library uses the logging system built into [pixl-server](https://github.com/jhuckaby/pixl-server#logging).  Essentially there is one combined "event log" which contains debug messages, errors and transactions (however, this can be split into multiple logs if desired).  The `component` column will be set to either `Storage`, or the storage engine Plugin (e.g. `Filesystem`).

In all these log examples the first 3 columns (`hires_epoch`, `date` and `hostname`) are omitted for display purposes.  The columns shown are `component`, `category`, `code`, `msg`, and `data`.

## Debug Logging

Log entries with the `category` set to `debug` are debug messages, and have a verbosity level from 1 to 10 (echoed in the `code` column).  Here is an example snippet, showing a hash being created and a key added:

```
[Storage][debug][9][Storing hash key: users: bsanders][]
[Storage][debug][9][Requesting lock: |users][]
[Storage][debug][9][Locked key: |users][]
[Storage][debug][9][Loading hash: users][]
[Filesystem][debug][9][Fetching Object: users][data/users.json]
[Storage][debug][9][Hash not found, creating it: users][]
[Storage][debug][9][Creating new hash: users][{"page_size":10,"length":0,"type":"hash"}]
[Filesystem][debug][9][Fetching Object: users][data/users.json]
[Filesystem][debug][9][Storing JSON Object: users][data/users.json]
[Filesystem][debug][9][Store operation complete: users][]
[Filesystem][debug][9][Storing JSON Object: users/data][data/users/data.json]
[Filesystem][debug][9][Store operation complete: users/data][]
[Filesystem][debug][9][Fetching Object: users/data][data/users/data.json]
[Filesystem][debug][9][JSON fetch complete: users/data][]
[Filesystem][debug][9][Storing JSON Object: users/data][data/users/data.json]
[Filesystem][debug][9][Store operation complete: users/data][]
[Filesystem][debug][9][Storing JSON Object: users][data/users.json]
[Filesystem][debug][9][Store operation complete: users][]
[Storage][debug][9][Unlocking key: |users (0 clients waiting)][]
```

## Error Logging

Errors have the `category` column set to `error`, and come with a `code` and `msg`, both strings.  Errors are typically things that should not ever occur, such as failures to read or write records.  Example:

```
[Filesystem][error][file][Failed to read file: bad/users: data/bad/users.json: EACCES: permission denied, open 'data/bad/users.json'][]
```

Other examples of errors include transaction commit failures and transaction rollbacks.

## Transaction Logging

Transactions (well, more specifically, all storage actions) are logged with the `category` column set to `transaction`.  The `code` column will be one of the following constants, denoting which action took place:

```
get, put, head, delete, expire_set, perf_sec, perf_min, commit, index, unindex, search, sort, maint
```

You can control which of these event types are logged, by including a `log_event_types` object in your storage configuration.  Include keys with true values for any log event types you want to see logged.  Example:

```js
log_event_types: { 
	get:0, put:1, head:0, delete:1, expire_set:1, perf_sec:1, perf_min:1,
	commit:1, index:1, unindex:1, search:0, sort:0, maint:1 
}
```

Alternatively, you can just set the `all` key to log all event types:

```js
log_event_types: { 
	all: 1
}
```

Finally, the `data` column will contain some JSON-formatted metadata about the event, always including the `elapsed_ms` (elapsed time in milliseconds), but often other information as well.

Here are some example transaction log entries:

```
[Storage][transaction][get][index/ontrack/summary/word/releas][{"elapsed_ms":1.971}]
[Storage][transaction][put][index/ontrack/created/sort/data][{"elapsed_ms":1.448}]
[Storage][transaction][commit][index/ontrack][{"id":"0f760e77075fdd18c8d39f88e76c1f5e","elapsed_ms":38.286,"actions":25}]
[Storage][transaction][index][index/ontrack][{"id":"2653","elapsed_ms":92.368}]
[Storage][transaction][search][index/ontrack][{"query":"(status = \"closed\" && summary =~ \"Released to Preproduction\")","elapsed_ms":14.206,"results":24}]
```

## Performance Logs

If your application has continuous storage traffic, you might be interested in logging aggregated performance metrics every second, and/or every minute.  These can be enabled by setting `perf_sec` and/or `perf_min` properties in the `log_event_types` configuration object, respectively:

```js
log_event_types: { 
	perf_sec: 1, 
	perf_min: 1
}
```

Performance metrics are logged with the `category` column set to `perf`.  The actual metrics are in JSON format, in the `data` column.  Here is an example performance log entry:

```
[Storage][perf][second][Last Second Performance Metrics][{"get":{"min":0.132,"max":8.828,"total":319.99,"count":249,"avg":1.285},"index":{"min":24.361,"max":31.813,"total":137.421,"count":5,"avg":27.484},"commit":{"min":16.693,"max":26.227,"total":105.538,"count":5,"avg":21.107},"put":{"min":0.784,"max":7.367,"total":198.952,"count":125,"avg":1.591}}]
```

That JSON data is the same format returned by the [getStats()](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/API.md#getstats) method.  See below for details.

Note that performance metrics are only logged if there was at least one event.  If your application is completely idle, it will not log anything.

# Performance Metrics

If you want to fetch performance metrics on-demand, call the [getStats()](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/API.md#getstats) method.  This returns an object containing a plethora of information, including min/avg/max metrics for all events.  Example response, formatted as JSON for display:

```json
{
	"version": "2.0.0",
	"engine": "Filesystem",
	"concurrency": 4,
	"transactions": true,
	"last_second": {
		"search": {
			"min": 14.306,
			"max": 14.306,
			"total": 14.306,
			"count": 1,
			"avg": 14.306
		},
		"get": {
			"min": 0.294,
			"max": 2.053,
			"total": 5.164,
			"count": 5,
			"avg": 1.032
		}
	},
	"last_minute": {},
	"recent_events": {
		"get": [
			{
				"date": 1519507643.523,
				"type": "get",
				"key": "index/ontrack/status/word/closed",
				"data": {
					"elapsed_ms": 1.795
				}
			},
			{
				"date": 1519507643.524,
				"type": "get",
				"key": "index/ontrack/summary/word/releas",
				"data": {
					"elapsed_ms": 2.053
				}
			}
		]
	},
	"locks": {}
}
```

Here are descriptions of the main elements:

| Property Name | Description |
|---------------|-------------|
| `version` | The current version of the `pixl-server-storage` module. |
| `engine` | The name of the current engine Plugin, e.g. `Filesystem`. |
| `concurrency` | The current concurrency setting (i.e. max threads). |
| `transactions` | Whether [transactions](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Transactions.md) are enabled (true) or disabled (false). |
| `last_second` | A performance summary of the last second (see below). |
| `last_minute` | A performance summary of the last minute (see below). |
| `recent_events` | The most recent N events (see below). |
| `locks` | Any storage keys that are currently locked (both exclusive and shared). |

The performance metrics (both `last_second` and `last_minute`) include minimums, averages, maximums, counts and totals for each event, and are provided in this format:

```json
{
	"search": {
		"min": 14.306,
		"max": 14.306,
		"total": 14.306,
		"count": 1,
		"avg": 14.306
	},
	"get": {
		"min": 0.294,
		"max": 2.053,
		"total": 5.164,
		"count": 5,
		"avg": 1.032
	}
}
```

All the measurements are in milliseconds, and represent any actions that took place over the last second or minute.

The `recent_events` object will only be populated if the `max_recent_events` configuration property is set to a positive number.  This will keep track of the last N events in each type, and provide them here.  This feature is disabled by default, as it incurs a small memory overhead for bookkeeping.

# Daily Maintenance

If you plan on expiring records for future deletion (see [Expiring Data](#expiring-data) above), you should enable the nightly maintenance job.  This will iterate over all the records that expired on the current day, and actually delete them.  To do this, set the [maintenance](#maintenance) key in your storage configuration, and set it to a `HH::MM` string:

```js
{
	"maintenance": "04:30" // run daily at 4:30 AM
}
```

This is mainly for daemons that run 24x7.  Also, there is no automated recovery if the server was down when the maintenance job was supposed to run.  So you may need to call `storage.runMaintenance()` manually for those rare cases, and pass in today's date (or the date when it should have ran), and a callback.

# Plugin Development

New engine plugins can easily be added.  All you need to do is create a class that implements a few standard API methods, and then load your custom engine using the [engine_path](#engine_path) configuration parameter.

Here are the API methods your class should define:

| API Method | Arguments | Description |
|--------|-----------|-------------|
| `startup()` | CALLBACK | Optional, called as the server starts up. Fire the callback when your engine is ready. |
| `put()` | KEY, VALUE, CALLBACK | Store the key/value pair, and then fire the callback. |
| `head()` | KEY, CALLBACK | Optional, fetch any metadata you may have about the record, and fire the callback. |
| `get()` | KEY, CALLBACK | Fetch the key, and pass the value to the callback. |
| `delete()` | KEY, CALLBACK | Delete the specified key, then fire the callback. |
| `shutdown()` | CALLBACK | Optional, called as the server shuts down. Fire the callback when your engine has stopped. |

It is recommended you inherit from the `pixl-server/component` base class.  This implements some useful methods such as `logDebug()`.

Here is an example skeleton class you can start from:

```js
const Component = require("pixl-server/component");

module.exports = class MyEngine extends Component {
	
	startup(callback) {
		// setup initial connection
		let self = this;
		this.logDebug(2, "Setting up MyEngine");
		callback();
	}
	
	put(key, value, callback) {
		// store record given key and value
		callback();
	}
	
	head(key, callback) {
		// retrieve metadata on record (mod, len)
		callback();
	}
	
	get(key, callback) {
		// fetch record value given key
		callback();
	}
	
	delete(key, callback) {
		// delete record
		callback();
	}
	
	shutdown(callback) {
		// shutdown storage
		this.logDebug(2, "Shutting down MyEngine");
		callback();
	}
	
};
```

# Unit Tests

To run the unit test suite, issue this command from within the module directory:

```sh
npm test
```

If you install the [pixl-unit](https://www.github.com/jhuckaby/pixl-unit) module globally, you can provide various command-line options, such as verbose mode:

```sh
pixl-unit test/test.js --verbose
```

This also allows you to specify an alternate test configuration file via the `--configFile` option.  Using this you can load your own test config, which may use a different engine (e.g. S3, etc.):

```sh
pixl-unit test/test.js --configFile /path/to/my/config.json
```

# License

**The MIT License (MIT)**

Copyright (c) 2015 - 2026 Joseph Huckaby.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

## File: `standalone.js`
```javascript
// Storage System - Standalone Mode
// Copyright (c) 2015 Joseph Huckaby
// Released under the MIT License

var Class = require("pixl-class");
var Config = require("pixl-config");
var Storage = require("pixl-server-storage");
var EventEmitter = require('events');

var server = new EventEmitter();
server.debug = false;
server.config = new Config({});

server.logger = {
	get: function(key) { return (key == 'debugLevel') ? 9 : ''; },
	set: function(key, value) { this[key] = value; },
	debug: function(level, msg, data) {
		if (server.debug) {
			if (data) msg += " (" + JSON.stringify(data) + ")";
			console.log('[' + ((new Date()).getTime() / 1000) + '][DEBUG] ' + msg);
		}
	},
	error: function(code, msg, data) {
		if (data) msg += " (" + JSON.stringify(data) + ")";
		console.log('[' + ((new Date()).getTime() / 1000) + '][ERROR]['+code+'] ' + msg);
	},
	transaction: function(code, msg, data) {
		if (data) msg += " (" + JSON.stringify(data) + ")";
		console.log('[' + ((new Date()).getTime() / 1000) + '][TRANSACTION]['+code+'] ' + msg);
	}
};

module.exports = Class.create({
	
	__parent: Storage,
	
	__construct: function(config, callback) {
		if (config.logger) {
			server.logger = config.logger;
			delete config.logger;
		}
		
		this.config = new Config(config);
		server.debug = !!this.config.get('debug');
		
		this.init( server, this.config );
		server.Storage = this;
		
		process.nextTick( function() {
			server.Storage.startup( callback || function() {;} );
		} );
	}
	
});
```

## File: `storage.js`
```javascript
// PixlServer Storage System
// Copyright (c) 2015 - 2018 Joseph Huckaby
// Released under the MIT License

var util = require("util");
var async = require('async');
var unidecode = require('unidecode');

var Class = require("pixl-class");
var Tools = require("pixl-tools");
var Perf = require("pixl-perf");
var Component = require("pixl-server/component");
var List = require("./list.js");
var Hash = require("./hash.js");
var Indexer = require("./indexer.js");
var Transaction = require("./transaction.js");

module.exports = Class.create({
	
	__name: 'Storage',
	__parent: Component,
	__mixins: [ List, Hash, Indexer, Transaction ],
	
	version: require('./package.json').version,
	
	defaultConfig: {
		list_page_size: 50,
		hash_page_size: 50,
		concurrency: 1,
		maintenance: 0,
		log_event_types: { 
			all:0, get:0, put:0, head:0, delete:0, expire_set:0, perf_sec:0, perf_min:0,
			commit:0, index:0, unindex:0, search:0, sort:0, maint:1 
		},
		max_recent_events: 0,
		cache_key_match: '',
		expiration_updates: false,
		lower_case_keys: true,
		queue_timeout: 30000
	},
	
	locks: null,
	cache: null,
	cacheKeyRegex: null,
	started: false,
	customRecordTypes: null,
	
	earlyStart: function() {
		// check for early transaction recovery
		if (!this.config.get('transactions')) return true;
		
		// transactions are enabled
		return this.transEarlyStart();
	},
	
	startup: function(callback) {
		// setup storage plugin
		var self = this;
		this.logDebug(5, "Setting up storage system v" + this.version);
		
		// advisory locking system (in RAM, single process only)
		this.locks = {};
		
		// ram cache for certain keys, configurable
		this.cache = {};
		this.cacheKeyRegEx = null;
		
		// cache some config values, and listen for config refresh
		this.prepConfig();
		this.config.on('reload', this.prepConfig.bind(this) );
		
		// dynamically load storage engine based on config
		var StorageEngine = require(
			this.config.get('engine_path') || 
			("./engines/" + this.config.get('engine') + ".js")
		);
		this.engine = new StorageEngine();
		this.engine.storage = this;
		this.engine.init( this.server, this.config.getSub( this.config.get('engine') ) );
		
		// queue for setting expirations and custom engine ops
		this.queue = async.queue( this.dequeue.bind(this), this.concurrency );
		
		// setup perf tracking system
		this.perf = new Perf();
		this.perf.minMax = true;
		
		this.minutePerf = new Perf();
		this.minutePerf.minMax = true;
		
		this.lastSecondMetrics = {};
		this.lastMinuteMetrics = {};
		this.recentEvents = {};
		
		// allow others to register custom record types for maint
		this.customRecordTypes = {};
		
		// bind to server tick, so we can aggregate perf metrics
		this.server.on('tick', this.tick.bind(this));
		this.server.on('minute', this.tickMinute.bind(this));
		
		// setup daily maintenance, if configured
		if (this.config.get('maintenance')) {
			// e.g. "day", "04:00", etc.
			this.server.on(this.config.get('maintenance'), function() {
				self.runMaintenance();
			});
		}
		
		// allow engine to startup as well
		this.engine.startup( function(err) {
			if (err) return callback(err);
			
			// set started flag, as transactions may need to recover from a crash
			self.started = true;
			
			// finally, init transaction system
			self.initTransactions( function(err) {
				
				// all done
				callback(err);
				
			} ); // initTransactions
		} ); // engine.startup
	},
	
	prepConfig: function() {
		// save some config values
		this.listItemsPerPage = this.config.get('list_page_size');
		this.hashItemsPerPage = this.config.get('hash_page_size');
		this.concurrency = this.config.get('concurrency');
		this.logEventTypes = this.config.get('log_event_types');
		this.maxRecentEvents = this.config.get('max_recent_events');
		this.expHash = this.config.get('expiration_updates');
		this.lowerKeys = this.config.get('lower_case_keys');
		this.queueTimeout = this.config.get('queue_timeout');
		
		this.cacheKeyRegex = null;
		if (this.config.get('cache_key_match')) {
			this.cacheKeyRegex = new RegExp( this.config.get('cache_key_match') );
		}
	},
	
	normalizeKey: function(key) {
		// downconvert unicode, lower-case, alphanum-dash-dot-slash only, strip leading and trailing slashes
		key = '' + key;
		if (this.lowerKeys) key = key.toLowerCase();
		return unidecode(key).replace(/[^\w\-\.\/]+/g, '').replace(/\/+/g, '/').replace(/^\//, '').replace(/\/$/, '');
	},
	
	isBinaryKey: function(key) {
		// binary keys have a built-in file extension, JSON keys do not
		return !!key.match(/\.\w+$/);
	},
	
	addRecordType: function(type, handlers) {
		// add custom record type handler (for maint)
		// handlers: { delete: function }
		this.customRecordTypes[type] = handlers;
	},
	
	put: function(key, value, callback) {
		// store key+value pair
		var self = this;
		
		if (!this.started) return callback( new Error("Storage has not completed startup.") );
		key = this.normalizeKey( key );
		
		// sanity checks
		if (!value) return callback( new Error("Record value cannot be false.") );
		
		var isBuffer = Buffer.isBuffer(value);
		if (isBuffer && !this.isBinaryKey(key)) {
			return callback( new Error("Buffer values are only allowed with keys containing file extensions, e.g. " + key + ".bin") );
		}
		else if (!isBuffer && this.isBinaryKey(key)) {
			return callback( new Error("You must pass a Buffer object as the value when using keys containing file extensions.") );
		}
		
		// ram cache
		if (this.cacheKeyRegex && key.match(this.cacheKeyRegex)) {
			this.cache[key] = value;
		}
		
		// invoke engine and track perf
		var pf = this.perf.begin('put');
		
		this.engine.put( key, value, function(err) {
			// put complete
			var elapsed = pf.end();
			
			if (!err) self.logTransaction('put', key, {
				elapsed_ms: elapsed
			});
			
			callback(err);
			if (!err) self.emit('put', key, value);
		} );
	},
	
	putStream: function(key, stream, callback) {
		// store key+stream
		var self = this;
		
		if (!this.started) return callback( new Error("Storage has not completed startup.") );
		key = this.normalizeKey( key );
		
		if (!this.isBinaryKey(key)) {
			return callback( new Error("Stream values are only allowed with keys containing file extensions, e.g. " + key + ".bin") );
		}
		
		// sanity checks
		if (!stream || !stream.pipe) return callback( new Error("Not a valid stream.") );
		
		// invoke engine and track perf
		var pf = this.perf.begin('put');
		
		this.engine.putStream( key, stream, function(err) {
			// put complete
			var elapsed = pf.end();
			
			if (!err) self.logTransaction('put', key, {
				elapsed_ms: elapsed
			});
			
			callback(err);
			if (!err) self.emit('putStream', key);
		} );
	},
	
	putStreamCustom: function(key, stream, opts, callback) {
		// store key+stream with engine-specific opts
		var self = this;
		
		if (!this.started) return callback( new Error("Storage has not completed startup.") );
		key = this.normalizeKey( key );
		
		if (!this.isBinaryKey(key)) {
			return callback( new Error("Stream values are only allowed with keys containing file extensions, e.g. " + key + ".bin") );
		}
		
		// sanity checks
		if (!stream || !stream.pipe) return callback( new Error("Not a valid stream.") );
		
		// invoke engine and track perf
		var pf = this.perf.begin('put');
		
		this.engine.putStreamCustom( key, stream, opts, function(err) {
			// put complete
			var elapsed = pf.end();
			
			if (!err) self.logTransaction('put', key, {
				elapsed_ms: elapsed
			});
			
			callback(err);
			if (!err) self.emit('putStream', key);
		} );
	},
	
	putMulti: function(records, callback) {
		// put multiple records at once, given object of keys and values
		var self = this;
		if (!this.started) return callback( new Error("Storage has not completed startup.") );
		
		// if engine provides its own putMulti, call that directly
		if (("putMulti" in this.engine) && !this.currentTransactionPath) {
			return this.engine.putMulti(records, callback);
		}
		
		async.eachLimit(Object.keys(records), this.concurrency, 
			function(key, callback) {
				// iterator for each key
				self.put(key, records[key], function(err) {
					callback(err);
				} );
			}, 
			function(err) {
				// all keys stored
				callback(err);
			}
		);
	},
	
	head: function(key, callback) {
		// fetch metadata given key: { mod, len }
		var self = this;
		
		if (!this.started) return callback( new Error("Storage has not completed startup.") );
		key = this.normalizeKey( key );
		
		// invoke engine and track perf
		var pf = this.perf.begin('head');
		
		this.engine.head( key, function(err, data) {
			// head complete
			var elapsed = pf.end();
			
			if (!err) self.logTransaction('head', key, {
				elapsed_ms: elapsed
			});
			
			callback(err, data);
			if (!err) self.emit('head', key, data);
		} );
	},
	
	headMulti: function(keys, callback) {
		// head multiple records at once, given array of keys
		// callback is provided an array of values in matching order to keys
		var self = this;
		var records = {};
		if (!this.started) return callback( new Error("Storage has not completed startup.") );
		
		// if engine provides its own headMulti, call that directly
		if (("headMulti" in this.engine) && !this.currentTransactionPath) {
			return this.engine.headMulti(keys, callback);
		}
		
		async.eachLimit(keys, this.concurrency, 
			function(key, callback) {
				// iterator for each key
				self.head(key, function(err, data) {
					if (err) callback(err);
					records[key] = data;
					callback();
				} );
			}, 
			function(err) {
				if (err) return callback(err);
				
				// sort records into array of values ordered by keys
				var values = [];
				for (var idx = 0, len = keys.length; idx < len; idx++) {
					values.push( records[keys[idx]] );
				}
				
				callback(null, values);
			}
		);
	},
	
	get: function(key, callback) {
		// fetch value given key
		var self = this;
		if (!this.started) return callback( new Error("Storage has not completed startup.") );
		
		key = this.normalizeKey( key );
		var cacheable = !!(this.cacheKeyRegex && key.match(this.cacheKeyRegex));
		
		// ram cache
		if (cacheable && (key in this.cache)) {
			return process.nextTick( callback, null, this.cache[key] );
		}
		
		// invoke engine and track perf
		var pf = this.perf.begin('get');
		
		this.engine.get( key, function(err, value, info) {
			// get complete
			var elapsed = pf.end();
			
			if (err) return callback(err);
			
			// ram cache
			if (cacheable) {
				self.cache[key] = value;
			}
			
			self.logTransaction('get', key, {
				elapsed_ms: elapsed
			});
			
			callback(null, value, info);
			if (!err) self.emit('get', key, value, info);
		} );
	},
	
	getBuffer: function(key, callback) {
		// fetch buffer given key
		var self = this;
		if (!this.started) return callback( new Error("Storage has not completed startup.") );
		
		key = this.normalizeKey( key );
		
		// invoke engine and track perf
		var pf = this.perf.begin('get');
		
		this.engine.getBuffer( key, function(err, value, info) {
			// get complete
			var elapsed = pf.end();
			if (err) return callback(err);
			
			self.logTransaction('get', key, {
				elapsed_ms: elapsed
			});
			
			callback(null, value, info);
			if (!err) self.emit('get', key, value, info);
		} );
	},
	
	getStream: function(key, callback) {
		// fetch value via stream pipe
		var self = this;
		if (!this.started) return callback( new Error("Storage has not completed startup.") );
		
		key = this.normalizeKey( key );
		
		if (!this.isBinaryKey(key)) {
			return callback( new Error("Stream values are only allowed with keys containing file extensions, e.g. " + key + ".bin") );
		}
		
		this.engine.getStream( key, callback );
	},
	
	getStreamRange: function(key, start, end, callback) {
		// fetch value via stream pipe and range
		// start and end are both inclusive
		var self = this;
		if (!this.started) return callback( new Error("Storage has not completed startup.") );
		
		key = this.normalizeKey( key );
		
		if (!this.isBinaryKey(key)) {
			return callback( new Error("Stream values are only allowed with keys containing file extensions, e.g. " + key + ".bin") );
		}
		
		this.engine.getStreamRange( key, start, end, callback );
	},
	
	getMulti: function(keys, callback) {
		// fetch multiple records at once, given array of keys
		// callback is provided an array of values in matching order to keys
		var self = this;
		var records = {};
		if (!this.started) return callback( new Error("Storage has not completed startup.") );
		
		// if engine provides its own getMulti, call that directly
		if (("getMulti" in this.engine) && !this.currentTransactionPath) {
			return this.engine.getMulti(keys, callback);
		}
		
		async.eachLimit(keys, this.concurrency, 
			function(key, callback) {
				// iterator for each key
				self.get(key, function(err, data) {
					if (err) return callback(err);
					records[key] = data;
					callback();
				} );
			}, 
			function(err) {
				if (err) return callback(err);
				
				// sort records into array of values ordered by keys
				var values = [];
				for (var idx = 0, len = keys.length; idx < len; idx++) {
					values.push( records[keys[idx]] );
				}
				
				callback(null, values);
			}
		);
	},
	
	delete: function(key, callback) {
		// delete record given key
		var self = this;
		
		if (!this.started) return callback( new Error("Storage has not completed startup.") );
		key = this.normalizeKey( key );
		
		// ram cache
		if (this.cacheKeyRegex && key.match(this.cacheKeyRegex) && (key in this.cache)) {
			delete this.cache[key];
		}
		
		// invoke engine and track perf
		var pf = this.perf.begin('delete');
		
		this.engine.delete( key, function(err) {
			// delete complete
			var elapsed = pf.end();
			
			if (!err) self.logTransaction('delete', key, {
				elapsed_ms: elapsed
			});
			
			callback(err);
			if (!err) self.emit('delete', key);
		} );
	},
	
	deleteMulti: function(keys, callback) {
		// delete multiple records at once, given array of keys
		var self = this;
		if (!this.started) return callback( new Error("Storage has not completed startup.") );
		
		// if engine provides its own deleteMulti, call that directly
		if (("deleteMulti" in this.engine) && !this.currentTransactionPath) {
			return this.engine.deleteMulti(keys, callback);
		}
		
		async.eachLimit(keys, this.concurrency, 
			function(key, callback) {
				// iterator for each key
				self.delete(key, function(err) {
					callback(err);
				} );
			}, 
			function(err) {
				// all keys deleted
				callback(err);
			}
		);
	},
	
	copy: function(old_key, new_key, callback) {
		// copy record to new key
		var self = this;
		this.logDebug(9, "Copying record: " + old_key + " to " + new_key);
		
		// branch here if binary keys
		if (this.isBinaryKey(old_key) && this.isBinaryKey(new_key)) {
			this.getStream(old_key, function(err, stream) {
				if (err) return callback(err, null);
				self.putStream(new_key, stream, callback);
			} );
			return;
		}
		
		// load old key
		this.get(old_key, function(err, data) {
			if (err) return callback(err, null);
			
			// save new key
			self.put(new_key, data, callback);
		} );
	},
	
	rename: function(old_key, new_key, callback) {
		// rename record (copy + delete old)
		var self = this;
		this.logDebug(9, "Renaming record: " + old_key + " to " + new_key);
		
		this.copy( old_key, new_key, function(err, data) {
			// copied, now delete old
			self.delete( old_key, callback );
		} );
	},
	
	expire: function(key, expiration, force) {
		// set expiration date on key, normalize to midnight
		var dargs = Tools.getDateArgs(
			Tools.normalizeTime( expiration, { hour:0, min:0, sec:0 } ) 
		);
		
		var dnow = Tools.getDateArgs( new Date() );
		if (!force && ((dargs.epoch <= dnow.epoch) || (dargs.yyyy_mm_dd == dnow.yyyy_mm_dd))) {
			// date is in past, move to tomorrow, to avoid race condition with maintenance()
			// this trick guarantees tomorrow midnight regardless of daylight savings time
			dargs = Tools.getDateArgs( Tools.normalizeTime(
				Tools.normalizeTime( dnow.epoch, { hour:12, min:0, sec:0 } ) + 86400,
				{ hour:0, min:0, sec:0 } )
			);
		}
		
		this.logDebug(9, "Setting expiration on: " + key + " to " + dargs.yyyy_mm_dd);
		
		this.enqueue({
			action: 'expire_set',
			key: key,
			expiration: dargs.epoch
		});
		
		this.emit('expire', key, dargs.epoch);
	},
	
	enqueue: function(task) {
		// enqueue task for execution soon
		if (!this.started) throw new Error("Storage has not completed startup.");
		
		if (typeof(task) == 'function') {
			var func = task;
			task = { action: 'custom', handler: func };
		}
		task._id = Tools.generateShortID();
		this.logDebug(9, "Enqueuing async task: " + task._id + ": " + (task.label || task.action), 
			this.debugLevel(10) ? task : null
		);
		this.queue.push( task );
	},
	
	dequeue: function(task, callback) {
		// run task and fire callback
		var self = this;
		this.logDebug(9, "Running async task: " + task._id + ": " + (task.label || task.action), 
			this.debugLevel(10) ? task : null
		);
		
		// optional timeout for queue item execution
		var timer = this.queueTimeout ? setTimeout( function() {
			self.logError('queue', "Async task timed out: " + task._id + ": " + (task.label || task.action), { ms: self.queueTimeout });
			if (callback) callback();
			callback = null;
			timer = null;
		}, this.queueTimeout ) : null;
		
		switch (task.action) {
			case 'expire_set':
				// set expiration on record
				var dargs = Tools.getDateArgs( task.expiration );
				var cleanup_list_path = '_cleanup/' + dargs.yyyy + '/' + dargs.mm + '/' + dargs.dd;
				var cleanup_hash_path = '_cleanup/expires';
				
				this.listPush( cleanup_list_path, { key: task.key }, { page_size: 1000 }, function(err, data) {
					// should never fail, but who knows
					if (err) self.logError('cleanup', "Failed to push cleanup list: " + cleanup_list_path + ": " + err);
					
					if (self.expHash) {
						self.hashPut( cleanup_hash_path, task.key, { expires: task.expiration }, { page_size: 1000 }, function(err) {
							// should never fail, but who knows
							if (err) self.logError('cleanup', "Failed to put cleanup hash: " + cleanup_hash_path + ": " + err);
							
							self.logTransaction('expire_set', task.key, {
								epoch: dargs.epoch,
								yyyy_mm_dd: dargs.yyyy_mm_dd,
								list_path: cleanup_list_path
							});
							
							if (timer) clearTimeout(timer);
							timer = null;
							
							if (callback) callback();
							callback = null;
						} ); // hashPut
					} // expHash
					else {
						self.logTransaction('expire_set', task.key, {
							epoch: dargs.epoch,
							yyyy_mm_dd: dargs.yyyy_mm_dd,
							list_path: cleanup_list_path
						});
						
						if (timer) clearTimeout(timer);
						timer = null;
						
						if (callback) callback();
						callback = null;
					}
				} ); // listPush
			break; // expire_set
			
			case 'custom':
				// custom handler
				task.handler( task, function(err) {
					if (err) self.logError('storage', "Failed to dequeue custom task: " + err);
					
					if (timer) clearTimeout(timer);
					timer = null;
					
					if (callback) callback();
					callback = null;
				} );
			break; // custom
		} // switch action
	},
	
	runMaintenance: function(date, callback) {
		// run daily maintenance (delete expired keys)
		var self = this;
		var dargs = Tools.getDateArgs( date || (new Date()) );
		var cleanup_list_path = '_cleanup/' + dargs.yyyy + '/' + dargs.mm + '/' + dargs.dd;
		var cleanup_hash_path = '_cleanup/expires';
		var stats = {
			time_start: Tools.timeNow(),
			num_deleted: 0,
			num_skipped: 0,
			num_errors: 0
		};
		
		this.logDebug(3, "Running daily maintenance", cleanup_list_path);
		
		var deleteExpiredRecord = function(key, callback) {
			// delete single expired record of any type
			
			var finishDelete = function(err) {
				// log errors here (some records may already be deleted, which is fine)
				if (err) stats.num_errors++;
				
				// also delete metadata (expires epoch)
				if (self.expHash) {
					self.hashDelete( cleanup_hash_path, key, function(herr) { 
						if (!err) stats.num_deleted++;
						callback(); 
					} );
				}
				else {
					callback();
				}
			};
			
			if (self.isBinaryKey(key)) {
				// straight up delete for binary records
				self.delete( key, finishDelete );
			}
			else {
				// get JSON record to determine type
				self.get( key, function(err, data) {
					if (!data) data = {};
					if (data.type && (data.type == 'list')) {
						self.listDelete( key, true, finishDelete );
					}
					else if (data.type && (data.type == 'hash')) {
						self.hashDeleteAll( key, true, finishDelete );
					}
					else if (data.type && self.customRecordTypes[data.type] && self.customRecordTypes[data.type].delete) {
						self.logDebug(6, "Invoking custom record delete handler for type: " + data.type + ": " + key);
						var func = self.customRecordTypes[data.type].delete;
						func( key, data, finishDelete );
					}
					else {
						self.delete( key, finishDelete );
					}
				} ); // get
			}
		}; // deleteExpiredRecord
		
		var doEngineMaint = function() {
			// allow engine to run maint as well
			self.engine.runMaintenance( function() {
				stats.elapsed_sec = Tools.shortFloat( Tools.timeNow() - stats.time_start );
				self.logDebug(3, "Daily maintenance complete");
				self.logTransaction('maint', cleanup_list_path, stats);
				if (callback) callback();
			} );
		}; // finish
		
		this.listEach( cleanup_list_path, 
			function(item, item_idx, callback) {
				// delete item if still expired
				var key = item.key;
				
				// see if expiration date is still overdue
				if (self.expHash) {
					self.hashGet( cleanup_hash_path, key, function(err, data) {
						if (data && data.expires) {
							var eargs = Tools.getDateArgs( data.expires );
							if ((eargs.epoch <= dargs.epoch) || (eargs.yyyy_mm_dd == dargs.yyyy_mm_dd)) {
								// still expired, kill it
								deleteExpiredRecord(key, callback);
							}
							else {
								// oops, expiration changed, skip
								stats.num_skipped++;
								self.logDebug(9, "Expiration on record " + key + " has changed to " + eargs.yyyy_mm_dd + ", skipping delete");
								callback();
							}
						}
						else {
							// no expiration date, just delete it
							deleteExpiredRecord(key, callback);
						}
					} ); // hashGet
				} // expHash
				else {
					deleteExpiredRecord(key, callback);
				}
			},
			function(err) {
				// list iteration complete
				if (err) {
					self.logDebug(10, "Failed to load list, skipping maintenance (probably harmless)", cleanup_list_path);
					doEngineMaint();
				}
				else {
					// no error, delete list
					self.listDelete( cleanup_list_path, true, function(err) {
						if (err) {
							self.logError('maint', "Failed to delete cleanup list: " + cleanup_list_path + ": " + err);
						}
						doEngineMaint();
					} ); // listDelete
				} // succes
			} // list complete
		); // listEach
	},
	
	lock: function(key, wait, callback) {
		// lock key in exclusive mode, possibly wait until acquired
		if (!this.started) return callback( new Error("Storage has not completed startup.") );
		
		if (key.match(/^(\w*\|+)(.+)$/)) key = RegExp.$1 + this.normalizeKey(RegExp.$2);
		else key = this.normalizeKey(key);
		
		this.logDebug(9, "Requesting lock: " + key);
		
		if (this.locks[key]) {
			var lock = this.locks[key];
			if (wait) {
				lock.clients.push(callback);
				this.logDebug(9, "Key is already locked: " + key + ", waiting for unlock (" + lock.clients.length + " clients waiting)");
			}
			else {
				this.logDebug(9, "Key is already locked: " + key);
				callback( new Error("Key is locked"), lock );
			}
		}
		else {
			this.logDebug(9, "Locked key: " + key);
			var lock = { type: 'ex', clients: [] };
			this.locks[key] = lock;
			callback(null, lock);
		}
	},
	
	unlock: function(key) {
		// release lock on key
		if (!this.started) throw new Error("Storage has not completed startup.");
		
		if (key.match(/^(\w*\|+)(.+)$/)) key = RegExp.$1 + this.normalizeKey(RegExp.$2);
		else key = this.normalizeKey(key);
		
		if (this.locks[key]) {
			var lock = this.locks[key];
			if (lock.type != 'ex') {
				this.logError('lock', "Lock is incorrect type (expected exclusive): " + key);
				return;
			}
			
			this.logDebug(9, "Unlocking key: " + key + " (" + lock.clients.length + " clients waiting)");
			var callback = lock.clients.shift();
			if (callback) {
				this.logDebug(9, "Locking key: " + key);
				callback(null, lock);
			}
			else delete this.locks[key];
		}
	},
	
	shareLock: function(key, wait, callback) {
		// lock key in shared (read-only) mode, possibly wait until acquired
		var self = this;
		if (!this.started) return callback( new Error("Storage has not completed startup.") );
		
		if (key.match(/^(\w*\|+)(.+)$/)) key = RegExp.$1 + this.normalizeKey(RegExp.$2);
		else key = this.normalizeKey(key);
		
		this.logDebug(9, "Requesting shared lock: " + key);
		
		if (this.locks[key]) {
			var lock = this.locks[key];
			if ((lock.type == 'sh') && !lock.clients.length) {
				// lock is already shared and no exclusive clients are waiting, so join the party
				lock.readers++;
				this.logDebug(9, "Joined shared lock: " + key, { readers: lock.readers });
				callback(null, lock);
			}
			else {
				// exclusive lock (or shared lock with exclusive clients waiting), so we must wait
				if (!wait) return callback( new Error("Key is locked"), lock );
				
				var func = function(err, lock) {
					if (err) return callback(err);
					
					// acquired lock, convert to shared
					if (lock.type == 'ex') {
						self.logDebug(9, "Locked key in shared mode: " + key);
						lock.type = 'sh';
						lock.readers = 1;
						callback(null, lock);
						
						// look for more pending shared readers
						while (lock.clients[0] && lock.clients[0].__pixl_share_client) {
							var client = lock.clients.shift();
							lock.readers++;
							self.logDebug(9, "Joined shared lock: " + key, { readers: lock.readers });
							client(null, lock);
						}
					}
					else {
						// lock already shared, and we've been joined to it
						callback(null, lock);
					}
				}; // got lock
				
				// add special flag so we know client wants to be shared
				func.__pixl_share_client = 1;
				
				// wait for exclusive lock (which we will convert to shared)
				this.lock(key, true, func);
			}
		}
		else {
			this.logDebug(9, "Locked key in shared mode: " + key);
			var lock = { type: 'sh', clients: [], readers: 1 };
			this.locks[key] = lock;
			callback(null, lock);
		}
	},
	
	shareUnlock: function(key) {
		// release lock on shared key
		if (!this.started) throw new Error("Storage has not completed startup.");
		
		if (key.match(/^(\w*\|+)(.+)$/)) key = RegExp.$1 + this.normalizeKey(RegExp.$2);
		else key = this.normalizeKey(key);
		
		if (this.locks[key]) {
			var lock = this.locks[key];
			if (lock.type != 'sh') {
				this.logError('lock', "Lock is incorrect type (expected shared): " + key);
				return;
			}
			
			if (lock.readers > 0) {
				lock.readers--;
				this.logDebug(9, "Removing reader from shared lock: " + key, { readers: lock.readers });
				if (lock.readers > 0) return;
			}
			
			// all readers gone, so treat as exclusive and fully unlock key
			lock.type = 'ex';
			this.unlock(key);
		}
	},
	
	waitForQueueDrain: function(callback) {
		// wait for queue to finish all pending tasks
		if (this.queue.idle()) callback();
		else {
			this.logDebug(3, "Waiting for queue to finish " + this.queue.running() + " active and " + this.queue.length() + " pending tasks");
			this.queue.drain = callback;
		}
	},
	
	waitForAllLocks: function(callback) {
		// wait for all locks to release before proceeding
		var self = this;
		var num_locks = Tools.numKeys(this.locks);
		
		if (num_locks) {
			this.logDebug(3, "Waiting for " + num_locks + " locks to be released", Object.keys(this.locks));
			
			async.whilst(
				function () {
					return (Tools.numKeys(self.locks) > 0);
				},
				function (callback) {
					setTimeout( function() { callback(); }, 250 );
				},
				function() {
					// all locks released
					self.logDebug(9, "All locks released.");
					callback();
				}
			); // whilst
		}
		else callback();
	},
	
	logTransaction: function(type, key, data) {
		// proxy request to system logger with correct component
		if (this.maxRecentEvents) {
			if (!this.recentEvents[type]) this.recentEvents[type] = [];
			this.recentEvents[type].push({
				date: Tools.timeNow(),
				type: type,
				key: key,
				data: data
			});
			if (this.recentEvents[type].length > this.maxRecentEvents) {
				this.recentEvents[type].shift();
			}
		}
		
		if (this.logEventTypes[type] || this.logEventTypes['all']) {
			this.logger.set( 'component', this.__name );
			this.logger.transaction( type, key, data );
		}
	},
	
	tick: function() {
		// called every second by pixl-server
		
		// rotate and log second perf metrics
		var metrics = this.lastSecondMetrics = this.perf.getMinMaxMetrics();
		
		if (Tools.numKeys(metrics) && (this.logEventTypes.perf_sec || this.logEventTypes.all)) {
			this.logger.print({ 
				component: this.__name,
				category: 'perf', 
				code: 'second', 
				msg: "Last Second Performance Metrics", 
				data: metrics 
			});
			if (this.engine.cache) {
				this.logger.print({ 
					component: this.__name,
					category: 'cache', 
					code: 'second', 
					msg: "Last Second Cache Stats", 
					data: this.engine.cache.getStats()
				});
			}
		}
		
		// import perf into minutePerf
		this.minutePerf.import( this.perf );
		
		// and reset second perf
		this.perf.reset();
	},
	
	tickMinute: function() {
		// called every minute by pixl-server
		
		// rotate and log minute perf metrics
		var metrics = this.lastMinuteMetrics = this.minutePerf.getMinMaxMetrics();
		
		if (Tools.numKeys(metrics) && (this.logEventTypes.perf_min || this.logEventTypes.all)) {
			this.logger.print({ 
				component: this.__name,
				category: 'perf', 
				code: 'minute', 
				msg: "Last Minute Performance Metrics", 
				data: metrics 
			});
			if (this.engine.cache) {
				this.logger.print({ 
					component: this.__name,
					category: 'cache', 
					code: 'minute', 
					msg: "Last Minute Cache Stats", 
					data: this.engine.cache.getStats()
				});
			}
		}
		
		// and reset minute perf
		this.minutePerf.reset();
	},
	
	getStats: function() {
		// get perf and other misc stats
		var stats = {
			version: this.version,
			engine: this.engine.__name,
			concurrency: this.concurrency,
			transactions: !!this.transactions,
			last_second: this.lastSecondMetrics,
			last_minute: this.lastMinuteMetrics,
			recent_events: this.recentEvents,
			queue: {
				active: this.queue.running(),
				pending: this.queue.length()
			},
			locks: {}
		};
		
		// locks have actual callback functions, so convert to JSON-friendly
		for (var key in this.locks) {
			var lock = this.locks[key];
			if (lock.type == 'ex') {
				stats.locks[key] = { type: 'exclusive', clients: lock.clients.length + 1 };
			}
			else if (lock.type == 'sh') {
				stats.locks[key] = { type: 'shared', readers: lock.readers };
			}
		}
		
		return stats;
	},
	
	shutdown: function(callback) {
		// shutdown storage
		var self = this;
		this.logDebug(2, "Shutting down storage system");
		
		this.waitForQueueDrain( function() {
			// queue drained, now wait for locks
			
			self.waitForAllLocks( function() {
				// all locks released, now shutdown engine
				
				if (self.engine) self.engine.shutdown(callback);
				else callback();
				
			} ); // waitForLocks
		} ); // waitForQueueDrain
	}
	
});
```

## File: `transaction.js`
```javascript
// PixlServer Storage System - Transaction Mixin
// Copyright (c) 2016 - 2017 Joseph Huckaby
// Released under the MIT License

var fs = require("fs");
var util = require("util");
var Path = require("path");
var cp = require("child_process");
var os = require("os");
var async = require('async');
var Class = require("pixl-class");
var Tools = require("pixl-tools");
var mkdirp = Tools.mkdirp;

// Transaction support is implemented as a mixin to Storage
// Config Keys:
//		transactions: true or false
//		trans_dir: temp dir, only used if non-local fs, defaults to ./transactions
//		trans_auto_recover: auto recover from crashes / fatal errors

// Subclass Storage so we can hoist get(), put(), head() and delete() for use inside transactions

var TransStorageFunctions = {
	
	__construct: function() {
		// class constructor
		this.tempFileCounter = 1;
	},
	
	put: function(key, value, callback) {
		// store key+value pair in transaction
		var self = this;
		key = this.normalizeKey( key );
		
		// get current transaction
		var trans = this.transactions[ this.currentTransactionPath ];
		if (!trans) return callback( new Error("The transaction has completed.  This instance can no longer be used.") );
		if (trans.aborting) return callback( new Error("The transaction is being aborted.  This instance can no longer be used.") );
		
		// binary keys not part of transaction system
		if (this.isBinaryKey(key)) return this.rawStorage.put(key, value, callback);
		if (!value) return callback( new Error("Value cannot be false.") );
		if (Buffer.isBuffer(value)) return callback( new Error("Buffers not allowed in transactions.") );
		
		this.logDebug(9, "Storing JSON Object in transaction: " + key, this.debugLevel(10) ? value : null);
		value = JSON.stringify( value );
		
		// flag key as written
		trans.keys[key] = 'W';
		
		// store in memory during transaction
		trans.values[key] = {
			mod: Tools.timeNow(true),
			len: Buffer.byteLength(value, 'utf8'),
			data: JSON.parse( value )
		};
		
		setImmediate( function() {
			self.logDebug(9, "Store operation complete (in transaction): " + key);
			callback( null, null );
		} );
	},
	
	head: function(key, callback) {
		// fetch metadata given key: { mod, len }
		var self = this;
		key = this.normalizeKey( key );
		
		// get current transaction
		var trans = this.transactions[ this.currentTransactionPath ];
		if (!trans) return callback( new Error("The transaction has completed.  This instance can no longer be used.") );
		if (trans.aborting) return callback( new Error("The transaction is being aborted.  This instance can no longer be used.") );
		
		// binary keys not part of transaction system
		if (this.isBinaryKey(key)) return this.rawStorage.head(key, callback);
		
		// if we haven't written key yet, use raw storage
		if (!(key in trans.keys)) return this.rawStorage.head(key, callback);
		
		if (trans.keys[key] == 'W') {
			// we've written the key, so fetch our version
			this.logDebug(9, "Pinging Object from transaction: " + key);
			
			setImmediate( function() {
				self.logDebug(9, "Head complete: " + key);
				var value = trans.values[key];
				callback( null, {
					mod: value.mod,
					len: value.len
				} );
			} );
		}
		else if (trans.keys[key] == 'D') {
			// simulate a deleted record
			// do this in next tick just to be safe (allow I/O to run)
			var err = new Error("Failed to head key: " + key + ": File not found");
			err.code = "NoSuchKey";
			
			setImmediate( function() {
				callback( err, null );
			} );
		}
	},
	
	get: function(key, callback) {
		// fetch value given key
		var self = this;
		key = this.normalizeKey( key );
		
		// get current transaction
		var trans = this.transactions[ this.currentTransactionPath ];
		if (!trans) return callback( new Error("The transaction has completed.  This instance can no longer be used.") );
		if (trans.aborting) return callback( new Error("The transaction is being aborted.  This instance can no longer be used.") );
		
		// binary keys not part of transaction system
		if (this.isBinaryKey(key)) return this.rawStorage.get(key, callback);
		
		// if we haven't written key yet, use raw storage
		if (!(key in trans.keys)) return this.rawStorage.get(key, callback);
		
		if (trans.keys[key] == 'W') {
			// we've written the key, so fetch our version
			this.logDebug(9, "Fetching Object in transaction: " + key);
			
			setImmediate( function() {
				var data = trans.values[key].data;
				self.logDebug(9, "JSON fetch complete: " + key, self.debugLevel(10) ? data : null);
				callback( err, Tools.copyHash(data, true) );
			} );
		}
		else if (trans.keys[key] == 'D') {
			// simulate fetching a deleted record
			// do this in next tick just to be safe (allow I/O to run)
			var err = new Error("Failed to fetch key: " + key + ": File not found");
			err.code = "NoSuchKey";
			
			setImmediate( function() {
				callback( err, null );
			} );
		}
	},
	
	delete: function(key, callback) {
		// delete record given key
		var self = this;
		key = this.normalizeKey( key );
		
		// get current transaction
		var trans = this.transactions[ this.currentTransactionPath ];
		if (!trans) return callback( new Error("The transaction has completed.  This instance can no longer be used.") );
		if (trans.aborting) return callback( new Error("The transaction is being aborted.  This instance can no longer be used.") );
		
		// binary keys not part of transaction system
		if (this.isBinaryKey(key)) return this.rawStorage.delete(key, callback);
		
		// if we haven't touched the key yet, then we need to simulate this using head()
		if (!(key in trans.keys)) {
			this.rawStorage.head(key, function(err, info) {
				if (err) return callback(err);
				
				// flag key as deleted
				trans.keys[key] = 'D';
				
				self.logDebug(9, "Deleting Object from transaction: " + key);
				
				if (callback) callback();
			});
			return;
		}
		
		this.logDebug(9, "Deleting Object from transaction: " + key);
		
		// flag key as deleted
		trans.keys[key] = 'D';
		delete trans.values[key];
		
		setImmediate( function() {
			self.logDebug(9, "Delete complete: " + key);
			if (callback) callback(null, null);
		} );
	},
	
	enqueue: function(task) {
		// enqueue task for execution AFTER commit
		var trans = this.transactions[ this.currentTransactionPath ];
		if (!trans) throw new Error("The transaction has completed.  This instance can no longer be used.");
		if (trans.aborting) return callback( new Error("The transaction is being aborted.  This instance can no longer be used.") );
		
		trans.queue.push( task );
	},
	
	abort: function(callback) {
		// abort current transaction
		var trans = this.transactions[ this.currentTransactionPath ];
		if (!trans) throw new Error("The transaction has completed.  This instance can no longer be used.");
		if (trans.aborting) return callback( new Error("The transaction is being aborted.  This instance can no longer be used.") );
		
		this.rawStorage.abortTransaction( this.currentTransactionPath, callback );
	},
	
	commit: function(callback) {
		// commit current transaction
		var trans = this.transactions[ this.currentTransactionPath ];
		if (!trans) throw new Error("The transaction has completed.  This instance can no longer be used.");
		if (trans.aborting) return callback( new Error("The transaction is being aborted.  This instance can no longer be used.") );
		
		this.rawStorage.commitTransaction( this.currentTransactionPath, callback );
	}
	
};

//
// Transaction Storage Mixin
//

module.exports = Class.create({
	
	transactions: null,
	
	transEarlyStart: function() {
		// early check for unclean shutdown
		var pid_file = this.server.config.get('pid_file');
		if (!pid_file) return true; // need pid file to check
		
		try { fs.statSync( pid_file ); }
		catch (e) { return true; } // no pid file, clean startup
		
		// if 'trans_auto_recover' is set, return normally
		if (this.config.get('trans_auto_recover')) return true;
		
		// if we got here then we found a PID file -- force recovery mode
		if (this.server.config.get('recover')) {
			// user added '--recovery' CLI param, good
			// force debug mode (no daemon fork) and allow startup to continue
			this.server.debug = true;
			this.server.echo = true;
			this.server.logger.set('echo', true);
			this.logDebug(1, "Entering database recovery mode");
			return true;
		}
		else {
			var msg = '';
			msg += "\n";
			msg += this.server.__name + " was shut down uncleanly and needs to run database recovery operations.\n";
			msg += "Please start it in recovery mode by issuing this command:\n\n";
			msg += "\t" + process.argv.join(' ') + " --recover\n";
			msg += "\n";
			process.stdout.write(msg);
			process.exit(1);
		}
	},
	
	initTransactions: function(callback) {
		// initialize transaction system, look for recovery files
		var self = this;
		if (!this.config.get('transactions')) return callback();
		
		// keep in-memory hash of active transactions
		this.transactions = {};
		
		// transaction IDs are sequence numbers starting from 1
		this.nextTransID = 1;
		
		// create temp trans dirs
		this.transDir = 'transactions';
		if (this.config.get('trans_dir')) this.transDir = this.config.get('trans_dir');
		else if (this.engine.baseDir) this.transDir = Path.join( this.engine.baseDir, "_transactions" );
		
		try {
			mkdirp.sync( Path.join(this.transDir, "logs") );
			mkdirp.sync( Path.join(this.transDir, "data") );
		}
		catch (err) {
			var msg = "FATAL ERROR: Transaction directory could not be created: " + this.transDir + "/*: " + err;
			this.logError('startup', msg);
			return callback( new Error(msg) );
		}
		
		// construct special subclass for cloning storage
		this.TransStorage = Class.create( Tools.mergeHashes( TransStorageFunctions, {
			__name: 'Storage',
			__parent: require("./storage.js")
		}) );
		
		// hoist compound functions to use transaction wrappers
		this.transHoistCompounds();
		
		// look for recovery logs
		var log_dir = Path.join(this.transDir, "logs");
		
		fs.readdir(log_dir, function(err, files) {
			if (err) return callback(err);
			
			// if no files found, then good, no recovery necessary, return ASAP
			if (!files || !files.length) {
				if (self.server.config.get('recover')) {
					self.logDebug(1, "Database recovery is complete (no recovery actions were required).");
					// self.logDebug(1, "Resuming normal startup");
					
					// we got here from '--recover' mode, so print message and exit now
					var msg = '';
					msg += "\n";
					msg += "Database recovery is complete.  No actions were required.\n";
					msg += self.server.__name + " can now be started normally.\n";
					msg += "\n";
					process.stdout.write(msg);
					
					var pid_file = self.server.config.get('pid_file');
					if (pid_file) try { fs.unlinkSync( pid_file ); } catch(e) {;}
					
					process.exit(0);
				}
				return callback();
			}
			
			// take over logging for this part
			var orig_log_path = self.logger.path;
			var recovery_log_path = Path.join( Path.dirname(orig_log_path), 'recovery.log' );
			var recovery_trans_count = 0;
			
			self.logDebug(1, "Beginning database recovery, see " + recovery_log_path + " for details");
			self.logger.path = recovery_log_path;
			self.logDebug(1, "Beginning database recovery");
			
			// sort logs by their IDs descending, so we roll back transactions in reverse order
			files.sort( function(a, b) {
				return parseInt(b) - parseInt(a);
			});
			
			// damn, unclean shutdown, iterate over recovery logs
			async.eachSeries( files,
				function(filename, callback) {
					var file = Path.join( log_dir, filename );
					self.logDebug(3, "Processing recovery log: " + file);
					
					fs.open(file, "r", function(err, fh) {
						if (err) {
							self.logError('rollback', "Failed to open recovery log: " + file + ": " + err.message);
							fs.unlink(file, function() { callback(); });
							return;
						}
						
						// read just enough to ensure we get the header
						var chunk = Buffer.alloc(8192);
						fs.read(fh, chunk, 0, 8192, null, function(err, num_bytes, chunk) {
							fs.close(fh, function() {});
							
							if (err) {
								self.logError('rollback', "Failed to read recovery log: " + file + ": " + err.message);
								fs.unlink(file, function() { callback(); });
								return;
							}
							if (!num_bytes) {
								self.logError('rollback', "Failed to read recovery log: " + file + ": 0 bytes read");
								fs.unlink(file, function() { callback(); });
								return;
							}
							
							var data = chunk.slice(0, num_bytes).toString().split("\n", 2)[0];
							
							// parse header (JSON)
							var trans = null;
							try { trans = JSON.parse( data ); }
							catch (err) {
								self.logError('rollback', "Failed to read recovery header: " + file + ": " + err.message);
								fs.unlink(file, function() { callback(); });
								return;
							}
							if (!trans.id || !trans.path || !trans.log || !trans.date || !trans.pid) {
								self.logError('rollback', "Failed to read recovery header: " + file + ": Malformed data");
								fs.unlink(file, function() { callback(); });
								return;
							}
							
							self.logDebug(1, "Rolling back partial transaction: " + trans.path, trans);
							
							// restore transaction info
							self.transactions[ trans.path ] = trans;
							
							// abort (rollback) transaction
							recovery_trans_count++;
							self.abortTransaction( trans.path, callback );
							
						}); // fs.read
					}); // fs.open
				}, // foreach file
				function(err) {
					// all logs complete
					// delete ALL temp data files (these are not used for recovery)
					var data_dir = Path.join(self.transDir, "data");
					
					fs.readdir(data_dir, function(err, files) {
						if (err) return callback(err);
						if (!files) files = [];
						
						async.eachLimit( files, self.concurrency,
							function(filename, callback) {
								var file = Path.join( data_dir, filename );
								fs.unlink( file, function() { callback(); } ); // ignoring error
							},
							function() {
								// recovery complete
								self.logDebug(1, "Database recovery is complete. " + recovery_trans_count + " transactions rolled back.");
								
								// restore original log setup
								self.logger.path = orig_log_path;
								self.logDebug(1, "Database recovery is complete, see " + recovery_log_path + " for details.");
								
								// save info in case app wants to sniff this on startup and notify user
								self.recovery_log = recovery_log_path;
								self.recovery_count = recovery_trans_count;
								
								if (self.server.config.get('recover')) {
									// we got here from '--recover' mode, so print message and exit now
									var msg = '';
									msg += "\n";
									msg += "Database recovery is complete.  Please see " + recovery_log_path + " for full details.\n";
									msg += self.server.__name + " can now be started normally.\n";
									msg += "\n";
									process.stdout.write(msg);
									
									var pid_file = self.server.config.get('pid_file');
									if (pid_file) try { fs.unlinkSync( pid_file ); } catch(e) {;}
									
									process.exit(0);
								}
								else {
									// continue startup
									callback();
								}
							}
						); // eachSeries (data)
					}); // readdir (data)
				} // all logs complete
			); // eachSeries (logs)
		}); // readdir (logs)
	},
	
	transHoistCompounds: function() {
		// hoist all compound storage API calls to use transaction wrappers
		// 1st arg MUST be key, last arg MUST be callback, errs are FATAL (trigger rollback)
		var self = this;
		var api_list = [
			'listCreate', 
			'listPush', 
			'listUnshift', 
			'listPop', 
			'listShift', 
			'listSplice', 
			'listDelete', 
			'listCopy', 
			'listRename', 
			'listEachUpdate',
			'listEachPageUpdate',
			'hashCreate', 
			'hashPut', 
			'hashPutMulti',
			'hashUpdate',
			'hashUpdateMulti', 
			'hashCopy', 
			'hashRename', 
			'hashDeleteMulti', 
			'hashDeleteAll', 
			'hashDelete' 
		];
		
		api_list.forEach( function(name) {
			// replace function with transaction-aware wrapper
			self[name] = function() {
				var self = this;
				var args = Array.prototype.slice.call(arguments);
				
				// if transaction already in progress, tag along
				if (self.currentTransactionPath) {
					return self.TransStorage.prototype[name].apply(self, args);
				}
				
				// 1st arg MUST be key, last arg MUST be callback
				var path = args[0];
				var origCallback = args.pop();
				
				// here we go
				self.beginTransaction(path, function(err, clone) {
					// transaction has begun, now insert our own callback to commit it
					
					var finish = function() {
						var args = Array.prototype.slice.call(arguments);
						var err = args[0];
						if (err) {
							// compound function generated an error
							// emergency abort, rollback
							self.abortTransaction(path, function() {
								// call original callback with error that triggered rollback
								origCallback( err );
							}); // abort
						}
						else {
							// no error, commit transaction
							self.commitTransaction(path, function(err) {
								if (err) {
									// commit failed, trigger automatic rollback
									self.abortTransaction(path, function() {
										// call original callback with commit error
										origCallback( err );
									}); // abort
								} // commit error
								else {
									// success!  call original callback with full args
									origCallback.apply( null, args );
								}
							}); // commit
						} // no error
					}; // finish
					
					// call original function on CLONE (transaction-aware version)
					args.push( finish );
					clone[name].apply(clone, args);
				}); // beginTransaction
			}; // hoisted func
		}); // forEach
	},
	
	begin: function(path, callback) {
		// shortcut for beginTransaction
		this.beginTransaction(path, callback);
	},
	
	beginTransaction: function(path, callback) {
		// begin a new transaction, starting at 'path' and encapsulating everything under it
		var self = this;
		if (!this.started) return callback( new Error("Storage has not completed startup.") );
		if (!this.transactions) return callback(null, this);
		if (this.currentTransactionPath) return callback(null, this);
		
		this._transLock(path, true, function() {
			// got lock for transaction
			var id = '' + Math.floor(self.nextTransID++);
			var log_file = Path.join( self.transDir, "logs", process.pid + '-' + id + '.log' );
			var trans = { id: id, path: path, log: log_file, date: Tools.timeNow(), pid: process.pid };
			
			self.logDebug(5, "Beginning new transaction on: " + path, trans);
			
			// transaction is ready to begin
			trans.keys = {};
			trans.values = {};
			trans.queue = [];
			self.transactions[path] = trans;
			
			// clone self with currentTransactionPath set
			var clone = new self.TransStorage();
			
			['config', 'server', 'logger', 'cache', 'cacheKeyRegEx', 'listItemsPerPage', 'hashItemsPerPage', 'concurrency', 'cacheKeyRegex', 'engine', 'queue', 'transactions', 'transDir', 'started', 'perf', 'logEventTypes' ].forEach( function(key) {
				clone[key] = self[key];
			});
			
			clone.currentTransactionPath = trans.path;
			clone.rawStorage = self;
			clone.locks = {};
			
			callback(null, clone);
		}); // lock
	},
	
	abortTransaction: function(path, callback) {
		// abort transaction in progress, rollback any actions taken
		var self = this;
		if (!this.transactions) return callback();
		if (this.currentTransactionPath) return callback();
		
		var trans = this.transactions[path];
		if (!trans) return callback( new Error("Unable to find transaction matching path: " + path) );
		
		if (trans.aborting) return callback( new Error("Transaction is already being aborted: " + path) );
		trans.aborting = true;
		
		var num_actions = Tools.numKeys(trans.keys || {});
		this.logError('rollback', "Aborting transaction: " + trans.id, { path: path, actions: num_actions });
		
		// read in file line by line
		// (file may not exist, which is fine, hence 'ignore_not_found')
		Tools.fileEachLine( trans.log, { ignore_not_found: true },
			function(line, callback) {
				var json = null;
				try { json = JSON.parse(line); }
				catch (err) {
					// non-fatal, file may have been partially written
					self.logError('rollback', "Failed to parse JSON in recovery log: " + err, line);
					return callback();
				}
				if (json) {
					if (json.key) {
						// restore or delete record
						if (json.value) {
							self.put( json.key, json.value, function(err) {
								if (err) {
									var msg = "Could not rollback transaction: " + path + ": Failed to restore record: " + json.key + ": " + err.message;
									self.logError('rollback', msg);
									return callback( new Error(msg) ); // this is fatal
								}
								callback();
							} );
						}
						else {
							self.delete( json.key, function(err) {
								if (err && (err.code != "NoSuchKey")) {
									var msg = "Could not rollback transaction: " + path + ": Failed to delete record: " + json.key + ": " + err.message;
									self.logError('rollback', msg);
									return callback( new Error(msg) ); // this is fatal
								}
								callback(); // record already deleted, non-fatal
							} );
						}
					}
					else if (json.id) {
						// must be the file header
						self.logDebug(3, "Transaction rollback metadata", json);
						return callback();
					}
					else {
						// non-fatal, file may have been partially written
						self.logError('rollback', "Unknown JSON record type", json);
						return callback();
					}
				}
			},
			function(err) {
				// check for fatal error
				if (err) {
					// rollback errors are fatal, as the DB cannot continue in a partial state
					self.transFatalError(err);
					return;
				}
				
				// delete transaction log
				self.logDebug(9, "Deleting transaction log: " + trans.log);
				
				fs.unlink( trans.log, function(err) {
					if (err && !err.message.match(/ENOENT/)) {
						self.logError('rollback', "Unable to delete rollback log: " + trans.log + ": " + err);
					}
					
					// complete, unlock and remove transaction from memory
					self.transactions[path].keys = {}; // release memory
					self.transactions[path].values = {}; // release memory
					self.transactions[path].queue = []; // release memory
					delete self.transactions[path];
					
					self.logDebug(3, "Transaction rollback complete: " + trans.id, { path: path });
					
					// unlock at the VERY end, as a new transaction may be waiting on the same path
					self.emit('commitEnd', trans, "rollback");
					self.unlock( 'C|'+path );
					self._transUnlock(path);
					
					callback();
				}); // fs.unlink
			} // done with log
		); // fileEachLine
	},
	
	commitTransaction: function(path, callback) {
		// commit transaction to storage
		var self = this;
		if (!this.transactions) return callback();
		if (this.currentTransactionPath) return callback();
		
		var trans = this.transactions[path];
		if (!trans) return callback( new Error("Unable to find transaction matching path: " + path) );
		
		if (trans.committing) return callback( new Error("Transaction is already being committed: " + path) );
		trans.committing = true;
		
		if (trans.aborting) return callback( new Error("Transaction has already been aborted: " + path) );
		
		var num_actions = Tools.numKeys(trans.keys);
		this.logDebug(5, "Committing transaction: " + trans.id, { path: path, actions: num_actions });
		
		if (!num_actions) {
			// transaction is complete
			this.logDebug(5, "Transaction has no actions, committing instantly");
			
			// transaction is complete
			trans.keys = {}; // release memory
			trans.values = {}; // release memory
			delete this.transactions[path];
			
			this._transUnlock(path);
			if (callback) callback();
			
			// enqueue any pending tasks that got added during the transaction
			if (trans.queue.length) {
				trans.queue.forEach( this.enqueue.bind(this) );
				trans.queue = []; // release memory
			}
			
			return;
		}
		
		// start commit and track perf
		var num_bytes = 0;
		var pf = this.perf.begin('commit');
		
		async.waterfall(
			[
				function(callback) {
					// acquire commit lock
					self.lock( 'C|'+path, true, function() { callback(); } );
				},
				function(callback) { 
					// open transaction log (exclusive append mode)
					fs.open( trans.log, "ax", callback ); 
				},
				function(fh, callback) {
					// store file handle, write file header
					trans.fh = fh;
					var header = Tools.copyHashRemoveKeys(trans, { keys: 1, values: 1, queue: 1, fh: 1, committing: 1 });
					fs.write( fh, JSON.stringify(header) + "\n", callback );
				},
				function(num_bytes, buf, callback) {
					// fetch all affected keys and append records to rollback log
					async.forEachOfLimit( trans.keys, self.concurrency, 
						function(record_state, key, callback) {
							self.get( key, function(err, value) {
								if (err && (err.code != "NoSuchKey")) return callback(err);
								fs.write( trans.fh, JSON.stringify({ key: key, value: value || 0 }) + "\n", callback );
							});
						},
						callback
					); // forEachOfLimit
				},
				function(callback) {
					// flush log contents to disk
					fs.fsync( trans.fh, function(err) {
						if (err) return callback(err);
						
						fs.close( trans.fh, callback );
						delete trans.fh;
					} );
				},
				function(callback) {
					// notify listeners that the commit is starting, and the rollback log is available
					self.emit('commitStart', trans);
					
					// We must fsync the directory as well, as per: http://man7.org/linux/man-pages/man2/fsync.2.html
					// Note: Yes, read-only is the only way: https://www.reddit.com/r/node/comments/4r8k11/how_to_call_fsync_on_a_directory/
					fs.open( Path.dirname(trans.log), "r", function(err, dh) {
						if (err) return callback(); // this may fail on certain OSes, so treat as non-fatal
						
						fs.fsync(dh, function(err) {
							// ignoring error here, as some filesystems may not allow this
							fs.close(dh, callback);
						});
					} );
				},
				function(callback) {
					// we now have a complete, 100% synced rollback log
					// now commit actual changes to storage -- as fast as possible
					async.forEachOfLimit( trans.keys, self.concurrency, 
						function(record_state, key, callback) {
							if (record_state == 'W') {
								// overwrite record with our transaction's state
								var value = trans.values[key];
								num_bytes += value.len;
								self.put( key, value.data, callback );
							}
							else if (record_state == 'D') {
								self.delete(key, function(err) {
									if (err) {
										if (err.code == "NoSuchKey") {
											// no problem - someone may have deleted the record, or it was already deleted to begin with
											self.logDebug(5, "Record already deleted: " + key);
										}
										else {
											// this should not happen
											return callback(err);
										}
									} // err
									callback();
								});
							} // state 'D'
						},
						callback
					); // forEachOfLimit
				}
			],
			function(err) {
				// commit complete
				var elapsed = pf.end();
				
				if (err) {
					// Note: in this case unlocking happens in abortTransaction
					var msg = "Failed to commit transaction: " + path + ": " + err.message;
					self.logError('commit', msg, { id: trans.id });
					return callback( new Error(msg) );
				}
				
				self.logDebug(5, "Transaction committed successfully: " + trans.id, { path: path, actions: num_actions });
				self.logTransaction('commit', path, {
					id: trans.id,
					elapsed_ms: elapsed,
					actions: num_actions,
					bytes_written: num_bytes
				});
				
				// transaction is complete
				delete trans.values; // release memory
				delete self.transactions[path];
				
				// enqueue any pending tasks that got added during the transaction
				if (trans.queue.length) {
					trans.queue.forEach( self.enqueue.bind(self) );
					trans.queue = []; // release memory
				}
				
				// engine may need to sync data records separately (i.e. fsync)
				// do this after releasing transaction lock, but hold log delete until after
				if (self.engine.sync) {
					self.enqueue( function(task, callback) {
						self.transPostSync( trans, callback );
					} );
				}
				else {
					// no sync needed for engine, just delete rollback log
					self.logDebug(9, "No sync needed, deleting transaction log: " + trans.log);
					fs.unlink( trans.log, function() {} );
					delete trans.keys; // release memory
				}
				
				self.emit('commitEnd', trans);
				self.unlock( 'C|'+path );
				self._transUnlock(path);
				callback();
			}
		); // waterfall
	},
	
	transPostSync: function(trans, callback) {
		// call sync after commit completes
		var self = this;
		var wrote_keys = Object.keys(trans.keys).filter( function(key) {
			return trans.keys[key] == 'W';
		});
		delete trans.keys; // release memory
		
		async.eachLimit( wrote_keys, self.concurrency,
			function(key, callback) {
				self.engine.sync( key, function() {
					// ignore error here, as key may be deleted
					callback();
				});
			},
			function(err) {
				// finally we can safely delete the transaction log
				self.logDebug(9, "All " + wrote_keys.length + " syncs complete, deleting transaction log: " + trans.log);
				fs.unlink( trans.log, callback );
			}
		); // forEachOfLimit
	},
	
	transFatalError: function(err) {
		// fatal error: scream loudly and shut down immediately
		var self = this;
		this.server.logger.set('sync', true);
		
		this.logError('fatal', "Fatal transaction error: " + err.message);
		
		// log to crash.log as well (in typical log configurations)
		this.server.logger.set( 'component', 'crash' );
		this.server.logger.debug( 1, "Emergency shutdown: " + err.message );
		
		// stop all future storage actions
		this.started = false;
		
		// allow application to hook fatal event and handle shutdown
		if (this.listenerCount('fatal')) {
			this.emit('fatal', err);
		}
		else {
			// just exit immediately
			self.logDebug(1, "Exiting");
			process.exit(1);
		}
	},
	
	_transLock: function(key, wait, callback) {
		// internal transaction lock wrapper
		// uses unique key prefix so won't deadlock with user locks
		this.lock( 'T|'+key, wait, callback );
	},
	
	_transUnlock: function(key) {
		// internal transaction unlock wrapper
		this.unlock( 'T|'+key );
	}
	
});
```

## File: `docs/API.md`
```markdown
# API Reference

Here are all the public methods you can call in the storage class.  These examples all assume you have your preloaded `Storage` component instance in a local variable named `storage`.  The component instance can be retrieved from a running server like this:

```js
let storage = server.Storage;
```

## Table of Contents

> &larr; [Return to the main document](https://github.com/jhuckaby/pixl-server-storage/blob/master/README.md)

<!-- toc -->
- [General Methods](#general-methods)
	* [put](#put)
	* [putMulti](#putmulti)
	* [putStream](#putstream)
	* [get](#get)
	* [getMulti](#getmulti)
	* [getBuffer](#getbuffer)
	* [getStream](#getstream)
	* [getStreamRange](#getstreamrange)
	* [head](#head)
	* [headMulti](#headmulti)
	* [delete](#delete)
	* [deleteMulti](#deletemulti)
	* [copy](#copy)
	* [rename](#rename)
	* [lock](#lock)
	* [unlock](#unlock)
	* [shareLock](#sharelock)
	* [shareUnlock](#shareunlock)
	* [expire](#expire)
	* [addRecordType](#addrecordtype)
	* [getStats](#getstats)
- [List Methods](#list-methods)
	* [listCreate](#listcreate)
	* [listPush](#listpush)
	* [listUnshift](#listunshift)
	* [listPop](#listpop)
	* [listShift](#listshift)
	* [listGet](#listget)
	* [listSplice](#listsplice)
	* [listFind](#listfind)
	* [listFindCut](#listfindcut)
	* [listFindReplace](#listfindreplace)
	* [listFindUpdate](#listfindupdate)
	* [listFindEach](#listfindeach)
	* [listInsertSorted](#listinsertsorted)
	* [listCopy](#listcopy)
	* [listRename](#listrename)
	* [listEach](#listeach)
	* [listEachPage](#listeachpage)
	* [listEachUpdate](#listeachupdate)
	* [listEachPageUpdate](#listeachpageupdate)
	* [listGetInfo](#listgetinfo)
	* [listDelete](#listdelete)
- [Hash Methods](#hash-methods)
	* [hashCreate](#hashcreate)
	* [hashPut](#hashput)
	* [hashPutMulti](#hashputmulti)
	* [hashGet](#hashget)
	* [hashGetMulti](#hashgetmulti)
	* [hashUpdate](#hashupdate)
	* [hashUpdateMulti](#hashupdatemulti)
	* [hashEach](#hasheach)
	* [hashEachSync](#hasheachsync)
	* [hashEachPage](#hasheachpage)
	* [hashGetAll](#hashgetall)
	* [hashCopy](#hashcopy)
	* [hashRename](#hashrename)
	* [hashDelete](#hashdelete)
	* [hashDeleteMulti](#hashdeletemulti)
	* [hashDeleteAll](#hashdeleteall)
	* [hashGetInfo](#hashgetinfo)
- [Transaction Methods](#transaction-methods)
	* [begin](#begin)
	* [commit](#commit)
	* [abort](#abort)
- [Indexer Methods](#indexer-methods)
	* [indexRecord](#indexrecord)
	* [unindexRecord](#unindexrecord)
	* [searchRecords](#searchrecords)
	* [sortRecords](#sortrecords)
	* [getFieldSummary](#getfieldsummary)
	* [searchSingle](#searchsingle)

# General Methods

## put

```js
storage.put( KEY, VALUE, CALLBACK );
```

The `put()` method stores a key/value pair.  It will create the record if it doesn't exist, or replace it if it does.  All keys should be strings.  The value may be an object or a `Buffer` (for binary blobs).  Objects are auto-serialized to JSON.  Your callback function is passed an error if one occurred.  Example:

```js
storage.put( 'test1', { foo: 'bar1' }, function(err) {
	if (err) throw err;
} );
```

For binary values, the key *must* contain a file extension, e.g. `test1.gif`.  Example:

```js
const fs = require('fs');
let buffer = fs.readFileSync('picture.gif');

storage.put( 'test1.gif', buffer, function(err) {
	if (err) throw err;
} );
```

## putMulti

```js
storage.putMulti( RECORDS, CALLBACK );
```

The `putMulti()` method stores multiple keys/values at once, from a specified object containing both.  Depending on your storage [concurrency](../README.md#concurrency) configuration, this may be significantly faster than storing the records in sequence.  Example:

```js
let records = {
	multi1: { fruit: 'apple' },
	multi2: { fruit: 'orange' },
	multi3: { fruit: 'banana' }
};

storage.putMulti( records, function(err) {
	if (err) throw err;
} );
```

Note that if any of the individual put operations fail, the entire `putMulti()` function is aborted, and the first error is passed to your callback.  At this point the operation may have been partially successful, with some records written, and others not.  Due to this uncertainty, you may want to use this method inside of a [transaction](./Transactions.md), which can be safely rolled back upon error.

## putStream

```js
storage.putStream( KEY, STREAM, CALLBACK );
```

The `putStream()` method stores a record using a [readable stream](https://nodejs.org/api/stream.html#stream_class_stream_readable), so it doesn't have to be read into memory.  This can be used to spool very large files to storage without using any RAM.  Note that this is treated as a binary record, so the key *must* contain a file extension, e.g. `test1.gif`.  Example:

```js
const fs = require('fs');
let stream = fs.createReadStream('picture.gif');

storage.putStream( 'test1.gif', stream, function(err) {
	if (err) throw err;
} );
```

Please note that as of this writing, the `Couchbase`, `Redis` and `RedisCluster` engines have no native stream API, so the `putStream()` method has to load the entire record into memory.

## get

```js
storage.get( KEY, CALLBACK );
```

The `get()` method fetches a value given a key.  If the record is an object, it will be returned as such.  Or, if the record is a binary blob, a `Buffer` object will be returned.  Your callback function is passed an error if one occurred, and the data value for the given record.  Example:

```js
storage.get( 'test1', function(err, data) {
	if (err) throw err;
} );
```

## getMulti

```js
storage.getMulti( KEYS, CALLBACK );
```

The `getMulti()` method fetches multiple values at once, from a specified array of keys.  Depending on your storage [concurrency](../README.md#concurrency) configuration, this may be significantly faster than fetching the records in sequence.  Your callback function is passed an array of values which correspond to the specified keys.  Example:

```js
storage.getMulti( ['test1', 'test2', 'test3'], function(err, values) {
	if (err) throw err;
	// values[0] will be the test1 record.
	// values[1] will be the test2 record.
	// values[2] will be the test3 record.
} );
```

Note that if *any* of the records fail, the entire operation fails, and the first error is passed to your callback.

## getBuffer

```js
storage.getBuffer( KEY, CALLBACK );
```

The `getBuffer()` method retrieves a [Buffer](https://nodejs.org/api/buffer.html) to a given record's data, regardless if the key points to a JSON record or a binary record.  Your callback function is passed an error if one occurred, and the buffer value for the given record.  Example:

```js
storage.getBuffer( 'test1', function(err, buf) {
	if (err) throw err;
} );
```

## getStream

```js
storage.getStream( KEY, CALLBACK );
```

The `getStream()` method retrieves a [readable stream](https://nodejs.org/api/stream.html#readable-streams) to a given record's data, so it can be read or piped to a writable stream.  This is for very large records, so nothing is loaded into memory.  Example of spooling to a local file:

```js
const fs = require('fs');
let writeStream = fs.createWriteStream('/let/tmp/downloaded.gif');

storage.getStream( 'test1.gif', function(err, readStream, info) {
	if (err) throw err;
	
	writeStream.on('finish', function() {
		// data is completely written
	} );
	readStream.pipe( writeStream );
} );
```

As you can see above, your callback is also passed a 3rd argument, which is an object containing the record's full byte length and modification date.  These properties match those returned when you call [head()](#head) (i.e. `len` and `mod`).

Please note that as of this writing, the `Couchbase`, `Redis` and `RedisCluster` engines have no native stream API, so the `getStream()` method has to load the entire record into memory.

## getStreamRange

```js
storage.getStreamRange( KEY, START, END, CALLBACK );
```

The `getStreamRange()` method retrieves a [readable stream](https://nodejs.org/api/stream.html#class-streamreadable) to a specific slice of a record's data, so it can be read or piped to a writable stream.  The `start` and `end` arguments should be set to the starting and ending byte offset of the slice you want.  Both values are *inclusive*.  Example of spooling bytes `0-99` of a record to a local file:

```js
const fs = require('fs');
let writeStream = fs.createWriteStream('/let/tmp/downloaded.gif');

storage.getStreamRange( 'test1.gif', 0, 99, function(err, readStream, info) {
	if (err) throw err;
	
	writeStream.on('finish', function() {
		// data is completely written
	} );
	readStream.pipe( writeStream );
} );
```

As you can see in the example above, your callback is also passed a 3rd argument, which is an object containing the record's full byte length and modification date.  These properties match those returned when you call [head()](#head) (i.e. `len` and `mod`).  The `len` is not affected by the `start` and `end` range -- it is always the full byte length of the record.

The API supports two special range cases:

- If `start` is valid but `end` is `NaN`, it is assumed you want the entire record starting at `start` offset.
- If `start` is `NaN` but `end` is valid, it is assumed you want `end` bytes from the end of the record.

Please note that as of this writing, the `Couchbase`, `Redis` and `RedisCluster` engines have no native stream API, so the `getStreamRange()` method has to load the entire record into memory.

## head

```js
storage.head( KEY, CALLBACK );
```

The `head()` method fetches metadata about an object given a key, without fetching the object itself.  This generally means that the object size, and last modification date are retrieved, however this is engine specific.  Your callback function will be passed an error if one occurred, and an object containing at least two keys:

| Key | Description |
| --- | ----------- |
| `mod` | The last modification date of the object, in Epoch seconds. |
| `len` | The size of the object value in bytes. |

Example:

```js
storage.head( 'test1', function(err, data) {
	if (err) throw err;
	// data.mod
	// data.len
} );
```

Please note that as of this writing, the `Couchbase`, `Redis` and `RedisCluster` engines have no native head API, so the `head()` method has to load the entire record.  It does return the record size in to the `len` property, but the `mod` property will always be set to `1`.

## headMulti

```js
storage.headMulti( KEYS, CALLBACK );
```

The `headMulti()` method pings multiple records at once, from a specified array of keys.  Depending on your storage [concurrency](../README.md#concurrency) configuration, this may be significantly faster than pinging the records in sequence.  Your callback function is passed an array of values which correspond to the specified keys.  Example:

```js
storage.headMulti( ['test1', 'test2', 'test3'], function(err, values) {
	if (err) throw err;
	// values[0] will be the test1 head info.
	// values[1] will be the test2 head info.
	// values[2] will be the test3 head info.
} );
```

## delete

```js
storage.delete( KEY, CALLBACK );
```

The `delete()` method deletes an object given a key.  Your callback function is passed an error if one occurred, otherwise it'll be falsey.  Example:

```js
storage.delete( 'test1', function(err) {
	if (err) throw err;
} );
```

## deleteMulti

```js
storage.deleteMulti( KEYS, CALLBACK );
```

The `deleteMulti()` method deletes multiple records at once, from a specified array of keys.  Depending on your storage [concurrency](../README.md#concurrency) configuration, this may be significantly faster than deleting the records in sequence.  Example:

```js
storage.deleteMulti( ['test1', 'test2', 'test3'], function(err) {
	if (err) throw err;
} );
```

## copy

```js
storage.copy( OLD_KEY, NEW_KEY, CALLBACK );
```

The `copy()` method copies a value from one key and stores it at another.  If the destination record doesn't exist it is created, otherwise it is replaced.  Your callback function is passed an error if one occurred, otherwise it'll be falsey.  Example:

```js
storage.copy( 'test1', 'test2', function(err) {
	if (err) throw err;
} );
```

**Note:** This is a compound function containing multiple sequential engine operations (in this case a `get` and a `put`).  You may require locking depending on your application.  See [lock()](#lock) and [unlock()](#unlock) below.

## rename

```js
storage.rename( OLD_KEY, NEW_KEY, CALLBACK );
```

The `rename()` method copies a value from one key, stores it at another, and deletes the original key.  If the destination record doesn't exist it is created, otherwise it is replaced.  Your callback function is passed an error if one occurred, otherwise it'll be falsey.  Example:

```js
storage.rename( 'test1', 'test2', function(err) {
	if (err) throw err;
} );
```

**Note:** This is a compound function containing multiple sequential engine operations (in this case a `get`, `put` and `delete`).  You may require locking depending on your application.  See [lock()](#lock) and [unlock()](#unlock) below.

## lock

```js
storage.lock( KEY, WAIT, CALLBACK );
```

The `lock()` method implements an in-memory advisory locking system, where you can request an exclusive lock on a particular key, and optionally wait for it to be unlocked.  It is up to you to call [unlock()](#unlock) for every record that you lock, even in the case of an error.

If you pass `true` for the wait argument and the specified record is already locked, your request is added to a queue and invoked in a FIFO manner.  If you pass `false` and the resource is locked, an error is passed to your callback immediately.

## unlock

```js
storage.unlock( KEY );
```

The `unlock()` method releases an exclusive lock on a particular record, specified by its key.  This is a synchronous function with no callback.  For a usage example, see [Advisory Locking](../README.md#advisory-locking).

## shareLock

```js
storage.shareLock( KEY, WAIT, CALLBACK );
```

The `shareLock()` method implements an in-memory advisory locking system, where you can request a shared lock on a particular key, and optionally wait for it to be unlocked.  Multiple clients may lock the same key in shared mode.  It is up to you to call [shareUnlock()](#shareunlock) for every record that you lock, even in the case of an error.

If you pass `true` for the wait argument and the specified record is already locked, your request is added to a queue and invoked in a FIFO manner.  If you pass `false` and the resource is locked, an error is passed to your callback immediately.

## shareUnlock

```js
storage.shareUnlock( KEY );
```

The `shareUnlock()` method releases a shared lock on a particular record, specified by its key.  This is a synchronous function with no callback.  For a usage example, see [Advisory Locking](../README.md#advisory-locking).

## expire

```js
storage.expire( KEY, DATE );
```

The `expire()` method sets an expiration date on a record given its key.  The date can be any string, Epoch seconds or `Date` object.  The daily maintenance system will automatically deleted all expired records when it runs (assuming it is enabled -- see [Daily Maintenance](../README.md#daily-maintenance)).  Example:

```js
let exp_date = ((new Date()).getTime() / 1000) + 86400; // tomorrow
storage.expire( 'test1', exp_date );
```

The earliest you can set a record to expire is the next day, as the maintenance script only runs once per day, typically in the early morning, and it only processes records expiring on the current day.

## addRecordType

```js
storage.addRecordType( TYPE, HANDLERS );
```

The `addRecordType()` method registers a custom record type, for deletion via the daily maintenance system.  Your custom records are identified by a `type` property set to a unique string which you register a handler for.  Then, your handler is called to delete expired records of your defined types.  Example use:

```js
storage.addRecordType( 'my_custom_type', {
	delete: function(key, value, callback) {
		// custom handler function, called from daily maint for expired records
		// execute my own custom deletion routine here, then fire the callback
		callback();
	}
});
```

See [Custom Record Types](../README.md#custom-record-types) for more details.

## getStats

```js
storage.getStats();
```

The `getStats()` method returns information about current system performance, including min/avg/max metrics for the last second and minute.  It takes no arguments, and returns an object containing the following:

```json
{
	"version": "2.0.0",
	"engine": "Filesystem",
	"concurrency": 4,
	"transactions": true,
	"last_second": {
		"search": {
			"min": 14.306,
			"max": 14.306,
			"total": 14.306,
			"count": 1,
			"avg": 14.306
		},
		"get": {
			"min": 0.294,
			"max": 2.053,
			"total": 5.164,
			"count": 5,
			"avg": 1.032
		}
	},
	"last_minute": {},
	"recent_events": {},
	"locks": {}
}
```

For details on these stats, see [Performance Metrics](../README.md#performance-metrics).

# List Methods

## listCreate

```js
storage.listCreate( KEY, OPTIONS, CALLBACK );
```

The `listCreate()` method creates a new, empty list.  Specify the desired key, options (see below) and a callback function.  Your callback function is passed an error if one occurred, otherwise it'll be falsey.  Example:

```js
storage.listCreate( 'list1', {}, function(err) {
	if (err) throw err;
} );
```

Unless otherwise specified, the list will be created with the default [page size](../README.md#list_page_size) (number of items per page).  However, you can override this in the options object by passing a `page_size` property:

```js
storage.listCreate( 'list1', { page_size: 100 }, function(err) {
	if (err) throw err;
} );
```

## listPush

```js
storage.listPush( KEY, ITEMS, [OPTIONS], CALLBACK );
```

Similar to the standard [Array.push()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push), the `listPush()` method pushes one or more items onto the end of a list.  The list will be created if it doesn't exist, using the default [page size](../README.md#list_page_size).  `ITEMS` can be a single object, or an array of objects.  Your callback function is passed an error if one occurred, otherwise it'll be falsey.  Example:

```js
storage.listPush( 'list1', { username: 'jhuckaby', age: 38 }, function(err) {
	if (err) throw err;
} );
```

If the list doesn't exist, `listPush()` will create it.  If you specify an `OPTIONS` object, this will be used in the creation of the list, i.e. to specify the [page size](../README.md#list_page_size), and add any custom params you want.

```js
storage.listPush( 'list1', { username: 'jhuckaby', age: 38 }, { page_size: 100 }, function(err) {
	if (err) throw err;
} );
```

## listUnshift

```js
storage.listUnshift( KEY, ITEMS, CALLBACK );
```

Similar to the standard [Array.unshift()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/unshift), the `listUnshift()` method unshifts one or more items onto the beginning of a list.  The list will be created if it doesn't exist, using the default [page size](../README.md#list_page_size).  `ITEMS` can be a single object, or an array of objects.  Your callback function is passed an error if one occurred, otherwise it'll be falsey.  Example:

```js
storage.listUnshift( 'list1', { username: 'jhuckaby', age: 38 }, function(err) {
	if (err) throw err;
} );
```

If the list doesn't exist, `listUnshift()` will create it.  If you specify an `OPTIONS` object, this will be used in the creation of the list, i.e. to specify the [page size](../README.md#list_page_size), and add any custom params you want.

```js
storage.listUnshift( 'list1', { username: 'jhuckaby', age: 38 }, { page_size: 100 }, function(err) {
	if (err) throw err;
} );
```

## listPop

```js
storage.listPop( KEY, CALLBACK );
```

Similar to the standard [Array.pop()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop), the `listPop()` method pops one single item off the end of a list, and returns it.  Your callback function is passed an error if one occurred, otherwise it'll be falsey.  The second argument will be the popped item, if successful.  Example:

```js
storage.listPop( 'list1', function(err, item) {
	if (err) throw err;
} );
```

If the list is empty, an error is not generated, but the item will be `null`.

## listShift

```js
storage.listShift( KEY, CALLBACK );
```

Similar to the standard [Array.shift()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/shift), the `listShift()` method shifts one single item off the beginning of a list, and returns it.  Your callback function is passed an error if one occurred, otherwise it'll be falsey.  The second argument will be the shifted item, if successful.  Example:

```js
storage.listShift( 'list1', function(err, item) {
	if (err) throw err;
} );
```

If the list is empty, an error is not generated, but the item will be `null`.

## listGet

```js
storage.listGet( KEY, INDEX, LENGTH, CALLBACK );
```

The `listGet()` method fetches one or more items from a list, given the key, the starting index number (zero-based), the number of items to fetch (defaults to the entire list), and a callback.  Your callback function is passed an error if one occurred, otherwise it'll be falsey.  The second argument will be an array of the fetched items, if successful.  Example:

```js
storage.listGet( 'list1', 40, 5, function(err, items) {
	if (err) throw err;
} );
```

This would fetch 5 items starting at item index 40 (zero-based).

You can specify a negative index number to fetch items from the end of the list.  For example, to fetch the last 3 items in the list, use `-3` as the index, and `3` as the length.

Your callback function is also passed the list info object as a 3rd argument, in case you need to know the list length, page size, or first/last page positions.

## listSplice

```js
storage.listSplice( KEY, INDEX, LENGTH, NEW_ITEMS, CALLBACK );
```

Similar to the standard [Array.splice()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice), the `listSplice()` method removes a chunk of items from a list, optionally replacing it with a new chunk of items.  You must specify the list key, the index number of the first item to remove (zero-based), the number of items to remove (can be zero), an array of replacement items (can be empty or null), and finally a callback.

Your callback function is passed an error if one occurred, otherwise it'll be falsey.  The second argument will be an array of the removed items, if successful.  Example:

```js
storage.listSplice( 'list1', 40, 5, [], function(err, items) {
	if (err) throw err;
} );
```

This example would remove 5 items starting at item index 40, and replace with nothing (no items inserted).  The list size would shrink by 5, and the spliced items would be passed to your callback in an array.

## listFind

```js
storage.listFind( KEY, CRITERIA, CALLBACK );
```

The `listFind()` method will search a list for a particular item, based on a criteria object, and return the first item found to your callback.  The criteria object may have one or more key/value pairs, which must *all* match a list item for it to be selected.  Criteria values may be any JavaScript primitive (string, number, etc.), or a regular expression object for more complex matching.

Your callback function is passed an error if one occurred, otherwise it'll be falsey.  If an item was found matching your criteria, the second argument will be the item itself, and the 3rd argument will be the item's index number (zero-based).  Example:

```js
storage.listFind( 'list1', { username: 'jhuckaby' }, function(err, item, idx) {
	if (err) throw err;
} );
```

If an item is not found, no error is generated.  However, the `item` will be null, and the `idx` will be `-1`.

## listFindCut

```js
storage.listFindCut( KEY, CRITERIA, CALLBACK );
```

The `listFindCut()` method will search a list for a particular item based on a criteria object, and if found, it'll delete it (remove it from the list using [listSplice()](#listsplice)).  Your callback function is passed an error if one occurred, otherwise it'll be falsey.  If an item was found matching your criteria, the second argument will be the item itself.  Example:

```js
storage.listFindCut( 'list1', { username: 'jhuckaby' }, function(err, item) {
	if (err) throw err;
} );
```

## listFindReplace

```js
storage.listFindReplace( KEY, CRITERIA, NEW_ITEM, CALLBACK );
```

The `listFindReplace()` method will search a list for a particular item based on a criteria object, and if found, it'll replace it with the specified item.  Your callback function is passed an error if one occurred, otherwise it'll be falsey.  Example:

```js
let criteria = { username: 'jhuckaby' };
let new_item = { username: 'huckabyj', foo: 'bar' };

storage.listFindReplace( 'list1', criteria, new_item, function(err) {
	if (err) throw err;
} );
```

## listFindUpdate

```js
storage.listFindUpdate( KEY, CRITERIA, UPDATES, CALLBACK );
```

The `listFindUpdate()` method will search a list for a particular item based on a criteria object, and if found, it'll "update" it with the keys/values specified.  Meaning, they are merged in with the existing item, adding new keys or replacing existing ones.  Your callback function is passed an error if one occurred, otherwise it'll be falsey.  If an item was found matching your criteria, the second argument will be the item itself, with all the updates applied.  Example:

```js
let criteria = { username: 'jhuckaby' };
let updates = { gender: 'male', age: 38 };

storage.listFindUpdate( 'list1', criteria, updates, function(err, item) {
	if (err) throw err;
} );
```

You can also increment or decrement numerical properties with this function.  If an item key exists and is a number, you can set any update key to a string prefixed with `+` (increment) or `-` (decrement), followed by the delta number (int or float), e.g. `+1`.  So for example, imagine a list of users, and an item property such as `number_of_logins`.  When a user logs in again, you could increment this counter like this:

```js
let criteria = { username: 'jhuckaby' };
let updates = { number_of_logins: "+1" };

storage.listFindUpdate( 'list1', criteria, updates, function(err, item) {
	if (err) throw err;
} );
```

## listFindEach

```js
storage.listFindEach( KEY, CRITERIA, ITERATOR, CALLBACK );
```

The `listFindEach()` method will search a list for a *all* items that match a criteria object, and fire an iterator function for each one.  The criteria object may have one or more key/value pairs, which must all match a list item for it to be selected.  Criteria values may be any JavaScript primitive (string, number, etc.), or a regular expression object for more complex matching. 

Your `ITERATOR` function is passed the item, the item index number, and a special callback function which must be called when you are done with the current item.  Pass it an error if you want to prematurely abort the loop, and jump to the final callback (the error will be passed through to it).  Otherwise, pass nothing to the iterator callback, to notify all is well and you want the next matched item.

Your `CALLBACK` function is called when the loop is complete and all items were iterated over, or an error occurred somewhere in the middle.  It is passed an error object, or something falsey for success.  Example:

```js
storage.listFindEach( 'list1', { username: 'jhuckaby' }, function(item, idx, callback) {
	// do something with item, then fire callback
	callback();
}, 
function(err) {
	if (err) throw err;
	// all matched items iterated over
} );
```

## listInsertSorted

```js
storage.listInsertSorted( KEY, ITEM, COMPARATOR, CALLBACK );
```

The `listInsertSorted()` method inserts an item into a list, while keeping it sorted.  It doesn't resort the entire list every time, but rather it locates the correct position to insert the one item, based on sorting criteria, then performs a splice to insert it into place.  Example:

```js
let new_user = {
	username: 'jhuckaby', 
	age: 38, 
	gender: 'male' 
};

let comparator = function(a, b) {
	return( (a.username < b.username) ? -1 : 1 );
};

storage.listInsertSorted( 'users', new_user, comparator, function(err) {
	if (err) throw err;
	// item inserted successfully
} );
```

If your sorting criteria is simple, i.e. a single top level property sorted ascending or descending, you can specify an array containing the key to sort by, and a direction (`1` for ascending, `-1` for descending), instead of a comparator function.  Example:

```js
storage.listInsertSorted( 'users', new_user, ['username', 1], function(err) {
	if (err) throw err;
} );
```

## listCopy

```js
storage.listCopy( OLD_KEY, NEW_KEY, CALLBACK );
```

The `listCopy()` method copies a list and all its items to a new key.  Specify the existing list key, a new key, and a callback.  If anything exists at the destination key, it is clobbered.  Your callback function is passed an error if one occurred, otherwise it'll be falsey.  Example:

```js
storage.listCopy( 'list1', 'list2', function(err) {
	if (err) throw err;
} );
```

If a list already exists at the destination key, you should delete it first.  It will be overwritten, but if the new list has differently numbered pages, some of the old list pages may still exist and occupy space, detached from their old parent list.  So it is always safest to delete first.

## listRename

```js
storage.listRename( OLD_KEY, NEW_KEY, CALLBACK );
```

The `listRename()` method renames (moves) a list and all its items to a new key.  Specify the existing list key, a new key, and a callback.  If anything exists at the destination key, it is clobbered.  Your callback function is passed an error if one occurred, otherwise it'll be falsey.  Example:

```js
storage.listRename( 'list1', 'list2', function(err) {
	if (err) throw err;
} );
```

If a list already exists at the destination key, you should delete it first.  It will be overwritten, but if the new list has differently numbered pages, some of the old list pages may still exist and occupy space, detached from their old parent list.  So it is always safest to delete first.

## listEach

```js
storage.listEach( KEY, ITERATOR, CALLBACK );
```

The `listEach()` method iterates over a list one item at a time, invoking your `ITERATOR` function for each item.  This is similar to how the [async eachSeries()](http://caolan.github.io/async/docs.html#.eachSeries) method works (in fact, it is used internally for each list page).  The list pages are loaded one at a time, as to not fill up memory with huge lists.

Your iterator function is passed the item, the item index number, and a special callback function which must be called when you are done with the current item.  Pass it an error if you want to prematurely abort the loop, and jump to the final callback (the error will be passed through to it).  Otherwise, pass nothing to the iterator callback, to notify all is well and you want the next item in the list.

Your `CALLBACK` function is finally called when the loop is complete and all items were iterated over, or an error occurred somewhere in the middle.  It is passed an error object, or something falsey for success.  Example:

```js
storage.listEach( 'list1', function(item, idx, callback) {
	// do something with item, then fire callback
	callback();
}, 
function(err) {
	if (err) throw err;
	// all items iterated over
} );
```

## listEachPage

```js
storage.listEachPage( KEY, ITERATOR, CALLBACK );
```

The `listEachPage()` method iterates over a list one *page* at a time, invoking your `ITERATOR` function for each page.  The list pages are loaded one at a time, as to not fill up memory with huge lists.

Your iterator function is passed each page's items as an array, and a special callback function which must be called when you are done with the current page.  Pass it an error if you want to prematurely abort the loop, and jump to the final callback (the error will be passed through to it).  Otherwise, pass nothing to the iterator callback, to notify all is well and you want the next page in the list.

Your `CALLBACK` function is finally called when the loop is complete and all items were iterated over, or an error occurred somewhere in the middle.  It is passed an error object, or something falsey for success.  Example:

```js
storage.listEachPage( 'list1', function(items, callback) {
	// do something with items, then fire callback
	callback();
}, 
function(err) {
	if (err) throw err;
	// all items iterated over
} );
```

## listEachUpdate

```js
storage.listEachUpdate( KEY, ITERATOR, CALLBACK );
```

The `listEachUpdate()` method iterates over a list one item at a time, invoking your `ITERATOR` function for each item.  You can then choose to update any of the items, which will be written back to storage.  The list pages are loaded one at a time, as to not fill up memory with huge lists.

Your iterator function is passed the item, the item index number, and a special callback function which must be called when you are done with the current item.  The iterator callback accepts two arguments, an error (or something false for success), and a boolean which should be set to `true` if you made changes.  The storage engine uses this to decide which list pages require updating.

Your `CALLBACK` function is finally called when the loop is complete and all items were iterated over, or an error occurred somewhere in the middle.  It is passed an error object, or something falsey for success.  Example:

```js
storage.listEachUpdate( 'list1', function(item, idx, callback) {
	// do something with item, then fire callback
	item.something = "something new!";
	callback(null, true);
}, 
function(err) {
	if (err) throw err;
	// all items iterated over
} );
```

## listEachPageUpdate

```js
storage.listEachPageUpdate( KEY, ITERATOR, CALLBACK );
```

The `listEachPageUpdate()` method iterates over a list one *page* at a time, invoking your `ITERATOR` function for each page.  You can then choose to update any of the items, which will be written back to storage.  The list pages are loaded one at a time, as to not fill up memory with huge lists.

Your iterator function is passed each page's items as an array, and a special callback function which must be called when you are done with the current page.  The iterator callback accepts two arguments, an error (or something false for success), and a boolean which should be set to `true` if you made changes to any items on the current page.  The storage engine uses this to decide which list pages require updating.

Your `CALLBACK` function is finally called when the loop is complete and all items were iterated over, or an error occurred somewhere in the middle.  It is passed an error object, or something falsey for success.  Example:

```js
storage.listEachPageUpdate( 'list1', function(items, callback) {
	// do something with items, then fire callback
	items.forEach( function(item) {
		item.something = "something new!";
	} );
	callback(null, true);
}, 
function(err) {
	if (err) throw err;
	// all items iterated over
} );
```

## listGetInfo

```js
storage.listGetInfo( KEY, CALLBACK );
```

The `listGetInfo()` method retrieves information about the list, without loading any items.  Specifically, it fetches the list length, first and last page numbers, page size, and any custom keys you passed to the `OPTIONS` object when first creating the list.  Your callback function is passed an error if one occurred, otherwise it'll be falsey.  The second argument will be the list info object, if successful.  Example:

```js
storage.listGetInfo( 'list1', function(err, list) {
	if (err) throw err;
} );
```

Here are the keys you can expect to see in the info object:

| Key | Description |
|-----|-------------|
| `type` | Type of record, will be `list`. |
| `length` | Total number of items in the list. |
| `first_page` | Number of the first page in the list. |
| `last_page` | Number of the last page in the list. |
| `page_size` | Number of items per page. |

## listDelete

```js
storage.listDelete( KEY, ENTIRE, CALLBACK );
```

The `listDelete()` method deletes a list.  If you pass `true` for the second argument, the *entire* list will be deleted, including the header (options, page size, etc.).  Otherwise the list will simply be "cleared" (all items deleted).  Your callback function is passed an error if one occurred, otherwise it'll be falsey.  Example:

```js
storage.listDelete( 'list1', true, function(err) {
	if (err) throw err;
} );
```

# Hash Methods

## hashCreate

```js
storage.hashCreate( PATH, OPTIONS, CALLBACK );
```

The `hashCreate()` method creates a new, empty hash.  Specify the desired path, options (see below) and a callback function.  Your callback function is passed an error if one occurred, otherwise it'll be falsey.  Example:

```js
storage.hashCreate( 'hash1', {}, function(err) {
	if (err) throw err;
} );
```

Unless otherwise specified, the hash will be created with the default [page size](../README.md#hash_page_size) (number of items per page).  However, you can override this in the options object by passing a `page_size` property:

```js
storage.hashCreate( 'hash1', { page_size: 100 }, function(err) {
	if (err) throw err;
} );
```

## hashPut

```js
storage.hashPut( PATH, KEY, VALUE, [OPTIONS], CALLBACK );
```

The `hashPut()` method stores a single key/value pair in a hash.  The `PATH` specifies the main storage path of the hash, and the hash key itself is identified by `KEY`, which should be a string.  The `VALUE` must be an object, serializable by JSON.

```js
storage.hashPut( 'users', 'bsanders', { name: 'Bernie', age: 75 }, function(err) {
	if (err) throw err;
} );
```

If the hash doesn't exist, `hashPut()` will create it.  If you specify an `OPTIONS` object, this will be used in the creation of the hash, i.e. to specify the [page size](../README.md#hash_page_size), and add any custom params you want.

```js
storage.hashPut( 'users', 'bsanders', { name: 'Bernie', age: 75 }, { page_size: 100 }, function(err) {
	if (err) throw err;
} );
```

## hashPutMulti

```js
storage.hashPutMulti( PATH, RECORDS, [OPTIONS], CALLBACK );
```

The `hashPutMulti()` method stores multiple key/value pairs in a hash.  The `PATH` specifies the main storage path of the hash, and `RECORDS` should be an object containing all the keys and values you want to store.

```js
let records = {
	"bsanders": { name: "Bernie", age: 75 },
	"hclinton": { name: "Hillary", age: 68 },
	"dtrump": { name: "Donald", age: 70 }
};

storage.hashPutMulti( 'users', records, function(err) {
	if (err) throw err;
} );
```

If the hash doesn't exist, `hashPutMulti()` will create it.  If you specify an `OPTIONS` object, this will be used in the creation of the hash, i.e. to specify the [page size](../README.md#hash_page_size), and add any custom params you want.

## hashGet

```js
storage.hashGet( PATH, KEY, CALLBACK );
```

The `hashGet()` method fetches a single value from a hash.  The `PATH` specifies the main storage path of the hash, and the hash key itself is identified by `KEY`, which should be a string.  Your callback will be passed an error object (falsey on success), and the desired hash value.

```js
storage.hashGet( 'users', 'bsanders', function(err, value) {
	if (err) throw err;
} );
```

## hashGetMulti

```js
storage.hashGetMulti( PATH, KEYS, CALLBACK );
```

The `hashGetMulti()` method fetches multiple hash values at once, from a specified `PATH` and array of hash `KEYS`.  Depending on your storage [concurrency](../README.md#concurrency) configuration, this may be significantly faster than fetching the values in sequence.  Your callback function is passed an array of values which correspond to the specified keys.  Example:

```js
storage.hashGetMulti( 'users', ['bsanders', 'hclinton', 'dtrump'], function(err, values) {
	if (err) throw err;
	// values[0] will be the bsanders record.
	// values[1] will be the hclinton record.
	// values[2] will be the dtrump record.
} );
```

## hashUpdate

```js
storage.hashUpdate( PATH, KEY, UPDATES, CALLBACK );
```

The `hashUpdate()` method updates an existing key/value pair in a hash.  The `PATH` specifies the main storage path of the hash, and the hash key itself is identified by `KEY`, which should be a string.  The `UPDATES` must be an object, but it can contain sparse keys.  Furthermore, it can contain dot or slash delimited paths, to update inner nested keys.  The updates are essentially applied atop the exiting record, merging and replacing (overwriting) where appropriate.  Example:

```js
storage.hashUpdate( 'users', 'bsanders', { age: 81 }, function(err) {
	if (err) throw err;
} );
```

This would update Bernie's age to 81 without affecting any of the other properties in his user record.

## hashUpdateMulti

```js
storage.hashUpdateMulti( PATH, RECORDS, CALLBACK );
```

The `hashUpdateMulti()` method updates multiple key/value pairs in a hash.  The `PATH` specifies the main storage path of the hash, and `RECORDS` should be an object containing all the keys and values you want to update.  See [hashUpdate()](#hashupdate) for details on the update format.

```js
let updates = {
	"bsanders": { age: 81 },
	"hclinton": { age: 75 },
	"dtrump": { age: 77 }
};

storage.hashUpdateMulti( 'users', records, function(err) {
	if (err) throw err;
} );
```

This would update the `age` properties in each record, without affecting the other data.

## hashEach

```js
storage.hashEach( PATH, ITERATOR, CALLBACK );
```

The `hashEach()` method iterates over a hash one key at a time (in undefined order), invoking your `ITERATOR` function for each key/value pair.  The iterator is invoked in an asynchronous manner, requiring a callback to be called for every loop iteration (similar to [async eachSeries()](http://caolan.github.io/async/docs.html#.eachSeries)).  The hash pages are loaded one at a time, so we use as little memory as possible.

Your iterator function is passed the key and value of the current item, and a callback reference.  If you pass an error to the iterator callback it will abort the loop and proceed directly to the end (firing the final `CALLBACK` function).

The `CALLBACK` function is finally called when the loop is complete and all items were iterated over, or an error occurred somewhere in the middle.  It is passed an error object, or something falsey for success.  Example:

```js
storage.hashEach( 'users', function(key, value, callback) {
	// do something with key/value
	callback();
}, 
function(err) {
	if (err) throw err;
	// all keys iterated over
} );
```

## hashEachSync

```js
storage.hashEachSync( PATH, ITERATOR, CALLBACK );
```

The `hashEachSync()` method iterates over a hash one key at a time (in undefined order), invoking your `ITERATOR` function for each key/value pair.  The iterator is invoked in a synchronous manner, i.e. continuing as soon as it returns (similar to [Array.forEach()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)).  The hash pages are loaded one at a time, so we use as little memory as possible.

Your iterator function is passed the key and value of the current item.  If you return `false` it will abort the loop and proceed directly to the end (firing the `CALLBACK` function).

The `CALLBACK` function is finally called when the loop is complete and all items were iterated over, or an error occurred somewhere in the middle.  It is passed an error object, or something falsey for success.  Example:

```js
storage.hashEach( 'users', function(key, value) {
	// do something with key/value
	// no callback here
}, 
function(err) {
	if (err) throw err;
	// all keys iterated over
} );
```

## hashEachPage

```js
storage.hashEachPage( PATH, ITERATOR, CALLBACK );
```

The `hashEachPage()` method iterates over a hash one *page* at a time, invoking `ITERATOR` with *all* the keys and values in each page.  This differs from [hashEach()](#hasheach) in that your iterator is only fired once per page, as opposed to once per key.  This reduces overhead, making this the fastest way to iterate over a large hash.  The other difference is that your iterator is invoked in an asynchronous manner, i.e. it must fire a callback to continue (similar to [async eachSeries()](http://caolan.github.io/async/docs.html#.eachSeries)).

Your iterator is passed exactly two arguments.  An object containing all the keys and values in the current page (this may contain up to [page size](../README.md#hash_page_size) items), and a callback function that you must fire to continue the loop.  Pass an error into the callback to abort the loop anywhere in the middle.  The final `CALLBACK` is fired when all keys are iterated over, or an error occurs.

```js
storage.hashEachPage( 'users', function(items, callback) {
	// do something with page of items
	for (let key in items) {
		let value = items[key];
		// do something with key/value pair
	}
	
	// fire callback to continue to next page
	callback();
}, 
function(err) {
	if (err) throw err;
	// all keys iterated over
} );
```

## hashGetAll

```js
storage.hashGetAll( PATH, CALLBACK );
```

The `hashGetAll()` method loads a hash entirely into memory as fast as possible, and fires your callback with a single in-memory object containing *all* the key/value pairs.  Please use this with caution on large hashes, and keep track of your process memory usage.  The `CALLBACK` is fired with two arguments: an error if one occurred (falsey if not), and a hash object containing all your keys and values.

```js
storage.hashGetAll( 'users', function(err, items) {
	if (err) throw err;
	
	// do something with all items
	for (let key in items) {
		let value = items[key];
		// do something with key/value pair
	}
} );
```

## hashCopy

```js
storage.hashCopy( OLD_PATH, NEW_PATH, CALLBACK );
```

The `hashCopy()` method copies a hash and all of its items to a new path.  Specify the existing hash path, a new path, and a callback.  If anything exists at the destination path, it will be clobbered.  Your callback function is passed an error if one occurred, otherwise it'll be falsey.  Example:

```js
storage.hashCopy( 'hash1', 'hash2', function(err) {
	if (err) throw err;
} );
```

If a hash already exists at the destination path, you should delete it first.  It will be overwritten, but if the new hash has different pages, some of the old hash pages may still exist and occupy space, detached from their old parent hash.  So it is always safest to delete first.

## hashRename

```js
storage.hashRename( OLD_PATH, NEW_PATH, CALLBACK );
```

The `hashRename()` method renames (moves) a hash and all of its items to a new path.  Specify the existing hash path, a new path, and a callback.  If anything exists at the destination path, it will be clobbered.  Your callback function is passed an error if one occurred, otherwise it'll be falsey.  Example:

```js
storage.hashRename( 'hash1', 'hash2', function(err) {
	if (err) throw err;
} );
```

If a hash already exists at the destination path, you should delete it first.  It will be overwritten, but if the new hash has different pages, some of the old hash pages may still exist and occupy space, detached from their old parent hash.  So it is always safest to delete first.

## hashDelete

```js
storage.hashDelete( PATH, KEY, [ENTIRE], CALLBACK );
```

The `hashDelete()` method deletes a single key/value pair from the specified hash.  Your callback function is passed an error if one occurred, otherwise it'll be falsey.  Example:

```js
storage.hashDelete( 'users', 'dtrump', function(err) {
	if (err) throw err;
} );
```

By default, if `hashDelete()` removes the last key from a hash, it leaves an "empty" hash in storage (i.e. one with a header, page size, options, etc.).  However, if you would prefer, you can trigger a full delete if the hash becomes empty after the key is removed.  To do this, pass `true` as the 3rd argument, just before your callback.  Example:

```js
storage.hashDelete( 'users', 'dtrump', true, function(err) {
	if (err) throw err;
} );
```

## hashDeleteMulti

```js
storage.hashDeleteMulti( PATH, KEYS, CALLBACK );
```

The `hashDeleteMulti()` method deletes multiple hash records at once, from a specified array of keys.  Depending on your storage [concurrency](../README.md#concurrency) configuration, this may be significantly faster than deleting the records in sequence.  Example:

```js
storage.hashDeleteMulti( 'users', ['bsanders', 'hclinton', 'dtrump'], function(err) {
	if (err) throw err;
} );
```

## hashDeleteAll

```js
storage.hashDeleteAll( PATH, [ENTIRE], CALLBACK );
```

The `hashDeleteAll()` method deletes a hash and all its contents.  If you pass `true` for the second argument, the *entire* hash will be deleted, including the header (options, page size, etc.).  Otherwise the hash will simply be "cleared" (all items deleted) but the hash header will remain.  Your callback function is passed an error if one occurred, otherwise it'll be falsey.  Example:

```js
storage.hashDeleteAll( 'users', true, function(err) {
	if (err) throw err;
} );
```

## hashGetInfo

```js
storage.hashGetInfo( PATH, CALLBACK );
```

The `hashGetInfo()` method retrieves information about the hash, without loading any items.  Specifically, it fetches the hash length, page size, and any custom properties you passed to the `OPTIONS` object when first creating the list.  Your callback function is passed an error if one occurred, otherwise it'll be falsey.  The second argument will be the hash info object, if successful.  Example:

```js
storage.hashGetInfo( 'users', function(err, info) {
	if (err) throw err;
	console.log( "The hash has " + info.length + " keys." );
} );
```

Here are the keys you can expect to see in the info object:

| Key | Description |
|-----|-------------|
| `type` | Type of record, will be `hash`. |
| `length` | Total number of records in the hash. |
| `page_size` | Maximum number of hash items per page. |

# Transaction Methods

## begin

```js
storage.begin( PATH, CALLBACK );
```

The `begin()` method starts a new transaction.  This asynchronous method passes a special storage proxy object to your callback, which presents a "branch" or "view" of the database.  It is a proxy object upon which you can call any standard storage API methods, e.g. [put()](#put), [get()](#get), [delete()](#delete) or other.  Any operations on the transaction object take place in complete isolation, separate from the main storage object.  Example:

```js
storage.begin( 'some_path', function(err, trans) {
	
	// perform actions using `trans` proxy
	// e.g. trans.put(), trans.get(), trans.delete()
	
	// commit transaction here (see below)
});
```

## commit

```js
trans.commit( CALLBACK );
```

The `commit()` method completes the transaction, applies all the changes to main storage, and releases the lock.  At that point you should discard the `trans` object, as it can no longer be used.  This method should be called on your transaction proxy object obtained by calling [begin()](#begin).  Example use:

```js
storage.begin( 'some_path', function(err, trans) {
	
	// perform actions using `trans` proxy
	// e.g. trans.put(), trans.get(), trans.delete()
	
	// commit transaction
	trans.commit( function(err) {
		// complete
	} );
});
```

You can omit the callback to `commit()` if you know your transaction has zero write operations.  In this case it should release the lock and discard the transaction in the same thread.  However, use this with care.

## abort

```js
trans.abort( CALLBACK );
```

The `abort()` method cancels a transaction in progress, and rolls everything back (if any changes occurred).  This also releases the transaction lock and renders the transaction object dead.  This method should be called on your transaction proxy object obtained by calling [begin()](#begin).  Example use:

```js
storage.begin( 'some_path', function(err, trans) {
	
	// perform actions using `trans` proxy
	// e.g. trans.put(), trans.get(), trans.delete()
	
	// commit transaction
	trans.commit( function(err) {
		// check for error
		if (err) {
			// error during commit, abort it and roll back
			return trans.abort( function() {
				// rollback complete
			} );
		}
		
		// transaction is complete
	} );
});
```

You can call `abort()` anytime before or after calling [commit()](#commit), to manually abort the transaction yourself.  However, it should be noted that if you receive an error from a [commit()](#commit) call, it is *vital* that you call `abort()` to undo whatever operations may have already executed.  A commit error is typically very bad, and your storage system will be in an unknown state.  Only by calling `abort()` can you restore it to before the transaction started.

If the abort also fails, then the database raises a fatal error and exits immediately.  See [Emergency Shutdown](Transactions.md#emergency-shutdown) for details about what this means, and [Recovery](Transactions.md#recovery) for how to get back up and running.  Examples of fatal errors include your disk running completely out of space, or a major network failure when using NFS, S3 or Couchbase.

# Indexer Methods

## indexRecord

```
storage.indexRecord( ID, RECORD, CONFIG, [CALLBACK] );
```

The `indexRecord()` method submits a data record to the [Indexer](Indexer.md) system, and associates it with a unique ID.  Based on a [configuration](Indexer.md#configuration) object you provide, one or more fields will be indexed by value.  Your record can then be [searched](Indexer.md#searching-records) using custom queries.  The method takes three arguments, plus an optional callback:

- A unique ID for the record (string).
- An object containing the record to be indexed.
- A configuration object describing all the fields and sorters to apply.
- An optional callback.

Example:

```js
storage.indexRecord( "TICKET0001", record, config, function(err) {
	// record is fully indexed
	if (err) throw err;
} );
```

For more details and a complete example, see the [Indexing Records](Indexer.md#indexing-records) section.

## unindexRecord

```
storage.unindexRecord( RECORD_ID, CONFIG, [CALLBACK] );
```

The `unindexRecord()` method removes a data record from the [Indexer](Indexer.md) system.  You *do not* need to include the data record itself for unindexing.  The method takes two arguments, plus an optional callback:

- A unique ID for the record (string).
- A configuration object describing all the fields and sorters.
- An optional callback.

Example:

```js
storage.unindexRecord( "TICKET0001", config, function(err) {
	// record is completely removed from the index
	if (err) throw err;
} );
```

For more details and a complete example, see the [Unindexing Records](Indexer.md#unindexing-records) section.

## searchRecords

```
storage.searchRecords( QUERY, CONFIG, CALLBACK );
```

The `searchRecords()` method performs an index search.  Pass in a search query, your [index configuration](Indexer.md#configuration) object, and a callback.  Your callback will be passed an Error object (or false on success), and a hash of all the matched record IDs.  Here is an example:

```js
storage.searchRecords( 'modified:2018/01/07 tags:bug', config, function(err, results) {
	// search complete
	if (err) throw err;
	
	// results will be hash of record IDs
	// { "TICKET0001": 1, "TICKET0002": 1 }
} );
```

This finds all records that were modified on Jan 7, 2018 **and** contain the tag `bug`.  This syntax is called a [simple query](Indexer.md#simple-queries), and is explained in detail below, along with the more complex [PxQL](Indexer.md#pxql-queries) syntax.

For more details on searching records, see the [Searching Records](Indexer.md#searching-records) section.

## sortRecords

```
storage.sortRecords( RESULTS, SORTER, DIRECTION, CONFIG, CALLBACK );
```

The `sortRecords()` method performs a sort operation on search results, as returned from [searchRecords()](#searchrecords).  The method accepts the following 5 arguments:

- An unsorted hash of record IDs, as returned from [searchRecords()](#searchrecords).
- The ID of the sorter field, e.g. `username`, `num_comments`.
- The sort direction, which should be `1` for ascending, or `-1` for descending (defaults to `1`).
- Your main index [configuration](Indexer.md#configuration) object, containing the `sorter` array.
- A callback to receive the final sorted IDs.

Here is an example sort:

```js
// sort the results by username ascending
storage.sortRecords( results, 'username', 1, config, function(err, sorted) {
	// sort complete
	if (err) throw err;
	
	// sorted IDs will be in array
	// [ "TICKET0001", "TICKET0002", "TICKET0003" ]
} ); // sortRecords
```

Once you have an array of your sorted record IDs, you can then implement your own pagination system (i.e. limit & offset), and load multiple records at at time via [getMulti()](#getmulti) or other.

For more details on sorting search results, see the [Sorting Results](Indexer.md#sorting-results) section.

## getFieldSummary

```
storage.getFieldSummary( FIELD_ID, CONFIG, CALLBACK );
```

The `getFieldSummary()` method fetches a summary of all word counts for an index field.  This requires a field indexed with the [master list](Indexer.md#master-list) feature enabled.  Then you can fetch a "summary" of the data values, which returns a hash containing all the unique words from the index, and their total counts (occurrences) in the data.  Example use:

```js
storage.getFieldSummary( 'status', config, function(err, values) {
	if (err) throw err;
	
	// values should contain a hash with word counts:
	// { "open": 45, "closed": 13, "assigned": 3 }
} );
```

Summaries work best for fields that contain a relatively small amount of unique words, such as a "status" field.

## searchSingle

```
storage.searchSingle( QUERY, RECORD_ID, CONFIG, CALLBACK );
```

The `searchSingle()` method performs a search on a *single* record, simply indicating if it matches the search criteria or not.  Pass in any [search query](Indexer.md#searching-records), the ID of the record you want to check, your [index configuration](Indexer.md#configuration) object, and a callback.  Your callback will be passed an Error object (or false on success), and a Boolean indicating if the specified record would be included in the search results, or not.  Here is an example:

```js
storage.searchSingle( 'modified:2018/01/07 tags:bug', "TICKET0001", config, function(err, result) {
	// search complete
	if (err) throw err;
	
	// result will be true in this case
} );
```

This is an internal method designed for "testing" searches against a single record.  One possible use is a "live search" system, which would test each changed record against a query, and then making individual changes to a live result set, and publishing those changes to subscribers.
```

## File: `docs/Hashes.md`
```markdown
# Hashes

A hash is a collection of JSON records, indexed by key, that can grow to virtually any size without using much memory.  The collection is split into one or more "pages" and each page holds up to N records (configurable).  When the hash grows beyond the page size, it is automatically re-indexed into nested pages.  The hash store and fetch operations are very fast, and hashes can also be iterated over (keys are retrieved in undefined order).

The benefit of using a hash over simply calling [get()](API.md#get) and [put()](API.md#put) is that a hash can be iterated over, the key count can be retrieved at any time, and repeated operations are accelerated due to the nature of the paging system.  Also, hash keys are not [normalized](../README.md#key-normalization) like storage paths are, so you could have full Unicode / Emoji hash keys if you wanted.

All hash operations will automatically lock the hash using [Advisory Locking](../README.md#advisory-locking) (shared locks or exclusive locks, depending on if the operation is read or write), and unlock it when complete.  This is because all hash operations involve multiple concurrent low-level storage calls.  Hashes can be used inside [Transactions](Transactions.md) as well.

The code examples all assume you have your preloaded `Storage` component instance in a local variable named `storage`.  The component instance can be retrieved from a running server like this:

```js
let storage = server.Storage;
```

## Table of Contents

> &larr; [Return to the main document](https://github.com/jhuckaby/pixl-server-storage/blob/master/README.md)

<!-- toc -->
- [Hash Page Size](#hash-page-size)
- [Creating Hashes](#creating-hashes)
- [Storing and Fetching](#storing-and-fetching)
- [Iterating Over Hashes](#iterating-over-hashes)
- [Copying and Renaming](#copying-and-renaming)
- [Deleting](#deleting)
- [Hash Internals](#hash-internals)

## Hash Page Size

Hash items are stored in groups called "pages", and each page can hold up to N items (the default is 50).  When the number of hash keys exceeds the page size, the hash is re-indexed into sub-pages.  This all happens automatically behind the scenes, but care should be taken to choose your optimal page size.  In general, the larger your hash records, the smaller the page size should be.

You can configure how many items are allowed in each page, by changing the default [page size](../README.md#hash_page_size) in your storage configuration, or setting it per hash by passing an option to [hashCreate()](API.md#hashcreate).

Care should be taken when calculating your hash page sizes.  It all depends on how large your items will be, and if you will be iterating over them often.  Note that you cannot easily change the page size on a populated hash (this may be added as a future feature).

## Creating Hashes

To create a hash, call [hashCreate()](API.md#hashcreate).  Specify the desired storage path, options, and a callback function.  You can optionally pass in a custom page size via the second argument (otherwise it'll use the default size):

```js
storage.hashCreate( 'hash1', { page_size: 100 }, function(err) {
	if (err) throw err;
} );
```

You can also store your own properties in the options object, which are retrievable via the [hashGetInfo()](API.md#hashgetinfo) method.  However, beware of name collision -- better to prefix your own option props with something unique.

## Storing and Fetching

Hashes have basic methods for storing and fetching keys, as you might expect.  When accessing hashes, you generally need to specify two different strings: A single base "storage path" (where the hash lives in storage), and then each record inside the hash also has its own key.

To store a key/value pair, call [hashPut](API.md#hashput), and to fetch a value based on its key, call [hashGet()](API.md#hashget).  If a key already exists, `hashPut()` will replace it.  If you try to fetch a nonexistent key via `hashGet()`, an Error object will be passed to your callback with its `code` property set to `NoSuchKey`.

Here is an example of storing and fetching a hash record.  The hash itself is located at the storage path `users`, and we are storing and fetching the hash key `bsanders` within that hash.

```js
// Store a key/value pair
storage.hashPut( 'users', 'bsanders', { name: 'Bernie', age: 75 }, function(err) {
	if (err) throw err;
	
	// Fetch a value given its key
	storage.hashGet( 'users', 'bsanders', function(err, value) {
		if (err) throw err;
		
		console.log( value );
		// { name: 'Bernie', age: 75 }
	} );
} );
```

Note that you do not need to explicitly create the hash via [hashCreate()](API.md#hashcreate).  The [hashPut](API.md#hashput) method will auto-create it for you if necessary.

In addition to storing single records, you can specify multiple at a time using the [hashPutMulti()](API.md#hashputmulti) method.  Instead of key and value arguments, pass in an object containing as many as you want:

```js
let records = {
	"bsanders": { name: "Bernie", age: 75 },
	"hclinton": { name: "Hillary", age: 68 },
	"dtrump": { name: "Donald", age: 70 }
};

storage.hashPutMulti( 'users', records, function(err) {
	if (err) throw err;
} );
```

Similarly, to fetch multiple records, use [hashGetMulti()](API.md#hashgetmulti).  Specify your desired keys in an array, and you'll get an array of values with numerical indexes that match up to your keys:

```js
storage.hashGetMulti( 'users', ['bsanders', 'hclinton', 'dtrump'], function(err, values) {
	if (err) throw err;
	// values[0] will be the bsanders record.
	// values[1] will be the hclinton record.
	// values[2] will be the dtrump record.
} );
```

Finally, if you simply want to fetch *all* the records in a hash in one fell swoop, and you aren't concerned with memory usage, call [hashGetAll()](API.md#hashgetall).

```js
storage.hashGetAll( 'users', function(err, items) {
	if (err) throw err;
	
	// do something with all items
	for (let key in items) {
		let value = items[key];
		// do something with key/value pair
	}
} );
```

## Iterating Over Hashes

For iterating over a hash, you have two options.  First, you can use [hashEach()](API.md#hasheach), which fires an asynchronous iterator for every key/value pair.  The iterator is passed the current key, value, and a callback which must be fired (similar to [async eachSeries()](http://caolan.github.io/async/docs.html#.eachSeries)).  Pass an error to the callback to abort the loop in the middle.  Example:

```js
storage.hashEach( 'users', function(key, value, callback) {
	// do something with key/value
	callback();
}, 
function(err) {
	if (err) throw err;
	// all keys iterated over
} );
```

Alternatively, you can use [hashEachSync()](API.md#hasheachsync) in which the iterator is invoked in a *synchronous* manner, i.e. continuing as soon as it returns (similar to [Array.forEach()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)).  However, please note that the full loop operation isn't synchronous, and you need to provide a callback to be fired when every key has been iterated over.  Example:

```js
storage.hashEachSync( 'users', function(key, value) {
	// do something with key/value
	// no callback here
}, 
function(err) {
	if (err) throw err;
	// all keys iterated over
} );
```

Finally, you can use [hashEachPage()](API.md#hasheachpage), which iterates over the internal hash pages, and only fires your iterator function once per page, instead of once per key.  This is typically faster as it requires fewer function calls.  Your iterator is invoked in an *asynchronous* manner, i.e. it must fire a callback to continue (similar to [async eachSeries()](http://caolan.github.io/async/docs.html#.eachSeries)).  Example:

```js
storage.hashEachPage( 'users', function(items, callback) {
	// do something with page of items
	for (let key in items) {
		let value = items[key];
		// do something with each key/value pair
	}
	
	// fire callback to continue to next page
	callback();
}, 
function(err) {
	if (err) throw err;
	// all keys iterated over
} );
```

## Copying and Renaming

To duplicate a hash and all of its items at a new storage path, call [hashCopy()](API.md#hashcopy), specifying the old and new paths.  Example:

```js
storage.hashCopy( 'hash1', 'hash2', function(err) {
	if (err) throw err;
} );
```

To rename a hash, call [hashRename()](API.md#hashrename).  This is basically just a [hashCopy()](API.md#hashcopy) followed by a [hashDeleteAll()](API.md#hashdeleteall).  Example:

```js
storage.hashRename( 'hash1', 'hash2', function(err) {
	if (err) throw err;
} );
```

With both of these functions, it is highly recommended you make sure the destination (target) path is empty before copying or renaming onto it.  If a hash already exists at the destination path, it will be overwritten, but if the new hash has different content, some of the old hash pages may still exist and occupy space, detached from their old parent hash.  So it is always safest to delete first, or use a path you know to be vacant.

## Deleting

To delete a single hash key, call [hashDelete()](API.md#hashdelete).  Example:

```js
storage.hashDelete( 'users', 'dtrump', function(err) {
	if (err) throw err;
} );
```

If you delete the last key from a hash, an "empty" hash will remain in storage (this includes metadata such as the options, page size, etc).  If you want to delete the *entire* hash when the last key is removed, pass `true` as the 3rd argument before the callback:

```js
storage.hashDelete( 'users', 'dtrump', true, function(err) {
	if (err) throw err;
} );
```

To delete multiple hash keys at once, use [hashDeleteMulti()](API.md#hashdeletemulti).  Specify your desired keys in an array:

```js
storage.hashDeleteMulti( 'users', ['bsanders', 'hclinton', 'dtrump'], function(err) {
	if (err) throw err;
} );
```

Finally, to delete an *entire* hash including all its keys, call [hashDeleteAll()](API.md#hashdeleteall):

```js
storage.hashDeleteAll( 'users', function(err) {
	if (err) throw err;
} );
```

As with `hashDelete()`, by default this will only empty a hash, leaving behind an empty header record (with options, page size, etc).  To delete that as well, pass `true` as the 2nd argument before the callback:

```js
storage.hashDeleteAll( 'users', true, function(err) {
	if (err) throw err;
} );
```

## Hash Internals

Hashes are implemented on top of basic storage using a paging system.  Each hash has a main header record containing basic information such as the number of keys, and options such as page size.  Then, under that base path lives each page, containing up to [N](../README.md#hash_page_size) hash records.  When enough keys are added to the hash so that a page overflows, it is automatically "reindexed" into sub-pages.

A basic hash with fewer than [N](../README.md#hash_page_size) keys looks like this on a [raw filesystem](../README.md#raw-file-paths):

```
data/
 ├ users/
 │  └ data.json
 └ users.json
```

In this example we have a simple users hash with 3 keys.  Storage key `users` (file: `users.json`) is the main header record containing metadata about the hash:

```js
{
	"page_size": 10,
	"length": 3,
	"type": "hash"
}
```

Here are descriptions of the header properties:

| Property | Description |
|----------|-------------|
| `type` | A static identifier, which will always be set to `hash` for the header record. |
| `length` | How many items are currently in the hash. |
| `page_size` | How many items are stored per page. |

The actual hash keys and values are stored in a sub-record, in this case `users/data` (file: `users/data.json`).  The format of this file is very simple:

```js
{
	"type": "hash_page",
	"length": 3,
	"items": {
		"bsanders": {
			"name": "Bernie",
			"age": 75
		},
		"hclinton": {
			"name": "Hillary",
			"age": 68
		},
		"dtrump": {
			"name": "Donald",
			"age": 70
		}
	}
}
```

This is a hash page, and represents one chunk of the hash, containing up to [N](../README.md#hash_page_size) keys.  It has a `type` property set to `hash_page`, its own `length` which holds the number of keys in the page, and the keys/values are all stored in `items`.

Now let's see what happens to the raw filesystem when we store more than one page of records.  Here is what it looks like after adding the 11th record (with a [hash_page_size](../README.md#hash_page_size) of 10):

```
data/
 ├ users/
 │  ├ data/
 │  │  ├ 0.json
 │  │  ├ 1.json
 │  │  ├ 3.json
 │  │  ├ 5.json
 │  │  ├ 6.json
 │  │  ├ 8.json
 │  │  ├ 9.json
 │  │  ├ c.json
 │  │  └ e.json
 │  └ data.json
 └ users.json
```

As you can see, the `users.json` and `users/data.json` files are still present.  The only difference in the main header file (`users.json`) is the `length` property, which is now `11`:

```js
{
	"page_size": 10,
	"length": 11,
	"type": "hash"
}
```

But look at what happened to `users/data.json`:

```js
{
	"type": "hash_index"
}
```

This record previously contained all the hash keys and values, so where did they all go?  Well, as you can see the `type` property was changed from `hash_page` to `hash_index` here.  This is a hint that the hash was re-indexed, and all the actual content is now located deeper.  Basically, there are too many records to stuff into one page, so they are now spread out amongst several:

```
users/data/0.json
users/data/1.json
users/data/3.json
users/data/5.json
users/data/6.json
users/data/8.json
users/data/9.json
users/data/c.json
users/data/e.json
```

Let's look at one of them, say `users/data/3.json`:

```js
{
	"type": "hash_page",
	"length": 2,
	"items": {
		"bsanders": {
			"name": "Bernie",
			"age": 75
		},
		"ecummings": {
			"name": "Eric",
			"age": 54
		}
	}
}
```

As you can see, this is where the `hash_page` records went, and in this case it contains two of our eleven items.  But why only these two, and why is it named `3.json`?  The answer is that the hash keys are run through the [MD5](https://en.wikipedia.org/wiki/MD5) algorithm, and the first character of the resultant MD5 digest (in hexadecimal format) is used to distribute the keys amongst sub-pages.

That's also why we are seemingly missing `2.json`, `7.json` and others.  The reason is, with only 11 keys total, only some hexadecimal characters are in use.  To illustrate, here are the 11 sample keys we used, and their MD5 digests:

| Hash Key | MD5 Digest |
|----------|------------|
| `bsanders` | `328cb5dbe722f89a329f8682a4de15d7` *(Starts with digit 3)* |
| `hclinton` | `ebdc9e6342a5adbc59781dfae3fca9fb` |
| `dtrump` | `107b9e22a331462e6c7431e3cc26e367` |
| `asmith` | `959074c6444c990db64c44e363b28b10` |
| `bhenry` | `05aadeb041feb91a515d1611a5a74210` |
| `crooster` | `e1132752dcaafcda8638a3ec37e4dee2` |
| `darment` | `547ba8d76f4e71ff3c0fe8b0389c9386` |
| `ecummings` | `3951e70aa4c883c97769f47929a4b88b` *(Starts with digit 3)* |
| `fhollister` | `cb53189cb9fabcc791e78e4a52e3a189` |
| `gsangrias` | `85ce076e883b53de15909cd9e6bd1346` |
| `hpostit` | `61aa3183de742f5361d6e83e110f8616` |

As you can see, the `bsanders` and `ecummings` keys both have MD5 digests that begin with `3`.  That's why they both share the `users/data/3.json` hash page.

The hash re-index system goes even deeper.  As soon as these sub-pages fill up and individually contain more than [hash_page_size](../README.md#hash_page_size) records, *another* re-index event occurs, on the specific page, and sends values even deeper down the index hole.  But in subsequent re-indexes, different MD5 digest characters are used.

For example, with two levels of indexing, the `bsanders` record would be relocated to this page:

```
data/users/data/3/2.json
```

This now uses the first 2 characters of the key's MD5 digest, in hexadecimal format.

And the previous `users/data/3.json` page is converted to a `hash_index` record (just like what happened with `users/data.json` on the first-level re-index):

```js
{
	"type": "hash_index"
}
```

This re-indexing process can continue virtually indefinitely, theoretically up to the full 32 hex characters of the MD5 digest.  There is effectively no limit to the number of keys (well, 2^128 keys max), but things definitely slow down in the millions, and filesystems run out of [inodes](https://en.wikipedia.org/wiki/Inode) at a certain point.

If keys are deleted from a hash, an "un-index" event may also occur, which is literally the reverse of a re-index.  The affected sub-pages are all deleted, and the remaining hash records, if any, are gathered together in a parent level.

Note that all re-index and un-index operations are automatic and happen in the background, so your code doesn't have to worry.  Locking is always used, so there is no chance of data corruption.
```

## File: `docs/Indexer.md`
```markdown
# Indexer

The indexer subsystem provides a way to "index" your JSON records by one or more fields, and then perform searches using a simple query language.  It is essentially a word indexer at its core, built on top of the standard storage APIs, but provides full text search capabilities, as well as unique keywords, numbers and dates.

Before using the indexer, please keep the following in mind:

- This is not a full database by any stretch -- merely a simplistic and rudimentary way to index and search records.
- All your records must have a unique ID string.
	- This will be the primary index, and the key you get back from searches.
- You are expected to store your record data yourself.
	- The indexer **only** indexes fields for searching purposes -- it does not store raw records for retrieval.
- When performing a search, you **only** get your record IDs back.  
	- You are expected to paginate and fetch your own record data (i.e. via [getMulti()](API.md#getmulti) or other).

The indexer works with any storage engine, but it is optimized for the local filesystem.  Transactions are automatically used for indexing and unindexing records, if they are enabled (this is highly recommended).

The code examples all assume you have your preloaded `Storage` component instance in a local variable named `storage`.  The component instance can be retrieved from a running server like this:

```js
let storage = server.Storage;
```

## Table of Contents

> &larr; [Return to the main document](https://github.com/jhuckaby/pixl-server-storage/blob/master/README.md)

<!-- toc -->
- [Caveats](#caveats)
- [Configuration](#configuration)
	* [Standard Indexes](#standard-indexes)
		+ [Master List](#master-list)
	* [Full Text Indexes](#full-text-indexes)
		+ [Text Filters](#text-filters)
		+ [Remove Words](#remove-words)
	* [Custom Field Types](#custom-field-types)
		+ [Number Type](#number-type)
		+ [Date Type](#date-type)
- [Indexing Records](#indexing-records)
	* [Source Paths](#source-paths)
	* [Text Cleanup](#text-cleanup)
	* [Boolean Values](#boolean-values)
	* [Null Values](#null-values)
	* [Default Values](#default-values)
	* [Unicode Characters](#unicode-characters)
	* [Stemming](#stemming)
- [Unindexing Records](#unindexing-records)
- [Searching Records](#searching-records)
	* [Simple Queries](#simple-queries)
	* [PxQL Queries](#pxql-queries)
	* [Fetching All Records](#fetching-all-records)
- [Sorting Results](#sorting-results)
- [Field Summaries](#field-summaries)
- [Bulk Reindexing](#bulk-reindexing)
	* [Adding Fields](#adding-fields)
	* [Deleting Fields](#deleting-fields)
	* [Changing Fields](#changing-fields)
- [Performance Tips](#performance-tips)
- [Indexer Internals](#indexer-internals)
	* [Date and Number Fields](#date-and-number-fields)
	* [Special Metadata](#special-metadata)

## Caveats

The indexer only processes words that contain standard U.S. ASCII alphanumeric characters, e.g. A-Z, 0-9, and underscore.  All other characters are skipped, and serve as word separators.  International (Unicode) characters are converted to ASCII at index and search time (see [Unicode Characters](#unicode-characters) below for more on this).

The indexer can be slow, depending on the storage engine.  All index operations involve reading and writing JSON storage records *at the word level* (i.e. a hash for each unique word!), and the system is designed to eat as little memory as possible.  Expect hundreds or even thousands of storage operations for indexing a single record.  Searching is fairly quick by comparison, because typically you're only searching on a small number of words.  This also assumes your storage back-end is fast (preferably local SSD filesystem, or you are using a very fast key/value store like Couchbase or SQLite), and your search queries are simple and straightforward.

This system is not designed for large query results.  Thousands of records returned is probably fine, and maybe even tens of thousands depending on the index types and data size.  *Hundreds of thousands* of records would likely end in tears.  Also, if you are using the Filesystem storage engine, keep an eye on your [inodes](https://en.wikipedia.org/wiki/Inode), because this thing is hungry for them.

## Configuration

To use the indexer, you need to provide a configuration object which describes how to index and sort your records.  This object must be stored externally by your application, and passed into all calls to [indexRecord()](API.md#indexrecord), [unindexRecord()](API.md#unindexrecord) and [sortRecords()](API.md#sortrecords).  Here is the general configuration layout:

```js
{
	"base_path": "index/myapp",
	"fields": [
		...
	],
	"sorters": [
		...
	],
	"remove_words": [
		...
	]
}
```

The `base_path` property tells the indexer where to store its records in main storage.  This can be any unique path, and it doesn't need to exist.  The indexer records will use this as a prefix.  Note that you should not store any of your own records under this path, to avoid potential collisions.  The base path is also used for transaction locking.

The `fields` array should contain an object for each field in your data you want indexed.  Here is an example field index definition:

```js
"fields": [
	{
		"id": "status",
		"source": "/TicketStatus"
	}
]
```

This would create a simple word field index with ID `status` (must be alphanumeric) and a source path of `/TicketStatus`.  The `source` should be a "virtual path" of where to locate the text value inside your record data.  See [Source Paths](#source-paths) below for more details.

For a full text search field (i.e. multi-word paragraph text), more properties are recommended:

```js
"fields": [
	{
		"id": "body",
		"source": "/BodyText",
		"min_word_length": 3,
		"max_word_length": 64,
		"use_remove_words": true,
		"use_stemmer": true,
		"filter": "html"
	}
]
```

This example would create a full text index with ID `body` and a source path of `/BodyText`.  It would only index words that are between 3 and 64 characters in length, use a [remove word](#remove-words) list, use [stemming](#stemming) for normalization, and apply a [HTML pre-filter](#text-filters).  See [Full Text Indexes](#full-text-indexes) for more on these types of fields.

Here is the full list of available properties for each index definition:

| Property Name | Type | Description |
|---------------|------|-------------|
| `id` | String | A unique alphanumeric ID for the field. |
| `type` | String | Optional custom field type (see [Custom Field Types](#custom-field-types) below). |
| `source` | String | A virtual path specifying the location of the text value inside your record data (see [Source Paths](#source-paths)). |
| `min_word_length` | Number | Optionally set a minimum word length (shorter words are skipped).  Highly recommended for [Full Text Indexes](#full-text-indexes).  Defaults to `1`. |
| `max_word_length` | Number | Optionally set a maximum word length (longer words are skipped).  Highly recommended for [Full Text Indexes](#full-text-indexes).  Defaults to `255`. |
| `max_words` | Number | Optionally set a maximum number of words to index per record.  If the source has additional words beyond the max they will be ignored. |
| `use_remove_words` | Boolean | Optionally use a remove word list for common words.  Highly recommended for [Full Text Indexes](#full-text-indexes).  See [Remove Words](#remove-words).  Defaults to `false` (disabled). |
| `use_stemmer` | Boolean | Optionally use a stemmer to normalize words.  Highly recommended for [Full Text Indexes](#full-text-indexes).  See [Stemming](#stemming).  Defaults to `false` (disabled). |
| `filter` | String | Optionally filter text with specified method before indexing.  See [Text Filters](#text-filters).  Defaults to disabled. |
| `master_list` | Boolean | Optionally keep a list of all unique words for the index.  See [Master List](#master-list).  Defaults to `false` (disabled). |
| `default_value` | String | Optional default value, for when record has no value for the field, or it is set to `null`.  See [Default Values](#default-values). |
| `no_cleanup` | Boolean | *(Advanced)* Set this to `true` to skip all text cleanup, and index it raw instead.  See [Text Cleanup](#text-cleanup).  Only use this if you know what you are doing. |
| `delete` | Boolean | *(Advanced)* Set this to `true` to force the indexer to delete the data for the field.  See [Deleting Fields](#deleting-fields) below.

The `sorters` array allows you to specify which fields you will need to sort by.  These fields do not need to be indexed -- they can be "sort only" fields.  Each needs an `id` and a `source` (data path, same as with fields).  Example:

```js
"sorters": [
	{
		"id": "created",
		"source": "/CreateDate",
		"type": "number"
	}
]
```

If you specify a `type` property and set it to `number`, then the values will be sorted numerically.  The default sort type is alphabetically.  In the above example the `CreateDate` property is assumed to be Epoch seconds (i.e. a sortable number).  See [Sorting Results](#sorting-results) below for more details.

The `remove_words` array allows you to specify a custom list of "remove words".  These words are removed (skipped) from indexing, if the definition sets the `use_remove_words` property.  Example:

```js
"remove_words": ["the", "of", "and", "a", "to", "in", "is", "you", "that", "it", "he", "was", "for", "on", "are", "as", "with", "his", "they"]
```

The idea here is that you only need to specify one global remove word list, and multiple fields can all share it.  See [Remove Words](#remove-words) below for more on this.

### Standard Indexes

A "standard" word index is one that simply doesn't have all the full text options enabled.  So instead of trying to clean, normalize, stem, filter and remove words for paragraph text, this instead indexes the *exact* word values provided.  It is designed to index one (or multiple) plain words, such as a "status", "flags" or "tags" database column.  Example:

```js
"fields": [
	{
		"id": "status",
		"source": "/TicketStatus"
	}
]
```

If you were designing a change control ticketing system, for example, then the `TicketStatus` property in your record data may contain something like `Open`, `Closed`, `Complete`, or `Canceled`.  This is a good candidate for a standard word index.

Multiple words will work fine as well.  Each word is indexed separately, so you can perform complex searches using one or more.  Just separate your words with any non-word character (comma, space, etc.).

#### Master List

If you want to be able to fetch all the unique words in an index, as well as their counts (number of records per word) you can use a "master list".  This feature is enabled by adding a `master_list` property to the definition, and setting it to `true`.  Example:

```js
"fields": [
	{
		"id": "status",
		"source": "/Status",
		"master_list": true
	}
]
```

Please note that this adds an extra storage operation per index per record, so do keep performance in mind.  This is only recommended for fields that have a relatively small amount of unique words, such as a "status" field.  This should **not** be used for full text search fields.  See [Field Summaries](#field-summaries) below for instructions on how to fetch the data.

### Full Text Indexes

A "full text" index is one that is designed to process multi-line or paragraph text.  Technically there is nothing you need to do to enable this, as all fields are word indexes, but there are several additional properties which are highly recommended if your source text is longer than a few single words.  Example:

```js
"fields": [
	{
		"id": "body",
		"source": "/BodyText",
		"min_word_length": 3,
		"max_word_length": 64,
		"max_words": 512,
		"use_remove_words": true,
		"use_stemmer": true,
		"filter": "html"
	}
]
```

All of these additional properties are designed to help the indexer be more efficient, skip over or otherwise reduce insignificant words.  They are all recommended settings, but you can customize them to your app's specific needs.

Setting a `min_word_length` will skip words that are under the specified number of characters, in this case all single and double character words (which are usually insignificant for searches).  Similarly, the `max_word_length` causes the indexer to skip any words over the specified length, in this case 64 characters (longer words probably won't be searched for).  Note that the same rules apply to search queries as well, so searches that contain skipped words along with real words will still work correctly.

The `max_words` property sets a maximum upper limit of words to be indexed per record for this field.  If the source input text exceeds this limit, the extra words are simply ignored by the indexer.

Setting `use_remove_words` allows the indexer to skip over common words that are typically insignificant for searches, like `the`, `of`, `and`, `that`, and so on.  The same words are removed from search queries, allowing them to work seamlessly.  See [Remove Words](#remove-words) below for more on this.

Setting `use_stemmer` instructs the indexer to reduce words to their common "[stems](https://en.wikipedia.org/wiki/Stemming)".  For example, `jumping` and `jumps` would both be reduced to `jump`.  Search queries get stemmed in the same way, so you can still search for `jumping` (or any variation) and find applicable records.  See [Stemming](#stemming) below for more on this.

#### Text Filters

Text filters provide a way to cleanup specific markup languages, leaving only searchable words in the text.  They are specified by including a `filter` property in your index definition, and setting it to one of the following strings:

| Filter | Description |
|--------|-------------|
| `html` | This filter strips all HTML tags, and decodes all HTML entities prior to indexing.  This also works for XML source. |
| `markdown` | This filter is designed for [Markdown](https://en.wikipedia.org/wiki/Markdown) source text.  It filters out [fenced code blocks](https://help.github.com/articles/creating-and-highlighting-code-blocks/) and also applies the `html` filter as well (you can embed HTML in markdown). |
| `alphanum` | This filter strips everything except for alphanumerics and underscores.  It's designed to reduce a string to a single indexable value. |

Note that URLs are always shortened so that only the hostname is indexed.  Full URLs are notoriously difficult (and rather useless) to index for searching.  See [Text Cleanup](#text-cleanup) below for details.

#### Remove Words

The remove word system allows you to specify a set of words to skip over when indexing.  This can be useful for things like common English words that have no real "search significance", like `the`, `it`, `them`, `that` and so on.  The words are removed from both indexing and search queries, so your users don't have to remember to omit certain words when searching.

For example, here are the 100 most common English words (sourced from this [top 1000 list](http://www.bckelk.ukfsn.org/words/uk1000n.html)), which are generally good candidates for removal:

```js
"remove_words": ["the", "of", "and", "a", "to", "in", "is", "you", "that", "it", "he", "was", "for", "on", "are", "as", "with", "his", "they", "I", "at", "be", "this", "have", "from", "or", "one", "had", "by", "word", "but", "not", "what", "all", "were", "we", "when", "your", "can", "said", "there", "use", "an", "each", "which", "she", "do", "how", "their", "if", "will", "up", "other", "about", "out", "many", "then", "them", "these", "so", "some", "her", "would", "make", "like", "him", "into", "time", "has", "look", "two", "more", "write", "go", "see", "number", "no", "way", "could", "people", "my", "than", "first", "water", "been", "call", "who", "oil", "its", "now", "find", "long", "down", "day", "did", "get", "come", "made", "may", "part"]
```

After defining the `remove_words` array once in the outer configuration object, your individual index definitions must specify that they want to use it.  This is done by setting a `use_remove_words` Boolean property in your full text fields.  Example:

```js
"fields": [
	{
		"id": "body",
		"source": "/BodyText",
		"use_remove_words": true
	}
]
```

### Custom Field Types

In addition to word indexing, you can also index numbers and dates.  These features are enabled by adding a `type` property to your index field definition, and setting it to either `number` or `date`.  Example:

```js
"fields": [
	{
		"id": "modified",
		"source": "/ModifyDate",
		"type": "date"
	}
]
```

#### Number Type

The number field type is enabled by setting the `type` property to `number`.  It is designed for "small integers" only.  Example:

```js
"fields": [
	{
		"id": "num_comments",
		"source": "/Comments/length",
		"type": "number"
	}
]
```

The number type is limited to integers, from -1,000,000 to 1,000,000.  Anything outside this range is clamped, and floating point decimals are rounded down to the nearest integer.

See [Searching Records](#searching-records) below for how to search on numbers and number ranges.

#### Date Type

The date field type is used to index dates.  The source input value can be any date format that Node.js supports, however the native word format is `YYYY_MM_DD`.  Example:

```js
"fields": [
	{
		"id": "modified",
		"source": "/ModifyDate",
		"type": "date"
	}
]
```

The date type is limited to dates only (i.e. time of day is not currently supported).  Also, if you specify any other input format besides `YYYY_MM_DD` then your source text is converted to `YYYY_MM_DD` using the server's local timezone.  Please keep this in mind when designing your app.

See [Searching Records](#searching-records) below for how to search on dates and date ranges.

## Indexing Records

To index a record, call the [indexRecord()](API.md#indexrecord) method, and pass in the following three arguments, plus an optional callback:

- A string ID for the record
	- Can contain any characters you want, but it must be valid and unique when [normalized](../README.md#key-normalization) as a storage key.
- An object containing the record to be indexed.
	- This may contain extraneous data, which is fine.  All it requires is that the data to be indexed is located at the expected [source paths](#source-paths).
- A configuration object describing all the fields and sorters to apply.
	- See [Configuration](#configuration) above.
- An optional callback.
	- Fired when the record is fully indexed and ready to search.
	- Passed an Error object, or something false on success.

Here is a simple example:

```js
// Index configuration
let config = {
	"base_path": "index/myapp",
	"fields": [
		{
			"id": "body",
			"source": "/BodyText",
			"min_word_length": 3,
			"max_word_length": 64,
			"max_words": 512,
			"use_remove_words": true,
			"use_stemmer": true,
			"filter": "html"
		},
		{
			"id": "modified",
			"source": "/ModifyDate",
			"type": "date"
		},
		{
			"id": "tags",
			"source": "/Tags",
			"master_list": true
		}
	],
	"remove_words": ["the", "of", "and", "a", "to", "in", "is", "you", "that", "it", "he", "was", "for", "on", "are", "as", "with", "his", "they"]
};

// Record object
let record = {
	"BodyText": "This is the body text of my ticket, which <b>may contain HTML</b> and \nmultiple\nlines.\n",
	"ModifyDate": "2018/01/07",
	"Tags": "bug, assigned, open"
};

// Index it!
storage.indexRecord( "TICKET0001", record, config, function(err) {
	// record is fully indexed
	if (err) throw err;
} );
```

This example would index three fields in our `TICKET0001` record:

- The `BodyText` property would be indexed as a full text string, using an [HTML pre-filter](#text-filters), 3/64 word length limits, [remove words](#remove-words) and [stemming](#stemming).
- The `ModifyDate` property would be indexed as a [date field](#date-type).
- The `Tags` property would be indexed as a simple word index, with a [master list](#master-list).

If you are performing an update to an existing record, you can provide a "sparse" data object.  Meaning, you can omit fields, and only include data sources for the fields you want to update.

### Source Paths

Source paths specify where in your record data to locate each value to be indexed.  They are formatted like filesystem paths (i.e. slash delimited), but refer to properties inside your record data.  For example:

```js
"fields": [
	{
		"id": "modified",
		"source": "/ModifyDate",
		"type": "date"
	}
]
```

Here the `source` property is set to `/ModifyDate`, which means that the indexer will look for the value in a property named `ModifyDate` at the top level of your record date.  The idea here is that your values may be nested several levels deep, or may even be something like an array length.  Consider this index configuration:

```js
"fields": [
	{
		"id": "num_comments",
		"source": "/Comments/length",
		"type": "number"
	}
]
```

Assuming your record data contained an array named `Comments`, this would index the *length* of that array into this number column.

You can also provide multiple sources of data to be indexed into a single source path.  To do this, wrap each source path in square brackets, and separate them by whitespace.  For example, consider a "combined" index containing both the record's title and body text:

```js
"fields": [
	{
		"id": "main_text",
		"source": "[/Title] [/BodyText]",
		"min_word_length": 3,
		"max_word_length": 64,
		"max_words": 512,
		"use_remove_words": true,
		"use_stemmer": true,
		"filter": "html"
	}
]
```

This would index both the `Title` and `BodyText` record data properties as one combined index with ID `main_text`.  Of course, you could just combine your own data strings and pass them into the indexer as one single property.  The source path system is just a convenience, so you can potentially pass in your original, unmodified record data object, and "point" the indexer at the right sub-elements for indexing.

### Text Cleanup

By default, all text goes through some basic cleanup prior to indexing.  This is to ensure better indexing quality, and to improve performance by skipping low-quality words.  The following input transformations are applied:

- Unicode characters are down-converted to ASCII equivalents, or stripped off.
	- See [Unicode Characters](#unicode-characters) below for details.
- URLs are stripped down to their hostnames only.
	- Word indexers do a very poor job of indexing URLs, and few people actually search for them.
	- URLs cause quite a bit of indexer churn, because they create a bunch of small "words" that are of low search quality.
- Single quotes are stripped off.
	- This way pluralized words are indexed as single words, e.g. `Nancy's` would be indexed as `Nancys`.
	- [Stemming](#stemming) also takes care of this by reducing even further.
- Floating-point numbers are converted to "words".
	- Underscores are considered word characters, so `2.5` is indexed as a single word: `2_5`.
	- This also handles version numbers like `2.5.1` (indexed as: `2_5_1`).
	- Note that this only applies to loose numbers found in text fields.  [Number](#number-type) fields are different, and currently accept only integers.

If you don't want this standard cleanup to take place, you can set the special `no_cleanup` property on your index definition.  But please only do this if you know exactly what you are doing.

### Boolean Values

While there is no native support for booleans, they are indexed as "words".  So if you have a data property that is a boolean, its value will be converted to a literal string (`true` or `false`) and that word is indexed just as if it was a string.  You can then search on it using `true` and `false` strings.

### Null Values

The indexer does **not** support null, undefined or empty values.  Meaning, no indexing takes place for these values, and thus you cannot search for "nothing".  If your app needs to handle this case, you simply need to come up with your own unique "null word", and pass that when you specifically want nothing indexed.  Consider using a string like `_NULL_` (underscores are word characters, so they get indexed as part of the word).

If your index field has a [master list](#master-list) and you query for a [field summary](#field-summaries), you will get back a `_null_` key with a record count, along with all your "actual" words in the index.  You can then massage this key in your UI, and show something like "(None)" instead.

### Default Values

You can optionally specify a "default value" for your indexes and sorters.  This is done by including an `default_value` property.  Records that are either completely missing a field value, or have it explicitly set to `null`, will be indexed as the default value.  Example configuration:

```js
"fields": [
	{
		"id": "status",
		"source": "/Status",
		"master_list": true,
		"default_value": "_none_"
	}
]
```

This would index all record statuses as `_none_` if the data field was missing (`undefined`) or explicitly set to `null`.  Combined with the [Master List](#master-list) feature, this allows you to count all your records that don't have a value for the field.

### Unicode Characters

The indexer only processes words that contain standard U.S. ASCII alphanumeric characters, e.g. A-Z, 0-9, and underscore.  All other characters are skipped, and serve as word separators.  International (Unicode) characters are converted to ASCII at index and search time, using the [unidecode](https://www.npmjs.com/package/unidecode) module.  This allows us to index words with accents and other symbols like this:

| Original | Indexed As |
|----------|------------|
| Café | `cafe` |
| El Niño | `el`, `nino` |
| Doppelgänger | `doppelganger` |

This also allows us to index words in non-European languages, because the amazing [unidecode](https://www.npmjs.com/package/unidecode) down-converts them to English / ASCII equivalents for us.  Examples:

| Original | Indexed As |
|----------|------------|
| 木 | `mu` |
| ネコ | `neko` |
| してく | `siteku` |

Note that this isn't a translation service, but more of a "*pronounced in English as*".  From the docs:

> The representation is almost always an attempt at transliteration -- i.e., conveying, in Roman letters, the pronunciation expressed by the text in some other writing system.

However, it serves the purpose of converting foreign words to ASCII phonetic equivalents, which are probably suitable for indexing in most cases.  The same conversion takes place behind the scenes on search queries, so you can actually search for international words as well.  Note that many of these conversions result in 2-letter "words", so make sure you set your `min_word_length` appropriately.

### Stemming

[Word Stemming](https://en.wikipedia.org/wiki/Stemming) is the process of removing common morphological and inflectional endings from words in English.  Basically, it normalizes or reduces words to their "stems", which involves stripping off pluralization and other extraneous characters from the end.  This improves searching, and reduces the number of unique words that the indexer is required to handle.  Stemming should really only be enabled on full-text indexes with English source text.

To enable stemming, set the `use_stemmer` property to `true` in your field definition.  It is disabled by default.  Example index configuration:

```js
"fields": [
	{
		"id": "body",
		"source": "/BodyText",
		"min_word_length": 3,
		"max_word_length": 64,
		"use_remove_words": true,
		"use_stemmer": true,
		"filter": "html"
	}
]
```

Here are a few example words and their stems:

| Original | Stemmed |
|----------|---------|
| jump | jump |
| jumps | jump |
| jumping | jump |
| jumped | jump |
| argue | argu |
| argued | argu |
| arguing | argu |
| argues | argu |
| argus | argu |
| argument | argument |
| arguments | argument |
| argumentative | argument |

Notice that in some cases it doesn't even produce a proper English word for the stem, e.g. `argu`.  Don't worry, this is normal -- remember that search queries are also stemmed, so you can search for any form of `argue` and still find the right records.  For this feature we lean on the wonderful [porter-stemmer](https://github.com/jedp/porter-stemmer) module, which uses [Martin Porter's stemmer algorithm](https://tartarus.org/martin/PorterStemmer/).

## Unindexing Records

To "unindex" a record (i.e. remove all indexed data for it), call the [unindexRecord()](API.md#unindexrecord) method and pass in the following two arguments, plus an optional callback.  You *do not* need to include the data record itself for unindexing.

- A string ID for the record
	- Needs to point to a valid record that was previously indexed.
	- The ID can contain any characters you want, but it must be valid and unique when [normalized](../README.md#key-normalization) as a storage key.
- A configuration object describing all the fields and sorters that were applied.
	- See [Configuration](#configuration) above.
- An optional callback.
	- Fired when the record is fully removed from the index.
	- Passed an Error object, or something false on success.

This effectively removes a record from the index, and leaves underlying storage as if the record was never indexed.  The only exception is when you are unindexing the *last* item in an index -- in that case, a few empty hashes and records are leftover (which are then reused if a new record is indexed again).

Remember that the indexer doesn't actually store your record data itself -- only index metadata.  If you want to also delete the record data, that is entirely up to your application.

Here is an example (see [Indexing Records](#indexing-records) above for details on the `config` object):

```js
storage.unindexRecord( "TICKET0001", config, function(err) {
	// record is completely removed from the index
	if (err) throw err;
} );
```

## Searching Records

To perform an index search, call the [searchRecords()](API.md#searchrecords) method and pass in a search query, your index configuration object, and a callback.  The search query can be in one of two different formats, which are both described below.  Your callback will be passed an Error object (or false on success), and a hash of all the matched record IDs.

Here is an example (see [Indexing Records](#indexing-records) above for details on the `config` object):

```js
storage.searchRecords( 'modified:2018/01/07 tags:bug', config, function(err, results) {
	// search complete
	if (err) throw err;
	
	// results will be hash of record IDs
	// { "TICKET0001": 1, "TICKET0002": 1 }
} );
```

This finds all records that were modified on Jan 7, 2018 **and** contain the tag `bug`.  This syntax is called a [simple query](#simple-queries), and is explained in detail below, along with the more complex [PxQL](#pxql-queries) syntax.

The search results are a hash of record IDs (just use the keys, ignore the values).  Note that the results are not sorted at this point.  If you need to sort them using an index sorter, you have to call [sortRecords()](API.md#sortrecords) as a secondary step.  See [Sorting Results](#sorting-results) below for details.

### Simple Queries

Simple queries are designed to be easy for users to type, but still provide adequate search functionality.  It is loosely based on some of the [GitHub Issue Search](https://help.github.com/articles/searching-issues-and-pull-requests/) syntax rules, essentially this part:

```
INDEX:WORDS [INDEX:WORDS ...]
```

Where `INDEX` is the ID of an index definition, and `WORDS` is one or more words to match in that index.  The pair can be repeated for multiple index searches (always in "AND" mode).  Here is a very simple query example:

```
status:open assigned:jhuckaby
```

This would find all records that contain the word `open` in their `status` index, **and** contain the word `jhuckaby` in their `assigned` index.  All words are matched case-insensitively, and follow all the index-specific rules like stemming, if enabled.

To specify multiple words for the same index and match any of them, use a pipe (`|`) delimiter, like this:

```
status:open assigned:jhuckaby|bsanders|hclinton
```

This would find all records that contain the word `open` in their `status` index, **and** contain any of the following words in their `assigned` index: `jhuckaby`, `bsanders` **or** `hclinton`.

Full-text fields have even more options.  For those, you can specify Google-style search queries, including negative word matches and exact (literal) matches for multi-word phrases.  Example:

```
body:wildlife +jungle "big cats" -bees
```

This would query the `body` index for all records that include the word `wildlife`, **and** the word `jungle` (the `+` prefix is redundant, but supported because it's Google-esque), **and** the phrase `big cats` (i.e. the word `cats` **must** appear just after the word `big`), but **not** any records that contain the word `bees`.

Note that negative word searches can only "take away" from a search result, so they must be accompanied by one or more normal (positive) word searches.

Dates must be specified in either `YYYY-MM-DD`, `MM-DD-YYYY` or Epoch (raw seconds) formats.  Slashes are also acceptable in addition to dashes.  Example:

```
status:open modified:2016-02-25
```

This would find all open records that were modified on February 25, 2016.

Both dates and numbers allow ranged searches.  Meaning, you can use  `>` (greater-than), `<` (less-than), `>=` (greater-or-equal) and `<=` (lesser-or-equal), as a prefix just before the date value.  Example:

```
status:open modified:>=2016-02-25
```

This would find all open records that were modified **on or after** February 25, 2016.

There is a shorthand available for closed range searches (i.e. records between two dates).  To use this, separate the two dates with two periods (`..`).  Both dates are inclusive.  Example:

```
status:open modified:2016-02-25..2016-12-31
```

This would find all open records that were modified **between** February 25, 2016 and December 31, 2016, inclusive.

Number indexes work in the same way as dates.  You can perform exact matches, and also range searches.  Example:

```
status:open num_comments:>=5
```

Simple queries were designed with user input in mind, like a Google search bar.  To that end, you can define a `default_search_field` property in your main index configuration, which designates one of your fields as the default to be used for searches if no field is specified.  For example, if you set the `default_search_field` to `body`, then you could accept queries like this:

```
wildlife +jungle "big cats" -bees
```

The idea here is, the user doesn't have to specify the `body:` prefix in their search.  They can just send in raw words, and `default_search_field` will detect this and redirect the query to the appropriate index.  This can, of course, be combined with other index searches with prefixes, such as:

```
wildlife +jungle "big cats" -bees status:open
```

### PxQL Queries

PxQL queries are more structured than simple ones, and allow for more complex logic and sub-queries in parenthesis.  It sort of resembles [SQL](https://en.wikipedia.org/wiki/SQL) syntax, but is much more rudimentary.  PxQL is identified by surrounding the entire query by parenthesis.  This style of query is geared more towards application usage, i.e. not raw user input.

The basic syntax is `(INDEX OPERATOR "VALUE")`, where `INDEX` is the ID of one of your indexed fields, `OPERATOR` is one of several operators (see below), and `"VALUE"` (always in quotes) is the word or words to match against.  Multiple expressions can be chained together with a logic separator `&` (AND) or `|` (OR).  Sub-queries should have nested inner parenthesis.

Here is a simple example:

```
(status = "open" & title = "Preproduction")
```

This would find all records that contain the word `open` in their `status` index, **and** contain the word `Preproduction` in their `title` index.  Note that the equals (`=`) operator really means "contains", as these are all word indexes.  For syntactic sugar, you can use `=~` instead of `=` which more resembles "contains".  To specify an exact phrase for a full-text index, simply include multiple words:

```
(status = "open" & title =~ "Released to Preproduction")
```

This would find all records that contain the word `open` in their `status` index, **and** contain the exact phrase `Released to Preproduction` in their `title` index.  This honors remove words and stemming if configured on the index, so queries do not need to be pre-filtered.

For negative word matches, use the `!~` operator, like this:

```
(status = "open" & title !~ "Released to Preproduction")
```

This would find all records that contain the word `open` in their `status` index, and **not** the exact phrase `Released to Preproduction` in their `title` index.

Here is a more complex example, with date ranges and nested sub-queries:

```
(modified >= "2016-02-22" & (title =~ "amazon" | title =~ "monitor") & (status = "open" | status = "closed" | status = "wallaby"))
```

This one makes more sense when formatted onto multiple lines (which is also acceptable PxQL):

```
(
	modified >= "2016-02-22" &
	(title =~ "amazon" | title =~ "monitor") & 
	(status = "open" | status = "closed" | status = "wallaby")
)
```

So here we have an outer group of three expressions matched with AND, and two sub-queries that use OR.  This would match all records that were modified on or after February 22, 2016, **and** the `title` contained *either* `amazon` or `monitor`, **and*** the `status` contained one of: `open`, `closed` or `wallaby`.  Basically, this is an outer group of "AND" matches, with inner "OR" matches, denoted with nested parenthesis.

In the example above, you can see that we're using `=` for searching the `status` index, but then `=~` for the `title` index.  This is entirely just syntactic sugar.  Both operators are functionally identical, and both mean "contains".  Double-equals (`==`) works too.

Here is the complete list of supported operators and their meanings:

| Operator | Description |
|----------|-------------|
| `=` | Contains |
| `==` | Contains |
| `=~` | Contains |
| `!~` | Does NOT contain |
| `>` | Greater than (dates and numbers only) |
| `<` | Less than (dates and numbers only) |
| `>=` | Greater or equal (dates and numbers only) |
| `<=` | Lesser or equal (dates and numbers only) |

The supported logic separators are `&` (AND) and `|` (OR).  You can substitute `&&` or `||` respectively.

### Fetching All Records

To fetch *all* records without using an index, use the special search query `*` (asterisk).  This is faster than performing an index search, as this simply fetches all the record keys from an internal master ID hash.  Example use:

```js
storage.searchRecords( '*', config, function(err, results) {
	// search complete
	if (err) throw err;
	
	// results will be hash of record IDs
	// { "TICKET0001": 1, "TICKET0002": 1 }
} );
```

## Sorting Results

Sorting your results is an optional, secondary operation, applied after searching is complete.  To do this, you first need to define special "sorter" definitions in your main configuration.  These tell the indexer which fields you will need to sort by.  Example:

```js
"sorters": [
	{
		"id": "username",
		"source": "/User",
		"type": "string"
	},
	{
		"id": "num_comments",
		"source": "/Comments/length",
		"type": "number"
	}
]
```

This would allow you to sort your records by the `User` property alphanumerically, and by the number of comments.  The latter assumes your data records have an array of comments in a `Comments` property, and this indexes the `length` of that array as a number sorter.

For sorting dates, you have two options.  Either provide the date as an Epoch timestamp and use a `number` sorter type, or provide it as an alphanumerically sortable date, like `YYYY-MM-DD` and use a `string` type.

To actually perform the sort, call the [sortRecords()](API.md#sortrecords) method, and provide the following 5 arguments:

- An unsorted hash of record IDs, as returned from [searchRecords()](API.md#searchrecords).
- The ID of the sorter field, e.g. `username`, `num_comments`.
- The sort direction, which should be `1` for ascending, or `-1` for descending (defaults to `1`).
- Your main index configuration object, containing the `sorter` array.
- A callback to receive the final sorted IDs.

Here is an example search and sort:

```js
storage.searchRecords( 'modified:2018/01/07 tags:bug', config, function(err, results) {
	// search complete
	if (err) throw err;
	
	// now sort the results by username ascending
	storage.sortRecords( results, 'username', 1, config, function(err, sorted) {
		// sort complete
		if (err) throw err;
		
		// sorted IDs will be in array
		// [ "TICKET0001", "TICKET0002", "TICKET0003" ]
	} ); // sortRecords
} ); // searchRecords
```

Given an array of your sorted record IDs, you can then implement your own pagination system (i.e. limit & offset), and load multiple records at at time via [getMulti()](API.md#getmulti) or other.

## Field Summaries

If you have any fields indexed with the [master list](#master-list) feature enabled, you can fetch a "summary" of the data values using the [getFieldSummary()](API.md#getfieldsummary) method.  This returns a hash containing all the unique words from the index, and their total counts (occurrences) in the data.  Example use:

```js
storage.getFieldSummary( 'status', config, function(err, values) {
	if (err) throw err;
	
	// values will contain a hash with word counts:
	// { "new": 4, "open": 45, "closed": 16, "assigned": 3 }
} );
```

Summaries work best for fields that contain a relatively small amount of unique words, such as a "status" field.  If the field contains more than 1,000 unique words or so, things might slow down, as the summary data has to be updated for every record.

## Bulk Reindexing

If you want to make changes to your index configuration, i.e. add or remove fields, then you will have to bulk reindex the data.  To do this, you need to [fetch all the record IDs](#fetching-all-records), and then iterate over them and issue the correct commands.  See below for specific examples, which all make use of the [async](https://www.npmjs.com/package/async) module for asynchronous array iteration.

### Adding Fields

To add a new field to your index, you simply have to apply the change to your index configuration, then call [indexRecord()](API.md#indexrecord) on all your records again.  The indexer is smart enough to know that all your existing field values haven't changed, but you have added a new one which needs to be indexed.  Example:

```js
const async = require('async');

// fetch all record ids
storage.searchRecords( '*', config, function(err, results) {
	if (err) throw err;
	
	// iterate over records
	async.eachSeries( Object.keys(results),
		function(id, callback) {
			// fetch record data from storage (your own path)
			storage.get( 'my/app/records/' + id, function(err, record) {
				if (err) return callback(err);
				
				// and reindex it
				storage.indexRecord( id, record, config, callback );
			} );
		},
		function(err) {
			// reindex complete
			if (err) throw err;
		}
	); // eachSeries
} ); // searchRecords
```

### Deleting Fields

To delete a field, the process is similar to adding one.  You will have to iterate over all your records, and call [indexRecord()](API.md#indexrecord) on each one, except this time we'll add a special `delete` property to the index you want to delete.  This tells the library to force a delete on reindex.  Here is an example:

```js
const async = require('async');

// mark the field you want to delete with a `delete` property
config.fields[2].delete = true;

// fetch all record ids
storage.searchRecords( '*', config, function(err, results) {
	if (err) throw err;
	
	// iterate over records
	async.eachSeries( Object.keys(results),
		function(id, callback) {
			// fetch record data from storage (your own path)
			storage.get( 'my/app/records/' + id, function(err, record) {
				if (err) return callback(err);
				
				// and reindex it
				storage.indexRecord( id, record, config, callback );
			} );
		},
		function(err) {
			// reindex complete
			if (err) throw err;
		}
	); // eachSeries
} ); // searchRecords
```

Once this reindex is complete, you can completely remove the index array entry from your configuration.

### Changing Fields

To change the settings for an index field, you must first unindex (delete) it, then reindex it.  This can be done by running the steps outlined in [Deleting Fields](#deleting-fields), followed by [Adding Fields](#adding-fields), in that order.

Make sure you leave the index field settings set to their old values when you add the `delete` property.  Then run through all records to unindex the field, remove the `delete` property, make your changes, and then reindex all records with the new settings.

## Performance Tips

- Use the local filesystem engine only, preferably a fast SSD.
- Crank up your [concurrency](../README.md#concurrency) setting to 4 or higher.
- Only index the fields you really need to search on.
- Only add sorters on the fields you really need to sort by.
- Make use of [Remove Words](#remove-words) and `min_word_length` for your full text fields.
- Make use of the [Stemmer](#stemming) for your full text fields.
- Only enable `master_list` on fields with a small number of unique words.
- Sorting is slow, consider using alphabetically sortable IDs, and sorting the records that way.
- Searching by date range and number range can be very slow.

## Indexer Internals

Indexes are essentially built on top of [Hashes](Hashes.md).  Each field value is distilled down to a list of words (possibly utilizing [remove words](#remove-words) and [stemming](#stemming)), and each unique word becomes a hash.  The hash keys are your record IDs, and the hash values are the locations within the record's word list where the word appears.  The latter is important for performing exact phrase searches.  Each search iterates over the appropriate hashes and combines all the matching record IDs.

A basic record indexed with the sample configuration detailed back in the [Indexing Records](#indexing-records) section looks like the following.  Note that this was created using a [raw filesystem](../README.md#raw-file-paths):

```
index/
 └ myapp/
    ├ _data/
    │  └ ticket0001.json
    ├ _id/
    │  └ data.json
    ├ _id.json
    ├ body/
    │  └ word/
    │     ├ bodi/
    │     │  └ data.json
    │     ├ bodi.json
    │     ├ contain/
    │     │  └ data.json
    │     ├ contain.json
    │     ├ html/
    │     │  └ data.json
    │     ├ html.json
    │     ├ line/
    │     │  └ data.json
    │     ├ line.json
    │     ├ mai/
    │     │  └ data.json
    │     ├ mai.json
    │     ├ multipl/
    │     │  └ data.json
    │     ├ multipl.json
    │     ├ nice/
    │     │  └ data.json
    │     ├ nice.json
    │     ├ text/
    │     │  └ data.json
    │     ├ text.json
    │     ├ thi/
    │     │  └ data.json
    │     ├ thi.json
    │     ├ ticket/
    │     │  └ data.json
    │     ├ ticket.json
    │     ├ which/
    │     │  └ data.json
    │     └ which.json
    ├ modified/
    │  ├ summary.json
    │  └ word/
    │     ├ 2018/
    │     │  └ data.json
    │     ├ 2018.json
    │     ├ 2018_01/
    │     │  └ data.json
    │     ├ 2018_01.json
    │     ├ 2018_01_07/
    │     │  └ data.json
    │     └ 2018_01_07.json
    └ tags/
       ├ summary.json
       └ word/
          ├ assigned/
          │  └ data.json
          ├ assigned.json
          ├ bug/
          │  └ data.json
          ├ bug.json
          ├ open/
          │  └ data.json
          └ open.json
```

The first thing to notice is that everything is under a base path of `index/myapp/...`.  This reflects the `base_path` property in your main configuration object.

So in our example configuration, we have three indexed fields: `body`, `modified` and `tags`.  As you can see in the data layout, each one occupies its own "namespace" in storage, and contains hashes for each unique value, and in some cases a [summary](#master-list) record as well.  For reference, here was our sample record ("TICKET0001") was was used to populate the indexes:

```js
let record = {
	"BodyText": "This is the body text of my ticket, which <b>may contain HTML</b> and \nmultiple\nlines.\n",
	"ModifyDate": "2018/01/07",
	"Tags": "bug, assigned, open"
};
```

Let's take a closer look at the `tags` index storage layout:

```
index/
 └ myapp/
    └ tags/
       ├ summary.json
       └ word/
          ├ assigned/
          │  └ data.json
          ├ assigned.json
          ├ bug/
          │  └ data.json
          ├ bug.json
          ├ open/
          │  └ data.json
          └ open.json
```

Our sample record had three tags, `bug`, `assigned`, and `open`.  You can see that we have a hash for each unique word.  If you were to grab all the hash contents of the `index/myapp/tags/word/open` hash, you'd get this:

```js
{
	"TICKET0001": "3"
}
```

The value `3` means that the `open` tag was the 3rd word in the list for record `TICKET0001`.  This word placement ranking only comes into play with full-text fields, and when you are performing an exact phrase query (where one word must come right after another).

The `tags` field also has the [master_list](#master-list) property set, so a special `index/myapp/tags/summary` record was created.  This contains all the unique words for the index, and the occurrence counts of each.  Example:

```js
{
	"bug": 1,
	"assigned": 1,
	"open": 1
}
```

### Date and Number Fields

Date and number fields are still technically indexed as "words", but some internal trickery is applied to allow for range searches.  Essentially numbers and dates are placed into several range buckets.  Along with a [Master List](#master-list) which is automatically enabled for these fields, the system can search across a range of values.

For example, let's look at the `modified` field from our record:

```
index/
 └ myapp/
    └ modified/
       ├ summary.json
       └ word/
          ├ 2018/
          │  └ data.json
          ├ 2018.json
          ├ 2018_01/
          │  └ data.json
          ├ 2018_01.json
          ├ 2018_01_07/
          │  └ data.json
          └ 2018_01_07.json
```

Our record had a single date (2018/01/07) as the value for the `modified` field, but as you can see here, three separate words were actually indexed: `2018`, `2018_01` and `2018_01_07`.  These are the "buckets" used for date range searches.  So in addition to the exact date, all the records modified in the year 2018 will have the `2018` word indexed, and all the records modified in January 2018 will have the `2018_01` word indexed.  In this way the search engine can limit the values it needs to search for ranges.

Numbers are handled in very much the same way, by splitting up the value into buckets.  Specifically, the number is divided into 1000s and 100s (thousands and hundreds) and bucket words are created for each one.

Both dates and numbers automatically enable the [Master List](#master-list), so a `summary` record is always created for these field types.

### Special Metadata

In addition to all your named fields, the system also stores a number of metadata records, for internal bookkeeping.  There's the `_data` namespace, and the `_id` hash.  As a result, you cannot have any fields named `_data` or `_id`, to prevent collisions.  Example storage layout:

```
index/
 └ myapp/
    ├ _data/
    │  └ ticket0001.json
    ├ _id/
    │  └ data.json
    └ _id.json
```

The `_data/` namespace has a single record for each of your records, named using your normalized record ID (e.g. `_data/ticket0001`), which is used to hold a copy of all the internal data that the indexer used to index the record.  This is used when comparing indexes on update, to see what changed.  Example record:

```js
{
	"body": {
		"words": ["thi", "bodi", "text", "ticket", "which", "mai", "contain", "html", "multipl", "line"],
		"checksum": "c4bcffe1726097581e4fb9ca87de3254"
	},
	"modified": {
		"words": ["2018_01_07", "2018_01", "2018"],
		"checksum": "46d43ab288b06fe7bdbc67daafc6e06b"
	},
	"tags": {
		"words": ["bug", "assigned", "open"],
		"checksum": "819fb23452936cc03cafbf29f30b5935"
	}
}
```

The `_id` hash simply stores every unique record ID.  This is used solely for the purpose of bookkeeping, and also to iterate over all records, i.e. when the wildcard (`*`) search query comes in.
```

## File: `docs/Lists.md`
```markdown
# Lists

A list is a collection of JSON records which can grow or shrink at either end, and supports fast random access.  It's basically a double-ended linked list, but implemented internally using "pages" of N records per page, and each page can be randomly accessed.  This allows for great speed with pushing, popping, shifting, unshifting, and random access, with a list of virtually any size.  Methods are also provided for iterating, searching and splicing, but those often involve reading / writing many pages, so use with caution.

All list operations will automatically lock the list using [Advisory Locking](../README.md#advisory-locking) (shared locks or exclusive locks, depending on if the operation is read or write), and unlock it when complete.  This is because all list operations involve multiple concurrent low-level storage calls.  Lists can be used inside [Transactions](Transactions.md) as well.

The code examples all assume you have your preloaded `Storage` component instance in a local variable named `storage`.  The component instance can be retrieved from a running server like this:

```js
let storage = server.Storage;
```

## Table of Contents

> &larr; [Return to the main document](https://github.com/jhuckaby/pixl-server-storage/blob/master/README.md)

<!-- toc -->
- [List Page Size](#list-page-size)
- [Creating Lists](#creating-lists)
- [Pushing, Popping, Shifting, Unshifting List Items](#pushing-popping-shifting-unshifting-list-items)
- [Fetching List Items](#fetching-list-items)
- [Splicing Lists](#splicing-lists)
- [Sorted Lists](#sorted-lists)
- [Iterating Over List Items](#iterating-over-list-items)
- [Updating List Items](#updating-list-items)
- [Searching Lists](#searching-lists)
- [Copying and Renaming](#copying-and-renaming)
- [Deleting Lists](#deleting-lists)
- [List Internals](#list-internals)

## List Page Size

List items are stored in groups called "pages", and each page can hold up to N items (the default is 50).  The idea is, when you want to store or fetch multiple items at once, the storage engine only has to read / write a small amount of records.  The downside is, fetching or storing a single item requires the whole page to be loaded and saved, so it is definitely optimized for batch operations.

You can configure how many items are allowed in each page, by changing the default [page size](../README.md#list_page_size) in your storage configuration, or setting it per list by passing an option to [listCreate()](API.md#listcreate).

Care should be taken when calculating your list page sizes.  It all depends on how large your items will be, and how many you will be storing / fetching at once.  Note that you cannot easily change the list page size on a populated list (this may be added as a future feature).

## Creating Lists

To create a list, call [listCreate()](API.md#listcreate).  Specify the desired key, options, and a callback function.  You can optionally pass in a custom page size via the second argument (otherwise it'll use the default size):

```js
storage.listCreate( 'list1', { page_size: 100 }, function(err) {
	if (err) throw err;
} );
```

You can also store your own key/value pairs in the options object, which are retrievable via the [listGetInfo()](API.md#listgetinfo) method.  However, beware of name collision -- better to prefix your own option keys with something unique.

## Pushing, Popping, Shifting, Unshifting List Items

Lists can be treated as arrays to a certain extent.  Methods are provided to [push](API.md#listpush), [pop](API.md#listpop), [shift](API.md#listshift) and [unshift](API.md#listunshift) items, similar to standard array methods.  These are all extremely fast operations, even with huge lists, as they only read/write the pages that are necessary.  Note that all list items must be objects (they cannot be other JavaScript primitives).

Examples:

```js
// push onto the end
storage.listPush( 'list1', { username: 'tsmith', age: 25 }, function(err) {
	if (err) throw err;
} );

// pop off the end
storage.listPop( 'list1', function(err, item) {
	if (err) throw err;
} );

// shift off the beginning
storage.listShift( 'list1', function(err, item) {
	if (err) throw err;
} );

// unshift onto the beginning
storage.listUnshift( 'list1', { username: 'fwilson', age: 40 }, function(err) {
	if (err) throw err;
} );
```

Furthermore, the [listPush()](API.md#listpush) and [listUnshift()](API.md#listunshift) methods also accept multiple items by passing an array of objects, so you can add in bulk.

## Fetching List Items

Items can be fetched from lists by calling [listGet()](API.md#listget), and specifying an index offset starting from zero.  You can fetch any number of items at a time, and the storage engine will figure out which pages need to be loaded.  To fetch items from the end of a list, use a negative index.  Example use:

```js
storage.listGet( 'list1', 40, 5, function(err, items) {
	if (err) throw err;
} );
```

This would fetch 5 items starting at item index 40 (zero-based).  To fetch the entire list, set the index and length to zero:

```js
storage.listGet( 'list1', 0, 0, function(err, items) {
	if (err) throw err;
} );
```

## Splicing Lists

You can "splice" a list just like you would an array.  That is, cut a chunk out of a list at any location, and optionally replace it with a new chunk, similar to the built-in JavaScript [Array.splice()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice) function.  [listSplice()](API.md#listsplice) is a highly optimized method which only reads/writes the pages it needs, but note that if the list length changes as a result of your splice (i.e. you insert more or less than you remove) it does have to rewrite multiple pages up to the nearest end page, to take up the slack or add new pages.  So please use with caution on large lists.

Here is an example which removes 2 items at index 40, and replaces with 2 new items:

```js
let new_items = [
	{ username: 'jhuckaby', age: 38, gender: 'male' },
	{ username: 'sfields', age: 34, gender: 'female' }
];
storage.listSplice( 'list1', 40, 2, new_items, function(err, items) {
	if (err) throw err;
	// 'items' will contain the 5 removed items
} );
```

You don't have to insert the same number of items that you remove.  You can actually remove zero items, and only insert new ones at the specified location.

As with [listGet()](API.md#listget) you can specify a negative index number to target items from the end of the list, as opposed to the beginning.

## Sorted Lists

While it is possible to manually sort your list by fetching all the items as an array, sorting it in memory, then rewriting the entire list, this can be quite time consuming.  Instead, you can perform a [listInsertSorted()](API.md#listinsertsorted) when adding items to a list.  This will find the correct location for a single item based on sorting criteria, and then splice it into place, keeping the list sorted as you go.  Example:

```js
let new_user = {
	username: 'jhuckaby', 
	age: 38, 
	gender: 'male' 
};

storage.listInsertSorted( 'users', new_user, ['username', 1], function(err) {
	if (err) throw err;
	// item inserted successfully
} );
```

That third argument is an array of sort criteria, consisting of the property name to sort by (e.g. `username`) and a sort direction (`1` for ascending, `-1` for descending).  You can alternately specify a comparator function here, which is called with the item you are inserting, and the item to compare it to.  This is similar to the built-in [Array.sort()](), which should return `1` or `-1` depending on if your item should come after, or before, the second item.  Example:

```js
let new_user = {
	username: 'jhuckaby', 
	age: 38, 
	gender: 'male' 
};

let comparator = function(a, b) {
	return( (a.username < b.username) ? -1 : 1 );
};

storage.listInsertSorted( 'users', new_user, comparator, function(err) {
	if (err) throw err;
	// item inserted successfully
} );
```

For large lists, this can still take considerable time, as it is iterating over the list to locate the correct location, and then performing a splice which grows the list, requiring all the remaining pages to be rewritten.  So please use with caution.

## Iterating Over List Items

Need to iterate over the items in your list, but don't want to load the entire thing into memory?  Use the [listEach()](API.md#listeach) method.  Example:

```js
storage.listEach( 'list1', function(item, idx, callback) {
	// do something with item, then fire callback
	callback();
}, 
function(err) {
	if (err) throw err;
	// all items iterated over
} );
```

Your iterator function is passed the item and a special callback function, which must be called when you are done with the current item.  Pass it an error if you want to prematurely abort the loop, and jump to the final callback (the error will be passed through to it).  Otherwise, pass nothing to the iterator callback, to notify all is well and you want the next item in the list.

Alternatively, you can use [listEachPage()](API.md#listeachpage), which iterates over the internal list [pages](#list-page-size), and only fires your iterator function once per page, instead of once per item.  This is typically faster as it requires fewer function calls.  Example:

```js
storage.listEachPage( 'list1', function(items, callback) {
	// do something with items, then fire callback
	callback();
}, 
function(err) {
	if (err) throw err;
	// all items iterated over
} );
```

## Updating List Items

To iterate over and possibly update items, you can use the [listEachUpdate()](API.md#listeachupdate) method.  Your iterator callback accepts a second boolean argument which can indicate that you made changes.  Example:

```js
storage.listEachUpdate( 'list1', function(item, idx, callback) {
	// do something with item, then fire callback
	item.something = "something new!";
	callback(null, true);
}, 
function(err) {
	if (err) throw err;
	// all items iterated over
} );
```

As you can see, the iterator callback accepts two arguments, an error (or something false for success), and a boolean which should be set to `true` if you made changes.  The storage engine uses this to decide which list pages require updating.

For a speed optimization, you can optionally iterate over entire list [pages](#list-page-size) rather than individual items.  To do this, use the [listEachPageUpdate()](API.md#listeachpageupdate) method.  In this case your iterator callback is passed an array of items on each page.  Example:

```js
storage.listEachPageUpdate( 'list1', function(items, callback) {
	// do something with items, then fire callback
	items.forEach( function(item) {
		item.something = "something new!";
	} );
	callback(null, true);
}, 
function(err) {
	if (err) throw err;
	// all items iterated over
} );
```

## Searching Lists

Several methods are provided for searching through lists for items matching a set of criteria.  Use [listFind()](API.md#listfind) to find and retrieve a single item, [listFindCut()](API.md#listfindcut) to find and delete, [listFindReplace()](API.md#listfindreplace) to find and replace, [listFindUpdate()](API.md#listfindupdate) to find and apply updates, or [listFindEach()](API.md#listfindeach) to find multiple items and iterate over them.

All of these methods accept a "criteria" object, which may have one or more key/value pairs.  These must *all* match a list item for it to be selected.  For example, if you have a list of users, and you want to find a male with blue eyes, you would pass a criteria object similar to this:

```js
{
	gender: "male",
	eyes: "blue"
}
```

Alternatively, you can use regular expression objects for the criteria values, for more complex matching.  Example:

```js
{
	gender: /^MALE$/i,
	eyes: /blu/
}
```

Example of finding a single object with [listFind()](API.md#listfind):

```js
storage.listFind( 'list1', { username: 'jhuckaby' }, function(err, item, idx) {
	if (err) throw err;
} );
```

Example of finding and deleting a single object with [listFindCut()](API.md#listfindcut):

```js
storage.listFindCut( 'list1', { username: 'jhuckaby' }, function(err, item) {
	if (err) throw err;
} );
```

Example of finding and replacing a single object with [listFindReplace()](API.md#listfindreplace):

```js
let criteria = { username: 'jhuckaby' };
let new_item = { username: 'huckabyj', foo: 'bar' };

storage.listFindReplace( 'list1', criteria, new_item, function(err) {
	if (err) throw err;
} );
```

Example of finding and updating a single object with [listFindUpdate()](API.md#listfindupdate):

```js
let criteria = { username: 'jhuckaby' };
let updates = { gender: 'male', age: 38 };

storage.listFindUpdate( 'list1', criteria, updates, function(err, item) {
	if (err) throw err;
} );
```

You can also increment or decrement numerical properties with [listFindUpdate()](API.md#listfindupdate).  If an item key exists and is a number, you can set any update key to a string prefixed with `+` (increment) or `-` (decrement), followed by the delta number (int or float), e.g. `+1`.  So for example, imagine a list of users, and an item property such as `number_of_logins`.  When a user logs in again, you could increment this counter like this:

```js
let criteria = { username: 'jhuckaby' };
let updates = { number_of_logins: "+1" };

storage.listFindUpdate( 'list1', criteria, updates, function(err, item) {
	if (err) throw err;
} );
```

And finally, here is an example of finding *all* items that match our criteria using [listFindEach()](API.md#listfindeach), and iterating over them:

```js
storage.listFindEach( 'list1', { gender: 'male' }, function(item, idx, callback) {
	// do something with item, then fire callback
	callback();
}, 
function(err) {
	if (err) throw err;
	// all matched items iterated over
} );
```

## Copying and Renaming

To duplicate a list and all of its items, call [listCopy()](API.md#listcopy), specifying the old and new key.  Example:

```js
storage.listCopy( 'list1', 'list2', function(err) {
	if (err) throw err;
} );
```

To rename a list, call [listRename()](API.md#listrename).  This is basically just a [listCopy()](API.md#listcopy) followed by a [listDelete()](API.md#listdelete).  Example:

```js
storage.listRename( 'list1', 'list2', function(err) {
	if (err) throw err;
} );
```

With both of these functions, it is highly recommended you make sure the destination (target) key is empty before copying or renaming onto it.  If a list already exists at the destination key, it will be overwritten, but if the new list has differently numbered pages, some of the old list pages may still exist and occupy space, detached from their old parent list.  So it is always safest to delete first.

## Deleting Lists

To delete a list and all of its items, call [listDelete()](API.md#listdelete).  The second argument should be a boolean set to `true` if you want the list *entirely* deleted including the header (options, page size, etc.), or `false` if you only want the list *cleared* (delete the items only, leaving an empty list behind).  Example:

```js
storage.listDelete( 'list1', true, function(err) {
	if (err) throw err;
	// list is entirely deleted
} );
```

## List Internals

Lists consist of a header record, plus additional records for each page.  The header is literally just a simple JSON record, stored at the exact key specified for the list.  So if you created an empty list with key `mylist`, and then you fetched the `mylist` record using a simple [get()](API.md#get), you'd see this:

```js
{
	type: 'list',
	length: 0,
	page_size: 50,
	first_page: 0,
	last_page: 0
}
```

This is the list header record, which defines the list and its pages.  Here are descriptions of the header properties:

| Property | Description |
|----------|-------------|
| `type` | A static identifier, which will always be set to `list`. |
| `length` | How many items are currently in the list. |
| `page_size` | How many items are stored per page. |
| `first_page` | The page number of the beginning of the list, zero-based. |
| `last_page` | The page number of the end of the list, zero-based. |

The list pages are stored as records "under" the main key, by adding a slash, followed by the page number.  So if you pushed one item onto the list, the updated header record would look like this:

```js
{
	type: 'list',
	length: 1,
	page_size: 50,
	first_page: 0,
	last_page: 0
}
```

Notice that the `first_page` and `last_page` are both still set to `0`, even though we added an item to the list.  That's because pages are zero-based, and the algorithm will fill up page `0` (`50` items in this case) before adding a new page.

So then if you then fetched the key `mylist/0` you'd actually get the raw page data, which is a JSON record with an `items` array:

```js
{
	items: [
		{ username: "jhuckaby", gender: "male" }
	]
}
```

This array will keep growing as you add more items.  Once it reaches 50, however, the next item pushed will go into a new page, with key `mylist/1`.  That's basically how the paging system works.

Remember that lists can grow from either end, so if the first page is filled and you *unshift* another item, it actually adds page `mylist/-1`.

The two "end pages" can have a variable amount of items, up to the `page_size` limit.  The algorithm then creates new pages as needed.  But the *inner* pages that exist between the first and last pages will *always* have the full amount of items (i.e. `page_size`).  Never more, never less.  So as future list operations are executed, the system will always maintain this rule.
```

## File: `docs/Transactions.md`
```markdown
# Transactions

A transaction is an isolated compound operation with atomic commit and rollback.  Using transactions you can execute a series of operations without affecting other views of the database until you commit, and then it all happens at once.  Commits are an "all or nothing" affair, providing atomicity.  They also provide a safe way to automatically rollback to a known good state in case of an error or crash.

The transaction system works with any storage engine, but it is optimized for the local filesystem.

The code examples all assume you have your preloaded `Storage` component instance in a local variable named `storage`.  The component instance can be retrieved from a running server like this:

```js
let storage = server.Storage;
```

## Table of Contents

> &larr; [Return to the main document](https://github.com/jhuckaby/pixl-server-storage/blob/master/README.md)

<!-- toc -->
- [Caveats](#caveats)
- [Configuration](#configuration)
- [Basic Use](#basic-use)
- [Aborting](#aborting)
- [Automatic API Wrappers](#automatic-api-wrappers)
- [Emergency Shutdown](#emergency-shutdown)
- [Recovery](#recovery)
- [Transaction Internals](#transaction-internals)
	* [Temporary Directory](#temporary-directory)
	* [Branch Process](#branch-process)
	* [Commit Process](#commit-process)
	* [Rollback Process](#rollback-process)

## Caveats

Transaction locking is advisory.  Meaning, transactions will all play nice with each other, ensuring isolation and atomicity, but you can "get around it" simply by calling one of the low-level write methods like [put()](API.md#put) on a storage path that intersects with a transaction in progress.  This would likely cause some undesired effects, especially if a commit or rollback is in the middle of executing.  In short, the system is designed with the assumption that your application will designate certain storage paths that will only be mutated using transactions.

The transaction system is designed for JSON records only.  Binary records are not included as part of a transaction, and operations are silently passed straight through.  Meaning, any calls accessing binary records inside of a transaction will result in the original record being changed.  This behavior may be changed in a future version.

Please note that transactions aren't 100% [ACID compliant](https://en.wikipedia.org/wiki/ACID), but they do follow *most* of the rules.  When using the local filesystem engine, the real question is durability, as in what happens in the event of a sudden power loss.  When a transaction is committed, by design it could involve changing a huge amount of files.  While this operation is "effectively atomic" by way of advisory locking, the filesystem may still end up in an unknown state after sudden reboot, for example in the middle of a very large commit.  Now, the system does have automatic recovery using a rollback log, and *should* be able to restore the filesystem to the state right before the commit.  But really, when we're talking about yanking power cords, lightning strikes and brown-outs, who the hell knows.  The rollback log may be incomplete or corrupted (yes, we call [fsync](https://nodejs.org/api/fs.html#fsfsyncfd-callback) on it before ever starting the commit, but even then, things can happen -- fsync isn't a 100% guarantee, especially with SSDs).

I guess the bottom line is, always keep backups of your data!

## Configuration

The transaction system is configured by a few additional properties in the `Storage` object of your main application configuration file.  At a minimum, just set the `transactions` property to `true`, which will enable transaction support.  However, there are some other optional properties you can set as well.  Here is the full list:

| Property Name | Type | Description |
|---------------|------|-------------|
| `transactions` | Boolean | Set to `true` to enable transactions (defaults to `false`). |
| `trans_dir` | String | Path to temporary directory on local disk to store transactions in progress (see below). |
| `trans_auto_recover` | Boolean | Automatically recover from fatal errors on startup (see [Recovery](#recovery) below). |

Choose your `trans_dir` carefully.  This directory is used to store temporary files during a transaction.  The optimum value depends on the storage engine, and also possibly the underlying filesystem type:

| Storage Engine | Recommendation |
|----------------|----------------|
| Local Filesystem | Make sure your `trans_dir` is on the *same mount* as your local storage data, to ensure speed and safety.  This is the default. |
| NFS Filesystem | Make sure your `trans_dir` is **NOT** on the NFS mount, but instead points to a local fast SSD mount. |
| S3 | Make sure your `trans_dir` points to a local fast SSD mount. |

So basically, if you plan to use the [Filesystem](../README.md#local-filesystem) engine with a local (i.e. non-network) disk, you don't need to make any adjustments.  The default setting for `trans_dir` is a subdirectory just inside your `base_dir` engine property.  But if you are going with a networked (i.e. NFS) filesystem, or you're going to use [S3](../README.md#amazon-s3), then you should set `trans_dir` to a local filesystem path on a fast disk (ideally SSD).

**Pro-Tip:** When using transactions with the Amazon S3 engine, consider setting the `maxAttempts` property in your `S3` configuration object, so the AWS client library makes multiple attempts before failing an operation.  Network hiccups can happen.

## Basic Use

You start a transaction by calling [begin()](API.md#begin).  This asynchronous method returns a special transaction object, which presents a "branch" or "view" of the database.  It is a proxy object upon which you can call any standard storage API methods, e.g. [put()](API.md#put), [get()](API.md#get), [delete()](API.md#delete) or other.  Any operations on the transaction object take place in complete isolation, separate from the main storage object.  When you're ready, call [commit()](API.md#commit) to complete the transaction, which applies all the changes to main storage.

Here is a very basic example:

```js
storage.begin( 'some_path', function(err, trans) {
	
	// perform actions using `trans` proxy
	// e.g. trans.put(), trans.get(), trans.delete()
	
	// commit transaction
	trans.commit( function(err) {
		// complete
	} );
});
```

The [begin()](API.md#begin) method accepts an arbitrary base storage path, which is used to obtain an exclusive lock.  This is to insure that only one transaction can be performed on a particular area of your storage data at a time.  The path doesn't necessarily have to exist.  

The [begin()](API.md#begin) method is asynchronous because obtaining a lock may have to wait on another active transaction using the same base path.  Calling [commit()](API.md#commit) (or [abort()](API.md#abort) -- see below) releases the lock, and completes the transaction.  At that point you should discard the `trans` object, as it can no longer be used.

Here is a more comprehensive example, which deposits a sum of money into a fictional bank account.  We are using the [async](https://www.npmjs.com/package/async) module for better flow control.

```js
const async = require('async');

storage.begin( 'accounts', function(err, trans) {
	// transaction has begun, now use 'trans' as storage proxy
	async.waterfall(
		[
			function(callback) {
				// load fictional bank account
				trans.get( 'accounts/jhuckaby', callback );
			},
			function(account, callback) {
				// make deposit
				account.balance += 500.00;
				
				// save account data
				trans.put( 'accounts/jhuckaby', account, callback );
			},
			function(callback) {
				// commit transaction
				trans.commit( callback );
			}
		],
		function (err) {
			if (err) {
				// error during transaction, abort it and roll back
				return trans.abort( function() {
					// rollback complete
				} );
			}
			
			// transaction is complete
			// accounts/jhuckaby is $500 richer!
		}
	);
});
```

So here we are beginning a transaction on path `accounts`, and then mutating an account record *under* this path, i.e. `accounts/jhuckaby`.  Inside of the transaction, we are loading the account, incrementing its balance, and saving it back out.  But nothing actually happens outside the transaction object until we commit it.  At that time our changes are applied to main storage, and the lock released.

You may be wondering why a global exclusive lock on the `accounts` path is necessary to simply make a deposit into one account.  Why not lock only the `accounts/jhuckaby` path, so multiple deposits into different accounts can all happen concurrently?  That would probably work fine in this example, but consider the case of transferring money between two accounts.  Your application may want both the withdraw *and* deposit to happen inside a single transaction, in which case you would probably want to obtain a global lock.

So what happens if another thread tries to load `accounts/jhuckaby` somewhere in the middle of the transaction, but using the main storage object?  Consider:

```js
storage.get( 'accounts/jhuckaby', function(err, account) {
	// what is account.balance here?
} );
```

The answer is either!  The account's balance may be its original value here, or it may be +500.00, depending on exactly when this code actually executed.  If the commit completed, it will reflect the new +500 value.  But if it ran anytime before that, it will be the old value.  All operations are atomic, so it will always be one or the other.

Depending on your application, the "proper" way to read an account balance may be to start another transaction using the same base transaction lock path, and then commit it with zero write operations (a zero-operation commit).  This way it has to wait for a lock, and will never run at the same time as an active transaction.  Example:

```js
storage.begin( 'accounts', function(err, trans) {
	// we have a lock
	trans.get( 'accounts/jhuckaby', function(err, account) {
		// read account.balance here
		trans.commit();
	} );
});
```

In this case we know the commit will be instant (zero operations) so we don't need to pass it a callback.  It'll release the lock in the same thread.

It is up to your application to decide when transactions and/or basic [locking](../README.md#advisory-locking) should be used.  Overusing global locks can be bad for performance, so if you can get away with calling a direct [get()](API.md#get) for reads then you should do it whenever possible.

## Aborting

If an error occurs during a transaction, you can call the [abort()](API.md#abort) method to cancel it and roll everything back (if any changes occurred).  This also releases the lock and renders the transaction object dead.  Example use:

```js
storage.begin( 'some_path', function(err, trans) {
	
	// perform actions using `trans` proxy
	// e.g. trans.put(), trans.get(), trans.delete()
	
	// commit transaction
	trans.commit( function(err) {
		// check for error
		if (err) {
			// error during commit, abort it and roll back
			return trans.abort( function() {
				// rollback complete
			} );
		}
		
		// transaction is complete
	} );
});
```

It should be noted that if you receive an error from a [commit()](API.md#commit) call, it is *vital* that you call [abort()](API.md#abort) to undo whatever operations may have already executed.  A commit error is typically very bad, and your storage system will be in an unknown state.  Only by calling [abort()](API.md#abort) can you restore it to before the transaction started.

If the [abort()](API.md#abort) also fails, then the database raises a fatal error and exits immediately.  See [Emergency Shutdown](#emergency-shutdown) below for details about what this means, and [Recovery](#recovery) for how to get back up and running.  Examples of fatal errors include your disk running completely out of space, or a major network failure when using NFS, or S3.

## Automatic API Wrappers

When transactions are enabled, many compound storage methods (those that execute multiple sequential write operations) are automatically wrapped in a self-contained transaction, if one isn't already active.  Basically this includes all the [List](Lists.md), [Hash](Hashes.md) and [Index](Indexer.md) APIs that write data.  This makes everything *much* safer to use, because data won't ever become corrupted due to a power loss or crash during a multi-part operation.  These transaction wrappers will also self-abort (rollback) upon error.  Here is the full list of API methods that are automatically wrapped:

- **List Methods**
	- [listCreate()](API.md#listcreate)
	- [listPush()](API.md#listpush)
	- [listUnshift()](API.md#listunshift)
	- [listPop()](API.md#listpop)
	- [listShift()](API.md#listshift)
	- [listSplice()](API.md#listsplice)
	- [listDelete()](API.md#listdelete)
	- [listCopy()](API.md#listcopy)
	- [listRename()](API.md#listrename)
- **Hash Methods**
	- [hashCreate()](API.md#hashcreate)
	- [hashPut()](API.md#hashput)
	- [hashPutMulti()](API.md#hashputmulti)
	- [hashUpdate()](API.md#hashupdate)
	- [hashUpdateMulti()](API.md#hashupdatemulti)
	- [hashCopy()](API.md#hashcopy)
	- [hashRename()](API.md#hashrename)
	- [hashDeleteMulti()](API.md#hashdeletemulti)
	- [hashDeleteAll()](API.md#hashdeleteall)
	- [hashDelete()](API.md#hashdelete)
- **Indexer Methods**
	- [indexRecord()](API.md#indexrecord)
	- [unindexRecord()](API.md#unindexrecord)

You can still use these methods inside of your own transaction, and they will "join" it (they won't start their own sub-transaction).  However, they all still obtain and release their own locks, for an extra layer of safety.

## Emergency Shutdown

If a fatal storage error is encountered in the middle of an abort (rollback) operation, the database immediately shuts itself down.  This is because your data will be in an undefined state, stuck in the middle of partial transaction.  This should be a very rare event, only occurring when the underlying storage completely fails to write records.  Examples include a disk running out of space (local or NFS filesystem), or a hard network failure with S3.  When this happens, the Node.js process will exit (by default), and will need to be recovered (see [Recovery](#recovery) below).

Upon fatal error, your application can hook the event and provide its own emergency shutdown procedure.  Simply add an event listener on the storage object for the `fatal` event.  It will be passed an `Error` object describing the actual error that occurred.  It is then up to your code to call `process.exit()`.  Example:

```js
storage.on('fatal', function(err) {
	// fatal storage error - emergency shutdown
	// alert the ops team here
	process.exit(1);
});
```

## Recovery

In the event of a fatal storage error, crash or sudden power loss, the database may be left in an "undefined" state.  Meaning, one or more transactions may have been in progress, or even in the middle of a commit.  To handle this, the system may need to perform recovery operations on startup.

By default, if the database experienced an unclean shutdown, it will not allow a normal startup.  It will exit immediately with this message on the console:

```
[YOUR_APP_NAME] was shut down uncleanly and needs to run database recovery operations.
Please start it in recovery mode by issuing this command:
	/path/to/your/app/start/cmd.js --recover
```

Adding the `--recover` command-line flag allows it to continue starting up, and then abort (rollback) any transactions that were active when it died.  It switches into "debug" mode during recovery (i.e. skips the background daemon fork), and echoes the main event log to the console, so you can see exactly what is happening.  When it is complete, another message will be printed to the console, and it will exit again:

```
Database recovery is complete.  Please see logs/recovery.log for full details.
[YOUR_APP_NAME] can now be started normally.
```

You can then start your application normally, i.e. without the `--recover` flag.  Alternatively, if you would prefer that the database automatically recovers and starts up on its own, just add the following property in your `Storage` configuration:

```json
{
	"trans_auto_recover": true
}
```

This will cause the recovery process to be completely automatic, perform everything during normal startup, and not require any additional restarts.  However, if you opt for this feature, it is recommended that you also monitor your application event logs, so you can see when/if a recovery event occurred.  All recovery operations are logged in a `recovery.log` file, which will be in the same directory as your other application logs (e.g. `log_dir` from pixl-server).

In addition, your application can optionally detect that a recovery took place on startup, and run further actions such as notifying the user.  To do this, look for a property on the `Storage` component named `recovery_count`.  If this property exists and is non-zero, then recovery operations took place, and the specified number of transactions were rolled back.  Furthermore, the path to the recovery log can be found in a property named `recovery_log`.  Example:

```js
// check for storage recovery
if (this.server.Storage.recovery_count) {
	this.sendSomeKindOfNotification("Database recovery took place.  See " + this.server.Storage.recovery_log + " for details.");
}
```

## Transaction Internals

The transaction system is implemented by temporarily "branching" the storage system into an isolated object with a dedicated temporary directory on disk.  Any operations performed on the branch are written to a temporary directory.  When the transaction is committed, the branch is "merged" back into main storage, with all operations tracked in a special rollback log which is discarded upon completion.

### Temporary Directory

A local temporary directory on disk is always used for transactions, regardless of the storage engine.  Even if you are using S3 for primary storage, transactions still use temp files on disk before and during commit.  This is to insure both speed and data safety.  You can control where the temporary files live by setting the `trans_dir` configuration property.

Inside the temp directory, two subdirectories are created: `data` and `logs`.  The `data` directory is used to hold all modified records during a transaction (before commit).  Each is named using a unique transaction ID (see below) and a hash of the original key.  This ensures no files will collide with each other, even with many concurrent transactions.  The `logs` directory is for rollback logs.  When a transaction is committed, the original state of the mutated records is written to the log, so it can be applied in reverse during a recovery event.

### Branch Process

When a transaction is first started, the only thing that happens is a unique ID is assigned, and a lock is obtained.  Both are based on the path that is passed into [begin()](API.md#begin).  Nothing is written to disk at this point -- that is deferred until actual operations are performed on the transaction object.

Each record that is mutated (created, updated or deleted) inside a transaction is written to a temporary file, and also a ledger is kept in memory to keep track of which records are changed.  The in-memory ledger only contains keys and a "state", representing a created, updated or deleted record.  Only records created or updated have an associated temp file on disk.  Deleted records are marked in memory only (no need for a temp file).

For example, consider a transaction that begins with path `test1`...

```js
storage.begin( 'test1', function(err, trans) {
	// transaction has begun
} );
```

The transaction ID will be `5a105e8b9d40e1329780d62ea2265d8a` (which is just an MD5 of `test1`).  Now, let's say our `trans_dir` was set to `/let/tmp/db`, and inside our transaction we store a record with key `test1/record1`...

```js
trans.put( 'test1/record1', { foo: 12345 }, function(err) {
	// record written inside transaction
} );
```

So at this point we wrote the `test1/record1` record using our `trans` object, but nothing has happened in the outer storage system (i.e. nothing was written to the primary storage engine).  Instead, the following temp file was written to disk, containing `{"foo":12345}`:

```
/tmp/db/data/5a105e8b9d40e1329780d62ea2265d8a-0d1454fd1bcdc024acedcbe5cfff4ffd.json
```

The temp filename is made up of the transaction ID (`5a105e8b9d40e1329780d62ea2265d8a`) and the MD5 hash of the record key (`0d1454fd1bcdc024acedcbe5cfff4ffd`).  This is to insure it will not collide with any other records in any other concurrent transactions, doesn't require any further subdirectories, and we can easily retrieve it at commit time if we know the plain key.

It should be noted that in these examples our record keys are *under* the `test1` base transaction path, e.g. `test1/record1`.  This is not required, as any record anywhere in storage can be read, written or deleted inside a transaction.  However, it keeps things much cleaner if you design your storage key layout in this way, especially with locking being completely advisory.  You want to ensure that your own application keeps its transaction-enabled records separate from non-transaction records (if any).  You can do this with a base key path like `test1/...` or some other method -- the storage system cares not.

The fact that we wrote to `test1/record1` is also noted in memory, in the transactions hash.  All the transaction keys are kept in memory, and the values are merely a state flag.  Here is the internal representation:

```js
"transactions": {
	"5a105e8b9d40e1329780d62ea2265d8a": {
		"id": "5a105e8b9d40e1329780d62ea2265d8a", 
		"path": "test1", 
		"date": 1514260380.343, 
		"pid": 9343,
		"keys": {
			"test1/record1": "W"
		},
		"queue": []
	}
}
```

In this case the state of the record is `W`, indicating "written".  If we deleted the record inside the transaction, the state would be `D`.  This ledger keeps track of all mutations, and is used to perform the actual commit.

Let's also delete a record just to see the internal representation.  Assuming `test1/deleteme` already existed before we started the transaction, we can do this:

```js
trans.delete( 'test1/deleteme', function(err) {
	// record deleted inside transaction
} );
```

This will not result in any temp file created on disk (although it will delete one if it already existed), but we do have to make a note in the transactions hash about the state of the deleted record:

```js
"keys": {
	"test1/record1": "W",
	"test1/deleteme": "D"
},
```

So now our transaction contains two mutations (operations).  One record written (has associated temp file), and one record deleted (no temp file).  Still, outside the transaction nothing has happened.  The `test1/deleteme` record still exists.

It is important to note that while some transaction metadata is kept in RAM, all the actual data is written to disk, as is the rollback log, and none of the metadata in RAM is required for recovery.  If you attempt a transaction containing hundreds of thousands of records, sure, it may cause a slowdown and memory bloat, but this database just isn't meant to scale that high.

Now let's see what happens if we fetch our `test1/record1` key, still inside the transaction and using the `trans` object...

```js
trans.get( 'test1/record1', function(err, data) {
	// record fetched inside transaction
	// data will be {"foo": 12345}
} );
```

Internally, the [get()](API.md#get) method is overridden, and the transaction layer intercepts the call.  First, we check the ledger, to see if the `test1/record1` key was branched, and in this case it was.  So instead of hitting primary storage, we simply load our temp file for the record, and return that value, since the state is `W`.  If the state is `D` (deleted inside transaction), then a `NoSuchKey` error is returned, just as if the record didn't exist in primary storage.  Alternatively, if `test1/record1` simply isn't in the transactions hash, the operation falls back to normal storage.

Similarly, if we try to fetch `test1/deleteme` using `trans`, we get an error:

```js
trans.get( 'test1/deleteme', function(err, data) {
	// record not found
	// err.code == "NoSuchKey"
} );
```

Even though the real `test1/deleteme` record still exists, our transaction "simulates" a deleted record by returning an error for the overridden [get()](API.md#get) method.

In this way, any records mutated inside the transaction are "branched" (written to temp files and/or added to the transaction ledger) and kept isolated until the transaction needs to be "merged" (committed), or possibly just discarded (transaction aborted before commit).

### Commit Process

The commit process basically replays all the transaction operations on primary storage, effectively "merging the branch".  However, it must do this in such a way so that a sudden crash or power loss at *any point* will still allow for full recovery, i.e. a clean rollback to the previous state.  To do this, we rely on a local rollback log, and of course [fsync](http://man7.org/linux/man-pages/man2/fsync.2.html), to insure the log is actually written to physical disk (and not in the OS cache).

The log will contain the original JSON contents of all the records that will be mutated by the transaction.  It is basically a "snapshot" of the previous state, before we start the commit.  The log goes into the `logs` subdirectory under our `trans_dir` temp directory, and is named using the same Transaction ID hash:

```
/tmp/db/logs/5a105e8b9d40e1329780d62ea2265d8a.log
```

The log file format is plain text with line-delimited JSON for the records.  The first line is a header record that describes the transaction.  Here is an example log:

```
{"id":"5a105e8b9d40e1329780d62ea2265d8a","path":"test1","date":1514260380.343,"pid":9343}
{"key":"test1/record1","value":{"foo":12345}}
{"key":"test1/deleteme","value":0}
```

The header record is just a copy of the in-memory transaction metadata, minus the verbose key map and queue.  It's just used to identify the transaction, and for debugging purposes.  The rest of the lines are for all the mutated records.  Each record is wrapped in an outer JSON with a `key` and `value` property.  The `value` is the actual record JSON contents.  If the record was deleted, as was the case with `test1/deleteme`, then the value is set to `0`.

So here is the commit process, step by step:

- Write rollback log to local disk (see above).
- Call [fsync](http://man7.org/linux/man-pages/man2/fsync.2.html) on the rollback log file, to flush it to physical disk.
- Call [fsync](http://man7.org/linux/man-pages/man2/fsync.2.html) on the rollback directory as well, just to be 100% sure.
	- See the [fsync manpage](http://man7.org/linux/man-pages/man2/fsync.2.html) for details.
- Apply all transaction record changes to primary storage, as fast as possible.
	- This uses the storage [concurrency](../README.md#concurrency) configuration setting for parallelization.
	- When using the [Filesystem](../README.md#local-filesystem) engine, additional optimizations take place here.  The temp files are essentially just "renamed" into place (if possible), rather than being read and written again.
- Call [fsync](http://man7.org/linux/man-pages/man2/fsync.2.html) on the temp `data` directory (where the temp files came from), to ensure they all get rewritten to disk as well, after their renames.
	- See this [Stack Overflow article](https://stackoverflow.com/questions/3764822/how-to-durably-rename-a-file-in-posix) for details.
	- This safety mechanism probably only has a real effect on local ext3/ext4 filesystems.
- Delete the rollback log.
- Remove transaction metadata from memory.
- Release the lock on the transaction base path.

The idea here is that no matter where a crash or sudden power loss occurs during the commit process, a full rollback can always be achieved.  The actual changes on the main storage system are only made once the rollback log is fully written and flushed to disk, and the log itself is only deleted when the record changes are also made (and flushed, where possible).

This is not a 100% guarantee of data durability, as corruption can happen during a crash or power loss.  The rollback log may only be partially written, or corrupted in some way where a replay is not possible.  This can happen because fsync calls are not guaranteed on all operating systems, filesystems or disk media (e.g. certain SSDs), and really all bets are off if you are using S3 for primary storage.

Basically it's all just a big crap shoot, but we're trying to cover as many error cases as possible.

### Rollback Process

There are two types of aborted transaction: one that happens before the commit (easy & safe), and one that happens as a result of an error *during* the commit (difficult & dangerous).  Let's take the easy one first.

When a transaction is aborted *before* commit, there is really nothing to roll back.  There is no rollback log, and nothing has touched primary storage yet.  Instead, we simply need to clean things up.  All the transaction temp files are deleted (if any), the in-memory transaction metadata is deleted, and the lock is released.  This kind of abort is typically user-driven, by calling [abort()](API.md#abort) in your application code.  It is typically quite safe, low risk and non-destructive to primary storage.

The other type of abort -- one that occurs as a result of an error, crash or power loss *during* a commit -- is more involved.  Here we have to basically "replay" the rollback log, and restore records to their original state.

The first step is to locate the rollback log.  It is named using the transaction ID hash, so we can easily find it if we are rolling back an active transaction in the same process (i.e. non-crash rollback).  However, for a full crash recovery, any and all leftover rollback logs are globbed, and then processed in order.

The rollback log is basically line-delimited JSON records, so we just have to open the file, and iterate over it, line by line.  Generally we skip over the first line (the file header), which is just metadata about the transaction.  This is only needed during a full crash recovery (see below).  Next, we process each line, which is a record to be restored to the specified JSON state, or deleted.  It should be noted that temp files are *not* used for rollback.  All the JSON record data is contained within the rollback log itself (this is why only JSON records are supported for transactions, and not binary records).

As noted above, during a full crash recovery we have no transaction metadata in memory (with the transaction ID, log file path, etc.).  To restore this internal state, we use the rollback log header (i.e. the first line).  This special JSON record is used to restore the internal metadata, so we have an active transaction that we are recovering.

The second phase of the rollback is cleanup.  Here we delete any temp files that may have been written as part of the transaction.  Temp files are only used for commit, not rollback, so we can just blindly delete them all.  For a non-crash rollback, we can use the in-memory `keys` hash to locate all the temp files.  For a full crash recovery, we just delete *all* temp files when recovery is complete (transaction temp files have their own directory).

Finally, the rollback log itself is deleted, the in-memory transaction metadata discarded, and the original lock is released (if applicable).  At this point storage has been restored to the state just before the commit, and everything should be happy.

Note that if a transaction abort operation fails due to a storage write failure, this is considered fatal.  The database immediately shuts down and issues a `fatal` error event.  We have to give up here because storage will be in an undefined state, and we should not attempt any further operations before a user addresses the underlying issue.  This is typically a disk that ran out of space, or some kind of "permanent" filesystem I/O error.  In the case of S3 or Couchbase, this would be a permanent network error.
```

## File: `engines/Couchbase.js`
```javascript
// Couchbase Storage Plugin
// Copyright (c) 2015 - 2018 Joseph Huckaby
// Released under the MIT License

// Requires the 'couchbase' module from npm
// npm install couchbase

var Class = require("pixl-class");
var Component = require("pixl-server/component");
var CouchbaseAPI = require('couchbase');
var Tools = require("pixl-tools");

module.exports = Class.create({
	
	__name: 'Couchbase',
	__parent: Component,
	
	defaultConfig: {
		connectString: "couchbase://127.0.0.1",
		bucket: "default",
		password: "",
		serialize: false,
		keyPrefix: "",
		keyTemplate: ""
	},
	
	startup: function(callback) {
		// setup Couchbase connection
		var self = this;
		this.logDebug(2, "Setting up Couchbase", 
			Tools.copyHashRemoveKeys( this.config.get(), { password:1 }) );
		
		this.setup(callback);
		// this.config.on('reload', function() { self.setup(); } );
	},
	
	setup: function(callback) {
		// setup Couchbase connection
		var self = this;
		
		this.keyPrefix = this.config.get('keyPrefix').replace(/^\//, '');
		if (this.keyPrefix && !this.keyPrefix.match(/\/$/)) this.keyPrefix += '/';
		
		this.keyTemplate = this.config.get('keyTemplate').replace(/^\//, '').replace(/\/$/, '');
		
		// support old legacy naming convention: connect_string
		this.cluster = new CouchbaseAPI.Cluster( this.config.get('connectString') || this.config.get('connect_string') );
		
		if (this.config.get('username') && this.config.get('password')) {
			// couchbase 2.5+ new auth style
			this.cluster.authenticate(this.config.get('username'), this.config.get('password'));
			
			this.bucket = this.cluster.openBucket( this.config.get('bucket'), function(err) {
				callback(err);
			} );
		}
		else if (!this.config.get('username') && this.config.get('password')) {
			// couchbase 2.0 old auth style
			this.bucket = this.cluster.openBucket( this.config.get('bucket'), this.config.get('password'), function(err) {
				callback(err);
			} );
		}
		else {
			// no auth
			this.bucket = this.cluster.openBucket( this.config.get('bucket'), function(err) {
				callback(err);
			} );
		}
	},
	
	prepKey: function(key) {
		// prepare key for S3 based on config
		var md5 = Tools.digestHex(key, 'md5');
		
		if (this.keyPrefix) {
			key = this.keyPrefix + key;
		}
		
		if (this.keyTemplate) {
			var idx = 0;
			var temp = this.keyTemplate.replace( /\#/g, function() {
				return md5.substr(idx++, 1);
			} );
			key = Tools.substitute( temp, { key: key, md5: md5 } );
		}
		
		return key;
	},
	
	put: function(key, value, callback) {
		// store key+value in Couchbase
		var self = this;
		key = this.prepKey(key);
		
		if (this.storage.isBinaryKey(key)) {
			this.logDebug(9, "Storing Couchbase Binary Object: " + key, '' + value.length + ' bytes');
		}
		else {
			this.logDebug(9, "Storing Couchbase JSON Object: " + key, this.debugLevel(10) ? value : null);
			if (this.config.get('serialize')) value = JSON.stringify( value );
		}
		
		this.bucket.upsert( key, value, {}, function(err) {
			if (err) {
				err.message = "Failed to store object: " + key + ": " + err.message;
				self.logError('couchbase', err.message);
			}
			else self.logDebug(9, "Store complete: " + key);
			
			if (callback) callback(err);
		} );
	},
	
	putStream: function(key, inp, callback) {
		// store key+value in Couchbase using read stream
		var self = this;
		
		// The Couchbase Node.JS 2.0 API has no stream support.
		// So, we have to do this the RAM-hard way...
		
		var chunks = [];
		inp.on('data', function(chunk) {
			chunks.push( chunk );
		} );
		inp.on('end', function() {
			var buf = Buffer.concat(chunks);
			self.put( key, buf, callback );
		} );
	},
	
	head: function(key, callback) {
		// head couchbase value given key
		var self = this;
		
		// The Couchbase Node.JS 2.0 API has no way to head / ping an object.
		// So, we have to do this the RAM-hard way...
		
		this.get( key, function(err, data) {
			if (err && (err.code != CouchbaseAPI.errors.keyNotFound)) {
				// some other error
				err.message = "Failed to head key: " + key + ": " + err.message;
				self.logError('couchbase', err.message);
				callback(err);
			}
			else if (!data) {
				// record not found
				// always use "NoSuchKey" in error code
				var err = new Error("Failed to head key: " + key + ": Not found");
				err.code = "NoSuchKey";
				
				callback( err, null );
			}
			else {
				callback( null, { mod: 1, len: data.length } );
			}
		} );
	},
	
	get: function(key, callback) {
		// fetch Couchbase value given key
		var self = this;
		key = this.prepKey(key);
		
		this.logDebug(9, "Fetching Couchbase Object: " + key);
		
		this.bucket.get( key, function(err, result) {
			if (!result) {
				if (err && (err.code != CouchbaseAPI.errors.keyNotFound)) {
					// some other error
					err.message = "Failed to fetch key: " + key + ": " + err.message;
					self.logError('couchbase', err.message);
					callback( err, null );
				}
				else {
					// record not found
					// always use "NoSuchKey" in error code
					var err = new Error("Failed to fetch key: " + key + ": Not found");
					err.code = "NoSuchKey";
					
					callback( err, null );
				}
			}
			else {
				var body = result.value;
				
				if (self.storage.isBinaryKey(key)) {
					self.logDebug(9, "Binary fetch complete: " + key, '' + body.length + ' bytes');
				}
				else {
					if (self.config.get('serialize')) {
						try { body = JSON.parse( body.toString() ); }
						catch (e) {
							self.logError('couchbase', "Failed to parse JSON record: " + key + ": " + e);
							callback( e, null );
							return;
						}
					}
					self.logDebug(9, "JSON fetch complete: " + key, self.debugLevel(10) ? body : null);
				}
				
				callback( null, body );
			}
		} );
	},
	
	getBuffer: function(key, callback) {
		// fetch Couchbase buffer given key
		var self = this;
		key = this.prepKey(key);
		
		this.logDebug(9, "Fetching Couchbase Object: " + key);
		
		this.bucket.get( key, function(err, result) {
			if (!result) {
				if (err && (err.code != CouchbaseAPI.errors.keyNotFound)) {
					// some other error
					err.message = "Failed to fetch key: " + key + ": " + err.message;
					self.logError('couchbase', err.message);
					callback( err, null );
				}
				else {
					// record not found
					// always use "NoSuchKey" in error code
					var err = new Error("Failed to fetch key: " + key + ": Not found");
					err.code = "NoSuchKey";
					callback( err, null );
				}
			}
			else {
				var body = result.value;
				self.logDebug(9, "Binary fetch complete: " + key, '' + body.length + ' bytes');
				callback( null, body );
			}
		} );
	},
	
	getStream: function(key, callback) {
		// get readable stream to record value given key
		var self = this;
		
		// The Couchbase Node.JS 2.0 API has no stream support.
		// So, we have to do this the RAM-hard way...
		this.get( key, function(err, buf) {
			if (err && (err.code != CouchbaseAPI.errors.keyNotFound)) {
				// some other error
				err.message = "Failed to fetch key: " + key + ": " + err.message;
				self.logError('couchbase', err.message);
				return callback(err);
			}
			else if (!buf) {
				// record not found
				var err = new Error("Failed to fetch key: " + key + ": Not found");
				err.code = "NoSuchKey";
				return callback( err, null );
			}
			
			var stream = new BufferStream(buf);
			callback(null, stream, { mod: 1, len: buf.length });
		} );
	},
	
	getStreamRange: function(key, start, end, callback) {
		// get readable stream to record value given key and range
		var self = this;
		
		// The Couchbase Node.JS 2.0 API has no stream support.
		// So, we have to do this the RAM-hard way...
		this.get( key, function(err, buf) {
			if (err && (err.code != CouchbaseAPI.errors.keyNotFound)) {
				// some other error
				err.message = "Failed to fetch key: " + key + ": " + err.message;
				self.logError('couchbase', err.message);
				return callback(err);
			}
			else if (!buf) {
				// record not found
				var err = new Error("Failed to fetch key: " + key + ": Not found");
				err.code = "NoSuchKey";
				return callback( err, null );
			}
			
			// validate byte range, now that we have the head info
			if (isNaN(start) && !isNaN(end)) {
				start = buf.length - end;
				end = buf.length ? buf.length - 1 : 0;
			} 
			else if (!isNaN(start) && isNaN(end)) {
				end = buf.length ? buf.length - 1 : 0;
			}
			if (isNaN(start) || isNaN(end) || (start < 0) || (start >= buf.length) || (end < start) || (end >= buf.length)) {
				download.destroy();
				callback( new Error("Invalid byte range (" + start + '-' + end + ") for key: " + key + " (len: " + buf.length + ")"), null );
				return;
			}
			
			var range = buf.slice(start, end + 1);
			var stream = new BufferStream(range);
			callback(null, stream, { mod: 1, len: buf.length });
		} );
	},
	
	delete: function(key, callback) {
		// delete Couchbase key given key
		// Example CB error message: The key does not exist on the server
		var self = this;
		key = this.prepKey(key);
		
		this.logDebug(9, "Deleting Couchbase Object: " + key);
		
		this.bucket.remove( key, {}, function(err) {
			if (err) {
				// if error was a non-existent key, make sure we use the standard code
				if (err.code == CouchbaseAPI.errors.keyNotFound) err.code = "NoSuchKey";
				
				self.logError('couchbase', "Failed to delete object: " + key + ": " + err.message);
			}
			else self.logDebug(9, "Delete complete: " + key);
			
			callback(err);
		} );
	},
	
	runMaintenance: function(callback) {
		// run daily maintenance
		callback();
	},
	
	shutdown: function(callback) {
		// shutdown storage
		this.logDebug(2, "Shutting down Couchbase");
		this.bucket.disconnect();
		callback();
	}
	
});

// Modified the following snippet from node-streamifier:
// Copyright (c) 2014 Gabriel Llamas, MIT Licensed

var util = require('util');
var stream = require('stream');

var BufferStream = function (object, options) {
	if (object instanceof Buffer || typeof object === 'string') {
		options = options || {};
		stream.Readable.call(this, {
			highWaterMark: options.highWaterMark,
			encoding: options.encoding
		});
	} else {
		stream.Readable.call(this, { objectMode: true });
	}
	this._object = object;
};

util.inherits(BufferStream, stream.Readable);

BufferStream.prototype._read = function () {
	this.push(this._object);
	this._object = null;
};
```

## File: `engines/Filesystem.js`
```javascript
// Local File Storage Plugin
// Copyright (c) 2015 - 2019 Joseph Huckaby
// Released under the MIT License

var path = require('path');
var fs = require('fs');
var async = require('async');
var crypto = require('crypto');

var Class = require("pixl-class");
var Component = require("pixl-server/component");
var Tools = require("pixl-tools");
var Cache = require("pixl-cache");

var mkdirp = Tools.mkdirp;

module.exports = Class.create({
	
	__name: 'Filesystem',
	__parent: Component,
	
	startup: function(callback) {
		// setup storage plugin
		var self = this;
		this.logDebug(2, "Setting up filesystem storage");
		
		this.setup();
		this.config.on('reload', function() { self.setup(); } );
		
		// counter so worker temp files don't collide
		this.tempFileCounter = 1;
		
		this.logDebug(3, "Base directory: " + this.baseDir);
		
		callback();
	},
	
	setup: function() {
		// setup storage system (also called for config reload)
		var self = this;
		this.baseDir = this.config.get('base_dir') || process.cwd();
		this.keyNamespaces = this.config.get('key_namespaces') || 0;
		this.pretty = this.config.get('pretty') || 0;
		this.rawFilePaths = this.config.get('raw_file_paths') || 0;
		
		this.keyPrefix = (this.config.get('key_prefix') || '').replace(/^\//, '');
		if (this.keyPrefix && !this.keyPrefix.match(/\/$/)) this.keyPrefix += '/';
		
		this.keyTemplate = (this.config.get('key_template') || '').replace(/^\//, '').replace(/\/$/, '');
		
		// perform some cleanup on baseDir, just in case
		// (baseDir is used as a sentinel for recursive parent dir deletes, so we have to be careful)
		this.baseDir = this.baseDir.replace(/\/$/, '').replace(/\/\//g, '/');
		
		// create initial data dir if necessary
		try {
			mkdirp.sync( this.baseDir ); 
		}
		catch (e) {
			var msg = "FATAL ERROR: Base directory could not be created: " + this.baseDir + ": " + e;
			this.logError('file', msg);
			throw new Error(msg);
		}
		
		// create temp dir
		// (MUST be on same filesystem as base dir, for atomic renames)
		this.tempDir = this.baseDir + '/_temp';
		
		try {
			mkdirp.sync( this.tempDir ); 
		}
		catch (e) {
			var msg = "FATAL ERROR: Temp directory could not be created: " + this.tempDir + ": " + e;
			this.logError('file', msg);
			throw new Error(msg);
		}
		
		// optional LRU cache
		this.cache = null;
		var cache_opts = this.config.get('cache');
		if (cache_opts && cache_opts.enabled) {
			this.logDebug(3, "Setting up LRU cache", cache_opts);
			this.cache = new Cache( Tools.copyHashRemoveKeys(cache_opts, { enabled: 1 }) );
			this.cache.on('expire', function(item, reason) {
				self.logDebug(9, "Expiring LRU cache object: " + item.key + " due to: " + reason, {
					key: item.key,
					reason: reason,
					totalCount: self.cache.count,
					totalBytes: self.cache.bytes
				});
			});
		}
	},
	
	getFilePath: function(key) {
		// get local path to file given storage key
		var file = '';
		
		if (this.rawFilePaths) {
			// file path is raw key, no md5 hashing
			// used for very small apps and testing
			file = this.baseDir + '/' + key;
			if (!key.match(/\.(\w+)$/)) file += '.json';
		}
		else {
			// hash key to get dir structure
			// no need for salt, as this is not for security, 
			// only for distributing the files evenly into a tree of subdirs
			var md5 = Tools.digestHex(key, 'md5');
			
			// locate directory on disk
			var dir = this.baseDir;
			
			if (this.keyPrefix) {
				dir += '/' + this.keyPrefix;
			}
			
			// if key contains a base "dir", use that on disk as well (one level deep only)
			// i.e. users/jhuckaby --> users/01/9a/aa/019aaa6887e5ce3533dcc691b05e69e4.json
			if (this.keyNamespaces) {
				if (key.match(/^([\w\-\.]+)\//)) dir += '/' + RegExp.$1;
				else dir += '/' + key;
			}
			
			if (this.keyTemplate) {
				// apply hashing using key template
				var idx = 0;
				var temp = this.keyTemplate.replace( /\#/g, function() {
					return md5.substr(idx++, 1);
				} );
				file = dir + '/' + Tools.substitute( temp, { key: key, md5: md5 } );
			}
			else {
				// classic legacy md5 hash dir layout, e.g. ##/##/##/[md5]
				dir += '/' + md5.substring(0, 2) + '/' + md5.substring(2, 4) + '/' + md5.substring(4, 6);
				
				// filename is full hash
				file = dir + '/' + md5;
			}
			
			// grab ext from key, or default to json
			// (all binary keys should have a file extension IN THE KEY)
			if (key.match(/\.(\w+)$/)) file += '.' + RegExp.$1;
			else file += '.json';
		}
		
		return file;
	},
	
	_makeDirs: function(dir, perms, callback) {
		// make directories recursively, with retries
		var self = this;
		var retries = 5;
		var last_err = null;
		
		mkdirp( dir, perms, function(err) {
			if (err) {
				// go into retry loop
				self.logDebug(6, "Error creating directory: " + dir + ": " + err + " (will retry)");
				
				async.whilst(
					function() { return( retries >= 0 ); },
					function(callback) {
						mkdirp( dir, perms, function(err) {
							if (err) {
								self.logDebug(6, "Error creating directory: " + dir + ": " + err + " (" + retries + " retries remain)");
								last_err = err;
								retries--;
							}
							else {
								// success, jump out of loop
								last_err = null;
								retries = -1;
							}
							callback();
						} );
					},
					function() {
						callback( last_err );
					}
				); // whilst
			} // err
			else callback();
		} ); // mkdirp
	},
	
	_renameFile: function(source_file, dest_file, callback) {
		// rename file plus mkdir if needed
		var self = this;
		
		fs.rename(source_file, dest_file, function(rn_err) {
			if (!rn_err || (rn_err.code == 'EXDEV')) return callback();
			
			self.logDebug(6, "Error renaming file: " + source_file + " --> " + dest_file + ": " + rn_err + " (will retry)");
			
			// we may need one more mkdir (race condition with delete)
			self._makeDirs( path.dirname(dest_file), 0o0775, function(mk_err) {
				if (mk_err) return callback(rn_err);
				
				// last try
				fs.rename(source_file, dest_file, callback);
			});
		});
	},
	
	put: function(key, value, callback) {
		// store key+value on disk
		var self = this;
		var file = this.getFilePath(key);
		var is_binary = this.storage.isBinaryKey(key);
		
		// serialize json if needed
		if (is_binary) {
			this.logDebug(9, "Storing Binary Object: " + key, '' + value.length + ' bytes');
		}
		else {
			this.logDebug(9, "Storing JSON Object: " + key, this.debugLevel(10) ? value : file);
			value = this.pretty ? JSON.stringify( value, null, "\t" ) : JSON.stringify( value );
		}
		
		var dir = path.dirname( file );
		
		var temp_file = this.tempDir + '/' + path.basename(file) + '.tmp.' + this.tempFileCounter;
		this.tempFileCounter = (this.tempFileCounter + 1) % 10000000;
		
		// write temp file (atomic mode)
		fs.writeFile( temp_file, value, function (err) {
			if (err) {
				// failed to write file
				var msg = "Failed to write file: " + key + ": " + temp_file + ": " + err.message;
				self.logError('file', msg);
				return callback( new Error(msg), null );
			}
			
			// make sure parent dirs exist, async
			self._makeDirs( dir, 0o0775, function(err) {
				if (err) {
					// failed to create directory
					var msg = "Failed to create directory: " + key + ": " + dir + ": " + err.message;
					self.logError('file', msg);
					return callback( new Error(msg), null );
				}
				
				// finally, rename temp file to final
				self._renameFile( temp_file, file, function (err) {
					if (err) {
						// failed to write file
						var msg = "Failed to rename file: " + key + ": " + temp_file + ": " + err.message;
						self.logError('file', msg);
						return callback( new Error(msg), null );
					}
					
					// possibly cache in LRU
					if (self.cache && !is_binary) {
						self.cache.set( key, value, { date: Tools.timeNow(true) } );
					}
					
					// all done
					self.logDebug(9, "Store operation complete: " + key);
					callback(null, null);
				} ); // rename
			} ); // mkdirp
		} ); // temp file
	},
	
	putStream: function(key, inp, callback) {
		// store key+stream of data to disk
		var self = this;
		var file = this.getFilePath(key);
		
		this.logDebug(9, "Storing Binary Stream Object: " + key, file);
		
		var dir = path.dirname( file );
		
		var temp_file = this.tempDir + '/' + path.basename(file) + '.tmp.' + this.tempFileCounter;
		this.tempFileCounter = (this.tempFileCounter + 1) % 10000000;
		
		// create the write stream to temp file
		var outp = fs.createWriteStream( temp_file );
		
		outp.on('error', function(err) {
			// failed to write file
			var msg = "Failed to write file: " + key + ": " + temp_file + ": " + err.message;
			self.logError('file', msg);
			return callback( new Error(msg), null );
		} );
		
		outp.on('finish', function() {
			// make sure parent dirs exist, async
			self._makeDirs( dir, 0o0775, function(err) {
				if (err) {
					// failed to create directory
					var msg = "Failed to create directory: " + key + ": " + dir + ": " + err.message;
					self.logError('file', msg);
					return callback( new Error(msg), null );
				}
				
				// rename temp file to final
				self._renameFile( temp_file, file, function (err) {
					if (err) {
						// failed to write file
						var msg = "Failed to rename file: " + key + ": " + temp_file + ": " + err.message;
						self.logError('file', msg);
						return callback( new Error(msg), null );
					}
					
					// all done
					self.logDebug(9, "Store operation complete: " + key);
					callback(null, null);
				} ); // rename
			} ); // mkdirp
		} ); // pipe finish
		
		// pipe inp to outp
		inp.pipe( outp );
	},
	
	putStreamCustom: function(key, inp, opts, callback) {
		// store key+stream of data to disk
		var self = this;
		var file = this.getFilePath(key);
		
		this.logDebug(9, "Storing Binary Stream Object: " + key, file);
		
		var dir = path.dirname( file );
		
		var temp_file = this.tempDir + '/' + path.basename(file) + '.tmp.' + this.tempFileCounter;
		this.tempFileCounter = (this.tempFileCounter + 1) % 10000000;
		
		// create the write stream to temp file
		var outp = fs.createWriteStream( temp_file, opts || {} );
		
		outp.on('error', function(err) {
			// failed to write file
			var msg = "Failed to write file: " + key + ": " + temp_file + ": " + err.message;
			self.logError('file', msg);
			return callback( new Error(msg), null );
		} );
		
		outp.on('finish', function() {
			// make sure parent dirs exist, async
			self._makeDirs( dir, 0o0775, function(err) {
				if (err) {
					// failed to create directory
					var msg = "Failed to create directory: " + key + ": " + dir + ": " + err.message;
					self.logError('file', msg);
					return callback( new Error(msg), null );
				}
				
				// rename temp file to final
				self._renameFile( temp_file, file, function (err) {
					if (err) {
						// failed to write file
						var msg = "Failed to rename file: " + key + ": " + temp_file + ": " + err.message;
						self.logError('file', msg);
						return callback( new Error(msg), null );
					}
					
					// all done
					self.logDebug(9, "Store operation complete: " + key);
					callback(null, null);
				} ); // rename
			} ); // mkdirp
		} ); // pipe finish
		
		// pipe inp to outp
		inp.pipe( outp );
	},
	
	head: function(key, callback) {
		// head value given key
		var self = this;
		var file = this.getFilePath(key);
		
		this.logDebug(9, "Pinging Object: " + key, file);
		
		// check cache first
		if (this.cache && this.cache.has(key)) {
			var item = this.cache.getMeta(key);
			
			process.nextTick( function() {
				self.logDebug(9, "Cached head complete: " + key);
				callback( null, {
					mod: item.date,
					len: item.value.length
				} );
			} );
			return;
		} // cache
		
		fs.stat(file, function(err, stats) {
			if (err) {
				if (err.message.match(/ENOENT/)) {
					err.message = "File not found";
					err.code = "NoSuchKey";
				}
				else {
					// log fs errors that aren't simple missing files (i.e. I/O errors)
					self.logError('file', "Failed to stat file: " + key + ": " + file + ": " + err.message);
				}
				
				err.message = "Failed to head key: " + key + ": " + err.message;
				return callback( err, null );
			}
			
			self.logDebug(9, "Head complete: " + key);
			callback( null, {
				mod: Math.floor(stats.mtime.getTime() / 1000),
				len: stats.size
			} );
		} );
	},
	
	get: function(key, callback) {
		// fetch value given key
		var self = this;
		var file = this.getFilePath(key);
		var is_binary = this.storage.isBinaryKey(key);
		
		this.logDebug(9, "Fetching Object: " + key, file);
		
		// check cache first
		if (this.cache && !is_binary && this.cache.has(key)) {
			var data = this.cache.get(key);
			
			process.nextTick( function() {
				try { data = JSON.parse( data ); }
				catch (e) {
					self.logError('file', "Failed to parse JSON record: " + key + ": " + e);
					callback( e, null );
					return;
				}
				self.logDebug(9, "Cached JSON fetch complete: " + key, self.debugLevel(10) ? data : null);
				
				callback( null, data );
			} );
			return;
		} // cache
		
		var opts = {};
		if (!this.storage.isBinaryKey(key)) opts = { encoding: 'utf8' };
		
		fs.readFile(file, opts, function (err, data) {
			if (err) {
				if (err.message.match(/ENOENT/)) {
					err.message = "File not found";
					err.code = "NoSuchKey";
				}
				else {
					// log fs errors that aren't simple missing files (i.e. I/O errors)
					self.logError('file', "Failed to read file: " + key + ": " + file + ": " + err.message);
				}
				
				err.message = "Failed to fetch key: " + key + ": " + err.message;
				return callback( err, null );
			}
			
			// possibly cache in LRU
			if (self.cache && !is_binary) {
				self.cache.set( key, data, { date: Tools.timeNow(true) } );
			}
			
			if (!is_binary) {
				try { data = JSON.parse( data ); }
				catch (e) {
					self.logError('file', "Failed to parse JSON record: " + key + ": " + e);
					callback( e, null );
					return;
				}
				self.logDebug(9, "JSON fetch complete: " + key, self.debugLevel(10) ? data : null);
			}
			else {
				self.logDebug(9, "Binary fetch complete: " + key, '' + data.length + ' bytes');
			}
			
			callback( null, data );
		} );
	},
	
	getBuffer: function(key, callback) {
		// fetch buffer given key
		var self = this;
		var file = this.getFilePath(key);
		
		this.logDebug(9, "Fetching Object: " + key, file);
		
		fs.readFile(file, function (err, data) {
			if (err) {
				if (err.message.match(/ENOENT/)) {
					err.message = "File not found";
					err.code = "NoSuchKey";
				}
				else {
					// log fs errors that aren't simple missing files (i.e. I/O errors)
					self.logError('file', "Failed to read file: " + key + ": " + file + ": " + err.message);
				}
				
				err.message = "Failed to fetch key: " + key + ": " + err.message;
				return callback( err, null );
			}
			
			self.logDebug(9, "Binary fetch complete: " + key, '' + data.length + ' bytes');
			callback( null, data );
		} );
	},
	
	getStream: function(key, callback) {
		// get readable stream to record value given key
		var self = this;
		var file = this.getFilePath(key);
		
		this.logDebug(9, "Fetching Binary Stream: " + key, file);
		
		// make sure record exists
		fs.stat(file, function(err, stats) {
			if (err) {
				if (err.message.match(/ENOENT/)) {
					err.message = "File not found";
					err.code = "NoSuchKey";
				}
				else {
					// log fs errors that aren't simple missing files (i.e. I/O errors)
					self.logError('file', "Failed to stat file: " + key + ": " + file + ": " + err.message);
				}
				
				err.message = "Failed to head key: " + key + ": " + err.message;
				return callback( err, null );
			}
			
			// create read stream
			var inp = fs.createReadStream( file );
			
			callback( null, inp, {
				mod: Math.floor(stats.mtime.getTime() / 1000),
				len: stats.size
			} );
		} );
	},
	
	getStreamRange: function(key, start, end, callback) {
		// get readable stream to record value given key and byte range
		var self = this;
		var file = this.getFilePath(key);
		
		this.logDebug(9, "Fetching ranged binary stream: " + key, { file, start, end } );
		
		// make sure record exists
		fs.stat(file, function(err, stats) {
			if (err) {
				if (err.message.match(/ENOENT/)) {
					err.message = "File not found";
					err.code = "NoSuchKey";
				}
				else {
					// log fs errors that aren't simple missing files (i.e. I/O errors)
					self.logError('file', "Failed to stat file: " + key + ": " + file + ": " + err.message);
				}
				
				err.message = "Failed to head key: " + key + ": " + err.message;
				return callback( err, null );
			}
			
			// validate byte range, now that we have the head info
			if (isNaN(start) && !isNaN(end)) {
				start = stats.size - end;
				end = stats.size ? stats.size - 1 : 0;
			} 
			else if (!isNaN(start) && isNaN(end)) {
				end = stats.size ? stats.size - 1 : 0;
			}
			if (isNaN(start) || isNaN(end) || (start < 0) || (start >= stats.size) || (end < start) || (end >= stats.size)) {
				download.destroy();
				callback( new Error("Invalid byte range (" + start + '-' + end + ") for key: " + key + " (len: " + stats.size + ")"), null );
				return;
			}
			
			// create read stream
			var inp = fs.createReadStream( file, { start, end } );
			
			callback( null, inp, {
				mod: Math.floor(stats.mtime.getTime() / 1000),
				len: stats.size
			} );
		} );
	},
	
	delete: function(key, callback) {
		// delete key given key
		var self = this;
		var file = this.getFilePath(key);
		
		this.logDebug(9, "Deleting Object: " + key, file);
		
		fs.unlink(file, function(err) {
			if (err) {
				if (err.message.match(/ENOENT/)) {
					err.message = "File not found";
					err.code = "NoSuchKey";
				}
				
				self.logError('file', "Failed to delete file: " + key + ": " + file + ": " + err.message);
				
				err.message = "Failed to delete key: " + key + ": " + err.message;
				return callback( err );
			}
			else {
				self.logDebug(9, "Delete complete: " + key);
				
				// possibly delete from LRU cache as well
				if (self.cache && self.cache.has(key)) {
					self.cache.delete(key);
				}
				
				// cleanup parent dirs if empty
				var done = false;
				var dir = path.dirname(file);
				
				if (dir != self.baseDir) {
					async.whilst(
						function() { 
							return (!done); 
						},
						function(callback) {
							fs.rmdir( dir, function(err) {
								if (err) {
									// dir has files, we're done
									done = true;
								}
								else {
									// success -- do we need to go shallower?
									self.logDebug(9, "Deleted empty parent dir: " + dir);
									
									dir = path.dirname( dir );
									if (dir == self.baseDir) {
										// cannot go any further
										done = true;
									}
								} // success
								callback();
							} ); // rmdir
						},
						callback
					);
				}
				else return callback();
			} // success
		} ); // unlink
	},
	
	sync: function(key, callback) {
		// sync data to disk for given key (i.e. fsync)
		var self = this;
		if (this.config.get('no_fsync')) return process.nextTick( callback );
		
		var file = this.getFilePath(key);
		this.logDebug(9, "Synchronizing Object: " + key, file);
		
		// fsync new file to make sure it is really written to disk
		fs.open( file, "r", function(err, fh) {
			if (err) {
				var msg = "Failed to open file: " + key + ": " + file + ": " + err.message;
				self.logError('file', msg);
				return callback( new Error(msg) );
			}
			
			fs.fsync(fh, function(err) {
				if (err) {
					var msg = "Failed to fsync file: " + key + ": " + file + ": " + err.message;
					self.logError('file', msg);
					return callback( new Error(msg) );
				}
				
				fs.close(fh, function(err) {
					if (err) {
						var msg = "Failed to close file: " + key + ": " + file + ": " + err.message;
						self.logError('file', msg);
						return callback( new Error(msg) );
					}
					
					// all done
					self.logDebug(9, "Sync operation complete: " + key);
					callback();
				}); // fs.close
			}); // fs.fsync
		}); // fs.open
	},
	
	runMaintenance: function(callback) {
		// run daily maintenance - delete old temp files
		var self = this;
		var now = Tools.timeNow(true);
		this.logDebug(3, "Running filesystem maintenance");
		
		fs.readdir( this.tempDir, function(err, files) {
			if (err) return callback();
			
			if (files && files.length) {
				// temp dir has files
				async.eachSeries( files, function(file, callback) {
					// stat each file to get mod date
					file = self.tempDir + '/' + file;
					
					fs.stat( file, function(err, stats) {
						if (err) return callback();
						
						if (stats && stats.isFile()) {
							// file is an ordinary file
							var mod = stats.mtime.getTime() / 1000;
							if (mod < now - 43200) {
								// file is old, delete it
								self.logDebug(9, "Deleting old temp file: " + file);
								fs.unlink( file, callback );
							}
							else callback();
						}
						else callback();
					} );
				},
				function(err) {
					if (err) self.logError('maint', "Failed to cleanup temp dir: " + err);
					callback();
				} );
			} // got files
			else callback();
		} );
	},
	
	shutdown: function(callback) {
		// shutdown storage
		this.logDebug(2, "Shutting down file storage");
		callback();
	}
	
});
```

## File: `engines/Hybrid.js`
```javascript
// Hybrid Storage Plugin
// Copyright (c) 2015 - 2020 Joseph Huckaby
// Released under the MIT License

var Class = require("pixl-class");
var Component = require("pixl-server/component");
var Tools = require("pixl-tools");
var async = require('async');

module.exports = Class.create({
	
	__name: 'Hybrid',
	__parent: Component,
	
	defaultConfig: {
		binaryEngine: "",
		docEngine: ""
	},
	
	startup: function(callback) {
		// setup multiple sub-engines
		this.logDebug(2, "Setting up hybrid engine", this.config.get() );
		
		var binaryClass = require( './' + this.config.get('binaryEngine') + '.js' );
		this.binaryEngine = new binaryClass();
		this.binaryEngine.storage = this.storage;
		this.binaryEngine.init( this.server, this.storage.config.getSub( this.config.get('binaryEngine') ) );
		
		var docClass = require( './' + this.config.get('docEngine') + '.js' );
		this.docEngine = new docClass();
		this.docEngine.storage = this.storage;
		this.docEngine.init( this.server, this.storage.config.getSub( this.config.get('docEngine') ) );
		
		async.series([
			this.binaryEngine.startup.bind(this.binaryEngine),
			this.docEngine.startup.bind(this.docEngine)
		], callback );
	},
	
	put: function(key, value, callback) {
		// store key+value in hybrid system
		if (this.storage.isBinaryKey(key)) {
			this.binaryEngine.put( key, value, callback );
		}
		else {
			this.docEngine.put( key, value, callback );
		}
	},
	
	putStream: function(key, inp, callback) {
		// store key+value in hybrid system using read stream
		// streams are binary only!
		this.binaryEngine.putStream( key, inp, callback );
	},
	
	head: function(key, callback) {
		// head hybrid value given key
		if (this.storage.isBinaryKey(key)) {
			this.binaryEngine.head( key, callback );
		}
		else {
			this.docEngine.head( key, callback );
		}
	},
	
	get: function(key, callback) {
		// fetch hybrid value given key
		if (this.storage.isBinaryKey(key)) {
			this.binaryEngine.get( key, callback );
		}
		else {
			this.docEngine.get( key, callback );
		}
	},
	
	getBuffer: function(key, callback) {
		// fetch hybrid buffer given key
		if (this.storage.isBinaryKey(key)) {
			this.binaryEngine.getBuffer( key, callback );
		}
		else {
			this.docEngine.getBuffer( key, callback );
		}
	},
	
	getStream: function(key, callback) {
		// get readable stream to record value given key
		// streams are binary only!
		this.binaryEngine.getStream( key, callback );
	},
	
	getStreamRange: function(key, start, end, callback) {
		// get readable stream to record value given key and range
		// streams are binary only!
		this.binaryEngine.getStreamRange( key, start, end, callback );
	},
	
	delete: function(key, callback) {
		// delete hybrid key given key
		if (this.storage.isBinaryKey(key)) {
			this.binaryEngine.delete( key, callback );
		}
		else {
			this.docEngine.delete( key, callback );
		}
	},
	
	runMaintenance: function(callback) {
		// run daily maintenance
		this.logDebug(3, "Running hybrid maintenance");
		
		async.series([
			this.binaryEngine.runMaintenance.bind(this.binaryEngine),
			this.docEngine.runMaintenance.bind(this.docEngine)
		], callback );
	},
	
	shutdown: function(callback) {
		// shutdown storage
		this.logDebug(2, "Shutting down hybrid system");
		
		async.series([
			this.binaryEngine.shutdown.bind(this.binaryEngine),
			this.docEngine.shutdown.bind(this.docEngine)
		], callback );
	}
	
});
```

## File: `engines/Redis.js`
```javascript
// Redis Storage Plugin
// Copyright (c) 2015 - 2024 Joseph Huckaby
// Released under the MIT License

// Requires the 'ioredis' module from npm
// npm install --save ioredis

const Class = require("pixl-class");
const Component = require("pixl-server/component");
const Redis = require('ioredis');
const Tools = require("pixl-tools");

module.exports = Class.create({
	
	__name: 'Redis',
	__parent: Component,
	
	defaultConfig: {
		
		host: 'localhost',
		port: 6379,
		commandTimeout: 5000,
		connectTimeout: 5000,
		username: "",
		password: "",
		
		keyPrefix: "",
		keyTemplate: ""
	},
	
	startup: function(callback) {
		// setup Redis connection
		var self = this;
		this.logDebug(2, "Setting up Redis", this.config.get() );
		this.setup(callback);
	},
	
	setup: function(callback) {
		// setup Redis connection
		var self = this;
		var r_config = this.config.get();
		
		this.keyPrefix = (r_config.keyPrefix || '').replace(/^\//, '');
		if (this.keyPrefix && !this.keyPrefix.match(/\/$/)) this.keyPrefix += '/';
		delete r_config.keyPrefix;
		
		this.keyTemplate = (r_config.keyTemplate || '').replace(/^\//, '').replace(/\/$/, '');
		delete r_config.keyTemplate;
		
		if (!r_config.username.length) delete r_config.username;
		if (!r_config.password.length) delete r_config.password;
		
		r_config.lazyConnect = true;
		r_config.reconnectOnError = function(err) { return true; };
		
		this.redis = new Redis(r_config);
		
		this.redis.on('error', function(err) {
			if (!self.storage.started) {
				return callback( new Error("Redis Startup Error: " + (err.message || err)) );
			}
			
			// error after startup?  Just log it I guess
			self.logError('redis', ''+err);
		}); // error
		
		this.redis.connect(function() {
			self.logDebug(8, "Successfully connected to Redis");
			callback();
		});
	},
	
	prepKey: function(key) {
		// prepare key for S3 based on config
		var md5 = Tools.digestHex(key, 'md5');
		
		if (this.keyPrefix) {
			key = this.keyPrefix + key;
		}
		
		if (this.keyTemplate) {
			var idx = 0;
			var temp = this.keyTemplate.replace( /\#/g, function() {
				return md5.substr(idx++, 1);
			} );
			key = Tools.substitute( temp, { key: key, md5: md5 } );
		}
		
		return key;
	},
	
	put: function(key, value, callback) {
		// store key+value in Redis
		var self = this;
		key = this.prepKey(key);
		
		if (this.storage.isBinaryKey(key)) {
			this.logDebug(9, "Storing Redis Binary Object: " + key, '' + value.length + ' bytes');
		}
		else {
			this.logDebug(9, "Storing Redis JSON Object: " + key, this.debugLevel(10) ? value : null);
			value = JSON.stringify( value );
		}
		
		this.redis.set( key, value, function(err) {
			if (err) {
				err.message = "Failed to store object: " + key + ": " + err;
				self.logError('redis', ''+err);
			}
			else self.logDebug(9, "Store complete: " + key);
			
			if (callback) callback(err);
		} );
	},
	
	putStream: function(key, inp, callback) {
		// store key+value in Redis using read stream
		var self = this;
		
		// The Redis API has no stream support.
		// So, we have to do this the RAM-hard way...
		
		var chunks = [];
		inp.on('data', function(chunk) {
			chunks.push( chunk );
		} );
		inp.on('end', function() {
			var buf = Buffer.concat(chunks);
			self.put( key, buf, callback );
		} );
	},
	
	head: function(key, callback) {
		// head redis value given key
		var self = this;
		key = this.prepKey(key);
		
		// The Redis API has no way to head / ping an object.
		// So, we have to do this the RAM-hard way...
		
		this.redis.get( key, function(err, data) {
			if (err) {
				// an actual error
				err.message = "Failed to head key: " + key + ": " + err;
				self.logError('redis', ''+err);
				callback(err);
			}
			else if (!data) {
				// record not found
				// always use "NoSuchKey" in error code
				var err = new Error("Failed to head key: " + key + ": Not found");
				err.code = "NoSuchKey";
				
				callback( err, null );
			}
			else {
				callback( null, { mod: 1, len: data.length } );
			}
		} );
	},
	
	get: function(key, callback) {
		// fetch Redis value given key
		var self = this;
		key = this.prepKey(key);
		
		this.logDebug(9, "Fetching Redis Object: " + key);
		
		var func = this.storage.isBinaryKey(key) ? 'getBuffer' : 'get';
		this.redis[func]( key, function(err, result) {
			if (!result) {
				if (err) {
					// an actual error
					err.message = "Failed to fetch key: " + key + ": " + err;
					self.logError('redis', ''+err);
					callback( err, null );
				}
				else {
					// record not found
					// always use "NoSuchKey" in error code
					var err = new Error("Failed to fetch key: " + key + ": Not found");
					err.code = "NoSuchKey";
					
					callback( err, null );
				}
			}
			else {
				if (self.storage.isBinaryKey(key)) {
					self.logDebug(9, "Binary fetch complete: " + key, '' + result.length + ' bytes');
				}
				else {
					try { result = JSON.parse( result.toString() ); }
					catch (err) {
						self.logError('redis', "Failed to parse JSON record: " + key + ": " + err);
						callback( err, null );
						return;
					}
					self.logDebug(9, "JSON fetch complete: " + key, self.debugLevel(10) ? result : null);
				}
				
				callback( null, result );
			}
		} );
	},
	
	getBuffer: function(key, callback) {
		// fetch Redis buffer given key
		var self = this;
		key = this.prepKey(key);
		
		this.logDebug(9, "Fetching Redis Object: " + key);
		
		this.redis.getBuffer( key, function(err, result) {
			if (!result) {
				if (err) {
					// an actual error
					err.message = "Failed to fetch key: " + key + ": " + err;
					self.logError('redis', ''+err);
					callback( err, null );
				}
				else {
					// record not found
					// always use "NoSuchKey" in error code
					var err = new Error("Failed to fetch key: " + key + ": Not found");
					err.code = "NoSuchKey";
					callback( err, null );
				}
			}
			else {
				self.logDebug(9, "Binary fetch complete: " + key, '' + result.length + ' bytes');
				callback( null, result );
			}
		} );
	},
	
	getStream: function(key, callback) {
		// get readable stream to record value given key
		var self = this;
		
		// The Redis API has no stream support.
		// So, we have to do this the RAM-hard way...
		
		this.get( key, function(err, buf) {
			if (err) {
				// an actual error
				err.message = "Failed to fetch key: " + key + ": " + err;
				self.logError('redis', ''+err);
				return callback(err);
			}
			else if (!buf) {
				// record not found
				var err = new Error("Failed to fetch key: " + key + ": Not found");
				err.code = "NoSuchKey";
				return callback( err, null );
			}
			
			var stream = new BufferStream(buf);
			callback(null, stream, { mod: 1, len: buf.length });
		} );
	},
	
	getStreamRange: function(key, start, end, callback) {
		// get readable stream to record value given key and range
		var self = this;
		
		// The Redis API has no stream support.
		// So, we have to do this the RAM-hard way...
		
		this.get( key, function(err, buf) {
			if (err) {
				// an actual error
				err.message = "Failed to fetch key: " + key + ": " + err;
				self.logError('redis', ''+err);
				return callback(err);
			}
			else if (!buf) {
				// record not found
				var err = new Error("Failed to fetch key: " + key + ": Not found");
				err.code = "NoSuchKey";
				return callback( err, null );
			}
			
			// validate byte range, now that we have the head info
			if (isNaN(start) && !isNaN(end)) {
				start = buf.length - end;
				end = buf.length ? buf.length - 1 : 0;
			} 
			else if (!isNaN(start) && isNaN(end)) {
				end = buf.length ? buf.length - 1 : 0;
			}
			if (isNaN(start) || isNaN(end) || (start < 0) || (start >= buf.length) || (end < start) || (end >= buf.length)) {
				download.destroy();
				callback( new Error("Invalid byte range (" + start + '-' + end + ") for key: " + key + " (len: " + buf.length + ")"), null );
				return;
			}
			
			var range = buf.slice(start, end + 1);
			var stream = new BufferStream(range);
			callback(null, stream, { mod: 1, len: buf.length });
		} );
	},
	
	delete: function(key, callback) {
		// delete Redis key given key
		var self = this;
		key = this.prepKey(key);
		
		this.logDebug(9, "Deleting Redis Object: " + key);
		
		this.redis.del( key, function(err, deleted) {
			if (!err && !deleted) {
				err = new Error("Failed to fetch key: " + key + ": Not found");
				err.code = "NoSuchKey";
			}
			if (err) {
				self.logError('redis', "Failed to delete object: " + key + ": " + err);
			}
			else self.logDebug(9, "Delete complete: " + key);
			
			callback(err);
		} );
	},
	
	runMaintenance: function(callback) {
		// run daily maintenance
		callback();
	},
	
	shutdown: function(callback) {
		// shutdown storage
		this.logDebug(2, "Shutting down Redis");
		if (this.redis) {
			this.redis.quit(callback);
			this.redis = null;
		}
		else callback();
	}
	
});

// Modified the following snippet from node-streamifier:
// Copyright (c) 2014 Gabriel Llamas, MIT Licensed

var util = require('util');
var stream = require('stream');

var BufferStream = function (object, options) {
	if (object instanceof Buffer || typeof object === 'string') {
		options = options || {};
		stream.Readable.call(this, {
			highWaterMark: options.highWaterMark,
			encoding: options.encoding
		});
	} else {
		stream.Readable.call(this, { objectMode: true });
	}
	this._object = object;
};

util.inherits(BufferStream, stream.Readable);

BufferStream.prototype._read = function () {
	this.push(this._object);
	this._object = null;
};
```

## File: `engines/RedisCluster.js`
```javascript
// RedisCluster Storage Plugin
// Copyright (c) 2015 - 2024 Joseph Huckaby
// Released under the MIT License

// Requires the 'ioredis' module from npm
// npm install --save ioredis

const Class = require("pixl-class");
const Component = require("pixl-server/component");
const Redis = require('ioredis');
const Tools = require("pixl-tools");

module.exports = Class.create({
	
	__name: 'RedisCluster',
	__parent: Component,
	
	defaultConfig: {
		
		host: 'localhost',
		port: 6379,
		connectRetries: 5,
		clusterOpts: {
			scaleReads: "master",
			redisOptions: {
				commandTimeout: 5000,
				connectTimeout: 5000
			}
		},
		
		keyPrefix: "",
		keyTemplate: ""
	},
	
	startup: function(callback) {
		// setup Redis connection
		var self = this;
		this.logDebug(2, "Setting up RedisCluster", this.config.get() );
		this.setup(callback);
	},
	
	setup: function(callback) {
		// setup Redis connection
		var self = this;
		var r_config = this.config.get();
		
		this.keyPrefix = (r_config.keyPrefix || '').replace(/^\//, '');
		if (this.keyPrefix && !this.keyPrefix.match(/\/$/)) this.keyPrefix += '/';
		
		this.keyTemplate = (r_config.keyTemplate || '').replace(/^\//, '').replace(/\/$/, '');
		
		r_config.clusterOpts.clusterRetryStrategy = function(attempts) {
			if (attempts > r_config.connectRetries) return false;
			return attempts;
		};
		
		this.redis = new Redis.Cluster(
			[{ port: r_config.port, host: r_config.host }],
			r_config.clusterOpts
		);
		
		this.redis.on('end', function() {
			self.logDebug(2, "Redis 'end' event fired" + (self.storage.started ? '' : ' (before connection succeeded)'));
			if (!self.storage.started) {
				callback( new Error("Redis end event fired before connection succeeded.") );
			}
			if (self.redis) self.redis.removeAllListeners();
		}); // end
		
		this.redis.on('error', function(err) {
			if (!self.storage.started) return callback(err);
			
			// error after startup?  Just log it I guess
			self.logError('redis', ''+err);
		}); // error
		
		this.redis.on('warning', function(err) {
			self.logError('redis', ''+err);
		}); // error
		
		this.redis.once('ready', function() {
			self.logDebug(8, "Successfully connected to Redis cluster");
			callback();
		});
	},
	
	prepKey: function(key) {
		// prepare key for S3 based on config
		var md5 = Tools.digestHex(key, 'md5');
		
		if (this.keyPrefix) {
			key = this.keyPrefix + key;
		}
		
		if (this.keyTemplate) {
			var idx = 0;
			var temp = this.keyTemplate.replace( /\#/g, function() {
				return md5.substr(idx++, 1);
			} );
			key = Tools.substitute( temp, { key: key, md5: md5 } );
		}
		
		return key;
	},
	
	put: function(key, value, callback) {
		// store key+value in Redis
		var self = this;
		key = this.prepKey(key);
		
		if (this.storage.isBinaryKey(key)) {
			this.logDebug(9, "Storing Redis Binary Object: " + key, '' + value.length + ' bytes');
		}
		else {
			this.logDebug(9, "Storing Redis JSON Object: " + key, this.debugLevel(10) ? value : null);
			value = JSON.stringify( value );
		}
		
		this.redis.set( key, value, function(err) {
			if (err) {
				err.message = "Failed to store object: " + key + ": " + err;
				self.logError('redis', ''+err);
			}
			else self.logDebug(9, "Store complete: " + key);
			
			if (callback) callback(err);
		} );
	},
	
	putStream: function(key, inp, callback) {
		// store key+value in Redis using read stream
		var self = this;
		
		// The Redis API has no stream support.
		// So, we have to do this the RAM-hard way...
		
		var chunks = [];
		inp.on('data', function(chunk) {
			chunks.push( chunk );
		} );
		inp.on('end', function() {
			var buf = Buffer.concat(chunks);
			self.put( key, buf, callback );
		} );
	},
	
	head: function(key, callback) {
		// head redis value given key
		var self = this;
		key = this.prepKey(key);
		
		// The Redis API has no way to head / ping an object.
		// So, we have to do this the RAM-hard way...
		
		this.redis.get( key, function(err, data) {
			if (err) {
				// an actual error
				err.message = "Failed to head key: " + key + ": " + err;
				self.logError('redis', ''+err);
				callback(err);
			}
			else if (!data) {
				// record not found
				// always use "NoSuchKey" in error code
				var err = new Error("Failed to head key: " + key + ": Not found");
				err.code = "NoSuchKey";
				
				callback( err, null );
			}
			else {
				callback( null, { mod: 1, len: data.length } );
			}
		} );
	},
	
	get: function(key, callback) {
		// fetch Redis value given key
		var self = this;
		key = this.prepKey(key);
		
		this.logDebug(9, "Fetching Redis Object: " + key);
		
		var func = this.storage.isBinaryKey(key) ? 'getBuffer' : 'get';
		this.redis[func]( key, function(err, result) {
			if (!result) {
				if (err) {
					// an actual error
					err.message = "Failed to fetch key: " + key + ": " + err;
					self.logError('redis', ''+err);
					callback( err, null );
				}
				else {
					// record not found
					// always use "NoSuchKey" in error code
					var err = new Error("Failed to fetch key: " + key + ": Not found");
					err.code = "NoSuchKey";
					
					callback( err, null );
				}
			}
			else {
				if (self.storage.isBinaryKey(key)) {
					self.logDebug(9, "Binary fetch complete: " + key, '' + result.length + ' bytes');
				}
				else {
					try { result = JSON.parse( result.toString() ); }
					catch (err) {
						self.logError('redis', "Failed to parse JSON record: " + key + ": " + err);
						callback( err, null );
						return;
					}
					self.logDebug(9, "JSON fetch complete: " + key, self.debugLevel(10) ? result : null);
				}
				
				callback( null, result );
			}
		} );
	},
	
	getBuffer: function(key, callback) {
		// fetch Redis buffer given key
		var self = this;
		key = this.prepKey(key);
		
		this.logDebug(9, "Fetching Redis Object: " + key);
		
		this.redis.getBuffer( key, function(err, result) {
			if (!result) {
				if (err) {
					// an actual error
					err.message = "Failed to fetch key: " + key + ": " + err;
					self.logError('redis', ''+err);
					callback( err, null );
				}
				else {
					// record not found
					// always use "NoSuchKey" in error code
					var err = new Error("Failed to fetch key: " + key + ": Not found");
					err.code = "NoSuchKey";
					callback( err, null );
				}
			}
			else {
				self.logDebug(9, "Binary fetch complete: " + key, '' + result.length + ' bytes');
				callback( null, result );
			}
		} );
	},
	
	getStream: function(key, callback) {
		// get readable stream to record value given key
		var self = this;
		
		// The Redis API has no stream support.
		// So, we have to do this the RAM-hard way...
		
		this.get( key, function(err, buf) {
			if (err) {
				// an actual error
				err.message = "Failed to fetch key: " + key + ": " + err;
				self.logError('redis', ''+err);
				return callback(err);
			}
			else if (!buf) {
				// record not found
				var err = new Error("Failed to fetch key: " + key + ": Not found");
				err.code = "NoSuchKey";
				return callback( err, null );
			}
			
			var stream = new BufferStream(buf);
			callback(null, stream, { mod: 1, len: buf.length });
		} );
	},
	
	getStreamRange: function(key, start, end, callback) {
		// get readable stream to record value given key and range
		var self = this;
		
		// The Redis API has no stream support.
		// So, we have to do this the RAM-hard way...
		
		this.get( key, function(err, buf) {
			if (err) {
				// an actual error
				err.message = "Failed to fetch key: " + key + ": " + err;
				self.logError('redis', ''+err);
				return callback(err);
			}
			else if (!buf) {
				// record not found
				var err = new Error("Failed to fetch key: " + key + ": Not found");
				err.code = "NoSuchKey";
				return callback( err, null );
			}
			
			// validate byte range, now that we have the head info
			if (isNaN(start) && !isNaN(end)) {
				start = buf.length - end;
				end = buf.length ? buf.length - 1 : 0;
			} 
			else if (!isNaN(start) && isNaN(end)) {
				end = buf.length ? buf.length - 1 : 0;
			}
			if (isNaN(start) || isNaN(end) || (start < 0) || (start >= buf.length) || (end < start) || (end >= buf.length)) {
				download.destroy();
				callback( new Error("Invalid byte range (" + start + '-' + end + ") for key: " + key + " (len: " + buf.length + ")"), null );
				return;
			}
			
			var range = buf.slice(start, end + 1);
			var stream = new BufferStream(range);
			callback(null, stream, { mod: 1, len: buf.length });
		} );
	},
	
	delete: function(key, callback) {
		// delete Redis key given key
		var self = this;
		key = this.prepKey(key);
		
		this.logDebug(9, "Deleting Redis Object: " + key);
		
		this.redis.del( key, function(err, deleted) {
			if (!err && !deleted) {
				err = new Error("Failed to fetch key: " + key + ": Not found");
				err.code = "NoSuchKey";
			}
			if (err) {
				self.logError('redis', "Failed to delete object: " + key + ": " + err);
			}
			else self.logDebug(9, "Delete complete: " + key);
			
			callback(err);
		} );
	},
	
	runMaintenance: function(callback) {
		// run daily maintenance
		callback();
	},
	
	shutdown: function(callback) {
		// shutdown storage
		this.logDebug(2, "Shutting down Redis");
		if (this.redis) {
			this.redis.disconnect();
			this.redis.removeAllListeners();
			this.redis = null;
		}
		callback();
	}
	
});

// Modified the following snippet from node-streamifier:
// Copyright (c) 2014 Gabriel Llamas, MIT Licensed

var util = require('util');
var stream = require('stream');

var BufferStream = function (object, options) {
	if (object instanceof Buffer || typeof object === 'string') {
		options = options || {};
		stream.Readable.call(this, {
			highWaterMark: options.highWaterMark,
			encoding: options.encoding
		});
	} else {
		stream.Readable.call(this, { objectMode: true });
	}
	this._object = object;
};

util.inherits(BufferStream, stream.Readable);

BufferStream.prototype._read = function () {
	this.push(this._object);
	this._object = null;
};
```

## File: `engines/S3.js`
```javascript
// Amazon AWS S3 Storage Plugin
// Copyright (c) 2015 - 2022 Joseph Huckaby
// Released under the MIT License

var Path = require('path');
var Class = require("pixl-class");
var Component = require("pixl-server/component");
var Tools = require("pixl-tools");
var Cache = require("pixl-cache");
var S3 = require("@aws-sdk/client-s3");
var { Upload } = require("@aws-sdk/lib-storage");
var { NodeHttpHandler } = require("@smithy/node-http-handler");
var streamToBuffer = require("fast-stream-to-buffer");
var StreamMeter = require("stream-meter");

module.exports = Class.create({
	
	__name: 'S3',
	__parent: Component,
	
	startup: function(callback) {
		// setup Amazon AWS connection
		var self = this;
		
		this.setup();
		// this.config.on('reload', function() { self.setup(); } );
		
		callback();
	},
	
	setup: function() {
		// setup AWS connection
		var self = this;
		var aws_config = this.storage.config.get('AWS') || this.server.config.get('AWS');
		var s3_config = this.config.get();
		
		this.logDebug(5, "Setting up Amazon S3 (" + aws_config.region + ")");
		this.logDebug(6, "S3 Bucket ID: " + s3_config.params.Bucket);
		
		this.keyPrefix = (s3_config.keyPrefix || '').replace(/^\//, '');
		if (this.keyPrefix && !this.keyPrefix.match(/\/$/)) this.keyPrefix += '/';
		
		this.keyTemplate = (s3_config.keyTemplate || '').replace(/^\//, '').replace(/\/$/, '');
		this.fileExtensions = !!s3_config.fileExtensions;
		this.pretty = !!s3_config.pretty;
		
		// optional LRU cache
		this.cache = null;
		var cache_opts = s3_config.cache;
		if (cache_opts && cache_opts.enabled) {
			this.logDebug(3, "Setting up LRU cache", cache_opts);
			this.cache = new Cache( Tools.copyHashRemoveKeys(cache_opts, { enabled: 1 }) );
			this.cache.on('expire', function(item, reason) {
				self.logDebug(9, "Expiring LRU cache object: " + item.key + " due to: " + reason, {
					key: item.key,
					reason: reason,
					totalCount: self.cache.count,
					totalBytes: self.cache.bytes
				});
			});
		}
		
		// merge AWS and S3 configs
		var combo_config = Tools.mergeHashes( aws_config, s3_config );
		
		// convert v2 config to v3
		if (!combo_config.maxAttempts && combo_config.maxRetries) {
			combo_config.maxAttempts = combo_config.maxRetries;
			delete combo_config.maxRetries;
		}
		if (combo_config.accessKeyId) {
			if (!combo_config.credentials) combo_config.credentials = {};
			combo_config.credentials.accessKeyId = combo_config.accessKeyId;
			delete combo_config.accessKeyId;
		}
		if (combo_config.secretAccessKey) {
			if (!combo_config.credentials) combo_config.credentials = {};
			combo_config.credentials.secretAccessKey = combo_config.secretAccessKey;
			delete combo_config.secretAccessKey;
		}
		delete combo_config.correctClockSkew;
		delete combo_config.httpOptions;
		delete combo_config.keyPrefix;
		delete combo_config.keyTemplate;
		delete combo_config.fileExtensions;
		delete combo_config.pretty;
		delete combo_config.cache;
		
		this.s3Params = combo_config.params || {};
		delete combo_config.params;
		
		// allow user to specify HTTP timeout options for S3
		if (combo_config.connectTimeout || combo_config.socketTimeout) {
			combo_config.requestHandler = new NodeHttpHandler({
				connectionTimeout: combo_config.connectTimeout || 0,
				socketTimeout: combo_config.socketTimeout || 0
			});
			delete combo_config.connectTimeout;
			delete combo_config.socketTimeout;
		}
		
		this.s3 = new S3.S3Client(combo_config);
	},
	
	prepKey: function(key) {
		// prepare key for S3 based on config
		var ns = '';
		if (key.match(/^([\w\-\.]+)\//)) ns = RegExp.$1;
		
		if (this.keyPrefix) {
			key = this.keyPrefix + key;
		}
		
		if (this.keyTemplate) {
			var md5 = Tools.digestHex(key, 'md5');
			var idx = 0;
			var temp = this.keyTemplate.replace( /\#/g, function() {
				return md5.substr(idx++, 1);
			} );
			key = Tools.sub( temp, { key: key, md5: md5, ns: ns } );
		}
		
		return key;
	},
	
	extKey: function(key, orig_key) {
		// possibly add suffix to key, if fileExtensions mode is enabled
		// and key is not binary
		if (this.fileExtensions && !this.storage.isBinaryKey(orig_key)) {
			key += '.json';
		}
		return key;
	},
	
	put: function(key, value, callback) {
		// store key+value in s3
		var self = this;
		var orig_key = key;
		var is_binary = this.storage.isBinaryKey(key);
		key = this.prepKey(key);
		
		var params = Tools.copyHash( this.s3Params );
		params.Key = this.extKey(key, orig_key);
		params.Body = value;
		
		// serialize json if needed
		if (is_binary) {
			this.logDebug(9, "Storing S3 Binary Object: " + key, '' + value.length + ' bytes');
		}
		else {
			this.logDebug(9, "Storing S3 JSON Object: " + key, this.debugLevel(10) ? params.Body : null);
			params.Body = this.pretty ? JSON.stringify( params.Body, null, "\t" ) : JSON.stringify( params.Body );
			params.ContentType = 'application/json';
		}
		
		this.s3.send( new S3.PutObjectCommand(params) )
			.then( function(data) {
				self.logDebug(9, "Store complete: " + key);
				self.storage.emit('billing', 's3_put', 1);
				
				// possibly cache in LRU
				if (self.cache && !is_binary) {
					self.cache.set( orig_key, params.Body, { date: Tools.timeNow(true) } );
				}
				
				if (callback) process.nextTick( function() { callback(null, data); });
			} )
			.catch( function(err) {
				if (err.name == 'SlowDown') {
					// special behavior for SlowDown errors
					self.logDebug(6, "Received SlowDown from S3 put: " + orig_key + ": " + err + " (will retry)");
					self.storage.emit('slowDown');
					setTimeout( function() { self.put(orig_key, value, callback); }, 1000 );
					return;
				}
				self.logError('s3', "Failed to store object: " + key + ": " + (err.message || err), err);
				if (callback) process.nextTick( function() { callback(err); });
			} );
	},
	
	putStream: function(key, inp, callback) {
		// store key+stream of data to S3
		var self = this;
		var orig_key = key;
		key = this.prepKey(key);
		
		var meter = new StreamMeter();
		inp.pipe(meter);
		
		var params = Tools.copyHash( this.s3Params );
		params.Key = this.extKey(key, orig_key);
		params.Body = meter;
		
		this.logDebug(9, "Storing S3 Binary Stream: " + key);
		
		var upload = new Upload({
			client: this.s3,
			params: params
		});
		
		upload.done()
			.then( function(data) {
				self.logDebug(9, "Stream store complete: " + key);
				self.storage.emit('billing', 's3_put', 1);
				self.storage.emit('billing', 's3_bytes_out', meter.bytes);
				if (callback) process.nextTick( function() { callback(null, data); });
			} )
			.catch( function(err) {
				self.logError('s3', "Failed to store stream: " + key + ": " + (err.message || err), err);
				if (callback) process.nextTick( function() { callback(err, null); });
			} );
	},
	
	putStreamCustom: function(key, inp, opts, callback) {
		// store key+stream of data to S3, inc options
		var self = this;
		var orig_key = key;
		key = this.prepKey(key);
		
		var meter = new StreamMeter();
		inp.pipe(meter);
		
		var params = Tools.copyHash( this.s3Params );
		params.Key = this.extKey(key, orig_key);
		params.Body = meter;
		if (opts) Tools.mergeHashInto(params, opts);
		
		this.logDebug(9, "Storing S3 Binary Stream: " + key);
		
		var upload = new Upload({
			client: this.s3,
			params: params
		});
		
		upload.done()
			.then( function(data) {
				self.logDebug(9, "Stream store complete: " + key);
				self.storage.emit('billing', 's3_put', 1);
				self.storage.emit('billing', 's3_bytes_out', meter.bytes);
				if (callback) process.nextTick( function() { callback(null, data); });
			} )
			.catch( function(err) {
				self.logError('s3', "Failed to store stream: " + key + ": " + (err.message || err), err);
				if (callback) process.nextTick( function() { callback(err, null); });
			} );
	},
	
	head: function(key, callback) {
		// head s3 value given key
		var self = this;
		var orig_key = key;
		key = this.prepKey(key);
		
		this.logDebug(9, "Pinging S3 Object: " + key);
		
		// check cache first
		if (this.cache && this.cache.has(orig_key)) {
			var item = this.cache.getMeta(orig_key);
			
			process.nextTick( function() {
				self.logDebug(9, "Cached head complete: " + orig_key);
				callback( null, {
					mod: item.date,
					len: item.value.length
				} );
			} );
			return;
		} // cache
		
		var params = Tools.copyHash( this.s3Params );
		params.Key = this.extKey(key, orig_key);
		
		this.s3.send( new S3.HeadObjectCommand(params) )
			.then( function(data) {
				self.logDebug(9, "Head complete: " + key);
				self.storage.emit('billing', 's3_head', 1);
				
				process.nextTick( function() {
					callback( null, {
						mod: Math.floor( (new Date(data.LastModified)).getTime() / 1000 ),
						len: data.ContentLength
					} );
				} );
			} )
			.catch( function(err) {
				if ((err.name == 'NoSuchKey') || (err.name == 'NotFound') || (err.code == 'NoSuchKey') || (err.code == 'NotFound')) {
					// key not found, special case, don't log an error
					// always include "Not found" in error message
					err = new Error("Failed to head key: " + key + ": Not found");
					err.code = "NoSuchKey";
				}
				else if (err.name == 'SlowDown') {
					// special behavior for SlowDown errors
					self.logDebug(6, "Received SlowDown from S3 head: " + orig_key + ": " + err + " (will retry)");
					self.storage.emit('slowDown');
					setTimeout( function() { self.head(orig_key, callback); }, 1000 );
					return;
				}
				else {
					// some other error
					self.logError('s3', "Failed to head key: " + key + ": " + (err.message || err), err);
				}
				process.nextTick( function() { callback( err ); } );
			} );
	},
	
	get: function(key, callback) {
		// fetch s3 value given key
		var self = this;
		var orig_key = key;
		var is_binary = this.storage.isBinaryKey(key);
		key = this.prepKey(key);
		
		this.logDebug(9, "Fetching S3 Object: " + key);
		
		// check cache first
		if (this.cache && !is_binary && this.cache.has(orig_key)) {
			var data = this.cache.get(orig_key);
			
			process.nextTick( function() {	
				try { data = JSON.parse( data ); }
				catch (e) {
					self.logError('file', "Failed to parse JSON record: " + orig_key + ": " + e);
					callback( e, null );
					return;
				}
				self.logDebug(9, "Cached JSON fetch complete: " + orig_key, self.debugLevel(10) ? data : null);
				
				callback( null, data );
			} );
			return;
		} // cache
		
		var params = Tools.copyHash( this.s3Params );
		params.Key = this.extKey(key, orig_key);
		
		this.s3.send( new S3.GetObjectCommand(params) )
			.then( function(data) {
				// stream to buffer
				streamToBuffer( data.Body, function (err, body) {
					if (err) {
						self.logError('s3', "Failed to fetch key: " + key + ": " + (err.message || err), err);
						return callback(err);
					}
					
					self.storage.emit('billing', 's3_get', 1);
					self.storage.emit('billing', 's3_bytes_in', body.length);
					
					if (is_binary) {
						self.logDebug(9, "Binary fetch complete: " + key, '' + body.length + ' bytes');
					}
					else {
						body = body.toString();
						
						// possibly cache in LRU
						if (self.cache) {
							self.cache.set( orig_key, body, { date: Tools.timeNow(true) } );
						}
						
						try { body = JSON.parse( body ); }
						catch (e) {
							self.logError('s3', "Failed to parse JSON record: " + key + ": " + e);
							callback( e, null );
							return;
						}
						self.logDebug(9, "JSON fetch complete: " + key, self.debugLevel(10) ? body : null);
					}
					
					callback( null, body, {
						mod: Math.floor((new Date(data.LastModified)).getTime() / 1000),
						len: data.ContentLength
					} );
				} ); // streamToBuffer
			} )
			.catch( function(err) {
				if ((err.name == 'NoSuchKey') || (err.name == 'NotFound') || (err.code == 'NoSuchKey') || (err.code == 'NotFound')) {
					// key not found, special case, don't log an error
					// always include "Not found" in error message
					err = new Error("Failed to fetch key: " + key + ": Not found");
					err.code = "NoSuchKey";
				}
				else if (err.name == 'SlowDown') {
					// special behavior for SlowDown errors
					self.logDebug(6, "Received SlowDown from S3 get: " + orig_key + ": " + err + " (will retry)");
					self.storage.emit('slowDown');
					setTimeout( function() { self.get(orig_key, callback); }, 1000 );
					return;
				}
				else {
					// some other error
					self.logError('s3', "Failed to fetch key: " + key + ": " + (err.message || err), err);
				}
				process.nextTick( function() { callback( err ); } );
			} );
	},
	
	getBuffer: function(key, callback) {
		// fetch s3 buffer given key
		var self = this;
		var orig_key = key;
		key = this.prepKey(key);
		
		this.logDebug(9, "Fetching S3 Object: " + key);
		
		var params = Tools.copyHash( this.s3Params );
		params.Key = this.extKey(key, orig_key);
		
		this.s3.send( new S3.GetObjectCommand(params) )
			.then( function(data) {
				// stream to buffer
				streamToBuffer( data.Body, function (err, body) {
					if (err) {
						self.logError('s3', "Failed to fetch key: " + key + ": " + (err.message || err), err);
						return callback(err);
					}
					
					self.logDebug(9, "Binary fetch complete: " + key, '' + body.length + ' bytes');
					self.storage.emit('billing', 's3_get', 1);
					self.storage.emit('billing', 's3_bytes_in', body.length);
					
					callback( null, body, {
						mod: Math.floor((new Date(data.LastModified)).getTime() / 1000),
						len: data.ContentLength
					} );
				} ); // streamToBuffer
			} )
			.catch( function(err) {
				if ((err.name == 'NoSuchKey') || (err.name == 'NotFound') || (err.code == 'NoSuchKey') || (err.code == 'NotFound')) {
					// key not found, special case, don't log an error
					// always include "Not found" in error message
					err = new Error("Failed to fetch key: " + key + ": Not found");
					err.code = "NoSuchKey";
				}
				else if (err.name == 'SlowDown') {
					// special behavior for SlowDown errors
					self.logDebug(6, "Received SlowDown from S3 getBuffer: " + orig_key + ": " + err + " (will retry)");
					self.storage.emit('slowDown');
					setTimeout( function() { self.getBuffer(orig_key, callback); }, 1000 );
					return;
				}
				else {
					// some other error
					self.logError('s3', "Failed to fetch key: " + key + ": " + (err.message || err), err);
				}
				process.nextTick( function() { callback( err ); } );
			} );
	},
	
	getStream: function(key, callback) {
		// get readable stream to record value given key
		var self = this;
		var orig_key = key;
		key = this.prepKey(key);
		
		this.logDebug(9, "Fetching S3 Stream: " + key);
		
		var params = Tools.copyHash( this.s3Params );
		params.Key = this.extKey(key, orig_key);
		
		this.s3.send( new S3.GetObjectCommand(params) )
			.then( function(data) {
				var download = data.Body;
				
				download.on('error', function(err) {
					self.logError('s3', "Failed to download key: " + key + ": " + (err.message || err), err);
				});
				download.once('end', function() {
					self.logDebug(9, "S3 stream download complete: " + key);
				} );
				download.once('close', function() {
					self.logDebug(9, "S3 stream download closed: " + key);
				} );
				
				self.storage.emit('billing', 's3_get', 1);
				self.storage.emit('billing', 's3_bytes_in', data.ContentLength);
				
				process.nextTick( function() {
					callback( null, download, {
						mod: Math.floor( (new Date(data.LastModified)).getTime() / 1000 ),
						len: data.ContentLength
					} );
				} );
			})
			.catch( function(err) {
				if ((err.name == 'NoSuchKey') || (err.name == 'NotFound') || (err.code == 'NoSuchKey') || (err.code == 'NotFound')) {
					// key not found, special case, don't log an error
					// always include "Not found" in error message
					err = new Error("Failed to fetch key: " + key + ": Not found");
					err.code = "NoSuchKey";
				}
				else {
					// some other error
					self.logError('s3', "Failed to fetch key: " + key + ": " + (err.message || err), err);
				}
				process.nextTick( function() { callback( err ); } );
			});
	},
	
	getStreamRange: function(key, start, end, callback) {
		// get readable stream to record value given key and range
		var self = this;
		var orig_key = key;
		key = this.prepKey(key);
		
		this.logDebug(9, "Fetching ranged S3 stream: " + key, { start, end });
		
		var params = Tools.copyHash( this.s3Params );
		params.Key = this.extKey(key, orig_key);
		
		// convert start/end to HTTP range header string
		var range = "bytes=";
		if (!isNaN(start)) range += start;
		range += '-';
		if (!isNaN(end)) range += end;
		
		params.Range = range;
		
		this.s3.send( new S3.GetObjectCommand(params) )
			.then( function(data) {
				var download = data.Body;
				
				download.on('error', function(err) {
					self.logError('s3', "Failed to download key: " + key + ": " + (err.message || err), err);
				});
				download.once('end', function() {
					self.logDebug(9, "S3 stream download complete: " + key);
				} );
				download.once('close', function() {
					self.logDebug(9, "S3 stream download closed: " + key);
				} );
				
				self.storage.emit('billing', 's3_get', 1);
				self.storage.emit('billing', 's3_bytes_in', data.ContentRange);
				
				// get full length from the ContentRange header
				var len = 0;
				if (data.ContentRange && data.ContentRange.toString().match(/\/\s*(\d+)\s*$/)) {
					len = parseInt( RegExp.$1 );
				}
				
				process.nextTick( function() { 
					callback( null, download, {
						mod: Math.floor( (new Date(data.LastModified)).getTime() / 1000 ),
						len: len,
						cr: data.ContentRange
					} );
				} );
			})
			.catch( function(err) {
				if ((err.name == 'NoSuchKey') || (err.name == 'NotFound') || (err.code == 'NoSuchKey') || (err.code == 'NotFound')) {
					// key not found, special case, don't log an error
					// always include "Not found" in error message
					err = new Error("Failed to fetch key: " + key + ": Not found");
					err.code = "NoSuchKey";
				}
				else {
					// some other error
					self.logError('s3', "Failed to fetch key: " + key + ": " + (err.message || err), err);
				}
				process.nextTick( function() { callback( err ); } );
			});
	},
	
	delete: function(key, callback) {
		// delete s3 key given key
		var self = this;
		var orig_key = key;
		key = this.prepKey(key);
		
		this.logDebug(9, "Deleting S3 Object: " + key);
		
		var params = Tools.copyHash( this.s3Params );
		params.Key = this.extKey(key, orig_key);
		
		this.s3.send( new S3.DeleteObjectCommand(params) )
			.then( function(data) {
				self.logDebug(9, "Delete complete: " + key);
				self.storage.emit('billing', 's3_delete', 1);
				
				// possibly delete from LRU cache as well
				if (self.cache && self.cache.has(orig_key)) {
					self.cache.delete(orig_key);
				}
				
				if (callback) process.nextTick( function() { callback(null, data); } );
			} )
			.catch( function(err) {
				if (err.name == 'SlowDown') {
					// special behavior for SlowDown errors
					self.logDebug(6, "Received SlowDown from S3 delete: " + orig_key + ": " + err + " (will retry)");
					self.storage.emit('slowDown');
					setTimeout( function() { self.delete(orig_key, callback); }, 1000 );
					return;
				}
				self.logError('s3', "Failed to delete object: " + key + ": " + (err.message || err), err);
				if (callback) process.nextTick( function() { callback(err); } );
			} );
	},
	
	list: function(opts, callback) {
		// generate list of objects in S3 given prefix
		// this repeatedly calls ListObjectsV2 for lists > 1000
		// opts: { remotePath, filespec, filter }
		// result: { files([{ key, size, mtime }, ...]), total_bytes }
		let self = this;
		let done = false;
		let files = [];
		let total_bytes = 0;
		let num_calls = 0;
		let now = Tools.timeNow(true);
		
		if (typeof(opts) == 'string') opts = { remotePath: opts };
		if (!opts.remotePath) opts.remotePath = '';
		if (!opts.filespec) opts.filespec = /.*/;
		if (!opts.filter) opts.filter = function() { return true; };
		
		if (opts.older) {
			// convert older to filter func with mtime
			if (typeof(opts.older) == 'string') opts.older = Tools.getSecondsFromText( opts.older );
			opts.filter = function(file) { return file.mtime <= now - opts.older; };
		}
		
		let params = Tools.mergeHashes( this.s3Params || {}, opts.params || {} );
		params.Prefix = this.keyPrefix + opts.remotePath;
		params.MaxKeys = 1000;
		
		let PREFIX_RE = new RegExp('^' + Tools.escapeRegExp(this.keyPrefix));
		
		this.logDebug(8, "Listing S3 files with prefix: " + params.Prefix, opts);
		let tracker = this.perf ? this.perf.begin('s3_list') : null;
		
		Tools.async.whilst(
			function() { 
				return !done; 
			},
			function(callback) {
				self.logDebug(9, "Listing chunk", params);
				
				self.s3.send( new S3.ListObjectsV2Command(params) )
					.then( function(data) {
						let items = data.Contents || [];
						for (let idx = 0, len = items.length; idx < len; idx++) {
							let item = items[idx];
							let key = item.Key.replace(PREFIX_RE, '');
							let bytes = item.Size;
							let mtime = item.LastModified.getTime() / 1000;
							let file = { key: key, size: bytes, mtime: mtime };
							
							// optional filter and filespec
							if (opts.filter(file) && Path.basename(key).match(opts.filespec)) {
								total_bytes += bytes;
								files.push(file);
							}
						}
						
						// check for end of key list
						if (!data.IsTruncated || !items.length) done = true;
						else {
							// advance to next chunk
							params.StartAfter = items[ items.length - 1 ].Key;
						}
						
						num_calls++;
						callback();
					} )
					.catch( function(err) {
						callback( err );
					} );
			},
			function(err) {
				if (tracker) tracker.end();
				if (err) return process.nextTick( function() { callback(err, null, null); });
				
				self.logDebug(9, "S3 listing complete (" + Tools.commify(files.length) + " objects, " + Tools.getTextFromBytes(total_bytes) + ")", {
					prefix: params.Prefix,
					count: files.length,
					bytes: total_bytes,
					calls: num_calls
				});
				
				// break out of promise context
				process.nextTick( function() { callback( null, files, total_bytes ); } );
			}
		); // whilst
	},
	
	runMaintenance: function(callback) {
		// run daily maintenance
		callback();
	},
	
	shutdown: function(callback) {
		// shutdown storage
		this.logDebug(2, "Shutting down S3 storage");
		delete this.s3;
		callback();
	}
	
});
```

## File: `engines/SQLite.js`
```javascript
// SQLite Storage Plugin
// Copyright (c) 2023 - 2026 Joseph Huckaby
// Released under the MIT License

// Requires the 'better-sqlite3' module

const fs = require('fs');
const Path = require('path');
const zlib = require('zlib');
const Class = require("pixl-class");
const Component = require("pixl-server/component");
const BetterSqlite3 = require('better-sqlite3');
const Tools = require("pixl-tools");
const Perf = require("pixl-perf");
const Cache = require("pixl-cache");
const async = require('async');
const noop = function() {};

module.exports = Class.create({
	
	__name: 'SQLite',
	__parent: Component,
	
	defaultConfig: {
		base_dir: '',
		filename: 'sqlite.db',
		keyPrefix: "",
		keyTemplate: ""
	},
	
	startup: function(callback) {
		// setup SQLite connection
		var self = this;
		this.logDebug(2, "Setting up SQLite", this.config.get() );
		this.setup(callback);
	},
	
	setup: function(callback) {
		// setup SQLite connection
		var self = this;
		var sql_config = this.config.get();
		
		this.keyPrefix = (sql_config.keyPrefix || '').replace(/^\//, '');
		if (this.keyPrefix && !this.keyPrefix.match(/\/$/)) this.keyPrefix += '/';
		
		this.keyTemplate = (sql_config.keyTemplate || '').replace(/^\//, '').replace(/\/$/, '');
		
		this.baseDir = sql_config.base_dir || process.cwd();
		this.commands = {
			get: 'SELECT value FROM items WHERE key = $key LIMIT 1',
			head: 'SELECT modified, length(value) FROM items WHERE key = $key LIMIT 1',
			put: 'INSERT INTO items VALUES($key, $value, $now) ON CONFLICT (key) DO UPDATE SET value = $value, modified = $now WHERE key = $key',
			delete: 'DELETE FROM items WHERE key = $key'
		};
		
		// create initial data dir if necessary
		try {
			Tools.mkdirp.sync( this.baseDir ); 
		}
		catch (e) {
			var msg = "FATAL ERROR: Base directory could not be created: " + this.baseDir + ": " + e;
			this.logError('sqlite', msg);
			throw new Error(msg);
		}
		
		// optional LRU cache
		this.cache = null;
		var cache_opts = this.config.get('cache');
		if (cache_opts && cache_opts.enabled) {
			this.logDebug(3, "Setting up LRU cache", cache_opts);
			this.cache = new Cache( Tools.copyHashRemoveKeys(cache_opts, { enabled: 1 }) );
			this.cache.on('expire', function(item, reason) {
				self.logDebug(9, "Expiring LRU cache object: " + item.key + " due to: " + reason, {
					key: item.key,
					reason: reason,
					totalCount: self.cache.count,
					totalBytes: self.cache.bytes
				});
			});
		}
		
		var db_file = Path.join( this.baseDir, sql_config.filename );
		this.logDebug(3, "Opening database file: " + db_file, sql_config.pragmas || {});
		
		try {
			// open sync connection
			this.db = new BetterSqlite3(db_file);
			
			// optionally set pragmas on the db
			if (sql_config.pragmas) {
				Object.keys(sql_config.pragmas).forEach(function(key) {
					var value = sql_config.pragmas[key];
					// value may be string (e.g. WAL) or number
					self.db.pragma(`${key} = ${value}`);
				});
			}
			
			// create our table if necessary
			this.db.prepare('CREATE TABLE IF NOT EXISTS items( key TEXT PRIMARY KEY, value BLOB, modified INTEGER )').run();
		}
		catch (err) {
			this.logError('sqlite', "FATAL ERROR: Database setup failed: " + err);
			return callback(err);
		}
		
		// behave asynchronously for API compatibility
		process.nextTick(function() {
			self.logDebug(3, "Setup complete");
			callback();
		});
	},
	
	prepKey: function(key) {
		// prepare key based on config
		var md5 = Tools.digestHex(key, 'md5');
		
		if (this.keyPrefix) {
			key = this.keyPrefix + key;
		}
		
		if (this.keyTemplate) {
			var idx = 0;
			var temp = this.keyTemplate.replace( /\#/g, function() {
				return md5.substr(idx++, 1);
			} );
			key = Tools.substitute( temp, { key: key, md5: md5 } );
		}
		
		return key;
	},
	
	put: function(key, value, callback) {
		// store key+value in SQLite
		var self = this;
		var now = Tools.timeNow(true);
		key = this.prepKey(key);
		
		var is_binary = this.storage.isBinaryKey(key);
		
		if (is_binary) {
			this.logDebug(9, "Storing SQLite Binary Object: " + key, '' + value.length + ' bytes');
		}
		else {
			this.logDebug(9, "Storing SQLite JSON Object: " + key, this.debugLevel(10) ? value : null);
			value = Buffer.from( JSON.stringify( value ) );
		}
		
		process.nextTick(function() {
			try {
				self.db.prepare(self.commands.put).run({ key: key, value: value, now: now });
			}
			catch (err) {
				err.message = "Failed to store object: " + key + ": " + err;
				self.logError('sqlite', '' + err);
				if (callback) callback(err);
			}
			
			self.logDebug(9, "Store complete: " + key);
			// possibly cache in LRU
			if (self.cache && !is_binary) {
				self.cache.set( key, value, { date: Tools.timeNow(true) } );
			}
			if (callback) callback(null);
		});
	},
	
	putStream: function(key, inp, callback) {
		// store key+value in SQLite using read stream
		var self = this;
		
		// The SQLite API has no stream support.
		// So, we have to do this the RAM-hard way...
		
		var chunks = [];
		inp.on('data', function(chunk) {
			chunks.push( chunk );
		} );
		inp.on('end', function() {
			var buf = Buffer.concat(chunks);
			self.put( key, buf, callback );
		} );
	},
	
	head: function(key, callback) {
		// head sqlite item given key
		var self = this;
		key = this.prepKey(key);
		
		// check cache first
		if (this.cache && this.cache.has(key)) {
			var item = this.cache.getMeta(key);
			
			process.nextTick( function() {
				self.logDebug(9, "Cached head complete: " + key);
				callback( null, {
					mod: item.date,
					len: item.value.length
				} );
			} );
			return;
		} // cache
		
		process.nextTick(function() {
			var row = null;
			try {
				row = self.db.prepare(self.commands.head).get({ key: key });
			}
			catch (err) {
				err.message = "Failed to head key: " + key + ": " + err;
				self.logError('sqlite', '' + err);
				callback(err);
			}
			
			if (!row) {
				var err = new Error("Failed to head key: " + key + ": Not found");
				err.code = "NoSuchKey";
				return callback(err, null);
			}
			callback(null, { mod: row.modified, len: row['length(value)'] });
		});
	},
	
	get: function(key, callback) {
		// fetch SQLite value given key
		var self = this;
		key = this.prepKey(key);
		
		var is_binary = this.storage.isBinaryKey(key);
		
		// check cache first
		if (this.cache && !is_binary && this.cache.has(key)) {
			var data = this.cache.get(key);
			
			process.nextTick( function() {
				try { data = JSON.parse( data.toString() ); }
				catch (e) {
					self.logError('file', "Failed to parse JSON record: " + key + ": " + e);
					callback( e, null );
					return;
				}
				self.logDebug(9, "Cached JSON fetch complete: " + key, self.debugLevel(10) ? data : null);
				
				callback( null, data );
			} );
			return;
		} // cache
		
		this.logDebug(9, "Fetching SQLite Object: " + key);
		
		process.nextTick(function() {
			var row = null;
			try {
				row = self.db.prepare(self.commands.get).get({ key: key });
			}
			catch (err) {
				err.message = "Failed to fetch key: " + key + ": " + err;
				self.logError('sqlite', '' + err);
				callback(err);
			}
			
			if (!row) {
				var err = new Error("Failed to fetch key: " + key + ": Not found");
				err.code = "NoSuchKey";
				return callback(err, null);
			}
			if (is_binary) {
				self.logDebug(9, "Binary fetch complete: " + key, '' + row.value.length + ' bytes');
				return callback(null, row.value);
			}
			if (self.cache) {
				self.cache.set( key, row.value, { date: Tools.timeNow(true) } );
			}
			var json = null;
			try { json = JSON.parse( row.value.toString() ); }
			catch (err) {
				self.logError('sqlite', "Failed to parse JSON record: " + key + ": " + err);
				return callback(err, null);
			}
			self.logDebug(9, "JSON fetch complete: " + key, self.debugLevel(10) ? json : null);
			callback(null, json);
		});
	},
	
	getBuffer: function(key, callback) {
		// fetch SQLite buffer given key
		var self = this;
		key = this.prepKey(key);
		
		this.logDebug(9, "Fetching SQLite Object: " + key);
		
		process.nextTick(function() {
			var row = null;
			try {
				row = self.db.prepare(self.commands.get).get({ key: key });
			}
			catch (err) {
				err.message = "Failed to fetch key: " + key + ": " + err;
				self.logError('sqlite', '' + err);
				callback(err);
			}
			
			if (!row) {
				var err = new Error("Failed to fetch key: " + key + ": Not found");
				err.code = "NoSuchKey";
				return callback(err, null);
			}
			self.logDebug(9, "Binary fetch complete: " + key, '' + row.value.length + ' bytes');
			callback(null, row.value);
		});
	},
	
	getStream: function(key, callback) {
		// get readable stream to record value given key
		var self = this;
		
		// The SQLite API has no stream support.
		// So, we have to do this the RAM-hard way...
		
		this.get( key, function(err, buf) {
			if (err) {
				// an actual error
				err.message = "Failed to fetch key: " + key + ": " + err;
				self.logError('sqlite', '' + err);
				return callback(err);
			}
			else if (!buf) {
				// record not found
				var err = new Error("Failed to fetch key: " + key + ": Not found");
				err.code = "NoSuchKey";
				return callback( err, null );
			}
			
			var stream = new BufferStream(buf);
			callback(null, stream, { mod: 1, len: buf.length });
		} );
	},
	
	getStreamRange: function(key, start, end, callback) {
		// get readable stream to record value given key and range
		var self = this;
		
		// The SQLite API has no stream support.
		// So, we have to do this the RAM-hard way...
		
		this.get( key, function(err, buf) {
			if (err) {
				// an actual error
				err.message = "Failed to fetch key: " + key + ": " + err;
				self.logError('sqlite', '' + err);
				return callback(err);
			}
			else if (!buf) {
				// record not found
				var err = new Error("Failed to fetch key: " + key + ": Not found");
				err.code = "NoSuchKey";
				return callback( err, null );
			}
			
			// validate byte range, now that we have the head info
			if (isNaN(start) && !isNaN(end)) {
				start = buf.length - end;
				end = buf.length ? buf.length - 1 : 0;
			} 
			else if (!isNaN(start) && isNaN(end)) {
				end = buf.length ? buf.length - 1 : 0;
			}
			if (isNaN(start) || isNaN(end) || (start < 0) || (start >= buf.length) || (end < start) || (end >= buf.length)) {
				download.destroy();
				callback( new Error("Invalid byte range (" + start + '-' + end + ") for key: " + key + " (len: " + buf.length + ")"), null );
				return;
			}
			
			var range = buf.slice(start, end + 1);
			var stream = new BufferStream(range);
			callback(null, stream, { mod: 1, len: buf.length });
		} );
	},
	
	delete: function(key, callback) {
		// delete SQLite key given key
		var self = this;
		key = this.prepKey(key);
		
		this.logDebug(9, "Deleting SQLite Object: " + key);
		
		process.nextTick(function() {
			var info = null;
			try {
				info = self.db.prepare(self.commands.delete).run({ key: key });
			}
			catch (err) {
				self.logError('sqlite', "Failed to delete object: " + key + ": " + err);
				callback(err);
			}
			
			if (!info.changes) {
				var err = new Error("Failed to delete object: " + key + ": Not found");
				err.code = "NoSuchKey";
				return callback(err);
			}
			self.logDebug(9, "Delete complete: " + key);
			if (self.cache && self.cache.has(key)) {
				self.cache.delete(key);
			}
			callback();
		});
	},
	
	runMaintenance: function(callback) {
		// run daily maintenance
		// config.backups: { enabled, dir, filename, compress?, keep? }
		var self = this;
		this.logDebug(3, "Running SQLite maintenance");
		
		var backups = this.config.get('backups') || null;
		if (!backups || !backups.enabled || !backups.dir || !backups.filename) return callback();
		
		// here be dragons: try to wait for a moment BETWEEN transaction commits, to minimize risk of an "inconsistent" backup
		if (this.storage.transactions && Tools.findObject(Object.values(this.storage.transactions), { committing: true })) {
			// wait for next commitEnd event and try again
			this.logDebug(9, "Maintenance: Transaction commit(s) are in progress, waiting until next commitEnd event...");
			
			this.storage.once('commitEnd', function(trans) {
				self.logDebug(9, "Maintenance: Transaction commit " + trans.id + " (" + trans.path + ") ended, retrying now...");
				self.runMaintenance(callback);
			});
			
			return;
		}
		
		// track perf for logging
		var perf = new Perf();
		perf.begin();
		perf.begin('prep');
		
		// allow dir & filename to have date/time placeholders, e.g. `backup-[yyyy]-[mm]-[dd].db`
		var dargs = Tools.getDateArgs( Tools.timeNow() );
		var file = Tools.sub( Path.join(backups.dir, backups.filename), dargs, true );
		if (!file) {
			this.logError('backup', "Failed to expand placeholders on backup file: " + backups.filename);
			return callback();
		}
		
		// strip .gz prefix, just in case the user added it
		file = file.replace(/\.gz$/i, '');
		
		// auto-create parent dirs as needed
		if (!fs.existsSync(backups.dir)) {
			try { Tools.mkdirp.sync(backups.dir); }
			catch (err) {
				this.logError('backup', "Failed to create backup directory: " + backups.dir);
				return callback();
			}
		}
		
		// here we go
		if (fs.existsSync(file)) fs.unlinkSync(file);
		this.logDebug(6, "Performing database backup to: " + file);
		perf.end('prep');
		
		var finish = function() {
			// all done
			perf.end();
			self.logDebug(6, "Maintenance complete", perf.metrics());
			callback();
		};
		
		var keep = function() {
			// delete oldest backups if over N on disk
			var files = Tools.findFilesSync( backups.dir, { stats: true } );
			if (files.length <= backups.keep) return finish();
			perf.begin('keep');
			
			self.logDebug(6, "There are " + files.length + " backup files in " + backups.dir + ", keeping the latest " + backups.keep);
			
			// sort mtime descending so the newest are at the start of the array, then splice those off, leaving only the oldest to delete
			Tools.sortBy( files, 'mtime', { type: 'number', dir: -1 } );
			files.splice( 0, backups.keep );
			
			files.forEach( function(file) {
				self.logDebug(7, "Deleting old backup file: " + file.path, file);
				try { fs.unlinkSync(file.path); } catch (err) {
					self.logError('backup', "Failed to delete backup file: " + file.path + ": " + err);
				}
			} );
			
			perf.end('keep');
			finish();
		}; // keep
		
		var compress = function() {
			// compress backup and delete original
			var gz_file = file + '.gz';
			perf.begin('compress');
			
			if (fs.existsSync(gz_file)) fs.unlinkSync(gz_file);
			self.logDebug(6, "Compressing backup to: " + gz_file);
			
			var gzip = zlib.createGzip();
			var inp = fs.createReadStream( file );
			var outp = fs.createWriteStream( gz_file );
			
			var handleError = function(err) {
				self.logError('backup', "Failed to compress backup: " + gz_file + ": " + err);
				fs.unlink(gz_file, noop);
				
				perf.end('compress');
				if (backups.keep) keep();
				else finish();
			};
			
			gzip.on('error', handleError);
			inp.on('error', handleError);
			outp.on('error', handleError);
			
			inp.pipe(gzip).pipe(outp).on('finish', function() {
				self.logDebug(6, "Backup compression complete: " + gz_file);
				fs.unlink(file, noop);
				
				perf.end('compress');
				if (backups.keep) keep();
				else finish();
			} );
		}; // compress
		
		// Perform the backup using better-sqlite3's async backup API
		// As long as WAL mode is enabled, this should only acquire a shared lock
		perf.begin('backup');
		var db = this.db;
		db.backup(file, {
			progress: function(info) {
				// transfer pages per tick (tuneable)
				return 100;
			}
		})
		.then(function() {
			perf.end('backup');
			self.logDebug(6, "SQLite backup operation completed: " + file);
			// now compress or keep or done
			if (backups.compress) compress();
			else if (backups.keep) keep();
			else finish();
		})
		.catch(function(err) {
			perf.end('backup');
			self.logError('backup', "SQLite backup operation failed.  Please check permissions and available disk space. " + err);
			fs.unlink(file, noop);
			finish();
		});
	},
	
	shutdown: function(callback) {
		// shutdown storage
		var self = this;
		this.logDebug(2, "Shutting down SQLite");
		
		if (this.db) {
			try { this.db.close(); }
			catch (err) { this.logError('sqlite', "Failed to shutdown database cleanly: " + err); }
			this.db = null;
			this.commands = null;
		}
		process.nextTick(function() {
			self.logDebug(3, "Shutdown complete");
			callback();
		});
	}
	
});

// Modified the following snippet from node-streamifier:
// Copyright (c) 2014 Gabriel Llamas, MIT Licensed

var util = require('util');
var stream = require('stream');

var BufferStream = function (object, options) {
	if (object instanceof Buffer || typeof object === 'string') {
		options = options || {};
		stream.Readable.call(this, {
			highWaterMark: options.highWaterMark,
			encoding: options.encoding
		});
	} else {
		stream.Readable.call(this, { objectMode: true });
	}
	this._object = object;
};

util.inherits(BufferStream, stream.Readable);

BufferStream.prototype._read = function () {
	this.push(this._object);
	this._object = null;
};
```

## File: `index_types/Date.js`
```javascript
// PixlServer Storage System - Date Index Type Mixin
// Copyright (c) 2016 Joseph Huckaby
// Released under the MIT License

// A "Date" is a compound word index, where the YYYY, MM and DD values are 
// indexed as three separate words: YYYY_MM_DD, YYYY_MM, and YYYY.

// Date Ranges are queried by loading the summary (master_list) and OR'ing in 
// all records in relevant buckets.

var util = require("util");
var async = require('async');
var Class = require("pixl-class");
var Tools = require("pixl-tools");

// utility
var parseDate = function(str) {
	// parse YYYY_MM_DD, YYYY_MM or YYYY specifically
	var args = {};
	if (str.match(/^(\d{4})_(\d{2})_(\d{2})$/)) {
		args.yyyy = RegExp.$1; args.mm = RegExp.$2; args.dd = RegExp.$3;
		args.yyyy_mm = args.yyyy + '_' + args.mm;
	}
	else if (str.match(/^(\d{4})_(\d{2})$/)) { 
		args.yyyy = RegExp.$1; args.mm = RegExp.$2; 
		args.yyyy_mm = args.yyyy + '_' + args.mm;
	}
	else if (str.match(/^(\d{4})$/)) { 
		args.yyyy = RegExp.$1; 
	}
	else args = null;
	return args;
};

module.exports = Class.create({
	
	prepIndex_date: function(words, def, state) {
		// prep index write for date type
		// dates always require a master_list (summary)
		def.master_list = 1;
		
		// if (!words || !words.length) return false;
		var unique_words = {};
		var good = false;
		
		words.forEach( function(date) {
			if (date.match(/^(\d{4})_(\d{2})_(\d{2})$/)) {
				var yyyy = RegExp.$1;
				var mm = RegExp.$2;
				var dd = RegExp.$3;
				
				unique_words[ yyyy + '_' + mm + '_' + dd ] = 1;
				unique_words[ yyyy + '_' + mm ] = 1;
				unique_words[ yyyy ] = 1;
				good = true;
			}
		});
		
		return Tools.hashKeysToArray(unique_words);
	},
	
	prepDeleteIndex_date: function(words, def, state) {
		// prep for index delete (no return value)
		
		// dates require a master_list (summary)
		def.master_list = 1;
	},
	
	filterWords_date: function(orig_value) {
		// filter date queries
		return orig_value.trim().replace(/\,/g, ' ').split(/\s+/).map( function(value) {
			if (!value.match(/\S/)) return '';
			
			// MM/DD/YYYY --> YYYY_MM_DD
			// FUTURE: This is a very US-centric format assumption here
			if (value.match(/^(\d{2})\D+(\d{2})\D+(\d{4})$/)) {
				value = RegExp.$3 + '_' + RegExp.$1 + '_' + RegExp.$2;
			}
			
			// special search month/year formats
			else if (value.match(/^(\d{4})\D+(\d{2})$/)) { value = RegExp.$1 + '_' + RegExp.$2; }
			else if (value.match(/^(\d{4})$/)) { value = RegExp.$1; }
			
			// special search keywords
			else if (value.match(/^(today|now)$/i)) {
				var dargs = Tools.getDateArgs( Tools.timeNow(true) );
				value = dargs.yyyy_mm_dd;
			}
			else if (value.match(/^(yesterday)$/i)) {
				var midnight = Tools.normalizeTime( Tools.timeNow(true), { hour:0, min:0, sec:0 } );
				var yesterday_noonish = midnight - 43200;
				var dargs = Tools.getDateArgs( yesterday_noonish );
				value = dargs.yyyy_mm_dd;
			}
			else if (value.match(/^(this\s+month)$/i)) {
				var dargs = Tools.getDateArgs( Tools.timeNow(true) );
				value = dargs.yyyy + '_' + dargs.mm;
			}
			else if (value.match(/^(this\s+year)$/i)) {
				var dargs = Tools.getDateArgs( Tools.timeNow(true) );
				value = dargs.yyyy;
			}
			else if (value.match(/^\d+(\.\d+)?$/)) {
				// convert epoch date (local server timezone)
				var epoch = parseInt(value);
				if (!epoch) return '';
				var dargs = Tools.getDateArgs( epoch );
				value = dargs.yyyy_mm_dd;
			}
			else if (!value.match(/^(\d{4})\D+(\d{2})\D+(\d{2})$/)) {
				// try to convert using node date (local timezone)
				var dargs = Tools.getDateArgs( value + " 00:00:00" );
				value = dargs.epoch ? dargs.yyyy_mm_dd : '';
			}
			
			value = value.replace(/\D+/g, '_');
			return value;
		} ).join(' ').replace(/\s+/g, ' ').trim();
	},
	
	searchIndex_date: function(query, state, callback) {
		// search date index
		var self = this;
		var record_ids = state.record_ids;
		var word = query.word || query.words[0];
		var base_path = state.config.base_path + '/' + query.def.id;
		var sum_path = base_path + '/summary';
		var temp_results = {};
		var words = [];
		
		if (!query.operator) query.operator = '=';
		
		this.logDebug(10, "Running date query", query);
		
		word = word.replace(/\D+/g, '_');
		query.word = word;
		
		if (word.match(/^\d{5,}$/)) {
			// epoch date (local server timezone)
			var dargs = Tools.getDateArgs( parseInt(word) );
			word = dargs.yyyy + '_' + dargs.mm + '_' + dargs.dd;
			query.word = word;
		}
		
		// check for simple equals
		if (query.operator == '=') {
			return this.searchWordIndex(query, state, callback);
		}
		
		// adjust special month/date search tricks for first of month/year
		if (word.match(/^(\d{4})_(\d{2})$/)) word += "_01";
		else if (word.match(/^(\d{4})$/)) word += "_01_01";
		query.word = word;
		
		// syntax check
		var date = parseDate(word);
		if (!date) {
			return callback( new Error("Invalid date format: " + word) );
		}
		
		// load index summary for list of all populated dates
		var dspf = state.perf.begin('date_summary');
		this.get( sum_path, function(err, summary) {
			dspf.end();
			if (err || !summary) {
				summary = { id: query.def.id, values: {} };
			}
			var values = summary.values;
			var lesser = !!query.operator.match(/</);
			
			// operator includes exact match
			if (query.operator.match(/=/)) words.push( word );
			
			// add matching date tags based on operator
			for (var value in values) {
				var temp = parseDate(value) || {};
				if (temp.dd) {
					// only compare if yyyy and mm match
					if (temp.yyyy_mm == date.yyyy_mm) {
						if (lesser) { if (value < word) words.push(value); }
						else { if (value > word) words.push(value); }
					}
				}
				else if (temp.mm) {
					if (lesser) { if (temp.yyyy_mm < date.yyyy_mm) words.push(value); }
					else { if (temp.yyyy_mm > date.yyyy_mm) words.push(value); }
				}
				else if (temp.yyyy) {
					if (lesser) { if (temp.yyyy < date.yyyy) words.push(value); }
					else { if (temp.yyyy > date.yyyy) words.push(value); }
				}
			}
			
			// now perform OR search for all applicable words
			var drpf = state.perf.begin('date_range');
			async.eachLimit( words, self.concurrency,
				function(word, callback) {
					// for each word, iterate over record ids
					self.hashEachPage( base_path + '/word/' + word,
						function(items, callback) {
							for (var record_id in items) temp_results[record_id] = 1;
							callback();
						},
						callback
					); // hashEachPage
				},
				function(err) {
					// all done, perform final merge
					drpf.end();
					state.perf.count('date_buckets', words.length);
					if (err) return callback(err);
					self.mergeIndex( record_ids, temp_results, state.first ? 'or' : state.mode );
					state.first = false;
					callback();
				}
			); // eachSeries
		} ); // get (summary)
	},
	
	searchSingle_date: function(query, record_id, idx_data, state) {
		// search date index vs single record (sync)
		var self = this;
		var record_ids = state.record_ids;
		var word = query.word || query.words[0];
		var def = query.def;
		var temp_results = {};
		var words = [];

		if (!query.operator) query.operator = '=';
		
		word = word.replace(/\D+/g, '_');
		query.word = word;
		
		if (word.match(/^\d{5,}$/)) {
			// epoch date (local server timezone)
			var dargs = Tools.getDateArgs( parseInt(word) );
			word = dargs.yyyy + '_' + dargs.mm + '_' + dargs.dd;
			query.word = word;
		}
		
		// check for simple equals
		if (query.operator == '=') {
			this._searchSingleWordIndex( query, record_id, idx_data, state );
			return;
		}
		
		// adjust special month/date search tricks for first of month/year
		if (word.match(/^(\d{4})_(\d{2})$/)) word += "_01";
		else if (word.match(/^(\d{4})$/)) word += "_01_01";
		query.word = word;
		
		// syntax check
		var date = parseDate(word);
		if (!date) {
			this.logError('index', "Invalid date format: " + word);
			return;
		}
		
		// create "fake" summary index for record
		var summary = { id: def.id, values: {} };
		if (idx_data[def.id] && idx_data[def.id].word_hash) {
			summary.values = idx_data[def.id].word_hash;
		}
		
		var values = summary.values;
		var lesser = !!query.operator.match(/</);
		
		// operator includes exact match
		if (query.operator.match(/=/)) words.push( word );
		
		// add matching date tags based on operator
		for (var value in values) {
			var temp = parseDate(value) || {};
			if (temp.dd) {
				// only compare if yyyy and mm match
				if (temp.yyyy_mm == date.yyyy_mm) {
					if (lesser) { if (value < word) words.push(value); }
					else { if (value > word) words.push(value); }
				}
			}
			else if (temp.mm) {
				if (lesser) { if (temp.yyyy_mm < date.yyyy_mm) words.push(value); }
				else { if (temp.yyyy_mm > date.yyyy_mm) words.push(value); }
			}
			else if (temp.yyyy) {
				if (lesser) { if (temp.yyyy < date.yyyy) words.push(value); }
				else { if (temp.yyyy > date.yyyy) words.push(value); }
			}
		}
		
		// now perform OR search for all applicable words
		words.forEach( function(word) {
			// create "fake" hash index for word, containing only our one record
			var items = {};
			if (idx_data[def.id] && idx_data[def.id].word_hash && idx_data[def.id].word_hash[word]) {
				items[ record_id ] = idx_data[def.id].word_hash[word];
			}
			
			for (var key in items) temp_results[key] = 1;
		} );
		
		this.mergeIndex( record_ids, temp_results, state.first ? 'or' : state.mode );
		state.first = false;
	}
	
});
```

## File: `index_types/Number.js`
```javascript
// PixlServer Storage System - Number Index Type Mixin
// Copyright (c) 2016 Joseph Huckaby
// Released under the MIT License

// A "Number" is a compound word index, where the value is split into multiple buckets (powers of 10)
// Example, 1536 is indexed as: 1536, T1000, H1500
// Another example: 5 is indexed as: 5, T0, H0
// This currently only works for integers, and is not very efficient for large numbers.
// This is better suited for counting smaller things, like the number of comments or 'likes' on a record.

// Number Ranges are queried by loading the summary (master_list) and OR'ing in 
// all records in relevant buckets.

var util = require("util");
var async = require('async');
var Class = require("pixl-class");
var Tools = require("pixl-tools");

var NUMBER_INDEX_MIN = -1000000;
var NUMBER_INDEX_MAX = 1000000;

// utility
var parseNumber = function(str) {
	// parse number, H# or T# keys
	var args = {};
	if (str.match(/^(N?)(\d+)$/)) {
		var neg = !!RegExp.$1;
		var value = parseInt( RegExp.$2 );
		args.value = value * (neg ? -1 : 1);
		args.tvalue = Math.floor( Math.floor(value / 1000) * 1000 ) * (neg ? -1 : 1);;
		args.hvalue = Math.floor( Math.floor(value / 100) * 100 ) * (neg ? -1 : 1);;
		args.exact = 1;
	}
	else if (str.match(/^H(N?)(\d+)$/)) {
		var neg = !!RegExp.$1;
		var value = parseInt( RegExp.$2 ) * (neg ? -1 : 1);
		args.hvalue = value;
		args.hundreds = 1;
	}
	else if (str.match(/^T(N?)(\d+)$/)) {
		var neg = !!RegExp.$1;
		var value = parseInt( RegExp.$2 ) * (neg ? -1 : 1);
		args.tvalue = value;
		args.thousands = 1;
	}
	else args = null;
	return args;
};

module.exports = Class.create({
	
	prepIndex_number: function(words, def, state) {
		// prep index write for number type
		var value = words[0] || '';
		words = [];
		
		// numbers always require a master_list (summary)
		def.master_list = 1;
		
		if (value.match(/^(N?)(\d+)$/i)) {
			var neg = RegExp.$1.toUpperCase();
			var value = Math.floor( parseInt( RegExp.$2 ) * (def.multiply || 1) / (def.divide || 1) );
			value = Math.min( NUMBER_INDEX_MAX, value );
			
			var tkey = 'T' + neg + Math.floor( Math.floor(value / 1000) * 1000 );
			var hkey = 'H' + neg + Math.floor( Math.floor(value / 100) * 100 );
			
			words.push( neg + value );
			words.push( hkey );
			words.push( tkey );
			
			return words;
		}
		else return false;
	},
	
	prepDeleteIndex_number: function(words, def, state) {
		// prep for index delete (no return value)
		
		// numbers require a master_list (summary)
		def.master_list = 1;
	},
	
	filterWords_number: function(value) {
		// filter number queries
		
		// support simple date-to-epoch conversion here
		if (value.match(/^(\d{4})\D+(\d{2})\D+(\d{2})$/)) {
			var dargs = Tools.getDateArgs( value + " 00:00:00" );
			value = '' + (dargs.epoch || 0);
		}
		else if (value.match(/^(today)$/)) {
			// normalize "today" to midnight today (server timezone)
			var midnight = Tools.normalizeTime( Tools.timeNow(true), { hour:0, min:0, sec:0 } );
			var dargs = Tools.getDateArgs( midnight );
			value = '' + (dargs.epoch || 0);
		}
		else if (value.match(/^(now)$/)) {
			var dargs = Tools.getDateArgs( Tools.timeNow(true) );
			value = '' + (dargs.epoch || 0);
		}
		
		value = value.replace(/\.\d+$/, '').replace(/[^\d\-]+/g, '').replace(/\-/, 'N');
		return value;
	},
	
	searchIndex_number: function(query, state, callback) {
		// search number index
		var self = this;
		var record_ids = state.record_ids;
		var word = query.word;
		var base_path = state.config.base_path + '/' + query.def.id;
		var sum_path = base_path + '/summary';
		var temp_results = {};
		var words = [];
		
		if (!query.operator) query.operator = '=';
		
		this.logDebug(10, "Running number query", query);
		
		// clean number up
		word = word.replace(/^N/i, '-').replace(/[^\d\-]+/g, '');
		word = '' + Math.min( NUMBER_INDEX_MAX, Math.max( NUMBER_INDEX_MIN, Math.floor( parseInt(word) * (query.def.multiply || 1) / (query.def.divide || 1) ) ) );
		word = word.replace(/\-/, 'N');
		query.word = word;
		
		// syntax check
		var num = parseNumber(word);
		if (!num) {
			return callback( new Error("Invalid number format: " + word) );
		}
		
		// check for simple equals
		if (query.operator == '=') {
			return this.searchWordIndex(query, state, callback);
		}
		
		// load index summary for list of all populated numbers
		var nspf = state.perf.begin('number_summary');
		this.get( sum_path, function(err, summary) {
			nspf.end();
			if (err || !summary) {
				summary = { id: query.def.id, values: {} };
			}
			var values = summary.values;
			var lesser = !!query.operator.match(/</);
			
			// operator includes exact match
			if (query.operator.match(/=/)) words.push( word );
			
			// add matching number tags based on operator
			for (var value in values) {
				var temp = parseNumber(value) || {};
				if (temp.exact) {
					// only compare if T and H match
					if (temp.hvalue == num.hvalue) {
						if (lesser) { if (temp.value < num.value) words.push(value); }
						else { if (temp.value > num.value) words.push(value); }
					}
				}
				else if (temp.hundreds) {
					if (lesser) { if (temp.hvalue < num.hvalue) words.push(value); }
					else { if (temp.hvalue > num.hvalue) words.push(value); }
				}
				else if (temp.thousands) {
					if (lesser) { if (temp.tvalue < num.tvalue) words.push(value); }
					else { if (temp.tvalue > num.tvalue) words.push(value); }
				}
			}
			
			// now perform OR search for all applicable words
			var nrpf = state.perf.begin('number_range');
			async.eachLimit( words, self.concurrency,
				function(word, callback) {
					// for each word, iterate over record ids
					self.hashEachPage( base_path + '/word/' + word,
						function(items, callback) {
							for (var record_id in items) temp_results[record_id] = 1;
							callback();
						},
						callback
					); // hashEachPage
				},
				function(err) {
					// all done, perform final merge
					nrpf.end();
					state.perf.count('number_buckets', words.length);
					if (err) return callback(err);
					self.mergeIndex( record_ids, temp_results, state.first ? 'or' : state.mode );
					state.first = false;
					callback();
				}
			); // eachSeries
		} ); // get (summary)
	},
	
	searchSingle_number: function(query, record_id, idx_data, state) {
		// search number index vs single record (sync)
		var self = this;
		var record_ids = state.record_ids;
		var word = query.word;
		var temp_results = {};
		var words = [];
		var def = query.def;
		
		if (!query.operator) query.operator = '=';
		
		// clean number up
		word = word.replace(/^N/i, '-').replace(/[^\d\-]+/g, '');
		word = '' + Math.min( NUMBER_INDEX_MAX, Math.max( NUMBER_INDEX_MIN, Math.floor( parseInt(word) * (query.def.multiply || 1) / (query.def.divide || 1) ) ) );
		word = word.replace(/\-/, 'N');
		query.word = word;
		
		// syntax check
		var num = parseNumber(word);
		if (!num) {
			this.logError('index', "Invalid number format: " + word);
			return;
		}
		
		// check for simple equals
		if (query.operator == '=') {
			this._searchSingleWordIndex( query, record_id, idx_data, state );
			return;
		}
		
		// create "fake" summary index for record
		var summary = { id: def.id, values: {} };
		if (idx_data[def.id] && idx_data[def.id].word_hash) {
			summary.values = idx_data[def.id].word_hash;
		}
		
		var values = summary.values;
		var lesser = !!query.operator.match(/</);
		
		// operator includes exact match
		if (query.operator.match(/=/)) words.push( word );
		
		// add matching number tags based on operator
		for (var value in values) {
			var temp = parseNumber(value) || {};
			if (temp.exact) {
				// only compare if T and H match
				if (temp.hvalue == num.hvalue) {
					if (lesser) { if (temp.value < num.value) words.push(value); }
					else { if (temp.value > num.value) words.push(value); }
				}
			}
			else if (temp.hundreds) {
				if (lesser) { if (temp.hvalue < num.hvalue) words.push(value); }
				else { if (temp.hvalue > num.hvalue) words.push(value); }
			}
			else if (temp.thousands) {
				if (lesser) { if (temp.tvalue < num.tvalue) words.push(value); }
				else { if (temp.tvalue > num.tvalue) words.push(value); }
			}
		}
		
		// now perform OR search for all applicable words
		words.forEach( function(word) {
			// create "fake" hash index for word, containing only our one record
			var items = {};
			if (idx_data[def.id] && idx_data[def.id].word_hash && idx_data[def.id].word_hash[word]) {
				items[ record_id ] = idx_data[def.id].word_hash[word];
			}
			
			for (var key in items) temp_results[key] = 1;
		} );
		
		this.mergeIndex( record_ids, temp_results, state.first ? 'or' : state.mode );
		state.first = false;
	}
	
});
```

## File: `test/config.json`
```json
{
	"log_dir": ".",
	"log_filename": "storage.log",
	"debug_level": 9,
	"debug": 1,
	"echo": 0,
	
	"Storage": {
		"engine": "Filesystem",
		"list_page_size": 10,
		"concurrency": 4,
		"cache_key_match": "",
		"expiration_updates": true,
		"transactions": 0,
		"log_event_types": { "all": 1 },
		
		"Filesystem": {
			"base_dir": "data",
			"key_namespaces": 0,
			"raw_file_paths": 0,
			"no_fsync": 1,
			"cache": {
				"enabled": true,
				"maxItems": 1000,
				"maxBytes": 10485760
			}
		},
		"AWS": {
			"region": "us-west-1",
			"credentials": {
				"accessKeyId": "YOUR_AMAZON_ACCESS_KEY", 
				"secretAccessKey": "YOUR_AMAZON_SECRET_KEY"
			}
		},
		"S3": {
			"connectTimeout": 5000,
			"socketTimeout": 5000,
			"maxAttempts": 50,
			"keyPrefix": "",
			"fileExtensions": true,
			"params": {
				"Bucket": "MY_S3_BUCKET_ID"
			},
			"cache": {
				"enabled": true,
				"maxItems": 1000,
				"maxBytes": 10485760
			}
		},
		"Couchbase": {
			"connectString": "couchbase://127.0.0.1",
			"bucket": "default",
			"password": "",
			"serialize": false,
			"keyPrefix": ""
		},
		"Redis": {
			"host": "127.0.0.1",
			"port": 6379,
			"keyPrefix": ""
		},
		"RedisCluster": {
			"host": "127.0.0.1",
			"port": 6379,
			"keyPrefix": ""
		},
		"SQLite": {
			"base_dir": "data",
			"filename": "sqlite.db",
			"pragmas": {
				"auto_vacuum": 0,
				"cache_size": -100000,
				"journal_mode": "WAL"
			},
			"cache": {
				"enabled": true,
				"maxItems": 1000,
				"maxBytes": 10485760
			},
			"backups": {
				"enabled": true,
				"dir": "data/backups",
				"filename": "backup-[yyyy]-[mm]-[dd]-[hh]-[mi]-[ss].db",
				"compress": true,
				"keep": 7
			}
		}
	}
}
```

## File: `test/sample-data.json`
```json
{
  "Ticket": [
    {
      "Assignedto": "dsmith",
      "Rfaccount": "_none_",
      "Environment": "Production",
      "Description": "SAMPLE PRODUCT 1.7.70 BUILD 1\nThis is an official release of Sample Product 1.7.70. This is build number 1. New features and changes are listed below.\n\nBUILD SUMMARY\n(See the release notes)\n\nNEW FEATURES / CHANGES\nOptimized implementation of cross-device profile merging in the Sample Library. See Sample Library Release Notes ( https://mydocs.net/document/d/1kZC1GiuF9zmDv6d5bkFGMW_eBIs8ItefJbUPh1Q2Erk/edit#bookmark=kix.ej2bhezbvjhf ) for details.\n\nBUG FIXES\n(See the release notes)\n\nGIT COMMITS\n(See the release notes)\n\nDOCUMENTATION\nSample Product Release Notes ( http://build.dev.company.net/releases/sampleproduct/1.7.70/ )\n\nbuild Build Report ( http://build.dev.company.net/build/?build_report=2wzbkvz9st )\n\nUnit Test Report ( http://build.dev.company.net/abc/data/util/releasemgr/rolls/2wzbkvz9st/unit.txt )\n\n\nREQUIREMENTS\nList any external dependencies here, such as another product release.\n\nINSTALLATION\n\nPreproduction\nsudo roll preprod x --import 2wzbkvz9st --save b4sampleproduct_1.7.70 --upgrade\n\nLive Production\nsudo roll live-prod x --import 2wzbkvz9st --save b4sampleproduct_1.7.70 --upgrade\n\n\nOpen Issues\n\nNone\n\nCopyright (c) 2016 My Company, LLC.  Confidential.",
      "Comments": {
        "Comment": [
          {
            "Date": "1455917142",
            "Id": "14559171421881",
            "Text": "Rolled to Preproduction.",
            "Username": "dsmith"
          },
          {
            "Date": "1456421696",
            "Id": "14564216963209",
            "Text": "ready for prod",
            "Username": "dsmith"
          },
          {
            "Date": "1456422035",
            "Text": "rolled to prod with kittens",
            "Username": "jhuckaby",
            "Id": "14564220358621"
          },
          {
            "Id": "14564229458651",
            "Text": "done in prod",
            "Username": "dsmith",
            "Date": "1456422945"
          }
        ]
      },
      "Priority": "Medium",
      "Completeby": "1456422945",
      "ID": "2653",
      "Status": "Open",
      "History": {
        "Event": [
          {
            "Description": "Dev Complete",
            "Tag": "Build 1",
            "Username": "dsmith",
            "Id": "14559168836745",
            "Date": "1455916883",
            "Comment": ""
          },
          {
            "Comment": "",
            "Date": "1455917142",
            "Id": "14559171421881",
            "Username": "dsmith",
            "Tag": "Build 1",
            "Description": "Preprod Release"
          },
          {
            "Description": "completeby=February 26, 2016|March 2, 2016;description=changed",
            "Username": "api",
            "Date": "1456356075"
          },
          {
            "Username": "dsmith",
            "Tag": "Build 1",
            "Description": "Prod Release",
            "Id": "14564216963206",
            "Date": "1456421696",
            "Comment": ""
          },
          {
            "Date": "1456421696",
            "Description": "assignedto=dsmith|jhuckaby;environment=Preproduction|Production",
            "Username": "api"
          },
          {
            "Date": "1456422036",
            "Description": "assignedto=jhuckaby|dsmith",
            "Username": "api"
          }
        ]
      },
      "Createdate": "1455916883",
      "Summary": "Sample Product 1.7.70 Released to Preproduction",
      "Customer": "_none_",
      "Ccemail": ", dsmith",
      "Modifydate": "1456422945",
      "Submittedby": "dsmith"
    },
    
    {
      "ID": "2654",
      "Comments": {
        "Comment": [
          {
            "Text": "Rolled to Preproduction.",
            "Username": "dsmith",
            "Id": "14559172477856",
            "Date": "1455917247"
          },
          {
            "Username": "dsmith",
            "Text": "Rolled to Preproduction.",
            "Id": "14563551670986",
            "Date": "1456355167"
          },
          {
            "Date": "1456420253",
            "Id": "14564202538017",
            "Text": "ready for prod",
            "Username": "dsmith"
          },
          {
            "Date": "1456420619",
            "Username": "jhuckaby",
            "Text": "rolled to prod",
            "Id": "14564206196519"
          },
          {
            "Date": "1456421665",
            "Id": "14564216650695",
            "Username": "dsmith",
            "Text": "done in prod"
          }
        ]
      },
      "Priority": "Medium",
      "Completeby": "1456421665",
      "Description": "Sample SERVICE 1.1.38 BUILD 1\nThis is an official release of Sample Service 1.1.38 to Preproduction.  This is build number 1.  New features and changes are listed below. \n\nBUILD SUMMARY\n(See the release notes)\n\nNEW FEATURES / CHANGES\nOptimized implementation of cross-device profile merging in the Sample Library. See Sample Library Release Notes ( https://mydocs.net/document/d/1kZC1GiuF9zmDv6d5bkFGMW_eBIs8ItefJbUPh1Q2Erk/edit#bookmark=kix.ej2bhezbvjhf ) for details.\n\nBUG FIXES\n(See the release notes)\n\nGIT COMMITS\n(See the release notes)\n\nDOCUMENTATION\nSample Service Release Notes ( http://build.dev.company.net/releases/Sampleservice/1.1.38/ )\n\nbuild Build Report ( http://build.dev.company.net/build/?build_report=hzd86vdxtd )\n\nUnit Test Report ( http://build.dev.company.net/abc/data/util/releasemgr/rolls/hzd86vdxtd/unit.txt )\n\n\nREQUIREMENTS\nList any external dependencies here, such as another product release.\n\nINSTALLATION\n\nPreproduction\nsudo roll preprod x --import hzd86vdxtd --save b4Sampleservice_1.1.38 --upgrade\n\nLive Production\nsudo roll live-prod x --import hzd86vdxtd --save b4Sampleservice_1.1.38 --upgrade\n\n\nOPEN ISSUES\nNone\n\nCopyright (c) 2016 MyCompany, Inc.  Confidential.",
      "Environment": "Production",
      "Rfaccount": "_none_",
      "Assignedto": "dsmith",
      "Submittedby": "dsmith",
      "Modifydate": "1456421665",
      "Ccemail": "rthomas",
      "Customer": "_none_",
      "Summary": "Sample Service 1.1.38 Released to Preproduction hzd86vdxtd",
      "Status": "Open",
      "History": {
        "Event": [
          {
            "Id": "14559171616402",
            "Tag": "Build 1",
            "Description": "Dev Complete",
            "Username": "dsmith",
            "Comment": "",
            "Date": "1455917161"
          },
          {
            "Date": "1455917247",
            "Comment": "",
            "Username": "dsmith",
            "Tag": "Build 1",
            "Description": "Preprod Release",
            "Id": "14559172477856"
          },
          {
            "Description": "ccemail=, dsmith|rthomas;completeby=February 26, 2016|March 2, 2016;description=changed",
            "Username": "api",
            "Date": "1456355061"
          },
          {
            "Username": "dsmith",
            "Description": "Preprod Release",
            "Tag": "Build 1",
            "Id": "14563551670986",
            "Date": "1456355167",
            "Comment": ""
          },
          {
            "Id": "14564202538014",
            "Username": "dsmith",
            "Tag": "Build 1",
            "Description": "Prod Release",
            "Comment": "",
            "Date": "1456420253"
          },
          {
            "Username": "api",
            "Description": "assignedto=dsmith|jhuckaby;environment=Preproduction|Production",
            "Date": "1456420254"
          },
          {
            "Username": "api",
            "Description": "assignedto=jhuckaby|dsmith",
            "Date": "1456420619"
          }
        ]
      },
      "Createdate": "1455917161"
    },
    
    {
      "Rfaccount": "_none_",
      "Assignedto": "dsmith",
      "ID": "2655",
      "Completeby": "1456423621",
      "Priority": "Medium",
      "Comments": {
        "Comment": [
          {
            "Date": "1455924170",
            "Id": "1455924170653",
            "Text": "Rolled to Preproduction.",
            "Username": "dsmith"
          },
          {
            "Date": "1456341599",
            "Username": "dsmith",
            "Text": "Rolled to Preproduction.",
            "Id": "14563415995226"
          },
          {
            "Date": "1456353963",
            "Id": "14563539634553",
            "Username": "dsmith",
            "Text": "Rolled to Preproduction."
          },
          {
            "Date": "1456423142",
            "Id": "14564231427161",
            "Username": "dsmith",
            "Text": "ready for prod"
          },
          {
            "Text": "rolled to prod",
            "Username": "jhuckaby",
            "Id": "14564235422873",
            "Date": "1456423542"
          },
          {
            "Date": "1456423621",
            "Id": "14564236210221",
            "Text": "done in prod",
            "Username": "dsmith"
          }
        ]
      },
      "Description": "Mapper 1.8.10 BUILD 1\nThis is an official release of Mapper 1.8.10 to QA for a testing pass.  This is build number 1.  New features and changes are listed below.  This release is code and feature complete, and fulfills all the requirements in the ERD.\n\nBUILD SUMMARY\n(See the release notes)\n\nNEW FEATURES / CHANGES\nOptimized implementation of cross-device profile merging in the Sample Library. See Sample Library Release Notes ( https://mydocs.net/document/d/1kZC1GiuF9zmDv6d5bkFGMW_eBIs8ItefJbUPh1Q2Erk/edit#bookmark=kix.ej2bhezbvjhf ) for details.\n\nBUG FIXES\n(See the release notes)\n\nGIT COMMITS\n(See the release notes)\n\nDOCUMENTATION\nMapper Release Notes ( http://build.dev.company.net/releases/Mapper/1.8.10/ )\n\nbuild Build Report ( http://build.dev.company.net/build/?build_report=jz592s8z29 )\n\nUnit Test Report ( http://build.dev.company.net/abc/data/util/releasemgr/rolls/jz592s8z29/unit.txt )\n\nPrevious Release Notes ( https://mydocs.net/a/test.cyangroup.com/document/d/1KOlisbyGvWd7EjprlhzdCbirJnoUnhY17FHR7ijO--M/edit )\n\n\nREQUIREMENTS\nList any external dependencies here, such as another product release.\n\nINSTALLATION\n\nPreproduction\nsudo roll preprod x --import jz592s8z29 --save b4Mapper_1.8.10 --upgrade\n\nLive Production\nsudo roll live-prod x --import jz592s8z29 --save b4Mapper_1.8.10 --upgrade\n\n\nOPEN ISSUES\nNone\n\nCopyright (c) 2016 MyCompany, Inc.  Confidential.",
      "Environment": "Production",
      "Summary": "Mapper 1.8.10 Released",
      "Status": "Closed",
      "History": {
        "Event": [
          {
            "Date": "1455924107",
            "Comment": "",
            "Username": "dsmith",
            "Description": "Dev Complete",
            "Tag": "Build 1",
            "Id": "1455924107864"
          },
          {
            "Comment": "",
            "Date": "1455924170",
            "Id": "14559241706529",
            "Username": "dsmith",
            "Tag": "Build 1",
            "Description": "Preprod Release"
          },
          {
            "Date": "1456341499",
            "Description": "assignedto=ebrown|dsmith;completeby=February 26, 2016|March 2, 2016;description=changed",
            "Username": "api"
          },
          {
            "Username": "dsmith",
            "Tag": "Build 1",
            "Description": "Preprod Release",
            "Id": "14563415995225",
            "Date": "1456341599",
            "Comment": ""
          },
          {
            "Date": "1456353888",
            "Description": "description=changed",
            "Username": "api"
          },
          {
            "Tag": "Build 1",
            "Description": "Preprod Release",
            "Username": "dsmith",
            "Id": "14563539634552",
            "Date": "1456353963",
            "Comment": ""
          },
          {
            "Comment": "",
            "Date": "1456423142",
            "Id": "14564231427158",
            "Description": "Prod Release",
            "Tag": "Build 1",
            "Username": "dsmith"
          },
          {
            "Date": "1456423142",
            "Username": "api",
            "Description": "assignedto=dsmith|jhuckaby;environment=Preproduction|Production"
          },
          {
            "Description": "assignedto=jhuckaby|dsmith",
            "Username": "api",
            "Date": "1456423542"
          },
          {
            "Date": "1456423621",
            "Description": "status=Open|Closed;completeby=March 2, 2016|February 25, 2016",
            "Username": "api"
          }
        ]
      },
      "Createdate": "1455924107",
      "Submittedby": "dsmith",
      "Modifydate": "1456423621",
      "Ccemail": "ebrown, dsmith",
      "Customer": "_none_"
    },
    
    {
      "Ccemail": "_none_",
      "Customer": "_none_",
      "Submittedby": "jhuckaby",
      "Modifydate": "1456164397",
      "Status": "Closed",
      "History": {
        "Event": [
          {
            "Username": "jhuckaby",
            "Description": "Opened",
            "Tag": "Build 1",
            "Id": "1456164267925",
            "Date": "1456164367"
          },
          {
            "Id": "1456164365626",
            "Username": "jhuckaby",
            "Tag": "Build 1",
            "Description": "Prod Release",
            "Comment": "",
            "Date": "1456164367"
          },
          {
            "Username": "jhuckaby",
            "Description": "_custom=Added event: Prod Release (Build 1)",
            "Date": "1456164367"
          },
          {
            "Date": "1456164397",
            "Username": "api",
            "Description": "status=New|Closed"
          }
        ]
      },
      "Createdate": "1456164367",
      "Summary": "Update config.xml to allow for Amazon monitor servers in ACL",
      "Description": "We have two Amazon monitor servers with static IPs which need to be able to send requests to ACL protected API endpoints.  This update covers that.\n\nGit Commit:\nhttp://source.dev.company.net/git/?p=dev/env.git;a=commitdiff;h=4f720f1\n\nProd Roll:\nroll prod w x t mgr mtx --import env config.xml --install env config.xml\n\n- Joe",
      "Environment": "Production",
      "Completeby": "1456164397",
      "Priority": "High",
      "Comments": {
        "Comment": [{
          "Date": "1456164397",
          "Id": "14561643975777",
          "Text": "rolled",
          "Username": "jhuckaby"
        }]
      },
      "ID": "2656",
      "Assignedto": "jhuckaby",
      "Rfaccount": "_none_"
    },
    
    {
      "Rfaccount": "_none_",
      "Assignedto": "jhuckaby",
      "ID": "2657",
      "Completeby": "1456387200",
      "Comments": {
        "Comment": [
          {
            "Date": "1456188357",
            "Id": "14561883571713",
            "Text": "Rolled to Preproduction.",
            "Username": "jhuckaby"
          },
          {
            "Date": "1456439459",
            "Id": "1456439454236",
            "Username": "jhuckaby",
            "Text": "Rolled to prod, looks good."
          }
        ]
      },
      "Priority": "Medium",
      "Environment": "Production",
      "Description": "VERSION 7.4.5 BUILD 1\r\nThis is an official release of AirCast 7.4.5.  This is build number 1.  New features and changes are listed below.  This release is code and feature complete, and fulfills all the requirements in the ERD.\r\n\r\nBUILD SUMMARY\r\n(See the release notes)\r\n\r\nNEW FEATURES / CHANGES\r\nThis version contains two major bug fixes:\r\n\r\nDEPLOYING PLUGIN XML CONFIG FILES WITHOUT RESTART CAUSES OUTAGE\r\nA bug in the Plugin XML configuration code caused a situation we recently ran into on production.  If a Plugin config file is \"hot reloaded\" (i.e. deployed without a restart) it wipes out the base configuration and uses only what is in the file.  The problem is, we use a hybrid config approach in AirCast, where much of our Plugin configuration is stored in a single \"master\" configuration file, and only some extra parameters are in external files.  But if a file is hot reloaded, the entire configuration was replaced with only whatever the file provided.  This has been fixed, so the file is now merged back into the base config on reload.\r\n\r\nPOSSIBLE FILE CORRUPTION IN Hash WITH SIMULTANEOUS WRITES\r\nA possible bug was found in the base Hash filesystem Plugin in AirCast, where local temp files simply did not have enough entropy.  AirCast is using a local temp file to store data just before it gets sent atomically to NFS, and is using only the mediaset hash and item name as the uniqueness.  So if two write requests for the same mediaset and same filename came in at the same exact moment on the same server, this temp file could clobber itself.  This has been fixed so that PID-specific temp subdirectories are used for all local temp files (these dirs already exists and are auto-created/destroyed with each child fork).\r\n\r\nBUG FIXES\r\n(See the release notes)\r\n\r\nGIT COMMITS\r\n(See the release notes)\r\n\r\nDOCUMENTATION\r\nAirCast Release Notes ( http://build.dev.company.net/releases/AirCast/7.4.5/ )\r\n\r\nbuild Build Report ( http://build.dev.company.net/build/?build_report=vqq56w3spg )\r\n\r\nAirCast Wiki ( https://confluence.cyan.com/display/DEV/company+AirCast )\r\n\r\n\r\nREQUIREMENTS\r\nNone.\r\n\r\nINSTALLATION\r\n\r\nPreproduction\r\nsudo roll preprod app mtx --import vqq56w3spg --save b4AirCast_7.4.5 --upgrade\r\n\r\nLive Production\r\nsudo roll live-prod app mtx --import vqq56w3spg --save b4AirCast_7.4.5 --upgrade\r\n\r\n\r\nOPEN ISSUES\r\nNone\r\n\r\nCopyright (c) 2016 My Company, LLC.  Confidential.",
      "Summary": "AirCast 7.4.5 Released",
      "History": {
        "Event": [
          {
            "Comment": "",
            "Date": "1456188218",
            "Id": "1456188218508",
            "Username": "jhuckaby",
            "Tag": "Build 1",
            "Description": "Dev Complete"
          },
          {
            "Username": "jhuckaby",
            "Tag": "Build 1",
            "Description": "Preprod Release",
            "Id": "14561883571713",
            "Date": "1456188357",
            "Comment": ""
          },
          {
            "Username": "jhuckaby",
            "Description": "Prod Release",
            "Tag": "Build 1",
            "Id": "1456438738122",
            "Date": "1456438742",
            "Comment": ""
          },
          {
            "Username": "jhuckaby",
            "Description": "priority=_none_|Medium;environment=Preproduction|Production;_custom=Added event: Prod Release (Build 1)",
            "Date": "1456438742"
          },
          {
            "Username": "jhuckaby",
            "Description": "status=Open|Closed;_custom=Added Comment: Rolled to prod, looks good.",
            "Date": "1456439459"
          },
          {
            "Date": "1456439469",
            "Username": "jhuckaby",
            "Description": "completeby=February 29, 2016|February 25, 2016"
          }
        ]
      },
      "Status": "Closed",
      "Createdate": "1456188218",
      "Modifydate": "1456439469",
      "Submittedby": "jhuckaby",
      "Customer": "_none_",
      "Ccemail": "jhuckaby"
    },
    
    {
      "Modifydate": "1456267649",
      "Submittedby": "dsmith",
      "Customer": "_none_",
      "Ccemail": "rthomas",
      "Summary": "Sample: Enable Partner for OEM regular expression sharing",
      "Status": "Closed",
      "Createdate": "1456267281",
      "History": {
        "Event": [
          {
            "Date": "1456267281",
            "Tag": "Build 1",
            "Description": "Opened",
            "Username": "dsmith",
            "Id": "1456267182801"
          },
          {
            "Date": "1456267342",
            "Username": "api",
            "Description": "assignedto=jhuckaby|dsmith"
          },
          {
            "Date": "1456267649",
            "Username": "api",
            "Description": "status=New|Closed"
          }
        ]
      },
      "Environment": "Production",
      "Description": "Enable Partner for OEM level regular expression sharing. All Partner owners will now be shared when fetching profile data.\n\nsudo roll prod t x mgr --import conf Sample/Sample-1.1.json --install conf Sample/Sample-1.1.json",
      "ID": "2658",
      "Priority": "High",
      "Comments": {
        "Comment": [
          {
            "Text": "rolled to prod",
            "Username": "jhuckaby",
            "Id": "14562673420862",
            "Date": "1456267342"
          },
          {
            "Date": "1456267649",
            "Id": "14562676493786",
            "Text": "good in prod",
            "Username": "dsmith"
          }
        ]
      },
      "Completeby": "1456267649",
      "Rfaccount": "_none_",
      "Assignedto": "dsmith"
    },
    
    {
      "Description": "Show Box 1.4.28 BUILD 1\nThis is an official release of Show Box 1.4.28.  This is build number 1.  New features and changes are listed below. \n\nBUILD SUMMARY\n(See the release notes)\n\nNEW FEATURES / CHANGES\nHandle empty dealerzip parameter as a 'special-fallback' situation.\n\nBUG FIXES\n(See the release notes)\n\nGIT COMMITS\n(See the release notes)\n\nDOCUMENTATION\nShow Box Release Notes ( http://build.dev.company.net/releases/showbox/1.4.28/ )\n\nbuild Build Report ( http://build.dev.company.net/build/?build_report=d8hwb6w79c )\n\nUnit Test Report ( http://build.dev.company.net/abc/data/util/releasemgr/rolls/d8hwb6w79c/unit.txt )\n\n\nREQUIREMENTS\nList any external dependencies here, such as another product release.\n\nINSTALLATION\n\nPreproduction\nsudo roll preprod x --import d8hwb6w79c --save b4showbox_1.4.28 --upgrade\n\nLive Production\nsudo roll live-prod x --import d8hwb6w79c --save b4showbox_1.4.28 --upgrade\n\n\nOPEN ISSUES\nNone\n\nCopyright (c) 2016 My Company, LLC.  Confidential.",
      "Environment": "Production",
      "ID": "2659",
      "Priority": "Medium",
      "Comments": {
        "Comment": [
          {
            "Date": "1456433412",
            "Id": "14564334120057",
            "Username": "dsmith",
            "Text": "Rolled to Preproduction."
          },
          {
            "Id": "1456433865112",
            "Text": "ready for prod",
            "Username": "dsmith",
            "Date": "1456433865"
          },
          {
            "Text": "rolled to prod",
            "Username": "jhuckaby",
            "Id": "14564341909746",
            "Date": "1456434191"
          },
          {
            "Text": "good in prod",
            "Username": "dsmith",
            "Id": "14564348981304",
            "Date": "1456434898"
          }
        ]
      },
      "Completeby": "1456434898",
      "Rfaccount": "_none_",
      "Assignedto": "dsmith",
      "Submittedby": "dsmith",
      "Modifydate": "1456434898",
      "Ccemail": "ebrown",
      "Customer": "_none_",
      "Summary": "Show Box 1.4.28 Released to Preproduction",
      "Createdate": "1456433331",
      "Status": "Closed",
      "History": {
        "Event": [
          {
            "Comment": "",
            "Date": "1456433331",
            "Id": "14564333313479",
            "Tag": "Build 1",
            "Description": "Dev Complete",
            "Username": "dsmith"
          },
          {
            "Date": "1456433412",
            "Comment": "",
            "Description": "Preprod Release",
            "Tag": "Build 1",
            "Username": "dsmith",
            "Id": "14564334120056"
          },
          {
            "Username": "dsmith",
            "Description": "Prod Release",
            "Tag": "Build 1",
            "Id": "14564338651116",
            "Date": "1456433865",
            "Comment": ""
          },
          {
            "Date": "1456433865",
            "Username": "api",
            "Description": "assignedto=dsmith|jhuckaby;environment=Preproduction|Production"
          },
          {
            "Date": "1456434191",
            "Username": "api",
            "Description": "assignedto=jhuckaby|dsmith"
          },
          {
            "Description": "status=Open|Closed;completeby=March 3, 2016|February 25, 2016",
            "Username": "api",
            "Date": "1456434898"
          }
        ]
      }
    },
    
    {
      "Environment": "Production",
      "Description": "When Box Creator makes calls to AirCast, they should never error out.  This alert threshold will catch these and send to Joe.\r\n\r\nGit Commit:\r\nhttp://source.dev.company.net/git/?p=dev/clear.git;a=commitdiff;h=49e88ad\r\n\r\nProd:\r\nroll prod mtx --import clear adcreator-schedule.xml --install clear adcreator-schedule.xml\r\n\r\n- Joe",
      "ID": "2660",
      "Modifydate": "1456439428",
      "Submittedby": "jhuckaby",
      "Customer": "_none_",
      "Priority": "High",
      "Completeby": "1456387200",
      "Ccemail": "_none_",
      "Summary": "New Box Creator threshold alert for AirCast API errors",
      "Status": "Closed",
      "Comments": { "Comment": [] },
      "History": {
        "Event": [
          {
            "Id": "1456439372634",
            "Description": "Opened",
            "Tag": "Build 1",
            "Username": "jhuckaby",
            "Date": "1456439428"
          },
          {
            "Description": "Prod Release",
            "Tag": "Build 1",
            "Username": "jhuckaby",
            "Id": "1456439425106",
            "Date": "1456439428",
            "Comment": ""
          },
          {
            "Date": "1456439428",
            "Description": "_custom=Added event: Prod Release (Build 1)",
            "Username": "jhuckaby"
          }
        ]
      },
      "Createdate": "1424903428",
      "Rfaccount": "_none_",
      "Assignedto": "jhuckaby"
    },
    
    {
      "Completeby": "1456473600",
      "Comments": {
        "Comment": [
          {
            "Date": "1456529662",
            "Text": "All of the above done on idb01 and idb02",
            "Username": "rthomas",
            "Id": "1456529661453"
          },
          {
            "Id": "1462588190608",
            "Username": "rthomas",
            "Text": "Reindexed ads and admarkup on 2016-05-06 after deleting 5 million ads",
            "Date": "1462588183"
          }
        ]
      },
      "Priority": "High",
      "ID": "2661",
      "Environment": "Production",
      "Description": "reindex index Podcasting.idx_campaign_campid_txt;\r\n\r\nreindex index Podcasting.idx_campaign_name;\r\n\r\nreindex index Podcasting.idx_campaign_promoid;\r\n\r\nreindex index Podcasting.idx_campaigns_webid;\r\n\r\nreindex index Podcasting.idx_retargetcampaigns_modifydate;\r\n\r\nreindex index Podcasting.idx_retcampaigns_status;\r\n\r\nreindex index Podcasting.pk_Podcasting_campaigns;\r\n\r\nreindex table Podcasting.adgroups;\r\nreindex table Podcasting.campaignmake ;\r\nreindex table Podcasting.campaigndma ;\r\nreindex table Podcasting.campaignsitetype ;\r\nreindex table Podcasting.campaignnetwork ;\r\nreindex table Podcasting.accounts;\r\nreindex table Podcasting.invgroupnetworks ;\r\nreindex table Podcasting.invgroups ;\r\n\r\nreindex index Podcasting.udx_campmake_campmakeid;\r\nreindex index Podcasting.udx_campdma_campdmaid;\r\n\r\nreindex index Podcasting.idx_ads_status;\r\nreindex index Podcasting.idx_retargetads_modifydate;\r\nreindex index Podcasting.idx_ads_adid_txt;\r\nreindex index Podcasting.idx_ads_adgroupid;\r\nreindex index Podcasting.pk_Podcasting_ads;\r\n\r\n\r\nreindex table Podcasting.admarkup;\r\nreindex index Podcasting.udx_admarkup_markupadid;\r\n\r\nvacuum full Podcasting.campaigns;\r\n//vacuum full Podcasting.ads; (didn't finish so cancelled)\r\nvacuum full Podcasting.admarkup;\r\n\r\nvacuum analyze Podcasting.campaigns;\r\nvacuum analyze Podcasting.ads;\r\nvacuum analyze Podcasting.admarkup;",
      "Assignedto": "rthomas",
      "Rfaccount": "_none_",
      "Customer": "_none_",
      "Ccemail": "_none_",
      "Modifydate": "1462588183",
      "Submittedby": "rthomas",
      "Createdate": "1456523929",
      "Status": "Closed",
      "History": {
        "Event": [
          {
            "Date": "1456523929",
            "Id": "1456523851407",
            "Description": "Opened",
            "Tag": "Build 1",
            "Username": "rthomas"
          },
          {
            "Description": "description=changed",
            "Username": "rthomas",
            "Date": "1456525684"
          },
          {
            "Date": "1456529662",
            "Username": "rthomas",
            "Description": "status=New|Closed;description=changed;_custom=Added Comment: All of the above done on idb01 and idb02"
          },
          {
            "Username": "rthomas",
            "Description": "_custom=Added Comment: Reindexed ads and admarkup on 2016-05-06 after deleting 5 million ads",
            "Date": "1462588183"
          }
        ]
      },
      "Summary": "Reindex Podcasting.campaigns table on prod idb01 and idb02"
    },
    
    {
      "Assignedto": "rthomas",
      "Rfaccount": "_none_",
      "Environment": "Production",
      "Description": "Podcasting 1.9.20 BUILD 1\r\nThis is an official release of Podcasting 1.9.20.  This is build number 1.  New features and changes are listed below.\r\n\r\nBUILD SUMMARY\r\n(See the release notes)\r\n\r\nNEW FEATURES / CHANGES\r\n\r\nAdded support for banner size smallskyscraper (120x240)\r\n\r\nBUG FIXES\r\n(See the release notes)\r\n\r\nGIT COMMITS\r\n(See the release notes)\r\n\r\nDOCUMENTATION\r\nPodcasting Release Notes ( http://build.dev.company.net/releases/Podcasting/1.9.20/ )\r\n\r\nbuild Build Report ( http://build.dev.company.net/build/?build_report=xchfqkk6d4 )\r\n\r\nUnit Test Report ( http://build.dev.company.net/abc/data/util/releasemgr/rolls/xchfqkk6d4/unit.txt )\r\n\r\nPodcasting Service Release Notes ( https://mydocs.net/a/test.cyangroup.com/document/d/1MkAx5j2Ia4K-f7iHrQ1WvnXhMfsqm-nyPkQYQ32eLfM/edit )\r\n\r\nPodcasting Ubercron Release Notes ( https://mydocs.net/a/test.cyangroup.com/document/d/1CMRKF2TV32aGQ2aO_mxFRg-fnZOpAPQGaiqjcq82348/edit )\r\n\r\nPodcasting Manager Release Notes ( https://mydocs.net/a/test.cyangroup.com/document/d/1vd8bOAFV75-m5DpCt-1ybFo4qeUa298KTXAV6gqttiw/edit )\r\n\r\n\r\nREQUIREMENTS\r\nList any external dependencies here, such as another product release.\r\n\r\nINSTALLATION\r\n\r\nPreproduction\r\nsudo roll preprod mgr --import xchfqkk6d4 --save b4Podcasting_1.9.20 --upgrade monitoring vip logs apache\r\n\r\nLive Production\r\nsudo roll live-prod mgr --import xchfqkk6d4 --save b4Podcasting_1.9.20 --upgrade monitoring vip logs apache\r\n\r\n\r\nOPEN ISSUES\r\nNone\r\n\r\nCopyright (c) 2016 My Company, LLC.  Confidential.",
      "Completeby": "1456732800",
      "Comments": {
        "Comment": [
          {
            "Date": "1456529326",
            "Text": "Rolled to Preproduction.",
            "Username": "rthomas",
            "Id": "14565293266093"
          },
          {
            "Date": "1456529575",
            "Id": "1456529567969",
            "Text": "Just assigning to you Joe, for Monday, since I don't know if Tory will be available.",
            "Username": "rthomas"
          },
          {
            "Date": "1456766114",
            "Id": "14567661145609",
            "Text": "rolled to prod",
            "Username": "jhuckaby"
          },
          {
            "Username": "rthomas",
            "Text": "Looks good. Thanks",
            "Id": "1456767895049",
            "Date": "1456767895"
          }
        ]
      },
      "Priority": "Medium",
      "ID": "2662",
      "History": {
        "Event": [
          {
            "Date": "1456529135",
            "Comment": "",
            "Username": "rthomas",
            "Description": "Dev Complete",
            "Tag": "Build 1",
            "Id": "14565291351972"
          },
          {
            "Id": "14565293266092",
            "Description": "Preprod Release",
            "Tag": "Build 1",
            "Username": "rthomas",
            "Comment": "",
            "Date": "1456529326"
          },
          {
            "Date": "1456529575",
            "Comment": "",
            "Tag": "Build 1",
            "Description": "Prod Release",
            "Username": "rthomas",
            "Id": "1456529568937"
          },
          {
            "Description": "assignedto=rthomas|jhuckaby;completeby=March 4, 2016|February 29, 2016;environment=Preproduction|Production;_custom=Added Comment: Just assigning to you Joe, for Monday, since I don't know if Rory will be available.;_custom=Added event: Prod Release (Build 1)",
            "Username": "rthomas",
            "Date": "1456529575"
          },
          {
            "Username": "api",
            "Description": "assignedto=jhuckaby|rthomas",
            "Date": "1456766114"
          },
          {
            "Description": "status=Open|Closed;_custom=Added Comment: Looks good. Thanks",
            "Username": "rthomas",
            "Date": "1456767895"
          }
        ]
      },
      "Status": "Closed",
      "Createdate": "1456529135",
      "Summary": "Podcasting 1.9.20 Released to Preproduction xchfqkk6d4",
      "Customer": "_none_",
      "Ccemail": "rthomas",
      "Modifydate": "1456767895",
      "Submittedby": "rthomas"
    },
    
    {
      "Description": "Increase threshold on Couchbase related alerts that we expect to see at our scale. Turning down the noise.\nAlso increasing threshold on integration errors since they aren't high volume and aren't getting corrected, e.g, leftover usedcars.com integration points.\n\nsudo roll prod mtx --import clear sampleproduct-schedule.xml --install clear sampleproduct-schedule.xml",
      "Environment": "Production",
      "ID": "2663",
      "Comments": {
        "Comment": [
          {
            "Id": "1456769346963",
            "Text": "rolled to prod",
            "Username": "jhuckaby",
            "Date": "1456769347"
          },
          {
            "Date": "1456769362",
            "Username": "dsmith",
            "Text": "done in prod",
            "Id": "14567693620438"
          }
        ]
      },
      "Completeby": "1456769362",
      "Priority": "Low",
      "Rfaccount": "_none_",
      "Assignedto": "dsmith",
      "Submittedby": "dsmith",
      "Modifydate": "1456769362",
      "Ccemail": "_none_",
      "Customer": "_none_",
      "Summary": "Increase CLEAR thresholds for Sample Product",
      "Status": "Closed",
      "History": {
        "Event": [
          {
            "Id": "1456769013905",
            "Username": "dsmith",
            "Description": "Opened",
            "Tag": "Build 1",
            "Date": "1456769309"
          },
          {
            "Date": "1456769347",
            "Description": "assignedto=jhuckaby|dsmith",
            "Username": "api"
          },
          {
            "Date": "1456769362",
            "Description": "status=New|Closed",
            "Username": "api"
          }
        ]
      },
      "Createdate": "1456769309"
    },
    
    {
      "Modifydate": "1456770319",
      "Submittedby": "dsmith",
      "Customer": "_none_",
      "Ccemail": "_none_",
      "Summary": "Increase CLEAR alert thresholds on Show Box",
      "Createdate": "1456770174",
      "Status": "Closed",
      "History": {
        "Event": [
          {
            "Id": "1456769921738",
            "Tag": "Build 1",
            "Description": "Opened",
            "Username": "dsmith",
            "Date": "1456770174"
          },
          {
            "Description": "assignedto=syang|dsmith",
            "Username": "api",
            "Date": "1456770284"
          },
          {
            "Description": "status=New|Closed",
            "Username": "api",
            "Date": "1456770319"
          }
        ]
      },
      "Environment": "Production",
      "Description": "Increase alert thresholds on Couchbase related errors.  We expect a low volume of these at our scale.  Let's turn down the noise.\n\nsudo roll prod mtx --import clear showbox-schedule.xml --install clear showbox-schedule.xml",
      "ID": "2664",
      "Priority": "Low",
      "Comments": {
        "Comment": [
          {
            "Date": "1456770284",
            "Id": "14567702843295",
            "Text": "to prod",
            "Username": "syang"
          },
          {
            "Username": "dsmith",
            "Text": "done in prod",
            "Id": "14567703193146",
            "Date": "1456770319"
          }
        ]
      },
      "Completeby": "1456770319",
      "Rfaccount": "_none_",
      "Assignedto": "dsmith"
    },
    
    {
      "Description": "Podcasting 1.9.21 BUILD 1\r\nThis is an official release of Podcasting 1.9.21.  This is build number 1.  New features and changes are listed below.\r\n\r\nBUILD SUMMARY\r\n(See the release notes)\r\n\r\nNEW FEATURES / CHANGES\r\n\r\nUpdated unit tests to avoid collision\r\n\r\nUse DCM adunits to get supported ad sizes and store necessary information in the db\r\n\r\nSupport for getAds API with ad_id passed it. Previously only supported campaign_id and adgroup_id\r\n\r\nBUG FIXES\r\n(See the release notes)\r\n\r\nGIT COMMITS\r\n(See the release notes)\r\n\r\nDOCUMENTATION\r\nPodcasting Release Notes ( http://build.dev.company.net/releases/Podcasting/1.9.21/ )\r\n\r\nbuild Build Report ( http://build.dev.company.net/build/?build_report=rgm3dzybtd )\r\n\r\nUnit Test Report ( http://build.dev.company.net/abc/data/util/releasemgr/rolls/rgm3dzybtd/unit.txt )\r\n\r\nPodcasting Service Release Notes ( https://mydocs.net/a/test.cyangroup.com/document/d/1MkAx5j2Ia4K-f7iHrQ1WvnXhMfsqm-nyPkQYQ32eLfM/edit )\r\n\r\nPodcasting Ubercron Release Notes ( https://mydocs.net/a/test.cyangroup.com/document/d/1CMRKF2TV32aGQ2aO_mxFRg-fnZOpAPQGaiqjcq82348/edit )\r\n\r\nPodcasting Manager Release Notes ( https://mydocs.net/a/test.cyangroup.com/document/d/1vd8bOAFV75-m5DpCt-1ybFo4qeUa298KTXAV6gqttiw/edit )\r\n\r\n\r\nREQUIREMENTS\r\nList any external dependencies here, such as another product release.\r\n\r\nINSTALLATION\r\n\r\nPreproduction\r\nsudo roll preprod mgr --import rgm3dzybtd --save b4Podcasting_1.9.21 --upgrade monitoring vip logs apache\r\n\r\nLive Production\r\nsudo roll live-prod mgr --import rgm3dzybtd --save b4Podcasting_1.9.21 --upgrade monitoring vip logs apache\r\n\r\n\r\nOPEN ISSUES\r\nNone\r\n\r\nCopyright (c) 2016 My Company, LLC.  Confidential.",
      "Environment": "Production",
      "ID": "2665",
      "Completeby": "1457596800",
      "Comments": {
        "Comment": [
          {
            "Text": "Rolled to Preproduction.",
            "Username": "rthomas",
            "Id": "1456770636454",
            "Date": "1456770636"
          },
          {
            "Id": "14570498590369",
            "Text": "Rolled to Preproduction.",
            "Username": "rthomas",
            "Date": "1457049859"
          },
          {
            "Date": "1457050887",
            "Id": "14570508878623",
            "Text": "pushed to prod",
            "Username": "syang"
          },
          {
            "Id": "1457051382113",
            "Text": "Looks good thx",
            "Username": "rthomas",
            "Date": "1457051382"
          }
        ]
      },
      "Priority": "Medium",
      "Rfaccount": "_none_",
      "Assignedto": "rthomas",
      "Submittedby": "rthomas",
      "Modifydate": "1457051382",
      "Ccemail": "rthomas",
      "Customer": "_none_",
      "Summary": "Podcasting 1.9.21 Released to Preproduction rgm3dzybtd",
      "Createdate": "1456770505",
      "Status": "Closed",
      "History": {
        "Event": [
          {
            "Date": "1456770505",
            "Comment": "",
            "Username": "rthomas",
            "Tag": "Build 1",
            "Description": "Dev Complete",
            "Id": "14567705055623"
          },
          {
            "Id": "1456770636454",
            "Description": "Preprod Release",
            "Tag": "Build 1",
            "Username": "rthomas",
            "Comment": "",
            "Date": "1456770636"
          },
          {
            "Date": "1457049724",
            "Description": "completeby=March 7, 2016|March 10, 2016;description=changed",
            "Username": "api"
          },
          {
            "Username": "rthomas",
            "Description": "Preprod Release",
            "Tag": "Build 1",
            "Id": "14570498590369",
            "Date": "1457049859",
            "Comment": ""
          },
          {
            "Date": "1457050577",
            "Comment": "",
            "Username": "rthomas",
            "Description": "Prod Release",
            "Tag": "Build 1",
            "Id": "1457050571679"
          },
          {
            "Description": "environment=Preproduction|Production;_custom=Added event: Prod Release (Build 1)",
            "Username": "rthomas",
            "Date": "1457050577"
          },
          {
            "Description": "assignedto=rthomas|syang",
            "Username": "rthomas",
            "Date": "1457050702"
          },
          {
            "Date": "1457050887",
            "Description": "assignedto=syang|rthomas",
            "Username": "api"
          },
          {
            "Date": "1457051382",
            "Description": "status=Open|Closed;_custom=Added Comment: Looks good thx",
            "Username": "rthomas"
          }
        ]
      }
    }
  ]
}
```

## File: `test/test-hash.js`
```javascript
// Unit tests for Storage System - Hash
// Copyright (c) 2015 - 2020 Joseph Huckaby
// Released under the MIT License

var os = require('os');
var fs = require('fs');
var path = require('path');
var cp = require('child_process');
var async = require('async');
var Tools = require('pixl-tools');

// const BAD_KEYS = Object.getOwnPropertyNames( Object.prototype );
const BAD_KEYS = ['constructor', '__defineGetter__', '__defineSetter__', 'hasOwnProperty', '__lookupGetter__', '__lookupSetter__', 'isPrototypeOf', 'propertyIsEnumerable', 'toString', 'valueOf', 'toLocaleString'];

module.exports = {
	tests: [
	
		function hashCreate1(test) {
			test.expect(1);
			
			this.storage.hashCreate( 'hash1', { page_size: 10 }, function(err, data) {
				test.ok( !err, "No error creating hash1: " + err );
				test.done();
			} );
		},
		
		function hashGetAllEmpty1(test) {
			test.expect(2);
			
			this.storage.hashGetAll( 'hash1', function(err, items) {
				test.ok( !!items, "Expected hash for empty hash" );
				test.ok( Object.keys(items).length == 0, "Expected zero length in items hash on empty hash" );
				test.done();
			} );
		},
		
		function hashPut1(test) {
			var self = this;
			test.expect(2);
			
			this.storage.hashPut( 'hash1', 'key1', { foo: 'bar', number: 122 }, function(err) {
				test.ok( !err, "No error storing into hash: " + err );
				test.ok( Object.keys(self.storage.locks).length == 0, "No more locks leftover in storage" );
				test.done();
			} );
		},
		
		function hashUpdate1(test) {
			var self = this;
			test.expect(2);
			
			this.storage.hashUpdate( 'hash1', 'key1', { number: 123 }, function(err) {
				test.ok( !err, "No error storing into hash: " + err );
				test.ok( Object.keys(self.storage.locks).length == 0, "No more locks leftover in storage" );
				test.done();
			} );
		},
		
		function hashGet1(test) {
			var self = this;
			test.expect(15);
			
			this.storage.hashGet( 'hash1', 'key1', function(err, item) {
				test.ok( !err, "No error fetching hash key: " + err );
				test.ok( !!item, "Item is real" );
				test.ok( item.number == 123, "Hash item number matches" );
				test.ok( item.foo == 'bar', "Hash item value matches" );
				
				// check internals
				self.storage.get( 'hash1', function(err, hash) {
					test.ok( !err, "No error fetching hash header: " + err );
					test.ok( !!hash, "Got hash data from header key" );
					test.ok( hash.type == 'hash', "Data type is hash: " + hash.type );
					test.ok( hash.length == 1, "Hash length is 1: " + hash.length );
					test.ok( hash.page_size > 0, "Hash page_size is non-zero: " + hash.page_size );
					
					self.storage.get( 'hash1/data', function(err, page) {
						test.ok( !err, "No error fetching hash page: " + err );
						test.ok( !!page, "Got hash page data" );
						test.ok( page.type == 'hash_page', "Page type is correct: " + page.type );
						test.ok( page.length == 1, "Page length is 1: " + page.length );
						test.ok( !!page.items, "Hash page has items" );
						test.ok( Object.keys(page.items).length == 1, "Hash page has 1 item" );
						test.done();
					} );
				} ); // internals
			} );
		},
		
		// hashDelete
		function hashDelete1(test) {
			var self = this;
			test.expect(13);
			
			this.storage.hashDelete( 'hash1', 'key1', function(err) {
				test.ok( !err, "No error deleting hash key: " + err );
				test.ok( Object.keys(self.storage.locks).length == 0, "No more locks leftover in storage" );
				
				// check internals
				self.storage.get( 'hash1', function(err, hash) {
					test.ok( !err, "No error fetching hash header: " + err );
					test.ok( !!hash, "Got hash data from header key" );
					test.ok( hash.type == 'hash', "Data type is hash: " + hash.type );
					test.ok( hash.length == 0, "Hash length is 0: " + hash.length );
					test.ok( hash.page_size > 0, "Hash page_size is non-zero: " + hash.page_size );
					
					self.storage.get( 'hash1/data', function(err, page) {
						test.ok( !err, "No error fetching hash page: " + err );
						test.ok( !!page, "Got hash page data" );
						test.ok( page.type == 'hash_page', "Page type is correct: " + page.type );
						test.ok( page.length == 0, "Page length is 0: " + page.length );
						test.ok( !!page.items, "Hash page has items" );
						test.ok( Object.keys(page.items).length == 0, "Hash page has 0 items" );
						test.done();
					} );
				} ); // internals
			});
		},
		
		// hashPutMulti
		function hashPutMulti1(test) {
			// this will fill up one page but not overflow it
			var self = this;
			test.expect(13);
			
			var obj = {};
			for (var idx = 0; idx < 10; idx++) {
				obj[ 'key'+idx ] = "Value " + Math.floor(idx * 1000);
			}
			
			this.storage.hashPutMulti( 'hash1', obj, function(err) {
				test.ok( !err, "No error storing hash multikey: " + err );
				test.ok( Object.keys(self.storage.locks).length == 0, "No more locks leftover in storage" );
				
				// check internals
				self.storage.get( 'hash1', function(err, hash) {
					test.ok( !err, "No error fetching hash header: " + err );
					test.ok( !!hash, "Got hash data from header key" );
					test.ok( hash.type == 'hash', "Data type is hash: " + hash.type );
					test.ok( hash.length == 10, "Hash length is 10: " + hash.length );
					test.ok( hash.page_size > 0, "Hash page_size is non-zero: " + hash.page_size );
					
					self.storage.get( 'hash1/data', function(err, page) {
						test.ok( !err, "No error fetching hash page: " + err );
						test.ok( !!page, "Got hash page data" );
						test.ok( page.type == 'hash_page', "Page type is correct: " + page.type );
						test.ok( page.length == 10, "Page length is 10: " + page.length );
						test.ok( !!page.items, "Hash page has items" );
						test.ok( Object.keys(page.items).length == 10, "Hash page has 10 items" );
						test.done();
					} );
				} ); // internals
			});
		},
		
		function hashPut2(test) {
			// cause a page overflow and reindex
			var self = this;
			test.expect(17);
			
			this.storage.hashPut( 'hash1', 'key10', "Value 10000", function(err) {
				test.ok( !err, "No error storing into hash: " + err );
				
				// key10 should trigger an async reindex, so we have to wait for that to complete
				var first = true;
				async.whilst(
					function () {
						return ( first || (Object.keys(self.storage.locks).length > 0) || !self.storage.queue.idle() );
					},
					function (callback) {
						test.debug("Waiting for locks / queue");
						first = false;
						setTimeout( function() { callback(); }, 250 );
					},
					function() {
						// all locks released and queue idle
						// check internals
						self.storage.get( 'hash1', function(err, hash) {
							test.ok( !err, "No error fetching hash header: " + err );
							test.ok( !!hash, "Got hash data from header key" );
							test.ok( hash.type == 'hash', "Data type is hash: " + hash.type );
							test.ok( hash.length == 11, "Hash length is 11: " + hash.length );
							test.ok( hash.page_size > 0, "Hash page_size is non-zero: " + hash.page_size );
							
							self.storage.get( 'hash1/data', function(err, page) {
								test.ok( !err, "No error fetching hash page: " + err );
								test.ok( !!page, "Got hash page data" );
								test.ok( page.type == 'hash_index', "Page type is correct: " + page.type );
								test.ok( !page.items, "Page no longer contains items" );
								
								self.storage.get( 'hash1/data/0', function(err, page) {
									test.ok( !err, "No error fetching nested hash page: " + err );
									test.ok( !!page, "Got nested hash page data" );
									test.ok( page.type == 'hash_page', "Nested page type is correct: " + page.type );
									test.ok( page.length == 1, "Nested page length is 1: " + page.length );
									test.ok( !!page.items, "Nested hash page has items" );
									test.ok( Object.keys(page.items).length == 1, "Nested hash page has 1 items" );
									
									// 'key9' has an MD5 that starts with '0', so we know it will be in hash1/data/0
									test.ok( page.items['key9'] == "Value 9000", "Nested hash page contains key9, and its value is correct" );
									test.done();
								} );
							} );
						} ); // internals
					} // idle
				); // whilst
			} ); // hashPut
		},
		
		// hashGetMulti
		function hashGetMulti1(test) {
			var self = this;
			var keys = ['key1', 'key3', 'key5', 'key7', 'key9'];
			var correct_values = ["Value 1000", "Value 3000", "Value 5000", "Value 7000", "Value 9000"];
			test.expect(8);
			
			this.storage.hashGetMulti( 'hash1', keys, function(err, values) {
				test.ok( !err, "No error fetching hash multikey: " + err );
				test.ok( !!values, "Got values in response");
				test.ok( values.length == 5, "Values has correct length: " + values.length);
				
				correct_values.forEach( function(value, idx) {
					test.ok( values[idx] == value, "Value correct for key: " + keys[idx] + ": " + values[idx]);
				} );
				
				test.done();
			});
		},
		
		// hashGetAll
		function hashGetAll1(test) {
			var self = this;
			test.expect(14);
			
			this.storage.hashGetAll( 'hash1', function(err, obj) {
				test.ok( !err, "No error fetching hash all: " + err );
				test.ok( !!obj, "Got object in resopnse" );
				test.ok( Object.keys(obj).length == 11, "Got 11 keys in response" );
				
				for (var idx = 0; idx < 11; idx++) {
					test.ok( obj[ 'key'+idx ] == "Value " + Math.floor(idx * 1000), "Value correct for key: key"+idx+": " + obj[ 'key'+idx ] );
				}
				
				test.done();
			});
		},
		
		// hashEach
		function hashEach1(test) {
			var self = this;
			var obj = {};
			
			this.storage.hashEach( 'hash1',
				function(key, value, callback) {
					obj[key] = value;
					callback();
				},
				function(err) {
					test.ok( !err, "No error fetching hash each: " + err );
					test.ok( Object.keys(obj).length == 11, "Got 11 keys in response" );
					
					for (var idx = 0; idx < 11; idx++) {
						test.ok( obj[ 'key'+idx ] == "Value " + Math.floor(idx * 1000), "Value correct for key: key"+idx+": " + obj[ 'key'+idx ] );
					}
					
					test.done();
				}
			);
		},
		
		function hashEachAbort1(test) {
			// abort hashEach in the middle
			var self = this;
			var obj = {};
			var count = 0;
			
			this.storage.hashEach( 'hash1',
				function(key, value, callback) {
					obj[key] = value;
					count++;
					if (count == 5) return callback(new Error("Abort!")); // abort
					else return callback();
				},
				function(err) {
					test.ok( !!err, "Error expected fetching hash each" );
					test.ok( err.message.toString().match(/abort/i), "Error message contains 'abort'" );
					test.ok( Object.keys(obj).length == 5, "Got 5 keys in response" );
					test.done();
				}
			);
		},
		
		// hashEachSync
		function hashEachSync1(test) {
			var self = this;
			var obj = {};
			
			this.storage.hashEachSync( 'hash1',
				function(key, value) {
					obj[key] = value;
				},
				function(err) {
					test.ok( !err, "No error fetching hash each: " + err );
					test.ok( Object.keys(obj).length == 11, "Got 11 keys in response" );
					
					for (var idx = 0; idx < 11; idx++) {
						test.ok( obj[ 'key'+idx ] == "Value " + Math.floor(idx * 1000), "Value correct for key: key"+idx+": " + obj[ 'key'+idx ] );
					}
					
					test.done();
				}
			);
		},
		
		function hashEachSyncAbort1(test) {
			// abort hashEach in the middle
			var self = this;
			var obj = {};
			var count = 0;
			
			this.storage.hashEachSync( 'hash1',
				function(key, value) {
					obj[key] = value;
					count++;
					if (count == 5) return false; // abort
				},
				function(err) {
					test.ok( !!err, "Error expected fetching hash each" );
					test.ok( err.message.toString().match(/abort/i), "Error message contains 'abort'" );
					test.ok( Object.keys(obj).length == 5, "Got 5 keys in response" );
					test.done();
				}
			);
		},
		
		// hashEachPage
		function hashEachPage1(test) {
			var self = this;
			var obj = {};
			
			this.storage.hashEachPage( 'hash1',
				function(data, callback) {
					test.ok( !!data, "Got data in page" );
					test.ok( Object.keys(data).length > 0, "At least one key in page" );
					
					for (var key in data) {
						test.ok( !(key in obj), "No duplicate key expected: " + key );
						obj[key] = data[key];
					}
					
					callback();
				},
				function(err) {
					test.ok( !err, "No error fetching hash page each: " + err );
					test.ok( Object.keys(obj).length == 11, "Got 11 keys in response" );
					
					for (var idx = 0; idx < 11; idx++) {
						test.ok( obj[ 'key'+idx ] == "Value " + Math.floor(idx * 1000), "Value correct for key: key"+idx+": " + obj[ 'key'+idx ] );
					}
					
					test.done();
				}
			);
		},
		
		// hashCopy
		function hashCopy1(test) {
			var self = this;
			
			this.storage.hashCopy( 'hash1', 'hashcopied', function(err) {
				// now make sure copied hash has everything we expect
				
				self.storage.hashGetAll( 'hashcopied', function(err, obj) {
					test.ok( !err, "No error fetching hashcopied all: " + err );
					test.ok( !!obj, "Got object in resopnse" );
					test.ok( Object.keys(obj).length == 11, "Got 11 hashcopied keys in response" );
					
					for (var idx = 0; idx < 11; idx++) {
						test.ok( obj[ 'key'+idx ] == "Value " + Math.floor(idx * 1000), "hashcopied Value correct for key: key"+idx+": " + obj[ 'key'+idx ] );
					}
					
					test.done();
				});
			} );
		},
		
		// hashRename
		function hashRename1(test) {
			var self = this;
			
			this.storage.hashRename( 'hashcopied', 'hashrenamed', function(err) {
				// now make sure renamed hash has everything we expect
				
				self.storage.hashGetAll( 'hashrenamed', function(err, obj) {
					test.ok( !err, "No error fetching hashcopied all: " + err );
					test.ok( !!obj, "Got object in resopnse" );
					test.ok( Object.keys(obj).length == 11, "Got 11 hashcopied keys in response" );
					
					for (var idx = 0; idx < 11; idx++) {
						test.ok( obj[ 'key'+idx ] == "Value " + Math.floor(idx * 1000), "hashcopied Value correct for key: key"+idx+": " + obj[ 'key'+idx ] );
					}
					
					// make sure original hash (hashcopied) is gone
					self.storage.get( 'hashcopied', function(err) {
						test.ok( !!err, "Error expected fetching head after deleting" );
						
						// clean up our mess
						self.storage.hashDeleteAll( 'hashrenamed', true, function(err) {
							test.done();
						});
					});
				});
			});
		},
		
		// hashDeleteMulti
		function hashDeleteMulti1(test) {
			var self = this;
			var keys = ['key1', 'key3', 'key5', 'key7', 'key9'];
			
			var even_keys = ['key0', 'key2', 'key4', 'key6', 'key8', 'key10'];
			var correct_evens = ["Value 0", "Value 2000", "Value 4000", "Value 6000", "Value 8000", "Value 10000"];
			
			this.storage.hashDeleteMulti( 'hash1', keys, function(err) {
				test.ok( !err, "No error deleting hash multi: " + err );
				// test.ok( Object.keys(self.storage.locks).length == 0, "No more locks leftover in storage" );
				
				// this should fail (re-fetch odds)
				self.storage.hashGetMulti( 'hash1', keys, function(err, values) {
					test.ok( !!err, "Error expected fetching deleted keys" );
					
					// this should work tho (fetch evens)
					self.storage.hashGetMulti( 'hash1', even_keys, function(err, values) {
						test.ok( !err, "No error fetching even hash multi: " + err );
						test.ok( !!values, "Got values in response");
						test.ok( values.length == 6, "Values has correct length: " + values.length);
						
						correct_evens.forEach( function(value, idx) {
							test.ok( values[idx] == value, "Value correct for key: " + even_keys[idx] + ": " + values[idx]);
						} );
						
						test.done();
					});
				});
			});
		},
		
		// hashDeleteAll
		function hashDeleteAll1(test) {
			var self = this;
			
			this.storage.hashDeleteAll( 'hash1', true, function(err) {
				test.ok( !err, "No error deleting hash: " + err );
				test.ok( Object.keys(self.storage.locks).length == 0, "No more locks leftover in storage" );
				
				// make sure it is really deleted
				self.storage.get( 'hash1', function(err) {
					test.ok( !!err, "Error expected fetching head after deleting" );
					
					self.storage.get( 'hash1/data', function(err) {
						test.ok( !!err, "Error expected fetching data after deleting" );
						
						self.storage.get( 'hash1/data/0', function(err) {
							test.ok( !!err, "Error expected fetching page after deleting" );
							test.done();
						});
					});
				});
			});
		},
		
		// Deep multi put
		function hashPutMulti2(test) {
			// this will fill up and overflow many pages, going nested 2 levels deep
			var self = this;
			
			var obj = {};
			for (var idx = 0; idx < 150; idx++) {
				obj[ 'key'+idx ] = "Value " + Math.floor(idx * 1000);
			}
			
			this.storage.hashCreate( 'hash2', { page_size: 10 }, function(err, data) {
				test.ok( !err, "No error creating hash2: " + err );
				
				self.storage.hashPutMulti( 'hash2', obj, function(err) {
					test.ok( !err, "No error storing hash multikey: " + err );
					
					var first = true;
					async.whilst(
						function () {
							return ( first || (Object.keys(self.storage.locks).length > 0) || !self.storage.queue.idle() );
						},
						function (callback) {
							test.debug("Waiting for locks / queue");
							first = false;
							setTimeout( function() { callback(); }, 250 );
						},
						function() {
							// check internals
							self.storage.get( 'hash2', function(err, hash) {
								test.ok( !err, "No error fetching hash header: " + err );
								test.ok( !!hash, "Got hash data from header key" );
								test.ok( hash.type == 'hash', "Data type is hash: " + hash.type );
								test.ok( hash.length == 150, "Hash length is 150: " + hash.length );
								test.ok( hash.page_size > 0, "Hash page_size is non-zero: " + hash.page_size );
								
								self.storage.get( 'hash2/data', function(err, page) {
									test.ok( !err, "No error fetching hash page: " + err );
									test.ok( !!page, "Got hash page data" );
									test.ok( page.type == 'hash_index', "Page type is correct: " + page.type );
									test.ok( !page.items, "Page no longer contains items" );
									
									self.storage.get( 'hash2/data/0', function(err, page) {
										test.ok( !err, "No error fetching hash page: " + err );
										test.ok( !!page, "Got hash page data" );
										test.ok( page.type == 'hash_index', "Page type is correct: " + page.type );
										test.ok( !page.items, "Page no longer contains items" );
										
										self.storage.get( 'hash2/data/0/3', function(err, page) {
											test.ok( !err, "No error fetching nested hash page: " + err );
											test.ok( !!page, "Got nested hash page data" );
											test.ok( page.type == 'hash_page', "Nested page type is correct: " + page.type );
											test.ok( page.length == 1, "Nested page length is 1: " + page.length );
											test.ok( !!page.items, "Nested hash page has items" );
											test.ok( Object.keys(page.items).length == 1, "Nested hash page has 1 items" );
											
											// 'key101' has an MD5 that starts with '03', so we know it will be in hash2/data/0/3
											test.ok( page.items['key101'] == "Value 101000", "Nested hash page contains key101, and its value is correct" );
											test.done();
										} ); // hash2/data/0/3
									} ); // hash2/data/0
								} ); // hash2/data
							} ); // internals
						} // whilst complete
					); // whilst
				}); // hashPutMulti
			} ); // hashCreate
		},
		
		function hashGetAll2(test) {
			var self = this;
			
			this.storage.hashGetAll( 'hash2', function(err, obj) {
				test.ok( !err, "No error fetching hash all: " + err );
				test.ok( !!obj, "Got object in resopnse" );
				test.ok( Object.keys(obj).length == 150, "Got 150 keys in response" );
				
				for (var idx = 0; idx < 150; idx++) {
					test.ok( obj[ 'key'+idx ] == "Value " + Math.floor(idx * 1000), "Value correct for key: key"+idx+": " + obj[ 'key'+idx ] );
				}
				
				test.done();
			});
		},
		
		function hashDeleteAll2(test) {
			var self = this;
			
			this.storage.hashDeleteAll( 'hash2', true, function(err) {
				test.ok( !err, "No error deleting hash: " + err );
				test.ok( Object.keys(self.storage.locks).length == 0, "No more locks leftover in storage" );
				
				// make sure it is really deleted
				self.storage.get( 'hash2', function(err) {
					test.ok( !!err, "Error expected fetching head after deleting" );
					
					self.storage.get( 'hash2/data', function(err) {
						test.ok( !!err, "Error expected fetching data after deleting" );
						
						self.storage.get( 'hash2/data/0', function(err) {
							test.ok( !!err, "Error expected fetching page after deleting" );
							
							self.storage.get( 'hash2/data/0/3', function(err) {
								test.ok( !!err, "Error expected fetching page after deleting" );
								test.done();
							});
						});
					});
				});
			});
		},
		
		function hashUnsplit1(test) {
			// this will fill up and overflow a page into an index
			var self = this;
			
			var obj = {};
			for (var idx = 0; idx < 11; idx++) {
				obj[ 'key'+idx ] = "Value " + Math.floor(idx * 1000);
			}
			
			this.storage.hashPutMulti( 'hash3', obj, { page_size: 10 }, function(err) {
				test.ok( !err, "No error storing hash multikey: " + err );
				
				// key10 should trigger an async reindex, so we have to wait for that to complete
				var first = true;
				async.whilst(
					function () {
						return ( first || (Object.keys(self.storage.locks).length > 0) || !self.storage.queue.idle() );
					},
					function (callback) {
						test.debug("Waiting for locks / queue");
						first = false;
						setTimeout( function() { callback(); }, 250 );
					},
					function() {
						// all locks released and queue idle
						// check internals
						self.storage.get( 'hash3', function(err, hash) {
							test.ok( !err, "No error fetching hash header: " + err );
							test.ok( !!hash, "Got hash data from header key" );
							test.ok( hash.type == 'hash', "Data type is hash: " + hash.type );
							test.ok( hash.length == 11, "Hash length is 11: " + hash.length );
							test.ok( hash.page_size > 0, "Hash page_size is non-zero: " + hash.page_size );
							
							self.storage.get( 'hash3/data', function(err, page) {
								test.ok( !err, "No error fetching hash page: " + err );
								test.ok( !!page, "Got hash page data" );
								test.ok( page.type == 'hash_index', "Page type is correct: " + page.type );
								test.ok( !page.items, "Page no longer contains items" );
								
								self.storage.get( 'hash3/data/0', function(err, page) {
									test.ok( !err, "No error fetching nested hash page: " + err );
									test.ok( !!page, "Got nested hash page data" );
									test.ok( page.type == 'hash_page', "Nested page type is correct: " + page.type );
									test.ok( page.length == 1, "Nested page length is 1: " + page.length );
									test.ok( !!page.items, "Nested hash page has items" );
									test.ok( Object.keys(page.items).length == 1, "Nested hash page has 1 items" );
									
									// 'key9' has an MD5 that starts with '0', so we know it will be in hash1/data/0
									test.ok( page.items['key9'] == "Value 9000", "Nested hash page contains key9, and its value is correct" );
									test.done();
								} );
							} );
						} ); // internals
					} // idle
				); // whilst
			}); // hashPutMulti
		},
		
		function hashUnsplit2(test) {
			// delete all but one key, make sure we DIDN'T trigger an unsplit
			var self = this;
			
			var keys = [];
			for (var idx = 0; idx < 10; idx++) {
				keys.push( 'key'+idx );
			}
			
			this.storage.hashDeleteMulti( 'hash3', keys, function(err) {
				test.ok( !err, "No error deleting hash multi: " + err );
				
				var first = true;
				async.whilst(
					function () {
						return ( first || (Object.keys(self.storage.locks).length > 0) || !self.storage.queue.idle() );
					},
					function (callback) {
						test.debug("Waiting for locks / queue");
						first = false;
						setTimeout( function() { callback(); }, 250 );
					},
					function() {
						// all locks released and queue idle
						// check internals
						self.storage.get( 'hash3', function(err, hash) {
							test.ok( !err, "No error fetching hash header: " + err );
							test.ok( !!hash, "Got hash data from header key" );
							test.ok( hash.type == 'hash', "Data type is hash: " + hash.type );
							test.ok( hash.length == 1, "Hash length is 1: " + hash.length );
							test.ok( hash.page_size > 0, "Hash page_size is non-zero: " + hash.page_size );
							
							self.storage.get( 'hash3/data/f', function(err, page) {
								test.ok( !err, "No error fetching nested hash page: " + err );
								test.ok( !!page, "Got nested hash page data" );
								test.ok( page.type == 'hash_page', "Nested page type is correct: " + page.type );
								test.ok( page.length == 1, "Nested page length is 1: " + page.length );
								test.ok( !!page.items, "Nested hash page has items" );
								test.ok( Object.keys(page.items).length == 1, "Nested hash page has 1 items" );
								
								// 'key10' has an MD5 that starts with 'f', so we know it will be in hash3/data/f
								test.ok( page.items['key10'] == "Value 10000", "Nested hash page contains key10, and its value is correct" );
								test.done();
							} );
						} );
					} // whilst done
				); // async.whilst
			}); // hashDeleteMulti
		},
		
		function hashUnsplit3(test) {
			// delete final key, triggering an unsplit
			var self = this;
			
			this.storage.hashDeleteMulti( 'hash3', ['key10'], function(err) {
				test.ok( !err, "No error deleting key10: " + err );
				
				var first = true;
				async.whilst(
					function () {
						return ( first || (Object.keys(self.storage.locks).length > 0) || !self.storage.queue.idle() );
					},
					function (callback) {
						test.debug("Waiting for locks / queue");
						first = false;
						setTimeout( function() { callback(); }, 250 );
					},
					function() {
						// all locks released and queue idle
						// check internals
						self.storage.get( 'hash3', function(err, hash) {
							test.ok( !err, "No error fetching hash header: " + err );
							test.ok( !!hash, "Got hash data from header key" );
							test.ok( hash.type == 'hash', "Data type is hash: " + hash.type );
							test.ok( hash.length == 0, "Hash length is 0: " + hash.length );
							test.ok( hash.page_size > 0, "Hash page_size is non-zero: " + hash.page_size );
							
							self.storage.get( 'hash3/data', function(err, page) {
								test.ok( !err, "No error fetching nested hash page: " + err );
								test.ok( !!page, "Got nested hash page data" );
								test.ok( page.type == 'hash_page', "Nested page type is correct: " + page.type );
								test.ok( page.length == 0, "Nested page length is 0: " + page.length );
								test.ok( !!page.items, "Nested hash page has items" );
								test.ok( Object.keys(page.items).length == 0, "Nested hash page has 0 items" );
								
								self.storage.get( 'hash3/data/f', function(err, page) {
									test.ok( !!err, "Error expected fetching deleted hash page: " + err );
									
									// finally, delete hash
									self.storage.hashDeleteAll( 'hash3', true, function(err) {
										test.ok( !err, "No error deleting hash3: " + err );
										test.ok( Object.keys(self.storage.locks).length == 0, "No more locks leftover in storage" );
										test.done();
									});
								} );
							} );
						} );
					} // whilst done
				); // async.whilst
			}); // hashDeleteMulti
		},
		
		function hashBadCreate(test) {
			// create hash we can use to test bad keys
			// this is designed to overflow (reindex) when all 12+ keys are added
			var self = this;
			
			this.storage.hashCreate( 'hashbad', { page_size: 10 }, function(err) {
				test.ok( !err, "Error creating hashbad: " + err );
				
				// put one normal (control) key in hash
				self.storage.hashPut( 'hashbad', 'control', 1, function(err) {
					test.ok( !err, "Got error putting control key: " + err );
					test.done();
				});
			} );
		},
		
		function hashGetBadKeysBefore(test) {
			// pre-fetch bad keys, make sure they do not exist in our empty hash
			var self = this;
			
			async.eachSeries( BAD_KEYS,
				function(key, callback) {
					self.storage.hashGet( 'hashbad', key, function(err, value) {
						test.ok( !!err, "No error fetching non-existent bad key: " + key );
						test.ok( !value, "Unexpected value fetching non-existent bad key: " + key + ": " + value );
						callback();
					} );
				},
				function(err) {
					test.done();
				}
			); // async.eachSeries
		},
		
		function hashPutBadKeys(test) {
			// put bad (toxic) keys in hash (Object.prototype stuff)
			// this should also trigger a reindex
			var self = this;
			
			async.eachSeries( BAD_KEYS,
				function(key, callback) {
					self.storage.hashPut( 'hashbad', key, 42, callback );
				},
				function(err) {
					test.ok( !err, "Got error putting bad keys: " + err );
					test.done();
				}
			); // async.eachSeries
		},
		
		function hashGetBadKeys(test) {
			// get bad keys in hash (Object.prototype stuff)
			// these should all succeed
			var self = this;
			
			async.eachSeries( BAD_KEYS,
				function(key, callback) {
					self.storage.hashGet( 'hashbad', key, function(err, value) {
						test.ok( !err, "Got error fetching bad key: " + key + ": " + err );
						test.ok( value == 42, "Unexpected value fetching bad key: " + key + ": " + value );
						callback();
					} );
				},
				function(err) {
					// make sure our control key is still there as well
					self.storage.hashGet( 'hashbad', 'control', function(err, value) {
						test.ok( !err, "Got error fetching control key: " + err );
						test.ok( value == 1, "Unexpected value fetching control key: " + value );
						test.done();
					});
				}
			); // async.eachSeries
		},
		
		function hashBadGetAll(test) {
			// fetch bad hash with hashGetAll() API
			this.storage.hashGetAll( 'hashbad', function(err, hash) {
				test.ok( !err, "Unexpected error fetching all bad: " + err );
				
				BAD_KEYS.forEach( function(key) {
					test.ok( hash[key] === 42, "(hashGetAll) Unexpected key value: " + key + ": " + hash[key] );
				});
				
				test.ok( hash.control == 1, "Expected control key to equal 1, got: " + hash.control );
				test.done();
			});
		},
		
		function hashBadEach(test) {
			// iterate over hash with bad keys
			var self = this;
			var found = [];
			
			this.storage.hashEach( 'hashbad', function(key, value, callback) {
				// do something with key/value
				found.push( key );
				process.nextTick( callback );
			}, 
			function(err) {
				// all keys iterated over
				test.ok( !err, "Got error async-iterating over bad hash: " + err );
				
				// we should have exactly BAD_KEYS + 1 keys
				test.ok( found.length == (BAD_KEYS.length + 1), "Unexpected found length: " + found.length );
				
				// make sure we have all the expected keys
				BAD_KEYS.forEach( function(key) {
					test.ok( !!found.includes(key), "Expected key not in found array: " + key );
				});
				
				// we should have the control key too
				test.ok( found.includes('control'), "Expected control key not in found array" );
				
				test.done();
			} );
		},
		
		function hashBadEachSync(test) {
			// iterate over hash with bad keys (sync)
			var self = this;
			var found = [];
			
			this.storage.hashEachSync( 'hashbad', function(key, value) {
				// do something with key/value
				found.push( key );
			}, 
			function(err) {
				// all keys iterated over
				test.ok( !err, "Got error sync-iterating over bad hash: " + err );
				
				// we should have exactly BAD_KEYS + 1 keys
				test.ok( found.length == (BAD_KEYS.length + 1), "Unexpected found length: " + found.length );
				
				// make sure we have all the expected keys
				BAD_KEYS.forEach( function(key) {
					test.ok( !!found.includes(key), "Expected key not in found array: " + key );
				});
				
				// we should have the control key too
				test.ok( found.includes('control'), "Expected control key not in found array" );
				
				test.done();
			} );
		},
		
		function hashBadDelete(test) {
			// delete individual keys so we trigger an unsplit
			var self = this;
			
			this.storage.hashDeleteMulti( 'hashbad', BAD_KEYS, function(err) {
				test.ok( !err, "Got error multi-deleting bad hash: " + err );
				
				// at this point only the control key should remain
				self.storage.hashGetAll( 'hashbad', function(err, hash) {
					test.ok( !err, "Unexpected error fetching all bad: " + err );
					test.ok( Tools.numKeys(hash) == 1, "Expected only 1 key in hash, got: " + JSON.stringify(hash) );
					test.ok( hash.control == 1, "Expected control key to equal 1, got: " + hash.control );
					test.done();
				});
			});
		},
		
		function hashBadDeleteAll(test) {
			// cleanup
			var self = this;
			
			this.storage.hashDeleteAll( 'hashbad', true, function(err) {
				test.ok( !err, "No error deleting hashbad: " + err );
				test.ok( Object.keys(self.storage.locks).length == 0, "No more locks leftover in storage" );
				
				// make sure it is really deleted
				self.storage.get( 'hashbad', function(err) {
					test.ok( !!err, "Error expected fetching head after deleting" );
					
					self.storage.get( 'hashbad/data', function(err) {
						test.ok( !!err, "Error expected fetching data after deleting" );
						test.done();
					});
				});
			});
		}
		
	] // tests array
};
```

## File: `test/test-indexer.js`
```javascript
// Unit tests for Storage System - Indexer
// Copyright (c) 2015 - 2016 Joseph Huckaby
// Released under the MIT License

var os = require('os');
var fs = require('fs');
var path = require('path');
var cp = require('child_process');
var async = require('async');
var Tools = require('pixl-tools');

var sample_tickets = null;
var fixtures = null;

var sample_data = require('./sample-data.json');
var orig_sample_tickets = sample_data.Ticket;

var index_config = {
	base_path: "/index/ontrack",
	fields: [
		{
			id: "status",
			source: "/Status",
			master_list: 1
		},
		{
			id: "title",
			source: "/Summary",
			min_word_length: 3,
			max_word_length: 128,
			use_remove_words: 1
		},
		{
			id: "modified",
			source: "/Modifydate",
			type: "date"
		},
		{
			id: "num_comments",
			source: "/Comments/Comment/length",
			type: "number"
		}
	],
	
	sorters: [
		{
			id: "created",
			source: "/Createdate",
			type: "number"
		}
	],
	
	remove_words: ["the","of","and","a","to","in","is","you","that","it","he","was","for","on","are","as","with","his","they","I","at","be","this","have","from","or","one","had","by","word","but","not","what","all","were","we","when","your","can","said","there","use","an","each","which","she","do","how","their","if","will","up","other","about","out","many","then","them","these","so","some","her","would","make","like","him","into","time","has","look","two","more","write","go","see","number","no","way","could","people","my","than","first","water","been","call","who","oil","its","now","find","long","down","day","did","get","come","made","may","part"]
};

var orig_fixtures = {
	searchRecordsExact2: {
		'title:"Released to Preproduction"': { "2653": 1, "2654": 1, "2659": 1, "2662": 1, "2665": 1 },
		'status:open title:"Released to Preproduction"': { "2653": 1, "2654": 1 },
		'status:closed title:"Released to Preproduction"': { "2659": 1, "2662": 1, "2665": 1 },
		'status:open title:"Released to Preproduction" -service +product': { "2653": 1 },
		'status:open title:"Released to Preproduction" +service -product': { "2654": 1 },
		
		'status:open title:"Released to" +"Preproduction"': { "2653": 1, "2654": 1 },
		
		'status:open title:"Product 1.7.70 Released" -"Preproduction hzd86vdxtd"': { "2653": 1 },
		'status:open title:"Service 1.1.38 Released" +"Preproduction hzd86vdxtd"': { "2654": 1 },
		
		'title:"xchfqkk6d4"': { "2662": 1 },
		'title:"Increase CLEAR thresholds"': { "2663": 1 },
		'title:"Increase CLEAR alert thresholds"': { "2664": 1 },
		'title:"prod idb01" +idb02 status:closed': { "2661": 1 },
		'title:"prod idb03" +idb02 status:closed': {},
		'title:"prod idb01" +idb03 status:closed': {},
		'title:"prod idb01" +idb02 status:open': {},
		'title:"Released to PreproductionZ"': {},
		'title:"KJFHSDLKFHLKSDFHKJDSF"': {},
		'title:"0"': {},
		'title:"a"': {},
		'title:""': {}
	},
	searchRecordsDateExact: {
		'modified:2016-02-21': {},
		
		'modified:2016-02-22': { "2656": 1 },
		'modified:2016/02/22': { "2656": 1 },
		'modified:2016_02_22': { "2656": 1 },
		'modified:1456164397': { "2656": 1 }, // epoch date
		
		'modified:2016-02-23': { "2658": 1 },
		'modified:2016-02-25': { "2653": 1, "2654": 1, "2655": 1, "2657": 1, "2659": 1, "2660": 1 },
		'modified:2016-02-29': { "2662": 1, "2663": 1, "2664": 1 },
		'modified:2016-03-03': { "2665": 1 },
		'modified:2016-05-06': { "2661": 1 },
		'modified:2016-05-07': {},
		'modified:2016-02-22 | 2016-02-23': { "2656": 1, "2658": 1 },
		'modified:2016-03-03 | 2016-05-06': { "2665": 1, "2661": 1 },
		'modified:2016-02-22 | 2016-02-23 | 2016-03-03 | 2016-05-06': { "2656": 1, "2658": 1, "2665": 1, "2661": 1 }
	},
	searchRecordsDateRangeOpen: {
		'modified:<2000-01-01': {},
		'modified:<2016-02-22': {},
		
		'modified:<=2016-02-22': { "2656": 1 },
		'modified:<2016-02-23': { "2656": 1 },
		
		'modified:>=2000-01-01': { "2656": 1, "2658": 1, "2653": 1, "2654": 1, "2655": 1, "2657": 1, "2659": 1, "2660": 1, "2662": 1, "2663": 1, "2664": 1, "2665": 1, "2661": 1 },
		
		'modified:>=2016-02-22': { "2656": 1, "2658": 1, "2653": 1, "2654": 1, "2655": 1, "2657": 1, "2659": 1, "2660": 1, "2662": 1, "2663": 1, "2664": 1, "2665": 1, "2661": 1 },
		'modified:>2016-02-22': { "2658": 1, "2653": 1, "2654": 1, "2655": 1, "2657": 1, "2659": 1, "2660": 1, "2662": 1, "2663": 1, "2664": 1, "2665": 1, "2661": 1 },
		
		'modified:>=2016-02-29': { "2662": 1, "2663": 1, "2664": 1, "2665": 1, "2661": 1 },
		'modified:>2016-02-29': { "2665": 1, "2661": 1 },
		
		'modified:>=2016-03-03': { "2665": 1, "2661": 1 },
		'modified:>2016-03-03': { "2661": 1 },
		
		'modified:<=2016-05-06': { "2656": 1, "2658": 1, "2653": 1, "2654": 1, "2655": 1, "2657": 1, "2659": 1, "2660": 1, "2662": 1, "2663": 1, "2664": 1, "2665": 1, "2661": 1 },
		'modified:<2016-05-06': { "2656": 1, "2658": 1, "2653": 1, "2654": 1, "2655": 1, "2657": 1, "2659": 1, "2660": 1, "2662": 1, "2663": 1, "2664": 1, "2665": 1 },
		
		'modified:>2016-05-06': {},
		'modified:>2020-12-31': {}
	},
	searchRecordsDateRangeClosed: {
		'modified:2000-01-01..2016-02-21': {},
		'modified:2000-01-01..2016-02-22': { "2656": 1 },
		'modified:2016-02-22..2016-02-24': { "2656": 1, "2658": 1 },
		'modified:2016-02-24..2016-02-28': { "2653": 1, "2654": 1, "2655": 1, "2657": 1, "2659": 1, "2660": 1 },
		'modified:2016-02-29..2016-02-29': { "2662": 1, "2663": 1, "2664": 1 },
		'modified:2016-03-01..2020-12-31': { "2665": 1, "2661": 1 },
		'modified:2016-05-04..2016-05-05': {},
		'modified:2016-05-07..2016-06-01': {}
	},
	searchRecordsNumberExact: {
		'num_comments:0': { "2660": 1 },
		'num_comments:1': { "2656": 1 },
		'num_comments:2': { "2657": 1, "2658": 1, "2661": 1, "2663": 1, "2664": 1 },
		'num_comments:3': {},
		'num_comments:4': { "2653": 1, "2659": 1, "2662": 1, "2665": 1 },
		'num_comments:5': { "2654": 1 },
		'num_comments:6': { "2655": 1 },
		'num_comments:7': {},
		'num_comments:99999': {},
		'num_comments:0|1': { "2660": 1, "2656": 1 },
		'num_comments:5|6': { "2654": 1, "2655": 1 },
		'num_comments:0|1|5|6': { "2660": 1, "2656": 1, "2654": 1, "2655": 1 }
	},
	searchRecordsNumberRangeOpen: {
		'num_comments:<0': {},
		'num_comments:<=0': { "2660": 1 },
		
		'num_comments:>=0': { "2656": 1, "2658": 1, "2653": 1, "2654": 1, "2655": 1, "2657": 1, "2659": 1, "2660": 1, "2662": 1, "2663": 1, "2664": 1, "2665": 1, "2661": 1 },
		
		'num_comments:>0': { "2656": 1, "2658": 1, "2653": 1, "2654": 1, "2655": 1, "2657": 1, "2659": 1, "2662": 1, "2663": 1, "2664": 1, "2665": 1, "2661": 1 },
		
		'num_comments:<1': { "2660": 1 },
		'num_comments:<=1': { "2660": 1, "2656": 1 },
		
		'num_comments:>=1': { "2656": 1, "2658": 1, "2653": 1, "2654": 1, "2655": 1, "2657": 1, "2659": 1, "2662": 1, "2663": 1, "2664": 1, "2665": 1, "2661": 1 },
		
		'num_comments:>1': { "2658": 1, "2653": 1, "2654": 1, "2655": 1, "2657": 1, "2659": 1, "2662": 1, "2663": 1, "2664": 1, "2665": 1, "2661": 1 },
		
		'num_comments:<3': { "2660": 1, "2656": 1, "2657": 1, "2658": 1, "2661": 1, "2663": 1, "2664": 1 },
		'num_comments:<=3': { "2660": 1, "2656": 1, "2657": 1, "2658": 1, "2661": 1, "2663": 1, "2664": 1 },
		
		'num_comments:>=3': { "2653": 1, "2659": 1, "2662": 1, "2665": 1, "2654": 1, "2655": 1 },
		'num_comments:>3': { "2653": 1, "2659": 1, "2662": 1, "2665": 1, "2654": 1, "2655": 1 },
		
		'num_comments:>=5': { "2655": 1, "2654": 1 },
		'num_comments:>5': { "2655": 1 },
		
		'num_comments:>=6': { "2655": 1 },
		'num_comments:>6': {},
		
		'num_comments:>=7': {},
		'num_comments:>7': {},
		'num_comments:>99999': {},
		
		'num_comments:<=6': { "2656": 1, "2658": 1, "2653": 1, "2654": 1, "2655": 1, "2657": 1, "2659": 1, "2660": 1, "2662": 1, "2663": 1, "2664": 1, "2665": 1, "2661": 1 },
		
		'num_comments:<7': { "2656": 1, "2658": 1, "2653": 1, "2654": 1, "2655": 1, "2657": 1, "2659": 1, "2660": 1, "2662": 1, "2663": 1, "2664": 1, "2665": 1, "2661": 1 },
		
		'num_comments:<99999': { "2656": 1, "2658": 1, "2653": 1, "2654": 1, "2655": 1, "2657": 1, "2659": 1, "2660": 1, "2662": 1, "2663": 1, "2664": 1, "2665": 1, "2661": 1 }
	},
	searchRecordsNumberRangeClosed: {
		'num_comments:0..0': { "2660": 1 },
		'num_comments:0..1': { "2660": 1, "2656": 1 },
		'num_comments:0..2': { "2660": 1, "2656": 1, "2657": 1, "2658": 1, "2661": 1, "2663": 1, "2664": 1 },
		'num_comments:0..3': { "2660": 1, "2656": 1, "2657": 1, "2658": 1, "2661": 1, "2663": 1, "2664": 1 },
		'num_comments:0..4': { "2660": 1, "2656": 1, "2657": 1, "2658": 1, "2661": 1, "2663": 1, "2664": 1, "2653": 1, "2659": 1, "2662": 1, "2665": 1 },
		'num_comments:0..5': { "2660": 1, "2656": 1, "2657": 1, "2658": 1, "2661": 1, "2663": 1, "2664": 1, "2653": 1, "2659": 1, "2662": 1, "2665": 1, "2654": 1 },
		'num_comments:0..6': { "2660": 1, "2656": 1, "2657": 1, "2658": 1, "2661": 1, "2663": 1, "2664": 1, "2653": 1, "2659": 1, "2662": 1, "2665": 1, "2654": 1, "2655": 1 },
		'num_comments:0..7': { "2660": 1, "2656": 1, "2657": 1, "2658": 1, "2661": 1, "2663": 1, "2664": 1, "2653": 1, "2659": 1, "2662": 1, "2665": 1, "2654": 1, "2655": 1 },
		'num_comments:0..99999': { "2660": 1, "2656": 1, "2657": 1, "2658": 1, "2661": 1, "2663": 1, "2664": 1, "2653": 1, "2659": 1, "2662": 1, "2665": 1, "2654": 1, "2655": 1 },
		
		'num_comments:1..6': { "2656": 1, "2657": 1, "2658": 1, "2661": 1, "2663": 1, "2664": 1, "2653": 1, "2659": 1, "2662": 1, "2665": 1, "2654": 1, "2655": 1 },
		'num_comments:2..6': { "2657": 1, "2658": 1, "2661": 1, "2663": 1, "2664": 1, "2653": 1, "2659": 1, "2662": 1, "2665": 1, "2654": 1, "2655": 1 },
		'num_comments:3..6': { "2653": 1, "2659": 1, "2662": 1, "2665": 1, "2654": 1, "2655": 1 },
		'num_comments:4..6': { "2653": 1, "2659": 1, "2662": 1, "2665": 1, "2654": 1, "2655": 1 },
		'num_comments:5..6': { "2654": 1, "2655": 1 },
		'num_comments:6..6': { "2655": 1 },
		
		'num_comments:6..7': { "2655": 1 },
		'num_comments:6..99999': { "2655": 1 },
		'num_comments:7..7': {},
		'num_comments:7..99999': {},
		
		// 'num_comments:0..0': { "2660": 1 },
		'num_comments:1..1': { "2656": 1 },
		'num_comments:2..2': { "2657": 1, "2658": 1, "2661": 1, "2663": 1, "2664": 1 },
		'num_comments:3..3': {},
		'num_comments:4..4': { "2653": 1, "2659": 1, "2662": 1, "2665": 1 },
		'num_comments:5..5': { "2654": 1 },
		// 'num_comments:6..6': { "2655": 1 }
	},
	searchRecordsAll: {
		'*': { "2660": 1, "2656": 1, "2657": 1, "2658": 1, "2661": 1, "2663": 1, "2664": 1, "2653": 1, "2659": 1, "2662": 1, "2665": 1, "2654": 1, "2655": 1 }
	},
	searchRecordsPxQL: {
		// basic
		'(title =~ "xchfqkk6d4")': { "2662": 1 },
		'(title =~ "Released to Preproduction")': { "2653": 1, "2654": 1, "2659": 1, "2662": 1, "2665": 1 },
		'(status = "open" & title =~ "Released to Preproduction")': { "2653": 1, "2654": 1 },
		'(status = "closed" & title =~ "Released to Preproduction")': { "2659": 1, "2662": 1, "2665": 1 },
		
		// useless extra parens
		'(status = "closed" & (title =~ "Released to Preproduction"))': { "2659": 1, "2662": 1, "2665": 1 },
		'((status = "closed") & title =~ "Released to Preproduction")': { "2659": 1, "2662": 1, "2665": 1 },
		'((status = "closed") & (title =~ "Released to Preproduction"))': { "2659": 1, "2662": 1, "2665": 1 },
		
		// date formats
		'(modified = "2016-02-22")': { "2656": 1 },
		'(modified = "2016/02/22")': { "2656": 1 },
		'(modified = "2016_02_22")': { "2656": 1 },
		'(modified = "1456164397")': { "2656": 1 }, // epoch date
		
		// date ranges
		'(modified < "2000-01-01")': {},
		'(modified < "2016-02-22")': {},
		
		'(modified <= "2016-02-22")': { "2656": 1 },
		'(modified < "2016-02-23")': { "2656": 1 },
		
		'(modified<="2016-02-22")': { "2656": 1 }, // no spaces
		'(modified<"2016-02-23")': { "2656": 1 }, // no spaces
		
		// numbers
		'(num_comments = 0)': { "2660": 1 },
		'(num_comments = 1)': { "2656": 1 },
		'(num_comments = 2)': { "2657": 1, "2658": 1, "2661": 1, "2663": 1, "2664": 1 },
		
		'(num_comments = "0")': { "2660": 1 }, // quotes should work with numbers
		'(num_comments = "1")': { "2656": 1 }, // quotes should work with numbers
		'(num_comments = "2")': { "2657": 1, "2658": 1, "2661": 1, "2663": 1, "2664": 1 }, // quotes should work with numbers
		
		'(num_comments < 0)': {},
		'(num_comments <= 0)': { "2660": 1 },
		
		'(num_comments >= 0)': { "2656": 1, "2658": 1, "2653": 1, "2654": 1, "2655": 1, "2657": 1, "2659": 1, "2660": 1, "2662": 1, "2663": 1, "2664": 1, "2665": 1, "2661": 1 },
		
		'(num_comments > 0)': { "2656": 1, "2658": 1, "2653": 1, "2654": 1, "2655": 1, "2657": 1, "2659": 1, "2662": 1, "2663": 1, "2664": 1, "2665": 1, "2661": 1 },
		
		'(num_comments < 1)': { "2660": 1 },
		'(num_comments <= 1)': { "2660": 1, "2656": 1 },
		
		// complex boolean
		'((status = "open" | status = "closed" | status = "wallaby") & (title =~ "amazon" & title =~ "monitor") & modified = "2016_02_22")': { "2656": 1 },
		
		// bad queries (expect errors)
		'(nonexist = "foo")': false, // index not found
		'(title =~ "preproduction" ^^ status = "open")': false, // invalid operator
		'(title =~ "preproduction" && status = "open)': false, // missing close quote
		'(title =~ "preproduction" && status = "open"))': false, // double close paren
		'(title =~ "preproduction" && (status = "open")': false // missing close paren
	},
	searchRecordsMultiDate: {
		'modified:2016-03-03': { "2665": 1 },
		'modified:2016-03-04': { "2665": 1 },
		'modified:2016-03-05': { "2665": 1 },
		
		'modified:>=2016-03-03': { "2661": 1, "2665": 1 },
		'modified:>=2016-03-04': { "2661": 1, "2665": 1 },
		'modified:>=2016-03-05': { "2661": 1, "2665": 1 },
		'modified:>=2016-03-06': { "2661": 1 },
		
		'modified:2016-03-03..2016-03-05': { "2665": 1 },
		'modified:2016-03-02..2016-03-03': { "2665": 1 },
		'modified:2016-03-05..2016-03-06': { "2665": 1 },
		'modified:2016-03-02..2016-03-06': { "2665": 1 },
		'modified:2016-03-01..2016-03-02': {},
		'modified:2016-03-06..2016-03-07': {}
	},
	searchRecordsBadKeys: {
		'title:control1': { "2665": 1 },
		'title:control2': { "2665": 1 },
		'title:control1 control2': { "2665": 1 },
		'title:"control1 control2"': {},
		
		'title:constructor': { "2665": 1 },
		'title:__defineGetter__': { "2665": 1 }, 
		'title:__defineSetter__': { "2665": 1 }, 
		'title:hasOwnProperty': { "2665": 1 }, 
		'title:__lookupGetter__': { "2665": 1 }, 
		'title:__lookupSetter__': { "2665": 1 }, 
		'title:isPrototypeOf': { "2665": 1 }, 
		'title:propertyIsEnumerable': { "2665": 1 }, 
		'title:toString': { "2665": 1 }, 
		'title:valueOf': { "2665": 1 }, 
		'title:__proto__': { "2665": 1 }, 
		'title:toLocaleString': { "2665": 1 },
		
		'title:"control1 constructor"': { "2665": 1 },
		'title:"toLocaleString control2"': { "2665": 1 },
		'title:"toLocaleString constructor"': {},
		
		'title:control1 -__proto__': {},
		'title:toLocaleString -__proto__': {}
	}
};

module.exports = {
	tests: [
		
		function resetFixtures(test) {
			fixtures = Tools.copyHash( orig_fixtures, true );
			sample_tickets = Tools.copyHash( orig_sample_tickets, true );
			test.ok( true );
			test.done();
		},
	
		// insert record
		
		function insertRecord1(test) {
			var self = this;
			
			var ticket = sample_tickets[0];
			
			this.storage.indexRecord( ticket.ID, ticket, index_config, function(err) {
				test.ok( !err, "No error indexing record: " + err );
				test.done();
			} );
		},
		
		// simple searches
		
		function searchRecord1(test) {
			var self = this;
			
			this.storage.searchRecords( 'status:open', index_config, function(err, results) {
				test.ok( !err, "No error searching record: " + err );
				
				test.debug("Search results:", results);
				test.ok( !!results, "Got results from search" );
				test.ok( typeof(results) == 'object', "Results is an object: " + typeof(results) );
				
				var keys = Object.keys(results);
				test.ok( keys.length == 1, "Found exactly one record: " + keys.length );
				test.ok( keys[0] == "2653", "Found correct record: " + keys[0] );
				
				test.done();
			} );
		},
		
		function searchRecord2(test) {
			// test negative (false) search
			var self = this;
			
			this.storage.searchRecords( 'status:closed', index_config, function(err, results) {
				test.ok( !err, "No error searching record: " + err );
				
				test.debug("Search results:", results);
				test.ok( !!results, "Got results from search" );
				test.ok( typeof(results) == 'object', "Results is an object: " + typeof(results) );
				
				var keys = Object.keys(results);
				test.ok( keys.length == 0, "Found exactly zero records: " + keys.length );
				
				test.done();
			} );
		},
		
		// update record
		
		function updateRecord1(test) {
			var self = this;
			
			// Note: this is a SPARSE update, missing some fields and sorters
			var update = {
				ID: "2653",
				Status: "Closed",
				Summary: "This has been updated the of and a to test12345"
			};
			
			this.storage.indexRecord( update.ID, update, index_config, function(err) {
				test.ok( !err, "No error updating record: " + err );
				test.done();
			} );
		},
		
		// search again
		
		function searchRecord3(test) {
			var self = this;
			
			this.storage.searchRecords( 'status:closed', index_config, function(err, results) {
				test.ok( !err, "No error searching record: " + err );
				
				test.debug("Search results:", results);
				test.ok( !!results, "Got results from search" );
				test.ok( typeof(results) == 'object', "Results is an object: " + typeof(results) );
				
				var keys = Object.keys(results);
				test.ok( keys.length == 1, "Found exactly one record: " + keys.length );
				test.ok( keys[0] == "2653", "Found correct record: " + keys[0] );
				
				test.done();
			} );
		},
		
		function searchRecord4(test) {
			// test negative (false) search (again)
			var self = this;
			
			this.storage.searchRecords( 'status:open', index_config, function(err, results) {
				test.ok( !err, "No error searching record: " + err );
				
				test.debug("Search results:", results);
				test.ok( !!results, "Got results from search" );
				test.ok( typeof(results) == 'object', "Results is an object: " + typeof(results) );
				
				var keys = Object.keys(results);
				test.ok( keys.length == 0, "Found exactly zero records: " + keys.length );
				
				test.done();
			} );
		},
		
		function searchRecord5(test) {
			var self = this;
			
			this.storage.searchRecords( 'title:This has been updated the of and a to test12345', index_config, function(err, results) {
				test.ok( !err, "No error searching record: " + err );
				
				test.debug("Search results:", results);
				test.ok( !!results, "Got results from search" );
				test.ok( typeof(results) == 'object', "Results is an object: " + typeof(results) );
				
				var keys = Object.keys(results);
				test.ok( keys.length == 1, "Found exactly one record: " + keys.length );
				test.ok( keys[0] == "2653", "Found correct record: " + keys[0] );
				
				test.done();
			} );
		},
		
		function searchRecord6(test) {
			var self = this;
			
			this.storage.searchRecords( 'title:updated test12345', index_config, function(err, results) {
				test.ok( !err, "No error searching record: " + err );
				
				test.debug("Search results:", results);
				test.ok( !!results, "Got results from search" );
				test.ok( typeof(results) == 'object', "Results is an object: " + typeof(results) );
				
				var keys = Object.keys(results);
				test.ok( keys.length == 1, "Found exactly one record: " + keys.length );
				test.ok( keys[0] == "2653", "Found correct record: " + keys[0] );
				
				test.done();
			} );
		},
		
		function searchRecord7(test) {
			// test negative (false) search (again)
			var self = this;
			
			this.storage.searchRecords( 'title:updatedZ test123456', index_config, function(err, results) {
				test.ok( !err, "No error searching record: " + err );
				
				test.debug("Search results:", results);
				test.ok( !!results, "Got results from search" );
				test.ok( typeof(results) == 'object', "Results is an object: " + typeof(results) );
				
				var keys = Object.keys(results);
				test.ok( keys.length == 0, "Found exactly zero records: " + keys.length );
				
				test.done();
			} );
		},
		
		// unindex record
		
		function unindexRecord1(test) {
			var self = this;
			
			this.storage.unindexRecord( "2653", index_config, function(err) {
				test.ok( !err, "No error indexing record: " + err );
				test.done();
			} );
		},
		
		function searchRecord8(test) {
			// test negative (false) search (again)
			var self = this;
			
			this.storage.searchRecords( 'title:test12345', index_config, function(err, results) {
				test.ok( !err, "No error searching record: " + err );
				
				test.debug("Search results:", results);
				test.ok( !!results, "Got results from search" );
				test.ok( typeof(results) == 'object', "Results is an object: " + typeof(results) );
				
				var keys = Object.keys(results);
				test.ok( keys.length == 0, "Found exactly zero records: " + keys.length );
				
				test.done();
			} );
		},
		
		// insert records
		
		function insertRecords(test) {
			var self = this;
			
			async.eachSeries( sample_tickets,
				function(ticket, callback) {
					self.storage.indexRecord( ticket.ID, ticket, index_config, callback );
				},
				function(err) {
					test.ok( !err, "No error indexing records: " + err );
					test.done();
				}
			);
		},
		
		// search records
		
		function searchRecordsBasic1(test) {
			var self = this;
			
			this.storage.searchRecords( 'status:open', index_config, function(err, results) {
				test.ok( !err, "No error searching record: " + err );
				
				test.debug("Search results:", results);
				test.ok( !!results, "Got results from search" );
				test.ok( typeof(results) == 'object', "Results is an object: " + typeof(results) );
				
				var correct = {};
				Tools.findObjects( sample_tickets, { Status: "Open" } ).forEach( function(ticket) {
					correct[ ticket.ID ] = 1;
				} );
				
				test.ok( Tools.numKeys(results) == Tools.numKeys(correct), "Correct number of records found" );
				
				test.ok( Tools.numKeys( Tools.mergeHashes(results, correct) ) == Tools.numKeys(results), "Correct records found: " + JSON.stringify(results) );
				test.done();
			} );
		},
		
		function searchRecordsBasic2(test) {
			var self = this;
			
			this.storage.searchRecords( 'status:closed', index_config, function(err, results) {
				test.ok( !err, "No error searching record: " + err );
				
				test.debug("Search results:", results);
				test.ok( !!results, "Got results from search" );
				test.ok( typeof(results) == 'object', "Results is an object: " + typeof(results) );
				
				var correct = {};
				Tools.findObjects( sample_tickets, { Status: "Closed" } ).forEach( function(ticket) {
					correct[ ticket.ID ] = 1;
				} );
				
				test.ok( Tools.numKeys(results) == Tools.numKeys(correct), "Correct number of records found" );
				
				test.ok( Tools.numKeys( Tools.mergeHashes(results, correct) ) == Tools.numKeys(results), "Correct records found: " + JSON.stringify(results) );
				test.done();
			} );
		},
		
		// search with negatives
		
		function searchRecordsNegative(test) {
			var self = this;
			
			this.storage.searchRecords( 'status:open title:-hzd86vdxtd', index_config, function(err, results) {
				test.ok( !err, "No error searching record: " + err );
				
				test.debug("Search results:", results);
				test.ok( !!results, "Got results from search" );
				test.ok( typeof(results) == 'object', "Results is an object: " + typeof(results) );
				
				var keys = Object.keys(results);
				test.ok( keys.length == 1, "Found exactly one record: " + keys.length );
				test.ok( keys[0] == "2653", "Found correct record: " + keys[0] );
				
				test.done();
			} );
		},
		
		// search extact phrase
		
		function searchRecordsExact(test) {
			var self = this;
			
			var map = {};
			sample_tickets.forEach( function(ticket) {
				var expected = {}; expected[ticket.ID] = 1;
				map[ 'title:"'+ticket.Summary+'"' ] = expected;
			} );
			
			this.multiIndexSearch(map, index_config, test, function() {
				test.done();
			});
		},
		
		function searchRecordsExact2(test) {
			var self = this;
			var map = fixtures.searchRecordsExact2;
			
			this.multiIndexSearch(map, index_config, test, function() {
				test.done();
			});
		},
		
		// search date exact
		
		function searchRecordsDateExact(test) {
			var self = this;
			var map = fixtures.searchRecordsDateExact;
			
			this.multiIndexSearch(map, index_config, test, function() {
				test.done();
			});
		},
		
		// search open date range
		
		function searchRecordsDateRangeOpen(test) {
			var self = this;
			var map = fixtures.searchRecordsDateRangeOpen;
			
			this.multiIndexSearch(map, index_config, test, function() {
				test.done();
			});
		},
		
		// search closed date range
		
		function searchRecordsDateRangeClosed(test) {
			var self = this;
			var map = fixtures.searchRecordsDateRangeClosed;
			
			this.multiIndexSearch(map, index_config, test, function() {
				test.done();
			});
		},
		
		// search number exact
		
		function searchRecordsNumberExact(test) {
			var self = this;
			var map = fixtures.searchRecordsNumberExact;
			
			this.multiIndexSearch(map, index_config, test, function() {
				test.done();
			});
		},
		
		// search number range open
		
		function searchRecordsNumberRangeOpen(test) {
			var self = this;
			var map = fixtures.searchRecordsNumberRangeOpen;
			
			this.multiIndexSearch(map, index_config, test, function() {
				test.done();
			});
		},
		
		// search number range closed
		
		function searchRecordsNumberRangeClosed(test) {
			var self = this;
			var map = fixtures.searchRecordsNumberRangeClosed;
			
			this.multiIndexSearch(map, index_config, test, function() {
				test.done();
			});
		},
		
		function searchRecordsAll(test) {
			var self = this;
			var map = fixtures.searchRecordsAll;
			
			this.multiIndexSearch(map, index_config, test, function() {
				test.done();
			});
		},
		
		// search complex boolean
		
		function searchRecordsComplexBoolean(test) {
			var self = this;
			
			var query = {
				mode: "and",
				criteria: [
					{
						mode: "or",
						criteria: [
							{ index: "status", word: "open" },
							{ index: "status", word: "closed" },
							{ index: "status", word: "wallaby" }
						]
					},
					{
						mode: "and",
						criteria: [
							{ index: "title", word: "amazon" },
							{ index: "title", word: "monitor" }
						]
					},
					{ index: "modified", word: "2016_02_22" }
				]
			};
			
			this.storage.searchRecords( query, index_config, function(err, results) {
				test.ok( !err, "No error searching records: " + err );
				
				test.debug("Search results:", results);
				test.ok( !!results, "Got results from search" );
				test.ok( typeof(results) == 'object', "Results is an object: " + typeof(results) );
				
				var keys = Object.keys(results);
				test.ok( keys.length == 1, "Found exactly one record: " + keys.length );
				test.ok( keys[0] == "2656", "Found correct record: " + keys[0] );
				
				test.done();
			} );
		},
		
		function searchRecordsPxQL(test) {
			var self = this;
			var map = fixtures.searchRecordsPxQL;
			
			this.multiIndexSearch(map, index_config, test, function() {
				test.done();
			});
		},
		
		function searchSingleRecords(test) {
			// test known set of searches and results on each record
			var self = this;
			var all_records = fixtures.searchRecordsAll['*'];
			var searches = [];
			
			var map = {};
			['searchRecordsExact2', 'searchRecordsDateExact', 'searchRecordsDateRangeOpen', 'searchRecordsDateRangeClosed', 'searchRecordsNumberExact', 'searchRecordsNumberRangeOpen', 'searchRecordsNumberRangeClosed', 'searchRecordsAll', 'searchRecordsPxQL'].forEach( function(cat) {
				Tools.mergeHashInto( map, fixtures[cat] );
			});
			
			for (var query in map) {
				var expected = map[query];
				if (expected) {
					for (var record_id in expected) {
						searches.push({ query: query, record_id: record_id, result: true });
					}
					for (var record_id in all_records) {
						if (!(record_id in expected)) {
							searches.push({ query: query, record_id: record_id, result: false });
						}
					}
				}
			}
			
			async.eachSeries( searches,
				function(search, callback) {
					var squery = search.query;
					var record_id = search.record_id;
					var expected_result = search.result;
					
					self.storage.searchSingle( squery, record_id, index_config, function(err, result) {
						test.ok( !err, "No error searching record: " + err );
						
						test.debug("Single Search: "+squery+" -- result for " + record_id + ": " + result);
						test.ok( result === expected_result, "Got correct results from search: " + result );
						
						callback();
					}); // searchSingle
				},
				function(err) {
					// all searches complete
					test.done();
				}
			); // eachSeries
		},
		
		// sort records
		
		function sortRecords(test) {
			var self = this;
			
			this.storage.searchRecords( 'status:open|closed', index_config, function(err, results) {
				test.ok( !err, "No error searching records: " + err );
				
				test.debug("Search results:", results);
				test.ok( !!results, "Got results from search" );
				test.ok( typeof(results) == 'object', "Results is an object: " + typeof(results) );
				
				var correct = [];
				var correct_ids = [];
				for (var id in results) {
					var ticket = Tools.findObject( sample_tickets, { ID: id } );
					correct.push({ id: id, created: parseInt(ticket.Createdate) });
				}
				correct = correct.sort( function(a, b) {
					return a.created - b.created;
				} );
				correct.forEach( function(obj) {
					correct_ids.push( obj.id );
				} );
				
				test.debug("Correct order:", correct);
				
				self.storage.sortRecords(results, 'created', 1, index_config, function(err, sorted) {
					test.ok( !err, "No error sorting records: " + err );
					
					test.ok( !!sorted, "Got sorted results" );
					test.ok( !!sorted.length, "Sorted results has a length" );
					
					test.debug("Got sorted tickets:", sorted);
					
					test.ok( sorted.join('|') == correct_ids.join('|'), "Correct sort order: " + sorted.join('|') );
					
					test.done();
				}); // sortRecords
			}); // searchRecords
		},
		
		function testMultiDate(test) {
			var self = this;
			var map = fixtures.searchRecordsMultiDate;
			
			// Note: this is a sparse update, missing some fields and sorters
			var update = {
				ID: "2665",
				// "Modifydate": "1457051382 1457137782 1457224182",
				"Modifydate": "2016/03/03, 2016/03/04, 2016/03/05",
			};
			
			this.storage.indexRecord( update.ID, update, index_config, function(err) {
				test.ok( !err, "No error updating record: " + err );
				
				self.multiIndexSearch(map, index_config, test, function() {
					test.done();
				});
			} );
		},
		
		function testBadPropertyNames(test) {
			var self = this;
			var map = fixtures.searchRecordsBadKeys;
			
			// Note: this is a sparse update, missing some fields and sorters
			var update = {
				ID: "2665",
				"Summary": "control1, constructor, __defineGetter__, __defineSetter__, hasOwnProperty, __lookupGetter__, __lookupSetter__, isPrototypeOf, propertyIsEnumerable, toString, valueOf, __proto__, toLocaleString, control2"
			};
			
			this.storage.indexRecord( update.ID, update, index_config, function(err) {
				test.ok( !err, "No error updating record: " + err );
				
				self.multiIndexSearch(map, index_config, test, function() {
					test.done();
				});
			} );
		},
		
		function testBadRecordID(test) {
			// add a record with a toxic ID, make sure it can be indexed and searched
			var self = this;
			var bad_ticket = {
				ID: "constructor",
				Summary: "hello frogtoad there"
			};
			var map = {
				'title:frogtoad': { "constructor": 1 },
				'title:"hello frogtoad"': { "constructor": 1 },
				'title:frogtoad -constructor': { "constructor": 1 }
			};
			
			// push onto sample_tickets so it gets cleaned up in unindexAllRecords
			sample_tickets.push(bad_ticket);
			
			this.storage.indexRecord( bad_ticket.ID, bad_ticket, index_config, function(err) {
				test.ok( !err, "No error inserting record: " + err );
				
				self.multiIndexSearch(map, index_config, test, function() {
					test.done();
				});
			}); // indexRecord
		},
		
		function testDoubleWordExactMatch(test) {
			// add a record with a repeating word, and search for exact phrases
			var self = this;
			var ticket = {
				ID: "double1",
				Summary: "lost dog dog park"
			};
			var map = {
				'title:"lost dog"': { "double1": 1 },
				'title:"lost dog dog"': { "double1": 1 },
				'title:"lost dog dog park"': { "double1": 1 },
				'title:"dog dog park"': { "double1": 1 },
				'title:"dog park"': { "double1": 1 },
				'title:"park dog"': {},
				'title:"lost park"': {},
				'title:"dog lost"': {},
				'title:"dog dog park park"': {},
				'title:"dog dog dog"': {}
			};
			
			// push onto sample_tickets so it gets cleaned up in unindexAllRecords
			sample_tickets.push(ticket);
			
			this.storage.indexRecord( ticket.ID, ticket, index_config, function(err) {
				test.ok( !err, "No error inserting record: " + err );
				
				self.multiIndexSearch(map, index_config, test, function() {
					test.done();
				});
			}); // indexRecord
		},
		
		function testDoubleWordRemoveWordExactMatch(test) {
			// add a record with a repeating word, and search for exact phrases
			// this time with remove words inserted
			var self = this;
			var ticket = {
				ID: "double2",
				Summary: "lost dog in the dog park"
			};
			var map = {
				'title:"lost dog"': { "double1": 1, "double2": 1 },
				'title:"lost dog dog"': { "double1": 1, "double2": 1 },
				'title:"lost dog dog park"': { "double1": 1, "double2": 1 },
				'title:"dog dog park"': { "double1": 1, "double2": 1 },
				'title:"dog park"': { "double1": 1, "double2": 1 },
				'title:"park dog"': {},
				'title:"lost park"': {},
				'title:"dog lost"': {},
				'title:"dog dog park park"': {},
				'title:"dog dog dog"': {}
			};
			
			// push onto sample_tickets so it gets cleaned up in unindexAllRecords
			sample_tickets.push(ticket);
			
			this.storage.indexRecord( ticket.ID, ticket, index_config, function(err) {
				test.ok( !err, "No error inserting record: " + err );
				
				self.multiIndexSearch(map, index_config, test, function() {
					test.done();
				});
			}); // indexRecord
		},
		
		function unindexAllRecords(test) {
			// unindex all records to remove temp disk space
			var self = this;
			
			async.eachSeries( sample_tickets,
				function(ticket, callback) {
					self.storage.unindexRecord( ticket.ID, index_config, callback );
				},
				function(err) {
					test.ok( !err, "No error unindexing records: " + err );
					test.done();
				}
			);
		},
		
		function indexerCleanup(test) {
			// remove data leftover by indexer
			var self = this;
			
			async.eachSeries( index_config.fields,
				function(def, callback) {
					if (def.master_list) {
						self.storage.delete( index_config.base_path + '/' + def.id + '/summary', callback );
					}
					else process.nextTick(callback);
				},
				function(err) {
					test.ok( !err, "No error cleaning up indexer: " + err );
					
					// and now the sorters
					async.eachSeries( index_config.sorters || [],
						function(sorter, callback) {
							self.storage.hashDeleteAll( index_config.base_path + '/' + sorter.id + '/sort', true, callback );
						},
						function(err) {
							test.ok( !err, "No error cleaning up sorters: " + err );
							
							// finally the primary _id hash
							self.storage.hashDeleteAll( index_config.base_path + '/_id', true, function(err) {
								test.ok( !err, "No error cleaning up indexer _id hash: " + err );
								test.done();
							} );
						} // done with sorters
					); // each sorter
				} // done with fields
			); // each field
		}
		
	] // tests array
};
```

## File: `test/test-list.js`
```javascript
// Unit tests for Storage System - List
// Copyright (c) 2015 - 2016 Joseph Huckaby
// Released under the MIT License

var os = require('os');
var fs = require('fs');
var path = require('path');
var cp = require('child_process');
var async = require('async');
var Tools = require('pixl-tools');

module.exports = {
	tests: [
	
		function listCreate1(test) {
			test.expect(1);
			this.storage.listCreate( 'list1', {}, function(err, data) {
				test.ok( !err, "No error creating list1: " + err );
				test.done();
			} );
		},
		
		function listGetEmpty1(test) {
			test.expect(2);
			this.storage.listGet( 'list1', 0, 0, function(err, items) {
				test.ok( !!items, "Expected array for empty list" );
				test.ok( !items.length, "Expected zero length in items array on empty list" );
				test.done();
			} );
		},
		
		function listPush1(test) {
			var self = this;
			test.expect(2);
			this.storage.listPush( 'list1', { foo: 'bar', number: 123 }, function(err, data) {
				test.ok( !err, "No error pushing onto list: " + err );
				test.ok( Object.keys(self.storage.locks).length == 0, "No more locks leftover in storage" );
				test.done();
			} );
		},
		
		function listGet1(test) {
			var self = this;
			test.expect(16);
			this.storage.listGet( 'list1', 0, 0, function(err, items) {
				test.ok( !err, "No error fetching list: " + err );
				test.ok( !!items, "Items is true" );
				test.ok( items.length == 1, "List has 1 item: " + items.length );
				test.ok( items[0].foo == 'bar', "List item value matches" );
				
				// check internals
				self.storage.get( 'list1', function(err, list) {
					test.ok( !err, "No error fetching list header: " + err );
					test.ok( !!list, "Got list data from header key" );
					test.ok( list.type == 'list', "List type is list: " + list.type );
					test.ok( list.length == 1, "List length is 1: " + list.length );
					test.ok( list.first_page == 0, "List first_page is 0: " + list.first_page );
					test.ok( list.last_page == 0, "List last_page is 0: " + list.last_page );
					test.ok( list.page_size > 0, "List page_size is non-zero: " + list.page_size );
					
					self.storage.get( 'list1/0', function(err, page) {
						test.ok( !err, "No error fetching list page: " + err );
						test.ok( !!page, "Got list page data" );
						test.ok( page.type == 'list_page', "Page type is correct: " + page.type );
						test.ok( !!page.items, "List page has items array" );
						test.ok( page.items.length == 1, "List page has 1 item: " + page.items.length );
						test.done();
					} );
				} ); // internals
			} );
		},
		
		function listPop1(test) {
			var self = this;
			test.expect(4);
			this.storage.listPop( 'list1', function(err, item) {
				test.ok( !err, "No error popping list: " + err );
				test.ok( !!item, "Item is true" );
				test.ok( item.foo == 'bar', "List popped item value matches" );
				test.ok( Object.keys(self.storage.locks).length == 0, "No more locks leftover in storage" );
				test.done();
			} );
		},
		
		function listGetEmpty2(test) {
			var self = this;
			test.expect(15);
			this.storage.listGet( 'list1', 0, 0, function(err, items) {
				test.ok( !err, "No error expected getting empty list again" );
				test.ok( !!items, "Expected array for empty list" );
				test.ok( !items.length, "Expected zero length in items array on empty list" );
				
				// check internals
				self.storage.get( 'list1', function(err, list) {
					test.ok( !err, "No error fetching list header: " + err );
					test.ok( !!list, "Got list data from header key" );
					test.ok( list.type == 'list', "List type is list: " + list.type );
					test.ok( list.length == 0, "List length is 0: " + list.length );
					test.ok( list.first_page == 0, "List first_page is 0: " + list.first_page );
					test.ok( list.last_page == 0, "List last_page is 0: " + list.last_page );
					test.ok( list.page_size > 0, "List page_size is non-zero: " + list.page_size );
					
					self.storage.get( 'list1/0', function(err, page) {
						test.ok( !err, "No error fetching list page: " + err );
						test.ok( !!page, "Got list page data" );
						test.ok( page.type == 'list_page', "Page type is correct: " + page.type );
						test.ok( !!page.items, "List page has items array" );
						test.ok( page.items.length == 0, "List page has 0 items: " + page.items.length );
						test.done();
					} );
				} ); // internals
			} );
		},
		
		function listPush2(test) {
			var self = this;
			test.expect(13);
			this.storage.listPush( 'list1', { foo: 'bar2', number: 124 }, function(err, data) {
				test.ok( !err, "No error pushing list again: " + err );
				
				// check internals
				self.storage.get( 'list1', function(err, list) {
					test.ok( !err, "No error fetching list header: " + err );
					test.ok( !!list, "Got list data from header key" );
					test.ok( list.type == 'list', "List type is list: " + list.type );
					test.ok( list.length == 1, "List length is 1: " + list.length );
					test.ok( list.first_page == 0, "List first_page is 0: " + list.first_page );
					test.ok( list.last_page == 0, "List last_page is 0: " + list.last_page );
					test.ok( list.page_size > 0, "List page_size is non-zero: " + list.page_size );
					
					self.storage.get( 'list1/0', function(err, page) {
						test.ok( !err, "No error fetching list page: " + err );
						test.ok( !!page, "Got list page data" );
						test.ok( page.type == 'list_page', "Page type is correct: " + page.type );
						test.ok( !!page.items, "List page has items array" );
						test.ok( page.items.length == 1, "List page has 1 item: " + page.items.length );
						test.done();
					} );
				} ); // internals
			} );
		},
		
		function listDelete1(test) {
			var self = this;
			test.expect(2);
			this.storage.listDelete( 'list1', true, function(err, data) {
				test.ok( !err, "No error deleting list: " + err );
				test.ok( Object.keys(self.storage.locks).length == 0, "No more locks leftover in storage" );
				test.done();
			} );
		},
		
		function listGetEmpty3(test) {
			test.expect(1);
			this.storage.listGet( 'list1', 0, 0, function(err, items) {
				test.ok( !!err, "Error expected getting deleted list" );
				test.done();
			} );
		},
		
		function listGetInfoEmpty1(test) {
			var self = this;
			test.expect(3);
			this.storage.listGetInfo( 'list1', function(err, list) {
				test.ok( !!err, "Error expected getting list info after delete" );
				
				// check internals
				self.storage.get( 'list1', function(err, list) {
					test.ok( !!err, "Error expected fetching list header: " + err );
					
					self.storage.get( 'list1/0', function(err, page) {
						test.ok( !!err, "Error expected fetching list page: " + err );
						test.done();
					} );
				} ); // internals
			} );
		},
		
		function listCreate2(test) {
			test.expect(1);
			this.storage.listCreate( 'list2', {}, function(err, data) {
				test.ok( !err, "No error creating list2: " + err );
				test.done();
			} );
		},
				
		function listPushMulti1(test) {
			var self = this;
			var idx = 0;
			test.expect(1);
			
			async.whilst(
				function() { return idx < 10; },
				function(callback) {
					self.storage.listPush( 'list2', { foo: 'bar', number: idx++ }, function(err, data) {
						callback(err);
					} );
				},
				function(err) {
					test.ok( !err, "No error pushing items to list: " + err );
					test.done();
				}
			);
		},
		
		function listGetMulti1(test) {
			test.expect(4);
			this.storage.listGet( 'list2', 0, 0, function(err, items) {
				test.ok( !err, "No error fetching list2: " + err );
				test.ok( !!items, "Items is true" );
				test.ok( items.length == 10, "List has 10 items: " + items.length );
				test.ok( items[5].number == 5, "List item 5 value matches" );
				test.done();
			} );
		},
		
		function listGetInfo1(test) {
			test.expect(2);
			this.storage.listGetInfo( 'list2', function(err, list) {
				test.ok( !err, "No error getting list info after multi-push: " + err );
				test.ok( list.first_page == list.last_page, "First page and last page are the same" );
				test.done();
			} );
		},
		
		function listPushNewPage1(test) {
			// This push should create a new page
			test.expect(1);
			this.storage.listPush( 'list2', { foo: 'bar', number: 10 }, function(err, data) {
				test.ok( !err, "No error pushing new page onto list: " + err );
				test.done();
			} );
		},
		
		function listGetMulti2(test) {
			test.expect(4);
			this.storage.listGet( 'list2', 0, 0, function(err, items) {
				test.ok( !err, "No error fetching list2: " + err );
				test.ok( !!items, "Items is true" );
				test.ok( items.length == 11, "List has 11 items: " + items.length );
				test.ok( items[5].number == 5, "List item 5 value matches" );
				test.done();
			} );
		},
		
		function listGetCrossPage1(test) {
			test.expect(5);
			this.storage.listGet( 'list2', 9, 2, function(err, items) {
				test.ok( !err, "No error fetching list2(9,2): " + err );
				test.ok( !!items, "Items is true" );
				test.ok( items.length == 2, "List has 2 items: " + items.length );
				test.ok( items[0].number == 9, "List item 0 value matches" );
				test.ok( items[1].number == 10, "List item 1 value matches" );
				test.done();
			} );
		},
		
		function listGetInfo2(test) {
			var self = this;
			test.expect(19);
			this.storage.listGetInfo( 'list2', function(err, list) {
				test.ok( !err, "No error getting list info after new page push: " + err );
				test.ok( list.first_page == list.last_page - 1, "First page and last page are one apart" );
				
				// check internals
				self.storage.get( 'list2', function(err, list) {
					test.ok( !err, "No error fetching list header: " + err );
					test.ok( !!list, "Got list data from header key" );
					test.ok( list.type == 'list', "List type is list: " + list.type );
					test.ok( list.length == 11, "List length is 11: " + list.length );
					test.ok( list.first_page == 0, "List first_page is 0: " + list.first_page );
					test.ok( list.last_page == 1, "List last_page is 1: " + list.last_page );
					test.ok( list.page_size > 0, "List page_size is non-zero: " + list.page_size );
					
					self.storage.get( 'list2/0', function(err, page) {
						test.ok( !err, "No error fetching first list page: " + err );
						test.ok( !!page, "Got list page data" );
						test.ok( page.type == 'list_page', "Page type is correct: " + page.type );
						test.ok( !!page.items, "List page has items array" );
						test.ok( page.items.length == 10, "List page has 10 items: " + page.items.length );
						
						self.storage.get( 'list2/1', function(err, page) {
							test.ok( !err, "No error fetching second list page: " + err );
							test.ok( !!page, "Got list page data" );
							test.ok( page.type == 'list_page', "Page type is correct: " + page.type );
							test.ok( !!page.items, "List page has items array" );
							test.ok( page.items.length == 1, "List page has 1 item: " + page.items.length );
							test.done();
						} );
					} );
				} ); // internals
			} );
		},
		
		function listEach(test) {
			// iterate over list items using listEach
			var num_items = 0;
			this.storage.listEach( 'list2',
				function(item, idx, callback) {
					test.ok( !!item, "Got item" );
					test.ok( item.number == idx, "Item has correct number property" );
					num_items++;
					callback();
				},
				function(err) {
					test.ok( !err, "No error iterating list: " + err );
					test.ok( num_items == 11, "Iterated 11 items: " + num_items );
					test.done();
				}
			);
		},
		
		function listEachPage(test) {
			// iterate over list pages
			var num_pages = 0;
			this.storage.listEachPage( 'list2',
				function(items, callback) {
					test.ok( !!items, "Got items from page" );
					test.ok( !!items.length, "Nonzero items from page" );
					num_pages++;
					callback();
				},
				function(err) {
					test.ok( !err, "No error iterating list: " + err );
					test.ok( num_pages == 2, "Iterated 2 pages: " + num_pages );
					test.done();
				}
			);
		},
		
		function listEachUpdate(test) {
			// update some items
			var self = this;
			
			this.storage.listEachUpdate( 'list2',
				function(item, idx, callback) {
					if (idx % 2 == 1) {
						item.odd = true;
						callback(null, true);
					}
					else callback();
				},
				function(err) {
					test.ok( !err, "No error iterating list: " + err );
					
					self.storage.listGet( 'list2', 0, 0, function(err, items) {
						test.ok( !err, "No error fetching list2: " + err );
						test.ok( !!items, "Items is true" );
						test.ok( items.length == 11, "List has 11 items: " + items.length );
						
						for (var idx = 0, len = items.length; idx < len; idx++) {
							var item = items[idx];
							if (idx % 2 == 1) test.ok( !!item.odd, "Odd item is now odd" );
							else test.ok( !item.odd, "Even item is not odd" );
						}
						
						test.done();
					} );
				}
			);
		},
		
		function listEachPageUpdate(test) {
			// update some items, a page at a time
			var self = this;
			
			this.storage.listEachPageUpdate( 'list2',
				function(items, callback) {
					items.forEach( function(item) {
						if (!item.odd) item.even = true;
					} );
					callback(null, true);
				},
				function(err) {
					test.ok( !err, "No error iterating list: " + err );
					
					self.storage.listGet( 'list2', 0, 0, function(err, items) {
						test.ok( !err, "No error fetching list2: " + err );
						test.ok( !!items, "Items is true" );
						test.ok( items.length == 11, "List has 11 items: " + items.length );
						
						for (var idx = 0, len = items.length; idx < len; idx++) {
							var item = items[idx];
							if (idx % 2 == 0) test.ok( !!item.even, "Even item is now even" );
							else test.ok( !item.even, "Odd item is not even" );
						}
						
						test.done();
					} );
				}
			);
		},
		
		function listPop2(test) {
			test.expect(3);
			this.storage.listPop( 'list2', function(err, item) {
				test.ok( !err, "No error popping list: " + err );
				test.ok( !!item, "Item is true" );
				test.ok( item.number == 10, "List popped item value matches 10: " + item.number );
				test.done();
			} );
		},
		
		function listGetInfo3(test) {
			var self = this;
			test.expect(15);
			this.storage.listGetInfo( 'list2', function(err, list) {
				test.ok( !err, "No error getting list info after new page push: " + err );
				test.ok( list.first_page == list.last_page, "First page and last page are the same after pop" );
				
				// check internals
				self.storage.get( 'list2', function(err, list) {
					test.ok( !err, "No error fetching list header: " + err );
					test.ok( !!list, "Got list data from header key" );
					test.ok( list.type == 'list', "List type is list: " + list.type );
					test.ok( list.length == 10, "List length is 10: " + list.length );
					test.ok( list.first_page == 0, "List first_page is 0: " + list.first_page );
					test.ok( list.last_page == 0, "List last_page is 0: " + list.last_page );
					test.ok( list.page_size > 0, "List page_size is non-zero: " + list.page_size );
					
					self.storage.get( 'list2/0', function(err, page) {
						test.ok( !err, "No error fetching first list page: " + err );
						test.ok( !!page, "Got list page data" );
						test.ok( page.type == 'list_page', "Page type is correct: " + page.type );
						test.ok( !!page.items, "List page has items array" );
						test.ok( page.items.length == 10, "List page has 10 items: " + page.items.length );
						
						self.storage.get( 'list2/1', function(err, page) {
							test.ok( !!err, "Expected error fetching second list page: " + err );
							test.done();
						} );
					} );
				} ); // internals
			} );
		},
		
		function listPushNewPage2(test) {
			// This push should create a new page (again)
			test.expect(1);
			this.storage.listPush( 'list2', { foo: 'bar', number: 10, again: 1 }, function(err, data) {
				test.ok( !err, "No error pushing new page again: " + err );
				test.done();
			} );
		},
		
		function listGetInfo4(test) {
			var self = this;
			test.expect(19);
			this.storage.listGetInfo( 'list2', function(err, list) {
				test.ok( !err, "No error getting list info after new page push again: " + err );
				test.ok( list.first_page == list.last_page - 1, "First page and last page are one apart again" );
				
				// check internals
				self.storage.get( 'list2', function(err, list) {
					test.ok( !err, "No error fetching list header: " + err );
					test.ok( !!list, "Got list data from header key" );
					test.ok( list.type == 'list', "List type is list: " + list.type );
					test.ok( list.length == 11, "List length is 11: " + list.length );
					test.ok( list.first_page == 0, "List first_page is 0: " + list.first_page );
					test.ok( list.last_page == 1, "List last_page is 1: " + list.last_page );
					test.ok( list.page_size > 0, "List page_size is non-zero: " + list.page_size );
					
					self.storage.get( 'list2/0', function(err, page) {
						test.ok( !err, "No error fetching first list page: " + err );
						test.ok( !!page, "Got list page data" );
						test.ok( page.type == 'list_page', "Page type is correct: " + page.type );
						test.ok( !!page.items, "List page has items array" );
						test.ok( page.items.length == 10, "List page has 10 items: " + page.items.length );
						
						self.storage.get( 'list2/1', function(err, page) {
							test.ok( !err, "No error fetching second list page: " + err );
							test.ok( !!page, "Got list page data" );
							test.ok( page.type == 'list_page', "Page type is correct: " + page.type );
							test.ok( !!page.items, "List page has items array" );
							test.ok( page.items.length == 1, "List page has 1 item: " + page.items.length );
							test.done();
						} );
					} );
				} ); // internals
			} );
		},
		
		function listShift1(test) {
			var self = this;
			test.expect(4);
			this.storage.listShift( 'list2', function(err, item) {
				test.ok( !err, "No error shifting list: " + err );
				test.ok( !!item, "Item is true" );
				test.ok( item.number === 0, "List popped item value matches 0" );
				test.ok( Object.keys(self.storage.locks).length == 0, "No more locks leftover in storage" );
				test.done();
			} );
		},
		
		function listGet2(test) {
			test.expect(5);
			this.storage.listGet( 'list2', 0, 0, function(err, items) {
				test.ok( !err, "No error fetching list: " + err );
				test.ok( !!items, "Items is true" );
				test.ok( items.length == 10, "List has 10 items: " + items.length );
				test.ok( items[0].number == 1, "First item value matches 1" );
				test.ok( items[9].number == 10, "Last item value matches 10" );
				test.done();
			} );
		},
		
		function listGetInfo5(test) {
			var self = this;
			test.expect(19);
			this.storage.listGetInfo( 'list2', function(err, list) {
				test.ok( !err, "No error getting list info after new page push again: " + err );
				test.ok( list.first_page == list.last_page - 1, "First page and last page are one apart again still" );
				
				// page 0 should have 9 items, and page 1 should have 1 item.
				
				// check internals
				self.storage.get( 'list2', function(err, list) {
					test.ok( !err, "No error fetching list header: " + err );
					test.ok( !!list, "Got list data from header key" );
					test.ok( list.type == 'list', "List type is list: " + list.type );
					test.ok( list.length == 10, "List length is 10: " + list.length );
					test.ok( list.first_page == 0, "List first_page is 0: " + list.first_page );
					test.ok( list.last_page == 1, "List last_page is 1: " + list.last_page );
					test.ok( list.page_size > 0, "List page_size is non-zero: " + list.page_size );
					
					self.storage.get( 'list2/0', function(err, page) {
						test.ok( !err, "No error fetching first list page: " + err );
						test.ok( !!page, "Got list page data" );
						test.ok( page.type == 'list_page', "Page type is correct: " + page.type );
						test.ok( !!page.items, "List page has items array" );
						test.ok( page.items.length == 9, "List page has 9 items: " + page.items.length );
						
						self.storage.get( 'list2/1', function(err, page) {
							test.ok( !err, "No error fetching second list page: " + err );
							test.ok( !!page, "Got list page data" );
							test.ok( page.type == 'list_page', "Page type is correct: " + page.type );
							test.ok( !!page.items, "List page has items array" );
							test.ok( page.items.length == 1, "List page has 1 item: " + page.items.length );
							test.done();
						} );
					} );
				} ); // internals
			} );
		},
		
		function listGetCrossPage2(test) {
			// Trying multi-page fetch with partial data on first page
			test.expect(5);
			this.storage.listGet( 'list2', 8, 2, function(err, items) {
				test.ok( !err, "No error fetching list2(8,2): " + err );
				test.ok( !!items, "Items is true" );
				test.ok( items.length == 2, "List has 2 items: " + items.length );
				test.ok( items[0].number == 9, "List item 0 value matches 9" );
				test.ok( items[1].number == 10, "List item 1 value matches 10" );
				test.done();
			} );
		},
		
		function listPushMulti2(test) {
			// Now filling up second page, should overflow onto third page
			var self = this;
			var idx = 0;
			test.expect(1);
			
			async.whilst(
				function() { return idx < 10; },
				function(callback) {
					self.storage.listPush( 'list2', { foo: 'bar3', number: 11 + idx++ }, function(err, data) {
						callback(err);
					} );
				},
				function(err) {
					test.ok( !err, "No error pushing items again: " + err );
					test.done();
				}
			);
		},
		
		function listGet3(test) {
			var self = this;
			test.expect(27);
			this.storage.listGet( 'list2', 0, 0, function(err, items) {
				test.ok( !err, "No error fetching list: " + err );
				test.ok( !!items, "Items is true" );
				test.ok( items.length == 20, "List has 20 items: " + items.length );
				test.ok( items[0].number == 1, "First item value matches 1" );
				test.ok( items[19].number == 20, "Last item value matches 20" );
				
				// page 0 should have 9 items, page 1 should have 10 items, and page 2 should have 1 item, totaling 20.
				
				// check internals
				self.storage.get( 'list2', function(err, list) {
					test.ok( !err, "No error fetching list header: " + err );
					test.ok( !!list, "Got list data from header key" );
					test.ok( list.type == 'list', "List type is list: " + list.type );
					test.ok( list.length == 20, "List length is 20: " + list.length );
					test.ok( list.first_page == 0, "List first_page is 0: " + list.first_page );
					test.ok( list.last_page == 2, "List last_page is 2: " + list.last_page );
					test.ok( list.page_size > 0, "List page_size is non-zero: " + list.page_size );
					
					self.storage.get( 'list2/0', function(err, page) {
						test.ok( !err, "No error fetching first list page: " + err );
						test.ok( !!page, "Got list page data" );
						test.ok( page.type == 'list_page', "Page type is correct: " + page.type );
						test.ok( !!page.items, "List page has items array" );
						test.ok( page.items.length == 9, "List page has 9 items: " + page.items.length );
						
						self.storage.get( 'list2/1', function(err, page) {
							test.ok( !err, "No error fetching second list page: " + err );
							test.ok( !!page, "Got list page data" );
							test.ok( page.type == 'list_page', "Page type is correct: " + page.type );
							test.ok( !!page.items, "List page has items array" );
							test.ok( page.items.length == 10, "List page has 10 items: " + page.items.length );
							
							self.storage.get( 'list2/2', function(err, page) {
								test.ok( !err, "No error fetching third list page: " + err );
								test.ok( !!page, "Got list page data" );
								test.ok( page.type == 'list_page', "Page type is correct: " + page.type );
								test.ok( !!page.items, "List page has items array" );
								test.ok( page.items.length == 1, "List page has 1 item: " + page.items.length );
								test.done();
							} );
						} );
					} );
				} ); // internals
			} );
		},
		
		function listCut1(test) {
			var self = this;
			test.expect(4);
			this.storage.listSplice( 'list2', 15, 2, null, function(err, items) {
				test.ok( !err, "No error cutting list: " + err );
				test.ok( !!items, "Items is true" );
				test.ok( items[0].foo == 'bar3', "List cut item value matches" );
				test.ok( Object.keys(self.storage.locks).length == 0, "No more locks leftover in storage" );
				test.done();
			} );
		},
		
		function listGet4(test) {
			test.expect(5);
			this.storage.listGet( 'list2', 0, 0, function(err, items) {
				test.ok( !err, "No error fetching list: " + err );
				test.ok( !!items, "Items is true" );
//console.log("GOT ITEMS", items);
				test.ok( items.length == 18, "List has 18 items: " + items.length );
				test.ok( items[0].number == 1, "First item value matches 1" );
				test.ok( items[17].number == 20, "Last item value matches 20" );
				test.done();
			} );
		},
		
		// Unshifting two items at beginning, should overflow first page and create new page at other end
		
		function listUnshiftNewPage1(test) {
			// These unshifts should create a new first page
			var self = this;
			test.expect(3);
			
			this.storage.listUnshift( 'list2', { foo: 'bar4', number: 0 }, function(err, data) {
				test.ok( !err, "No error unshifting list: " + err );
				
				self.storage.listUnshift( 'list2', { foo: 'bar4', number: -1 }, function(err, data) {
					test.ok( !err, "No error unshifting new page: " + err );
					test.ok( Object.keys(self.storage.locks).length == 0, "No more locks leftover in storage" );
					test.done();
				} );
			} );
		},
		
		function listGet5(test) {
			test.expect(5);
			this.storage.listGet( 'list2', 0, 0, function(err, items) {
				test.debug( "List Items:", items );
				test.ok( !err, "No error fetching list: " + err );
				test.ok( !!items, "Items is true" );
				test.ok( items.length == 20, "List has 20 items: " + items.length );
				test.ok( items[0].number == -1, "First item value matches -1" );
				test.ok( items[19].number == 20, "Last item value matches 20" );
				test.done();
			} );
		},
		
		// Cutting off last 2 items that were unshifted, this causes root page to move back to 0
		
		function listCut2(test) {
			test.expect(3);
			this.storage.listSplice( 'list2', 0, 2, null, function(err, items) {
				test.debug( "Items Cut:", items );
				test.ok( !err, "No error cutting list: " + err );
				test.ok( !!items, "Items is true" );
				test.ok( items[0].number == -1, "List cut item value matches -1" );
				test.done();
			} );
		},
		
		function listGet6(test) {
			test.expect(5);
			this.storage.listGet( 'list2', 0, 0, function(err, items) {
				test.ok( !err, "No error fetching list: " + err );
				test.ok( !!items, "Items is true" );
				test.ok( items.length == 18, "List has 18 items: " + items.length );
				test.ok( items[0].number == 1, "First item value matches 1" );
				test.ok( items[17].number == 20, "Last item value matches 20" );
				test.done();
			} );
		},
		
		function listGet7(test) {
			// Testing fetching 5 items from 'end' of list (without knowing length)
			test.expect(5);
			this.storage.listGet( 'list2', -5, 0, function(err, items) {
				test.ok( !err, "No error fetching negative list: " + err );
				test.ok( !!items, "Items is true" );
				test.ok( items.length == 5, "Got 5 items: " + items.length );
				test.ok( items[0].number == 14, "First item value matches 14" );
				test.ok( items[4].number == 20, "Last item value matches 20" );
				test.done();
			} );
		},
		
		// Adding 1000 items...
		
		function listPushMulti1000(test) {
			test.expect(1);
			
			var items = [];
			for (var idx = 0; idx < 1000; idx++) {
				items.push({ foo: 'bar5', number: 1000 + idx });
			}
			
			this.storage.listPush( 'list2', items, function(err, data) {
				test.ok( !err, "No error pushing 1000 items: " + err );
				test.done();
			} );
		},
		
		function listGet8(test) {
			test.expect(5);
			this.storage.listGet( 'list2', 0, 0, function(err, items) {
				test.ok( !err, "No error fetching list: " + err );
				test.ok( !!items, "Items is true" );
				test.ok( items.length == 1018, "List has 1018 items: " + items.length );
				test.ok( items[0].number == 1, "First item value matches 1" );
				test.ok( items[1017].number == 1999, "Last item value matches 1999" );
				test.done();
			} );
		},
		
		function listEach1(test) {
			// test listEach on large list with multiple pages
			test.expect(2);
			var num_items = 0;
			this.storage.listEach( 'list2',
				function(item, idx, callback) {
					if (item) num_items++;
					callback();
				},
				function(err) {
					test.ok( !err, "No error iterating list: " + err );
					test.ok( num_items == 1018, "Iterated 1018 items: " + num_items );
					test.done();
				}
			);
		},
		
		// Fetching 45 items from numerous pages in the middle
		
		function listGet9(test) {
			test.expect(5);
			this.storage.listGet( 'list2', 500, 45, function(err, items) {
				test.ok( !err, "No error fetching list: " + err );
				test.ok( !!items, "Items is true" );
				test.ok( items.length == 45, "Got 45 items: " + items.length );
				test.ok( items[0].number == 1482, "First item value matches 1482" );
				test.ok( items[44].number == 1526, "Last item value matches 1526" );
				test.done();
			} );
		},
		
		// Cutting those 45 items out
		
		function listCut3(test) {
			test.expect(5);
			this.storage.listSplice( 'list2', 500, 45, null, function(err, items) {
				test.ok( !err, "No error cutting list: " + err );
				test.ok( !!items, "Items is true" );
				test.ok( items.length == 45, "Got 45 items: " + items.length );
				test.ok( items[0].number == 1482, "First item value matches 1482" );
				test.ok( items[44].number == 1526, "Last item value matches 1526" );
				test.done();
			} );
		},
		
		function listGet10(test) {
			test.expect(4);
			this.storage.listGet( 'list2', 499, 1, function(err, items) {
				test.ok( !err, "No error fetching list: " + err );
				test.ok( !!items, "Items is true" );
				test.ok( items.length == 1, "Got 1 item: " + items.length );
				test.ok( items[0].number == 1481, "First item value matches 1481" );
				test.done();
			} );
		},
		
		function listGet11(test) {
			test.expect(4);
			this.storage.listGet( 'list2', 500, 1, function(err, items) {
				test.ok( !err, "No error fetching list: " + err );
				test.ok( !!items, "Items is true" );
				test.ok( items.length == 1, "Got 1 item: " + items.length );
				test.ok( items[0].number == 1527, "First item value matches 1527" );
				test.done();
			} );
		},
		
		function listGetInfo6(test) {
			test.expect(2);
			this.storage.listGetInfo( 'list2', function(err, list) {
				test.ok( !err, "No error getting list info after new page push again: " + err );
				test.ok( list.length == 973, "List has 973 items: " + list.length );
				test.done();
			} );
		},
		
		// Testing fetching 5 items from 'end' of list (without knowing length) -- again
		
		function listGet12(test) {
			// Testing fetching 5 items from 'end' of list (without knowing length)
			test.expect(5);
			this.storage.listGet( 'list2', -5, 0, function(err, items) {
				test.ok( !err, "No error fetching negative list: " + err );
				test.ok( !!items, "Items is true" );
				test.ok( items.length == 5, "Got 5 items: " + items.length );
				test.ok( items[0].number == 1995, "First item value matches 1995" );
				test.ok( items[4].number == 1999, "Last item value matches 1999" );
				test.done();
			} );
		},
		
		// Most difficult of all -- cut 11 items, one item at a time, from the second page (first page can shrink / move, second page cannot)
		
		function listCutMultiInsane(test) {
			var self = this;
			var idx = 0;
			// test.expect(1);
			
			async.whilst(
				function() { return idx < 11; },
				function(callback) {
					self.storage.listSplice( 'list2', 18, 1, null, function(err, items) {
						test.ok( !err, "No error cutting list: " + err );
						test.ok( !!items, "Items is true" );
						test.ok( items.length == 1, "Got 1 items: " + items.length );
						test.ok( items[0].number == idx + 1000, "First item value matches 1482" );
						
						if (err) return callback(err);
						
						self.storage.listGet( 'list2', -1, 0, function(err, items) {
							test.ok( !err, "No error fetching negative list: " + err );
							test.ok( !!items, "Items is true" );
							test.ok( items.length == 1, "Got 1 items: " + items.length );
							test.ok( items[0].number == 1999, "Last item value matches 1999" );
							
							idx++;
							callback(err);
						} );
					} );
				},
				function(err) {
					test.ok( !err, "No error splicing insanity: " + err );
					test.ok( Object.keys(self.storage.locks).length == 0, "No more locks leftover in storage" );
					test.done();
				}
			);
		},
		
		function listGetInfo7(test) {
			test.expect(2);
			this.storage.listGetInfo( 'list2', function(err, list) {
				test.ok( !err, "No error getting list info after multi-cut: " + err );
				test.ok( list.length == 962, "List has 962 items: " + list.length );
				test.done();
			} );
		},
		
		function listGet13(test) {
			// Testing fetching 5 items from 'end' of list (without knowing length)
			test.expect(5);
			this.storage.listGet( 'list2', -5, 0, function(err, items) {
				test.ok( !err, "No error fetching negative list: " + err );
				test.ok( !!items, "Items is true" );
				test.ok( items.length == 5, "Got 5 items: " + items.length );
				test.ok( items[0].number == 1995, "First item value matches 1995" );
				test.ok( items[4].number == 1999, "Last item value matches 1999" );
				test.done();
			} );
		},
		
		function listFind1(test) {
			test.expect(4);
			this.storage.listFind( 'list2', { foo: 'bar5', number: 1527 }, function(err, item, idx) {
				test.ok( !err, "No error searching list: " + err );
				test.ok( !!item, "Item is true" );
				test.ok( item.foo == 'bar5', "Item foo matches bar5" );
				test.ok( item.number == 1527, "Item value matches 1527" );
				test.done();
			} );
		},
		
		function listFindRegExp1(test) {
			var self = this;
			test.expect(7);
			
			this.storage.listFind( 'list2', { foo: /^BAR5$/i, number: /1527/ }, function(err, item, idx) {
				test.ok( !err, "No error searching list: " + err );
				test.ok( !!item, "Item is true" );
				test.ok( item.foo == 'bar5', "Item foo matches bar5" );
				test.ok( item.number == 1527, "Item value matches 1527" );
				
				// check negative case
				self.storage.listFind( 'list2', { foo: /^bar6$/ }, function(err, item, idx) {
					test.ok( !err, "No error expected searching list: " + err );
					test.ok( !item, "Item is expected to be null" );
					test.ok( idx == -1, "Item idx is expected to be -1: " + idx );
					test.done();
				} );
			} );
		},
		
		function listFindBad1(test) {
			test.expect(3);
			this.storage.listFind( 'list2', { number: 2000 }, function(err, item, idx) {
				test.ok( !err, "No error expected searching list: " + err );
				test.ok( !item, "Item is expected to be null" );
				test.ok( idx == -1, "Item idx is expected to be -1: " + idx );
				test.done();
			} );
		},
		
		function listCopy1(test) {
			var self = this;
			test.expect(5);
			
			this.storage.listCopy( 'list2', 'list3', function(err) {
				test.ok( !err, "No error expected copying list: " + err );
				
				self.storage.listGet( 'list3', 0, 0, function(err, items) {
					test.ok( !err, "No error fetching list: " + err );
					test.ok( !!items, "Items is true" );
					test.ok( items.length == 962, "New list3 has 962 items: " + items.length );
					test.ok( items[961].number == 1999, "List item value matches" );
					test.done();
				} );
				
			} );
		},
		
		function listRename1(test) {
			var self = this;
			test.expect(8);
			
			this.storage.listRename( 'list3', 'list4', function(err) {
				test.ok( !err, "No error expected renaming list: " + err );
				
				self.storage.listGet( 'list3', 0, 0, function(err, items) {
					test.ok( !!err, "Expected error fetching the now deleted list3" );
					test.ok( !items, "Items is false" );
					
					self.storage.listGet( 'list4', 0, 0, function(err, items) {
						test.ok( !err, "No error fetching list: " + err );
						test.ok( !!items, "Items is true" );
						test.ok( items.length == 962, "New list4 has 962 items: " + items.length );
						test.ok( items[961].number == 1999, "List item value matches" );
						
						self.storage.listDelete( 'list4', true, function(err, data) {
							test.ok( !err, "No error deleting list4: " + err );
							test.done();
						} );
					} );
				} );
				
			} );
		},
		
		// Splice cut with a larger insert
		
		function listSpliceInsertLarger(test) {
			var self = this;
			test.expect(8);
			
			var to_insert = [
				{ inserted: 1 },
				{ inserted: 2 }
			];
			this.storage.listSplice( 'list2', 400, 1, to_insert, function(err, items) {
				test.ok( !err, "No error splicing list: " + err );
				test.ok( !!items, "Items is true" );
				test.ok( items.length == 1, "List cut 1 item" );
				
				self.storage.listGet( 'list2', 0, 0, function(err, items) {
					test.ok( !err, "No error fetching list: " + err );
					test.ok( !!items, "Items is true" );
					test.ok( items.length == 963, "list2 now has 963 items: " + items.length );
					test.ok( items[400].inserted == 1, "Inserted item value matches" );
					test.ok( items[962].number == 1999, "Last item value matches" );
					test.done();
				} );
			} );
		},
		
		// Splice cut with a smaller insert
		
		function listSpliceInsertSmaller(test) {
			var self = this;
			test.expect(8);
			
			var to_insert = [
				{ inserted: 3 }
			];
			this.storage.listSplice( 'list2', 410, 2, to_insert, function(err, items) {
				test.ok( !err, "No error splicing list: " + err );
				test.ok( !!items, "Items is true" );
				test.ok( items.length == 2, "List cut 2 items" );
				
				self.storage.listGet( 'list2', 0, 0, function(err, items) {
					test.ok( !err, "No error fetching list: " + err );
					test.ok( !!items, "Items is true" );
					test.ok( items.length == 962, "list2 now has 962 items: " + items.length );
					test.ok( items[410].inserted == 3, "Inserted item value matches" );
					test.ok( items[961].number == 1999, "Last item value matches" );
					test.done();
				} );
			} );
		},
		
		// Splice with an equal cut + insert
		
		function listSpliceInsertEqual(test) {
			var self = this;
			test.expect(8);
			
			var to_insert = [
				{ inserted: 4 },
				{ inserted: 5 }
			];
			this.storage.listSplice( 'list2', 420, 2, to_insert, function(err, items) {
				test.ok( !err, "No error splicing list: " + err );
				test.ok( !!items, "Items is true" );
				test.ok( items.length == 2, "List cut 2 items" );
				
				self.storage.listGet( 'list2', 0, 0, function(err, items) {
					test.ok( !err, "No error fetching list: " + err );
					test.ok( !!items, "Items is true" );
					test.ok( items.length == 962, "list2 now has 962 items: " + items.length );
					test.ok( items[420].inserted == 4, "Inserted item value matches" );
					test.ok( items[961].number == 1999, "Last item value matches" );
					test.done();
				} );
			} );
		},
		
		// 0-item cut splice with an insert
		
		function listSpliceZeroInsert(test) {
			var self = this;
			test.expect(8);
			
			var to_insert = [
				{ inserted: 6 },
				{ inserted: 7 }
			];
			this.storage.listSplice( 'list2', 430, 0, to_insert, function(err, items) {
				test.ok( !err, "No error splicing list: " + err );
				test.ok( !!items, "Items is true" );
				test.ok( items.length == 0, "List cut 0 items" );
				
				self.storage.listGet( 'list2', 0, 0, function(err, items) {
					test.ok( !err, "No error fetching list: " + err );
					test.ok( !!items, "Items is true" );
					test.ok( items.length == 964, "list2 now has 964 items: " + items.length );
					test.ok( items[430].inserted == 6, "Inserted item value matches" );
					test.ok( items[963].number == 1999, "Last item value matches" );
					test.done();
				} );
			} );
		},
		
		// Splice insert with enough new items to cause a new page
		
		function listSpliceInsertLarger2(test) {
			var self = this;
			test.expect(8);
			
			var to_insert = [
				{ inserted: 10 },
				{ inserted: 11 },
				{ inserted: 12 },
				{ inserted: 13 },
				{ inserted: 14 },
				{ inserted: 15 },
				{ inserted: 16 },
				{ inserted: 17 },
				{ inserted: 18 },
				{ inserted: 19 },
				{ inserted: 20, vegetable: "carrot" },
				{ inserted: 21, vegetable: "carrot" },
				{ inserted: 22, vegetable: "carrot" }
			];
			this.storage.listSplice( 'list2', 440, 1, to_insert, function(err, items) {
				test.ok( !err, "No error splicing list: " + err );
				test.ok( !!items, "Items is true" );
				test.ok( items.length == 1, "List cut 1 item" );
				
				self.storage.listGet( 'list2', 0, 0, function(err, items) {
					test.ok( !err, "No error fetching list: " + err );
					test.ok( !!items, "Items is true" );
					test.ok( items.length == 976, "list2 now has 976 items: " + items.length );
					test.ok( items[440].inserted == 10, "Inserted item value matches" );
					test.ok( items[975].number == 1999, "Last item value matches" );
					test.done();
				} );
			} );
		},
		
		function listFindCut1(test) {
			// test the listFindCut macro function
			var self = this;
			test.expect(10);
			
			this.storage.listFindCut( 'list2', { inserted: 17 }, function(err, item) {
				test.ok( !err, "No error after listFindCut: " + err );
				test.ok( !!item, "Cut item is true" );
				test.ok( item.inserted == 17, "Cut item value matches" );
				test.ok( Object.keys(self.storage.locks).length == 0, "No locks remaining after listFindCut" );
				
				self.storage.listGet( 'list2', 0, 0, function(err, items) {
					test.ok( !err, "No error fetching list: " + err );
					test.ok( !!items, "Items is true" );
					test.ok( items.length == 975, "list2 now has 975 items: " + items.length );
					test.ok( items[440].inserted == 10, "Item value matches before splice area" );
					test.ok( items[447].inserted == 18, "Item value matches after splice area" );
					test.ok( items[974].number == 1999, "Last item value matches" );
					test.done();
				} );
			} );
		},
		
		function listFindReplace1(test) {
			// test the listFindReplace macro function
			var self = this;
			test.expect(7);
			
			this.storage.listFindReplace( 'list2', { inserted: 18 }, { replaced: 18, counter: 1 }, function(err) {
				test.ok( !err, "No error after listFindReplace: " + err );
				test.ok( Object.keys(self.storage.locks).length == 0, "No locks remaining after listFindReplace" );
				
				self.storage.listGet( 'list2', 0, 0, function(err, items) {
					test.ok( !err, "No error fetching list: " + err );
					test.ok( !!items, "Items is true" );
					test.ok( items.length == 975, "list2 still has 975 items: " + items.length );
					test.ok( items[447].replaced == 18, "Item value matches after replace" );
					test.ok( items[974].number == 1999, "Last item value matches" );
					test.done();
				} );
			} );
		},
		
		function listFindUpdate1(test) {
			// test the listFindUpdate macro function
			var self = this;
			var criteria = { replaced: 18 };
			var updates = { replaced: 118, counter: "+1", newfoo: "hello" };
			test.expect(9);
			
			this.storage.listFindUpdate( 'list2', criteria, updates, function(err, item) {
				test.ok( !err, "No error after listFindUpdate: " + err );
				test.ok( Object.keys(self.storage.locks).length == 0, "No locks remaining after listFindUpdate" );
				
				self.storage.listGet( 'list2', 0, 0, function(err, items) {
					test.ok( !err, "No error fetching list: " + err );
					test.ok( !!items, "Items is true" );
					test.ok( items.length == 975, "list2 still has 975 items: " + items.length );
					test.ok( items[447].replaced == 118, "Item value matches after update" );
					test.ok( items[447].counter == 2, "Counter was successfully incremented" );
					test.ok( items[447].newfoo == "hello", "New property was successfully added" );
					test.ok( items[974].number == 1999, "Last item value matches" );
					test.done();
				} );
			} );
		},
		
		function listFindEach1(test) {
			// test listFindEach on large list with multiple pages
			test.expect(8);
			var num_items = 0;
			var criteria = { vegetable: "carrot" };
			
			this.storage.listFindEach( 'list2', criteria, 
				function(item, idx, callback) {
					if (item) num_items++;
					test.ok( !!item, "Item was passed to iterator" );
					test.ok( item.vegetable == 'carrot', "Item has correct vegetable" );
					callback();
				},
				function(err) {
					test.ok( !err, "No error iterating list: " + err );
					test.ok( num_items == 3, "Found 3 items: " + num_items );
					test.done();
				}
			);
		},
		
		function listFindEachRegExp1(test) {
			// test listFindEach on large list with multiple pages, using reg exp
			test.expect(8);
			var num_items = 0;
			var criteria = { vegetable: /^CARROT$/i };
			
			this.storage.listFindEach( 'list2', criteria, 
				function(item, idx, callback) {
					if (item) num_items++;
					test.ok( !!item, "Item was passed to iterator" );
					test.ok( item.vegetable == 'carrot', "Item has correct vegetable" );
					callback();
				},
				function(err) {
					test.ok( !err, "No error iterating list: " + err );
					test.ok( num_items == 3, "Found 3 items: " + num_items );
					test.done();
				}
			);
		},
		
		// Deleting entire list
		
		function listDelete2(test) {
			test.expect(1);
			this.storage.listDelete( 'list2', true, function(err, data) {
				test.ok( !err, "No error deleting list2: " + err );
				test.done();
			} );
		},
		
		// Making sure list2 was deleted
		
		function listGetEmpty4(test) {
			test.expect(1);
			this.storage.listGet( 'list2', 0, 0, function(err, items) {
				test.ok( !!err, "Error expected getting deleted list2" );
				test.done();
			} );
		},
		
		function listGetInfoEmpty2(test) {
			test.expect(1);
			this.storage.listGetInfo( 'list2', function(err, list) {
				test.ok( !!err, "Error expected getting list2 info after delete" );
				test.done();
			} );
		},
		
		function listShiftClear(test) {
			// create list with 1 item, then shift it off, and make sure we have a clean empty list leftover
			var self = this;
			var key = 'clearlist1';
			test.expect( 17 );
			
			this.storage.listPush( key, { foo: 'bar' }, function(err) {
				test.ok( !err, "No error pushing list: " + err );
				
				self.storage.listShift( key, function(err, item) {
					test.ok( !err, "No error shifting list: " + err );
					
					self.storage.get( key, function(err, list) {
						test.ok( !err, "No error fetching list header: " + err );
						test.ok( !!list, "Got list data from header key" );
						test.ok( list.type == 'list', "List type is list: " + list.type );
						test.ok( list.length == 0, "List length is 0: " + list.length );
						test.ok( list.first_page == 0, "List first_page is 0: " + list.first_page );
						test.ok( list.last_page == 0, "List last_page is 0: " + list.last_page );
						test.ok( list.page_size > 0, "List page_size is non-zero: " + list.page_size );
						
						self.storage.get( key + '/0', function(err, page) {
							test.ok( !err, "No error fetching list page: " + err );
							test.ok( !!page, "Got list page data" );
							test.ok( page.type == 'list_page', "Page type is correct: " + page.type );
							test.ok( !!page.items, "List page has items array" );
							test.ok( page.items.length == 0, "List page has 0 items: " + page.items.length );
							
							self.storage.listDelete( key, true, function(err) {
								test.ok( !err, "No error deleting list: " + err );
								
								self.storage.get( key, function(err, list) {
									test.ok( !!err, "Error expected fetching list header after delete: " + err );
									
									self.storage.get( key + '/0', function(err, page) {
										test.ok( !!err, "Error expected fetching list page after delete: " + err );
										test.done();
									} ); // get page
								} ); // get header
							} ); // delete
						} ); // get page
					} ); // get header
				} ); // shift
			} ); // push
		},
		
		function listPopClear(test) {
			// create list with 1 item, then pop it off, and make sure we have a clean empty list leftover
			var self = this;
			var key = 'clearlist2';
			test.expect( 17 );
			
			this.storage.listPush( key, { foo: 'bar' }, function(err) {
				test.ok( !err, "No error pushing list: " + err );
				
				self.storage.listPop( key, function(err, item) {
					test.ok( !err, "No error popping list: " + err );
					
					self.storage.get( key, function(err, list) {
						test.ok( !err, "No error fetching list header: " + err );
						test.ok( !!list, "Got list data from header key" );
						test.ok( list.type == 'list', "List type is list: " + list.type );
						test.ok( list.length == 0, "List length is 0: " + list.length );
						test.ok( list.first_page == 0, "List first_page is 0: " + list.first_page );
						test.ok( list.last_page == 0, "List last_page is 0: " + list.last_page );
						test.ok( list.page_size > 0, "List page_size is non-zero: " + list.page_size );
						
						self.storage.get( key + '/0', function(err, page) {
							test.ok( !err, "No error fetching list page: " + err );
							test.ok( !!page, "Got list page data" );
							test.ok( page.type == 'list_page', "Page type is correct: " + page.type );
							test.ok( !!page.items, "List page has items array" );
							test.ok( page.items.length == 0, "List page has 0 items: " + page.items.length );
							
							self.storage.listDelete( key, true, function(err) {
								test.ok( !err, "No error deleting list: " + err );
								
								self.storage.get( key, function(err, list) {
									test.ok( !!err, "Error expected fetching list header after delete: " + err );
									
									self.storage.get( key + '/0', function(err, page) {
										test.ok( !!err, "Error expected fetching list page after delete: " + err );
										test.done();
									} ); // get page
								} ); // get header
							} ); // delete
						} ); // get page
					} ); // get header
				} ); // pop
			} ); // push
		},
		
		function listSpliceClear(test) {
			// create list with 1 item, then splice it off, and make sure we have a clean empty list leftover
			var self = this;
			var key = 'clearlist3';
			test.expect( 17 );
			
			this.storage.listPush( key, { foo: 'bar' }, function(err) {
				test.ok( !err, "No error pushing list: " + err );
				
				self.storage.listSplice( key, 0, 1, [], function(err, item) {
					test.ok( !err, "No error splicing list: " + err );
					
					self.storage.get( key, function(err, list) {
						test.ok( !err, "No error fetching list header: " + err );
						test.ok( !!list, "Got list data from header key" );
						test.ok( list.type == 'list', "List type is list: " + list.type );
						test.ok( list.length == 0, "List length is 0: " + list.length );
						test.ok( list.first_page == 0, "List first_page is 0: " + list.first_page );
						test.ok( list.last_page == 0, "List last_page is 0: " + list.last_page );
						test.ok( list.page_size > 0, "List page_size is non-zero: " + list.page_size );
						
						self.storage.get( key + '/0', function(err, page) {
							test.ok( !err, "No error fetching list page: " + err );
							test.ok( !!page, "Got list page data" );
							test.ok( page.type == 'list_page', "Page type is correct: " + page.type );
							test.ok( !!page.items, "List page has items array" );
							test.ok( page.items.length == 0, "List page has 0 items: " + page.items.length );
							
							self.storage.listDelete( key, true, function(err) {
								test.ok( !err, "No error deleting list: " + err );
								
								self.storage.get( key, function(err, list) {
									test.ok( !!err, "Error expected fetching list header after delete: " + err );
									
									self.storage.get( key + '/0', function(err, page) {
										test.ok( !!err, "Error expected fetching list page after delete: " + err );
										test.done();
									} ); // get page
								} ); // get header
							} ); // delete
						} ); // get page
					} ); // get header
				} ); // splice
			} ); // push
		},
		
		function testListInsertSorted(test) {
			// test listInsertSorted with a bunch of unsorted items
			var self = this;
			test.expect( 207 );
			
			var original_usernames = ["fowlscottish", "cerebellumcameraman", "lewdastatine", "letterslist", "wildsquishy", "mailerresigned", "fobbingboyscouts", "cashewvenomed", "tetherballinterval", "hornjacket", "arcvallis", "soccersquish", "voltgummy", "garnthief", "interfaceagreeable", "publishercoma", "keygristle", "risingobliquity", "chorleyhoop", "inventorybugbear", "achingrigil", "wingedcohert", "unfastenplates", "chewingharrier", "tearfultor", "superiorlevers", "cracklescaly", "intnamibian", "nappingconcerns", "belchsurfing", "facialcantata", "pintailgroovy", "vanadiumcoxcomb", "floatintroduced", "muggergrilled", "fancyfacts", "darcynorth", "copernicuswinding", "gathertelephone", "stuffingxpath", "dopplericing", "thighapricots", "blazezany", "producecasimir", "diphthongpage", "staineddrones", "aboveyorkie", "isolatestick", "chillyamazon", "leadhonky", "clothingcompany", "crumpetssartorial", "austrinaworms", "terminallyimproper", "smewfarrum", "sundaycoloured", "evalblot", "tripglobe", "russelpatrick", "methodtiming", "expertnoodles", "rubbishroomy", "sonorefactor", "lagrangeskipping", "alcoholicwho", "biotapet", "cooksweak", "onioneconomic", "tillitewhispered", "morfilk", "tubprompting", "offensethirsty", "pavoconcave", "varicoseroseate", "hooklaunching", "lambbossy", "dauphineabove", "auctionwhip", "joystough", "triggersantenna", "papesslicer", "cancersmoronic", "porridgeio", "abashedscrubbing", "bushfinished", "dewmumps", "mugrail", "whatloin", "clerkmilitary", "hindermoral", "relateactivity", "boundedstutter", "strikingtrusty", "itchingtheory", "genderscodelevels", "pilcrowpresenting", "actuallyarray", "harpyeven", "brownplain", "herbroot", "cinderdote", "stashrattle", "departmentovert", "sandwicharmy", "mensaleft", "levelpickled", "precipitatepicked", "neutrinosmashed", "fagwholesale", "faculaefett", "pradamind", "geezersabine", "keepbowel", "combineschist", "housestinging", "kettleneigh", "resonantwakeful", "tawnydeal", "cutsordid", "agitatedmammary", "tractorposition", "sootsubmerge", "negativelytugofwar", "obsequioustemperature", "mexicancompiler", "stipulatebaste", "occulationcola", "fashionsoblateness", "equipmentbelieve", "pesterstaccato", "prettyingcramer", "russianparanoid", "joyousslamming", "tinglingfix", "painsplace", "thalliumbabyish", "residenceduality", "stringsbaa", "resultbiggest", "patisseriesuggestion", "planetshedgehog", "crossfairly", "subtleextinct", "cosinespies", "codsole", "grippingclosed", "appealsmaple", "feathercliche", "distractedstall", "grottysince", "initsardonic", "washgarden", "ablazelowly", "bastingplutonic", "nepalesebloviate", "dogsiberian", "stammerbreasts", "includedmettled", "scenesterpitter", "cherriestotal", "lethalhappen", "facebookprograde", "crownbetter", "cheekyfluctus", "jetproton", "droppingsuntimely", "egretimpish", "sparcpluck", "grantgross", "whickerkebab", "boanagging", "neighborlykaput", "powerfulbubble", "respondcreep", "celestgoes", "observeacidic", "aldermancrow", "leafyshortstop", "bombsecurity", "hushedus", "cratehornbill", "daughterenjoy", "heapxna", "gradesynth", "clamtrust", "doublingdover", "renamebreak", "unwrittentattler", "olympicslow", "stumblingvenues", "ossifiedproof", "ruffwilderness", "vanquishimportance", "dnabefore", "designedtit", "woodenblackwell", "chainbroil", "boulangereascension", "joneslegato", "factwizards"];
			
			var sorted_usernames = ["abashedscrubbing", "ablazelowly", "aboveyorkie", "achingrigil", "actuallyarray", "agitatedmammary", "alcoholicwho", "aldermancrow", "appealsmaple", "arcvallis", "auctionwhip", "austrinaworms", "bastingplutonic", "belchsurfing", "biotapet", "blazezany", "boanagging", "bombsecurity", "boulangereascension", "boundedstutter", "brownplain", "bushfinished", "cancersmoronic", "cashewvenomed", "celestgoes", "cerebellumcameraman", "chainbroil", "cheekyfluctus", "cherriestotal", "chewingharrier", "chillyamazon", "chorleyhoop", "cinderdote", "clamtrust", "clerkmilitary", "clothingcompany", "codsole", "combineschist", "cooksweak", "copernicuswinding", "cosinespies", "cracklescaly", "cratehornbill", "crossfairly", "crownbetter", "crumpetssartorial", "cutsordid", "darcynorth", "daughterenjoy", "dauphineabove", "departmentovert", "designedtit", "dewmumps", "diphthongpage", "distractedstall", "dnabefore", "dogsiberian", "dopplericing", "doublingdover", "droppingsuntimely", "egretimpish", "equipmentbelieve", "evalblot", "expertnoodles", "facebookprograde", "facialcantata", "factwizards", "faculaefett", "fagwholesale", "fancyfacts", "fashionsoblateness", "feathercliche", "floatintroduced", "fobbingboyscouts", "fowlscottish", "garnthief", "gathertelephone", "geezersabine", "genderscodelevels", "gradesynth", "grantgross", "grippingclosed", "grottysince", "harpyeven", "heapxna", "herbroot", "hindermoral", "hooklaunching", "hornjacket", "housestinging", "hushedus", "includedmettled", "initsardonic", "interfaceagreeable", "intnamibian", "inventorybugbear", "isolatestick", "itchingtheory", "jetproton", "joneslegato", "joyousslamming", "joystough", "keepbowel", "kettleneigh", "keygristle", "lagrangeskipping", "lambbossy", "leadhonky", "leafyshortstop", "lethalhappen", "letterslist", "levelpickled", "lewdastatine", "mailerresigned", "mensaleft", "methodtiming", "mexicancompiler", "morfilk", "muggergrilled", "mugrail", "nappingconcerns", "negativelytugofwar", "neighborlykaput", "nepalesebloviate", "neutrinosmashed", "obsequioustemperature", "observeacidic", "occulationcola", "offensethirsty", "olympicslow", "onioneconomic", "ossifiedproof", "painsplace", "papesslicer", "patisseriesuggestion", "pavoconcave", "pesterstaccato", "pilcrowpresenting", "pintailgroovy", "planetshedgehog", "porridgeio", "powerfulbubble", "pradamind", "precipitatepicked", "prettyingcramer", "producecasimir", "publishercoma", "relateactivity", "renamebreak", "residenceduality", "resonantwakeful", "respondcreep", "resultbiggest", "risingobliquity", "rubbishroomy", "ruffwilderness", "russelpatrick", "russianparanoid", "sandwicharmy", "scenesterpitter", "smewfarrum", "soccersquish", "sonorefactor", "sootsubmerge", "sparcpluck", "staineddrones", "stammerbreasts", "stashrattle", "stipulatebaste", "strikingtrusty", "stringsbaa", "stuffingxpath", "stumblingvenues", "subtleextinct", "sundaycoloured", "superiorlevers", "tawnydeal", "tearfultor", "terminallyimproper", "tetherballinterval", "thalliumbabyish", "thighapricots", "tillitewhispered", "tinglingfix", "tractorposition", "triggersantenna", "tripglobe", "tubprompting", "unfastenplates", "unwrittentattler", "vanadiumcoxcomb", "vanquishimportance", "varicoseroseate", "voltgummy", "washgarden", "whatloin", "whickerkebab", "wildsquishy", "wingedcohert", "woodenblackwell"];
			
			async.eachSeries( original_usernames, 
				function(username, callback) {
					self.storage.listInsertSorted( 'sortedlist1', { username: username, foo: "barsorted1" }, ['username', 1], callback );
				}, 
				function(err) {
					test.ok( !err, "No error inserting items: " + err );
					
					// now fetch entire list to see if sorting worked
					self.storage.listGet( 'sortedlist1', 0, 0, function(err, items) {
						test.ok( !err, "No error fetching list: " + err );
						test.ok( !!items, "Items is true" );
						test.ok( items.length == 200, "sortedlist1 has 200 items: " + items.length );
						test.ok( items[0].foo == "barsorted1", "First item has expected content" );
						test.ok( items[199].foo == "barsorted1", "Last item has expected content" );
						
						for (var idx = 0, len = items.length; idx < len; idx++) {
							test.ok(
								items[idx].username == sorted_usernames[idx], 
								"Item " + idx + " matches sorted username: " + items[idx].username + " == " + sorted_usernames[idx]
							);
						}
						
						self.storage.listDelete( 'sortedlist1', true, function(err, data) {
							test.ok( !err, "No error deleting sortedlist1: " + err );
							test.done();
						} );
					} ); // loaded list
				} // eachSeries complete 
			); // eachSeries
		}
		
	], // tests array
	
	makeIntArray: function(from, to, max) {
		// create array containing range of integers
		var arr = [];
		for (var idx = from; idx <= to; idx++) arr.push(idx);
		
		if (max && (arr.length > max)) {
			arr = [];
			for (var amount = 0; amount < max; amount++) {
				arr.push( Math.floor( from + ((to - from) * (amount / (max - 1))) ) );
			}
		}
		
		return arr;
	},
	
	generateSpliceTest: function(setup_func, initial_len, cut_idx, cut_len, ins_len) {
		// generate single splice test given specific args
		var test_func = function(test) {
			// run test
			var self = this;
			var key = 'listomatic';
			
			var initial_items = [];
			for (var idx = 0; idx < initial_len; idx++) {
				initial_items.push({ name: "initial " + idx });
			}
			
			var new_items = [];
			for (var idx = 0; idx < ins_len; idx++) {
				new_items.push({ name: "INSERTED " + idx });
			}
			
			// create and splice reference array
			var ref_arr = JSON.parse( JSON.stringify(initial_items) );
			var ref_splice_args = [ cut_idx, cut_len ].concat( JSON.parse( JSON.stringify(new_items) ) );
			[].splice.apply( ref_arr, ref_splice_args );
			
			async.series(
				[
					function(callback) {
						// create list
						if (initial_len) {
							// listPush or listUnshift
							self.storage[setup_func]( key, initial_items, callback );
						}
						else {
							// no initial items, so use listCreate
							self.storage.listCreate( key, {}, callback );
						}
					},
					function(callback) {
						// splice
						self.storage.listSplice( key, cut_idx, cut_len, new_items, callback );
					},
					function(callback) {
						// load entire list to compare
						self.storage.listGet( key, 0, 0, function(err, items, list) {
							test.ok( !err, "No error fetching list: " + err );
							test.ok( !!items, "Items is true" );
							test.ok( !!list, "List is true" );
							
							test.debug( "Ref Array: ", ref_arr );
							test.debug( "Final Items: ", items );
							test.debug( "List Header: ", list );
							
							test.ok( list.length == items.length, "List has correct number of items: " + list.length );
							test.ok( items.length == ref_arr.length, "Item length matches reference array: " + items.length );
							
							for (var idx = 0, len = items.length; idx < len; idx++) {
								test.ok( !!items[idx], "Item " + idx + " exists" );
								test.ok( !!items[idx].name, "Item " + idx + " has a name property" );
								test.ok(
									items[idx].name == ref_arr[idx].name, 
									"Item " + idx + " value matches ref array: " + items[idx].name + " == " + ref_arr[idx].name
								);
							}
							
							callback();
						}); // listGet
					}
				],
				function(err) {
					test.ok( !err, "No error during splice operations: " + err );
					
					// always delete list
					self.storage.listDelete( key, true, function(err) {
						test.ok( !err, "No error deleting list: " + err );
						test.done();
					} );
				}
			); // async.series
		}; // test func
		
		test_func.testName = 'listSpliceMatrix_' + 
			((setup_func == 'listPush') ? 'Psh' : 'Unsh') + 
			'_Init' + initial_len + '_Idx' + cut_idx + '_Cut' + cut_len + '_Ins' + ins_len;
			
		return test_func;
	},
	
	generateSpliceTests: function() {
		// generate special splice tests with known args
		var self = this;
		var tests = [];
		
		// try creating list with push and unshift
		['listPush', 'listUnshift'].forEach( function(setup_func) {
		// ['listPush'].forEach( function(setup_func) {
			
			// try all different initial list sizes
			[0, 1, 4, 5, 6, 9, 10, 11, 15, 19, 20, 21, 25, 29, 30, 31].forEach( function(initial_len) {
			// [0, 1, 4, 5, 9, 10, 11, 19, 20, 30, 31].forEach( function(initial_len) {
				
				// try all cut positions
				self.makeIntArray(0, initial_len, 5).forEach( function(cut_idx) {
					
					// try all cut lengths
					var max_cut_len = initial_len - cut_idx;
					self.makeIntArray(0, max_cut_len, 5).forEach( function(cut_len) {
						
						// try various insert lengths
						[0, 1, 2, 9, 10, 11, 19, 20, 30, 32, 40].forEach( function(ins_len) {
						// [0, 1, 2, 9, 10, 11, 19, 32, 40].forEach( function(ins_len) {
						// [0].forEach( function(ins_len) {
							
							// generate test function
							tests.push( 
								self.generateSpliceTest( setup_func, initial_len, cut_idx, cut_len, ins_len ) 
							);
						} ); // ins_len loop
					} ); // cut_len loop
				} ); // cut_idx loop
			} ); // initial_len loop
		} ); // setup_func loop
		
		return tests;
	}
};
```

## File: `test/test-main.js`
```javascript
// Unit tests for Storage System - Main
// Copyright (c) 2015 - 2016 Joseph Huckaby
// Released under the MIT License

var os = require('os');
var fs = require('fs');
var path = require('path');
var cp = require('child_process');
var crypto = require('crypto');
var async = require('async');

var digestHex = function(str) {
	// digest string using SHA256, return hex hash
	var shasum = crypto.createHash('sha256');
	shasum.update( str );
	return shasum.digest('hex');
};

module.exports = {
	tests: [
	
		/* function test1(test) {
			test.ok(true, 'bar');
			test.done();
		}, */
		
		/* function test2(test) {
			test.ok(false, 'bar THIS SHOULD FAILZZZZ');
			test.done();
		}, */
		
		function put1(test) {
			test.expect(1);
			this.storage.put( 'test1', { foo: 'bar1' }, function(err) {
				test.ok( !err, "No error creating test1: " + err );
				test.done();
			} );
		},
		
		function get1(test) {
			test.expect(3);
			this.storage.get( 'test1', function(err, data) {
				test.ok( !err, "No error fetching test1: " + err );
				test.ok( !!data, "Data is true" );
				test.ok( data.foo == 'bar1', "Value is correct" );
				test.done();
			} );
		},
		
		function setExp1(test) {
			var self = this;
			test.expect(1);
			this.storage.put( 'test_expire', { foo: 'delete me!' }, function(err) {
				test.ok( !err, "No error creating test_expire: " + err );
				var exp_date = Math.floor( (new Date()).getTime() / 1000 );
				self.storage.expire( 'test_expire', exp_date, true );
				
				var first = true;
				async.whilst(
					function () {
						return ( first || (Object.keys(self.storage.locks).length > 0) || !self.storage.queue.idle() );
					},
					function (callback) {
						test.debug("Waiting for locks / queue");
						first = false;
						setTimeout( function() { callback(); }, 250 );
					},
					function() {
						// locks / queue are free, proceed
						test.done();
					} // whilst complete
				); // whilst
			} );
		},
		
		function head1(test) {
			test.expect(4);
			this.storage.head( 'test1', function(err, meta) {
				test.ok( !err, "No error heading test1: " + err );
				test.ok( !!meta, "Meta is true" );
				test.ok( meta.len > 0, "Length is non-zero" );
				test.ok( meta.mod > 0, "Mod is non-zero" );
				test.done();
			} );
		},
		
		function headFail1(test) {
			test.expect(2);
			this.storage.head( 'test_NO_EXIST', function(err, meta) {
				test.ok( !!err, "Error expected heading non-existent key" );
				test.ok( !meta, "Meta expected to be false" );
				test.done();
			} );
		},
		
		function getFail1(test) {
			test.expect(2);
			this.storage.get( 'test_NO_EXIST', function(err, data) {
				test.ok( !!err, "Error expected getting non-existent key" );
				test.ok( !data, "Data expected to be false" );
				test.done();
			} );
		},
		
		function replace1(test) {
			var self = this;
			test.expect(4);
			
			this.storage.put( 'test1', { foo: 'bar2' }, function(err) {
				test.ok( !err, "No error updating test1: " + err );
				
				self.storage.get( 'test1', function(err, data) {
					test.ok( !err, "No error fetching test1 after replace: " + err );
					test.ok( !!data, "Data is true afer replace" );
					test.ok( data.foo == 'bar2', "Value is correct after replace" );
					test.done();
				} );
			} );
		},
		
		function copy1(test) {
			var self = this;
			test.expect(8);
			
			this.storage.copy( 'test1', 'test2', function(err) {
				test.ok( !err, "No error copying test1: " + err );
				
				self.storage.get( 'test1', function(err, data) {
					test.ok( !err, "No error fetching test1 after copy: " + err );
					test.ok( !!data, "Old data is true afer copy" );
					test.ok( data.foo == 'bar2', "Old value is correct after copy" );
					
					self.storage.get( 'test2', function(err, data) {
						test.ok( !err, "No error fetching test2 after copy: " + err );
						test.ok( !!data, "Data is true afer copy" );
						test.ok( data.foo == 'bar2', "Value is correct after copy" );
						
						self.storage.delete( 'test2', function(err) {
							test.ok( !err, "No error deleting test2 after copy: " + err );
							test.done();
						} );
					} );
				} );
			} );
		},
		
		function rename1(test) {
			var self = this;
			test.expect(6);
			
			this.storage.rename( 'test1', 'test3', function(err) {
				test.ok( !err, "No error copying test1: " + err );
				
				self.storage.get( 'test1', function(err, data) {
					test.ok( !!err, "Error expected fetching test1 after rename" );
					test.ok( !data, "Old data expected to be false after rename" );
					
					self.storage.get( 'test3', function(err, data) {
						test.ok( !err, "No error fetching test3 after rename: " + err );
						test.ok( !!data, "Data is true afer rename" );
						test.ok( data.foo == 'bar2', "Value is correct after rename" );
						test.done();
					} );
				} );
			} );
		},
		
		function delete1(test) {
			var self = this;
			test.expect(3);
			
			this.storage.delete( 'test3', function(err) {
				test.ok( !err, "No error deleting test3: " + err );
				
				self.storage.get( 'test3', function(err, data) {
					test.ok( !!err, "Error expected fetching test1 after delete" );
					test.ok( !data, "Data expected to be false after delete" );
					test.done();
				} );
			} );
		},
		
		function testLocking(test) {
			// test advisory locking
			var self = this;
			var key = 'test-lock';
			var storage = this.storage;
			test.expect( 28 );
			
			test.ok( Object.keys(self.storage.locks).length == 0, "No locks at start of test" );
			
			storage.put( key, { foo:"hello", counter:0 }, function(err) {
				test.ok( !err, "No error putting lock key: " + err );
				
				async.times( 10,
					function(idx, callback) {
						
						storage.lock( key, true, function() {
							storage.get( key, function(err, data) {
								test.ok( !err, "No error fetching lock key: " + err );
								
								data.counter++;
								
								storage.put( key, data, function(err) {
									test.ok( !err, "No error updating lock key: " + err );
									
									storage.unlock(key);
									callback();
								} ); // put
							} ); // get
						} ); // lock
						
					}, // iterator
					function(err) {
						// all done, now fetch and check counter
						test.ok( !err, "No error at end of lock async.times: " + err );
						
						storage.get( key, function(err, data) {
							test.ok( !err, "No error fetching lock key last time: " + err );
							test.ok( !!data, "Got data from lock key" );
							test.ok( data.counter == 10, "Correct counter value after async lock update: " + data.counter );
							test.ok( Object.keys(storage.locks).length == 0, "No more locks leftover in storage" );
							
							storage.delete( key, function(err) {
								test.ok( !err, "No error deleting lock key: " + err );
								test.done();
							} );
						} );
					} // completion
				);
			} );
		},
		
		function testSharedLocking(test) {
			// test shared locking
			var self = this;
			var key = 'test-lock';
			var storage = this.storage;
			
			test.expect( 19 );
			test.ok( Object.keys(storage.locks).length == 0, "No locks at start of test" );
			
			storage.lock( key, true, function(err, lock) {
				// got exclusive lock
				test.ok( lock.type == 'ex', "Expected exclusive lock type: " + lock.type);
				
				setTimeout( function() {
					// unlocking exclusive
					test.ok( lock.type == 'ex', "Expected exclusive lock type: " + lock.type);
					test.ok( lock.clients.length == 3, "Expected 3 waiting clients: " + lock.clients.length);
					test.ok( !lock.readers, "No readers expected here: " + lock.readers);
					
					storage.unlock( key );
				}, 100 );
			} );
			
			setTimeout( function() {
				async.times( 3, 
					function(idx, callback) {
						storage.shareLock( key, true, function(err, lock) {
							// got shared lock
							test.ok( lock.type == 'sh', "Expected shared lock type: " + lock.type);
							
							setTimeout( function() {
								storage.shareUnlock( key );
								callback();
							}, 100 );
						} );
					},
					function(err) {
						// async.times complete
					}
				);
			}, 50 );
			
			setTimeout( function() {
				// at this point, all 3 shared locks should be active
				var lock = storage.locks[key];
				test.ok( !!lock, "Got expected lock record" );
				test.ok( lock.type == 'sh', "Expected shared lock type: " + lock.type);
				test.ok( lock.readers == 3, "Expected 3 readers: " + lock.readers);
				
				var got_ex_lock = false;
				
				storage.lock( key, true, function(err, lock) {
					// got exclusive lock again
					test.ok( lock.type == 'ex', "Expected exclusive lock type: " + lock.type);
					got_ex_lock = true;
					
					setTimeout( function() {
						// unlocking exclusive AGAIN
						test.ok( lock.type == 'ex', "Expected exclusive lock type: " + lock.type);
						test.ok( lock.clients.length == 3, "Expected 3 waiting clients: " + lock.clients.length);
						test.ok( !lock.readers, "No readers expected here: " + lock.readers);
						
						storage.unlock( key );
					}, 100 ); // setTimeout
				} ); // lock
				
				setTimeout( function() {
					async.times( 3, 
						function(idx, callback) {
							storage.shareLock( key, true, function(err, lock) {
								// got shared lock AGAIN
								test.ok( got_ex_lock, "Got exclusive lock before second shared lock" );
								
								setTimeout( function() {
									storage.shareUnlock( key );
									callback();
								}, 100 );
							} );
						},
						function(err) {
							// async.times complete again
							test.ok( Object.keys(storage.locks).length == 0, "No more locks leftover in storage" );
							test.done();
						}
					); // async.times
				}, 25 ); // setTimeout (inner)
			}, 150 ); // setTimeout (outer)
		},
		
		function testKeyNormalization(test) {
			test.expect(6);
			var self = this;
			var key1 = ' / / / // HELLO-KEY @*#&^$*@/#&^$(*@#&^$   test   / ';
			var key2 = 'hello-key/test';
			
			this.storage.put( key1, { foo: 9876 }, function(err) {
				test.ok( !err, "No error creating weird key: " + err );
				
				self.storage.get( key2, function(err, data) {
					test.ok( !err, "No error fetching weird key: " + err );
					test.ok( !!data, "Data is true" );
					test.ok( typeof(data) == 'object', "Data is an object (not a string)" );
					test.ok( data.foo == 9876, "Data contains expected key and value" );
					
					self.storage.delete( key1, function(err) {
						test.ok( !err, "No error deleting weird key: " + err );
						test.done();
					} );
				} );
			} );
		},
		
		function testBinary(test) {
			test.expect(10);
			var self = this;
			var key = 'spacer.gif';
			var spacerBuf = fs.readFileSync( __dirname + '/' + key );
			var spacerHash = digestHex( spacerBuf );
			
			test.ok( !!spacerBuf, "Got buffer from file" );
			test.ok( typeof(spacerBuf) == 'object', "Buffer is an object" );
			test.ok( spacerBuf.length > 0, "Buffer has size" );
			
			this.storage.put( key, spacerBuf, function(err) {
				test.ok( !err, "No error creating binary: " + err );
				
				self.storage.get( key, function(err, data) {
					test.ok( !err, "No error fetching binary: " + err );
					test.ok( !!data, "Data is true" );
					test.ok( typeof(data) == 'object', "Data is an object (not a string)" );
					test.ok( data.length == spacerBuf.length, "Data length is correct" );
					
					var hashTest = digestHex( data );
					test.ok( hashTest == spacerHash, "SHA256 hash of data matches original" );
					
					self.storage.delete( key, function(err) {
						test.ok( !err, "No error deleting binary key: " + err );
						test.done();
					} );
				} );
			} );
		},
		
		function testBuffer(test) {
			test.expect(8);
			var self = this;
			var key = 'buftest';
			var value = { buf: "test" };
			
			this.storage.put( key, value, function(err) {
				test.ok( !err, "No error creating buftest: " + err );
				
				self.storage.getBuffer( key, function(err, data) {
					test.ok( !err, "No error fetching binary: " + err );
					test.ok( !!data, "Data is true" );
					test.ok( typeof(data) == 'object', "Data is an object (not a string)" );
					test.ok( data.length > 0, "Data length is non-zero" );
					
					var json = JSON.parse( data.toString() );
					test.ok( !!json, "Parsed JSON object from buftest" );
					test.ok( json.buf === "test", "Correct data inside JSON buftest" );
					
					self.storage.delete( key, function(err) {
						test.ok( !err, "No error deleting buftest key: " + err );
						test.done();
					} );
				} );
			} );
		},
		
		function testStream(test) {
			test.expect(14);
			var self = this;
			
			var key = 'spacer-stream.gif';
			var filename = 'spacer.gif';
			var spacerBuf = fs.readFileSync( __dirname + '/' + filename );
			var spacerHash = digestHex( spacerBuf );
			var spacerStream = fs.createReadStream( __dirname + '/' + filename );
			
			test.ok( !!spacerBuf, "Got buffer from file" );
			test.ok( typeof(spacerBuf) == 'object', "Buffer is an object" );
			test.ok( spacerBuf.length > 0, "Buffer has size" );
			test.ok( !!spacerStream, "Got read stream" );
			
			this.storage.putStream( key, spacerStream, function(err) {
				test.ok( !err, "No error creating stream: " + err );
				
				var tempFile = __dirname + '/' + filename + '.streamtemp';
				var outStream = fs.createWriteStream( tempFile );
				
				self.storage.getStream( key, function(err, storageStream, streamInfo) {
					test.ok( !err, "No error fetching stream: " + err );
					test.ok( !!storageStream, "Got storage stream as 2nd arg");
					test.ok( !!storageStream.pipe, "Storage stream has a pipe");
					test.ok( !!streamInfo, "Info was provided as the 3rd arg");
					test.ok( streamInfo.len == 43, "Info has correct data length");
					test.ok( streamInfo.mod > 0, "Info has a non-zero mod date");
					
					outStream.on('finish', function() {
						var newSpacerBuf = fs.readFileSync( tempFile );
						test.ok( newSpacerBuf.length == spacerBuf.length, "Stream length is correct" );
						
						var hashTest = digestHex( newSpacerBuf );
						test.ok( hashTest == spacerHash, "SHA256 hash of data matches original" );
						
						self.storage.delete( key, function(err) {
							test.ok( !err, "No error deleting stream key: " + err );
							fs.unlinkSync( tempFile );
							test.done();
						} ); // delete
					} ); // stream finish
					
					storageStream.pipe( outStream );
					
				} ); // getStream
			} ); // putStream
		},
		
		function testStreamRange(test) {
			// grab a range from within a stream, with both start and end specified
			test.expect(14);
			var self = this;
			
			var key = 'spacer-stream.gif';
			var filename = 'spacer.gif';
			var spacerBuf = fs.readFileSync( __dirname + '/' + filename );
			var spacerStream = fs.createReadStream( __dirname + '/' + filename );
			
			test.ok( !!spacerBuf, "Got buffer from file" );
			test.ok( typeof(spacerBuf) == 'object', "Buffer is an object" );
			test.ok( spacerBuf.length > 0, "Buffer has size" );
			test.ok( !!spacerStream, "Got read stream" );
			
			this.storage.putStream( key, spacerStream, function(err) {
				test.ok( !err, "No error creating stream: " + err );
				
				var tempFile = __dirname + '/' + filename + '.streamtemp';
				var outStream = fs.createWriteStream( tempFile );
				
				self.storage.getStreamRange( key, 0, 5, function(err, storageStream, streamInfo) {
					test.ok( !err, "No error fetching stream: " + err );
					test.debug( "streamInfo: ", streamInfo );
					test.ok( !!storageStream, "Got storage stream as 2nd arg");
					test.ok( !!storageStream.pipe, "Storage stream has a pipe");
					test.ok( !!streamInfo, "Info was provided as the 3rd arg");
					test.ok( streamInfo.len == 43, "Info has correct data length (expected 43, got " + streamInfo.len + ")");
					test.ok( streamInfo.mod > 0, "Info has a non-zero mod date");
					
					outStream.on('finish', function() {
						var newSpacerBuf = fs.readFileSync( tempFile );
						test.ok( newSpacerBuf.length == 6, "Stream length is correct" );
						test.ok( newSpacerBuf.toString() == "GIF89a", "Range buffer content is correct" );
						
						self.storage.delete( key, function(err) {
							test.ok( !err, "No error deleting stream key: " + err );
							fs.unlinkSync( tempFile );
							test.done();
						} ); // delete
					} ); // stream finish
					
					storageStream.pipe( outStream );
					
				} ); // getStream
			} ); // putStream
		},
		
		function testStreamRangeStart(test) {
			// grab a range from within a stream, with end missing
			test.expect(14);
			var self = this;
			
			var key = 'spacer-stream.gif';
			var filename = 'spacer.gif';
			var spacerBuf = fs.readFileSync( __dirname + '/' + filename );
			var spacerStream = fs.createReadStream( __dirname + '/' + filename );
			
			test.ok( !!spacerBuf, "Got buffer from file" );
			test.ok( typeof(spacerBuf) == 'object', "Buffer is an object" );
			test.ok( spacerBuf.length > 0, "Buffer has size" );
			test.ok( !!spacerStream, "Got read stream" );
			
			this.storage.putStream( key, spacerStream, function(err) {
				test.ok( !err, "No error creating stream: " + err );
				
				var tempFile = __dirname + '/' + filename + '.streamtemp';
				var outStream = fs.createWriteStream( tempFile );
				
				self.storage.getStreamRange( key, 20, NaN, function(err, storageStream, streamInfo) {
					test.ok( !err, "No error fetching stream: " + err );
					test.ok( !!storageStream, "Got storage stream as 2nd arg");
					test.ok( !!storageStream.pipe, "Storage stream has a pipe");
					test.ok( !!streamInfo, "Info was provided as the 3rd arg");
					test.ok( streamInfo.len == 43, "Info has correct data length (expected 43, got " + streamInfo.len + ")");
					test.ok( streamInfo.mod > 0, "Info has a non-zero mod date");
					
					outStream.on('finish', function() {
						var newSpacerBuf = fs.readFileSync( tempFile );
						test.ok( newSpacerBuf.length == 23, "Stream range length is correct" );
						test.ok( newSpacerBuf.equals( spacerBuf.slice(20) ), "Range buffer content is correct" );
						
						self.storage.delete( key, function(err) {
							test.ok( !err, "No error deleting stream key: " + err );
							fs.unlinkSync( tempFile );
							test.done();
						} ); // delete
					} ); // stream finish
					
					storageStream.pipe( outStream );
					
				} ); // getStream
			} ); // putStream
		},
		
		function testStreamRangeEnd(test) {
			// grab a range from within a stream, with start missing
			test.expect(14);
			var self = this;
			
			var key = 'spacer-stream.gif';
			var filename = 'spacer.gif';
			var spacerBuf = fs.readFileSync( __dirname + '/' + filename );
			var spacerStream = fs.createReadStream( __dirname + '/' + filename );
			
			test.ok( !!spacerBuf, "Got buffer from file" );
			test.ok( typeof(spacerBuf) == 'object', "Buffer is an object" );
			test.ok( spacerBuf.length > 0, "Buffer has size" );
			test.ok( !!spacerStream, "Got read stream" );
			
			this.storage.putStream( key, spacerStream, function(err) {
				test.ok( !err, "No error creating stream: " + err );
				
				var tempFile = __dirname + '/' + filename + '.streamtemp';
				var outStream = fs.createWriteStream( tempFile );
				
				self.storage.getStreamRange( key, NaN, 10, function(err, storageStream, streamInfo) {
					test.ok( !err, "No error fetching stream: " + err );
					test.ok( !!storageStream, "Got storage stream as 2nd arg");
					test.ok( !!storageStream.pipe, "Storage stream has a pipe");
					test.ok( !!streamInfo, "Info was provided as the 3rd arg");
					test.ok( streamInfo.len == 43, "Info has correct data length (expected 43, got " + streamInfo.len + ")");
					test.ok( streamInfo.mod > 0, "Info has a non-zero mod date");
					
					outStream.on('finish', function() {
						var newSpacerBuf = fs.readFileSync( tempFile );
						test.ok( newSpacerBuf.length == 10, "Stream range length is correct" );
						test.ok( newSpacerBuf.equals( spacerBuf.slice(43 - 10) ), "Range buffer content is correct" );
						
						self.storage.delete( key, function(err) {
							test.ok( !err, "No error deleting stream key: " + err );
							fs.unlinkSync( tempFile );
							test.done();
						} ); // delete
					} ); // stream finish
					
					storageStream.pipe( outStream );
					
				} ); // getStream
			} ); // putStream
		},
		
		function testPutMulti(test) {
			// test storing multiple keys at once
			test.expect(1);
			var keys = ['multi1', 'multi2', 'multi3'];
			var records = {
				multi1: { fruit: 'apple' },
				multi2: { fruit: 'orange' },
				multi3: { fruit: 'banana' }
			};
			this.storage.putMulti( records, function(err) {
				test.ok( !err, "No error calling putMulti: " + err );
				test.done();
			} );
		},
		
		function testGetMulti(test) {
			// test getMulti using several keys
			test.expect(6);
			var keys = ['multi1', 'multi2', 'multi3'];
			
			this.storage.getMulti( keys, function(err, values) {
				test.ok( !err, "No error calling getMulti: " + err );
				test.ok( !!values, "Got values from getMulti" );
				test.ok( values.length == 3, "Got 3 values from getMulti" );
				test.ok( values[0].fruit == 'apple', "First fruit is apple" );
				test.ok( values[1].fruit == 'orange', "Second fruit is orange" );
				test.ok( values[2].fruit == 'banana', "Third fruit is banana" );
				test.done();
			} );
		},
		
		function testHeadMulti(test) {
			// test headMulti using several keys
			test.expect(6);
			var keys = ['multi1', 'multi2', 'multi3'];
			
			this.storage.headMulti( keys, function(err, values) {
				test.ok( !err, "No error calling headMulti: " + err );
				test.ok( !!values, "Got values from headMulti" );
				test.ok( values.length == 3, "Got 3 values from headMulti" );
				test.ok( !!values[0].mod, "First metadata has a positive mod date" );
				test.ok( !!values[1].mod, "Second metadata has a positive mod date" );
				test.ok( !!values[2].mod, "Third metadata has a positive mod date" );
				test.done();
			} );
		},
		
		function testDeleteMulti(test) {
			// delete multiple keys at once using deleteMulti
			test.expect(2);
			var self = this;
			var keys = ['multi1', 'multi2', 'multi3'];
			
			this.storage.deleteMulti( keys, function(err) {
				test.ok( !err, "No error calling deleteMulti: " + err );
				
				// make sure they're really gone
				self.storage.getMulti( keys, function(err, values) {
					test.ok( !!err, "Expected error calling getMulti after delete" );
					test.done();
				} );
			} );
		},
		
		function testMaintenance(test) {
			var self = this;
			test.expect(3);
			
			var first = true;
			async.whilst(
				function () {
					return ( first || (Object.keys(self.storage.locks).length > 0) || !self.storage.queue.idle() );
				},
				function (callback) {
					test.debug("Waiting for locks / queue");
					first = false;
					setTimeout( function() { callback(); }, 250 );
				},
				function() {
					// locks / queue are free, proceed
					self.storage.runMaintenance( new Date(), function(err) {
						test.ok( !err, "No error running maintenance: " + err );
						
						self.storage.get( 'test_expire', function(err, data) {
							test.ok( !!err, "Error expected getting test_expire, should be deleted" );
							test.ok( !data, "Data expected to be false" );
							test.done();
						} );
					} );
				} // whilst complete
			); // whilst
		},
		
		function maintCleanup(test) {
			// cleanup leftover hash from expiration system
			this.storage.hashDeleteAll( '_cleanup/expires', true, function(err) {
				test.ok( !err, "No error deleting cleanup hash: " + err );
				test.done();
			} );
		}
		
	] // tests array
};
```

## File: `test/test-transaction.js`
```javascript
// Unit tests for Storage System - Transactions
// Copyright (c) 2015 - 2016 Joseph Huckaby
// Released under the MIT License

var os = require('os');
var fs = require('fs');
var path = require('path');
var cp = require('child_process');
var async = require('async');

module.exports = {
	tests: [
		
		function testTransactionEnable(test) {
			// enable transaction support
			// wait for queue and locks first
			var self = this;
			
			var first = true;
			async.whilst(
				function () {
					return ( first || (Object.keys(self.storage.locks).length > 0) || !self.storage.queue.idle() );
				},
				function (callback) {
					test.debug("Waiting for locks / queue");
					first = false;
					setTimeout( function() { callback(); }, 250 );
				},
				function() {
					// all locks released and queue idle
					
					// enable transactions in config
					self.storage.config.set('transactions', 1);
					
					// init transactions
					self.storage.initTransactions( function() {
						test.ok( true, "Initialized transaction system" );
						test.done();
					} ); // initTransactions
				} // no locks
			); // whlist
		},
		
		function testTransactionBasic(test) {
			// basic transaction
			var self = this;
			var storage = this.storage;
			var trans = null;
			
			var orig = {
				orig1: { value: "orig value 1" }, // will be untouched
				orig2: { value: "orig value 2" }, // will be changed
				orig3: { value: "orig value 3" }  // will be deleted
			};
			
			async.series(
				[
					function(callback) {
						// get some initial data in first
						storage.putMulti( orig, callback );
					},
					function(callback) {
						// begin the transaction
						storage.begin( "transtest", function(err, t) {
							if (err) return callback(err);
							trans = t;
							callback();
						});
					},
					
					// make some changes inside the transaction
					function(callback) { trans.put( "transtest", { value: "brand new" }, callback ); },
					function(callback) { trans.put( "orig2", { value: "changed 2" }, callback ); },
					function(callback) { trans.delete( "orig3", callback ); },
					
					// validate changes inside transaction
					function(callback) {
						self.multiCheck({
							"orig1": { "/value": "orig value 1" },
							"orig2": { "/value": "changed 2" },
							"orig3": false, // deleted
							"transtest": { "/value": "brand new" }
						}, trans, callback );
					},
					
					// make sure changes didn't take effect OUTSIDE transaction
					function(callback) {
						self.multiCheck({
							"orig1": { "/value": "orig value 1" },
							"orig2": { "/value": "orig value 2" },
							"orig3": { "/value": "orig value 3" },
							"transtest": false // not created yet
						}, storage, callback );
					},
					
					// commit transaction
					function(callback) {
						trans.commit( callback );
					},
					
					// make sure changes took
					function(callback) {
						self.multiCheck({
							"orig1": { "/value": "orig value 1" },
							"orig2": { "/value": "changed 2" },
							"orig3": false, // deleted
							"transtest": { "/value": "brand new" }
						}, storage, callback );
					},
					
					// make sure transaction object can no longer be used
					// (expecting error here)
					function(callback) {
						trans.put( "something", "other", function(err) {
							if (!err) return callback( new Error("Expected error using transaction after commit, got success instead.") );
							else callback();
						});
					},
					
					// cleanup
					function(callback) {
						storage.deleteMulti( ['orig1', 'orig2', 'transtest'], callback );
					}
					
				],
				function(err) {
					test.ok( !err, "Transaction Error: " + err );
					test.done();
				}
			); // series
		},
		
		// abort (rollback)
		function testTransactionAbort(test) {
			// abort transaction
			var self = this;
			var storage = this.storage;
			var trans = null;
			
			var orig = {
				orig1: { value: "orig value 1" }, // will be untouched
				orig2: { value: "orig value 2" }, // will be changed
				orig3: { value: "orig value 3" }  // will be deleted
			};
			
			async.series(
				[
					function(callback) {
						// get some initial data in first
						storage.putMulti( orig, callback );
					},
					function(callback) {
						// begin the transaction
						storage.begin( "transtest", function(err, t) {
							if (err) return callback(err);
							trans = t;
							callback();
						});
					},
					
					// make some changes inside the transaction
					function(callback) { trans.put( "transtest", { value: "brand new" }, callback ); },
					function(callback) { trans.put( "orig2", { value: "changed 2" }, callback ); },
					function(callback) { trans.delete( "orig3", callback ); },
					
					// validate changes inside transaction
					function(callback) {
						self.multiCheck({
							"orig1": { "/value": "orig value 1" },
							"orig2": { "/value": "changed 2" },
							"orig3": false, // deleted
							"transtest": { "/value": "brand new" }
						}, trans, callback );
					},
					
					// make sure changes didn't take effect OUTSIDE transaction
					function(callback) {
						self.multiCheck({
							"orig1": { "/value": "orig value 1" },
							"orig2": { "/value": "orig value 2" },
							"orig3": { "/value": "orig value 3" },
							"transtest": false // not created yet
						}, storage, callback );
					},
					
					// abort transaction
					function(callback) {
						trans.abort( callback );
					},
					
					// make sure changes reverted
					function(callback) {
						self.multiCheck({
							"orig1": { "/value": "orig value 1" },
							"orig2": { "/value": "orig value 2" },
							"orig3": { "/value": "orig value 3" },
							"transtest": false
						}, storage, callback );
					},
					
					// cleanup
					function(callback) {
						storage.deleteMulti( ['orig1', 'orig2', 'orig3'], callback );
					}
					
				],
				function(err) {
					test.ok( !err, "Transaction Error: " + err );
					test.done();
				}
			); // series
		},
		
		// compound function transaction
		function testTransactionCompound(test) {
			// basic transaction
			var self = this;
			var storage = this.storage;
			var trans = null;
			
			async.series(
				[
					function(callback) {
						// create initial list
						storage.listPush( 'comptranslist', { value: 'init_1' }, callback );
					},
					function(callback) {
						// create initial hash
						storage.hashPut( 'comptranshash', 'hkey1', { value: 'init_2' }, callback );
					},
					function(callback) {
						// begin the transaction
						storage.begin( "comptranstest", function(err, t) {
							if (err) return callback(err);
							trans = t;
							callback();
						});
					},
					
					// make some changes inside the transaction
					function(callback) { trans.listPush( "comptranslist", { value: "brand_new" }, callback ); },
					function(callback) { trans.hashPut( "comptranshash", "hkey2", { value: "yoyo_3" }, callback ); },
					
					// validate changes inside transaction
					function(callback) {
						self.multiCheck({
							"comptranslist": { "/length": 2 },
							"comptranslist/0": {
								"/items/0/value": "init_1",
								"/items/1/value": "brand_new" 
							},
							"comptranshash": { "/length": 2 },
							"comptranshash/data": {
								"/items/hkey1/value": "init_2",
								"/items/hkey2/value": "yoyo_3"
							}
						}, trans, callback );
					},
					
					// make sure changes didn't take effect OUTSIDE transaction
					function(callback) {
						self.multiCheck({
							"comptranslist": { "/length": 1 },
							"comptranslist/0": {
								"/items/0/value": "init_1",
								"/items/1/value": null
							},
							"comptranshash": { "/length": 1 },
							"comptranshash/data": {
								"/items/hkey1/value": "init_2",
								"/items/hkey2/value": null
							}
						}, storage, callback );
					},
					
					// commit transaction
					function(callback) {
						trans.commit( callback );
					},
					
					// make sure changes took
					function(callback) {
						self.multiCheck({
							"comptranslist": { "/length": 2 },
							"comptranslist/0": {
								"/items/0/value": "init_1",
								"/items/1/value": "brand_new" 
							},
							"comptranshash": { "/length": 2 },
							"comptranshash/data": {
								"/items/hkey1/value": "init_2",
								"/items/hkey2/value": "yoyo_3"
							}
						}, storage, callback );
					},
					
					// cleanup
					function(callback) {
						storage.listDelete( 'comptranslist', true, callback );
					},
					function(callback) {
						storage.hashDeleteAll( 'comptranshash', true, callback );
					}
					
				],
				function(err) {
					test.ok( !err, "Transaction Error: " + err );
					test.done();
				}
			); // series
		}
		
	] // tests array
};
```

## File: `test/test.js`
```javascript
// Unit tests for Storage System
// Copyright (c) 2015 - 2018 Joseph Huckaby
// Released under the MIT License

var os = require('os');
var fs = require('fs');
var path = require('path');
var cp = require('child_process');
var async = require('async');

var Class = require("pixl-class");
var PixlServer = require('pixl-server');
var Tools = require('pixl-tools');

process.chdir( __dirname );

var base_data_dir = path.join( os.tmpdir(), 'pixl-server-storage-unit-test-data' );

var server = new PixlServer({
	
	__name: 'Mock Server',
	__version: "1.0",
	
	configFile: "config.json",
	
	components: [
		require("../storage.js")
	]
	
});

// Unit Tests

var mainTests = require('./test-main.js');
var listTests = require('./test-list.js');
var hashTests = require('./test-hash.js');
var transactionTests = require('./test-transaction.js');
var indexerTests = require('./test-indexer.js');

module.exports = {
	setUp: function (callback) {
		var self = this;
		this.server = server;
		
		// hook server prestart to massage config to our liking
		server.on('prestart', function() {
			var storage_config = server.Storage.config.get();
			
			// optionally swap out engine on CLI
			if (self.args.engine) storage_config.engine = self.args.engine;
			
			// override Filesystem base dir to go somewhere more sane
			if (storage_config.Filesystem) storage_config.Filesystem.base_dir = base_data_dir;
			if (storage_config.SQLite) storage_config.SQLite.base_dir = base_data_dir;
		});
		
		// delete old unit test log
		cp.exec("rm -rf storage.log " + base_data_dir, function(err, stdout, stderr) {
			// startup mock server
			server.startup( function() {
				// startup complete
				server.logger.debug(9, "BASE DIR: " + base_data_dir);
				
				// write log in sync mode, for troubleshooting
				server.logger.set('sync', true);
				
				// save ref to storage
				self.storage = server.Storage;
				
				// build our test array dynamically
				// we have some repeating tests with different configuration options
				self.tests = self.tests.concat( 
					listTests.tests, 
					
					(self.args.splice || self.args.all || self.args.comprehensive) ? 
						listTests.generateSpliceTests() : [],
					
					hashTests.tests 
				);
				
				// now add transaction tests, which enable and init transactions
				self.tests = self.tests.concat( transactionTests.tests );
				
				// now repeat list and hash tests, with transactions enabled
				// augment test names for clarity
				[].concat( listTests.tests, hashTests.tests ).forEach( function(func) {
					var wrapper = function(test) { func.apply(this, [test]); };
					wrapper.testName = 'Transaction_' + func.name;
					self.tests.push( wrapper );
				} );
				
				// finally add indexer tests
				self.tests = self.tests.concat( indexerTests.tests );
				
				// log memory usage at end
				self.tests.push( function(test) {
					if (global.gc) { global.gc(); global.gc(); }
					test.ok( true );
					setTimeout( function() { 
						self.storage.logDebug(9, "MEMORY USAGE: " + Tools.getTextFromBytes( process.memoryUsage.rss() ), process.memoryUsage() );
						test.done(); 
					}, 1 );
				} );
				
				// startup complete
				// delay this by 1ms so the log is in the correct order (pre-start is async)
				setTimeout( function() { callback(); }, 1 );
			} ); // startup
		} ); // delete
	},
	
	beforeEach: function(test) {
		this.storage.logDebug(9, "BEGIN UNIT TEST: " + test.name);
	},
	
	afterEach: function(test) {
		this.storage.logDebug(9, "END UNIT TEST: " + test.name);
	},
	
	onAssertFailure: function(test, msg, data) {
		this.storage.logDebug(9, "UNIT ASSERT FAILURE: " + test.file + ": " + test.name + ": " + msg, data);
	},
	
	tests: [].concat(
		mainTests.tests
	),
	
	tearDown: function (callback) {
		// clean up
		this.server.shutdown( function() {
			cp.exec("rm -rf transactions " + base_data_dir, callback);
		} );
	},
	
	multiCheck: function(map, storage, callback) {
		// check multiple records against map
		// map format: { key: { "/xpath/thingy": "asserted value" }, key2: false (deleted) }
		async.forEachOfLimit( map, storage.concurrency,
			function(xpaths, key, callback) {
				// fetch record
				storage.get( key, function(err, data) {
					if (err) {
						if (!xpaths) return callback(); // expected
						return callback(err);
					}
					
					for (var xpath in xpaths) {
						var value = Tools.lookupPath( xpath, data );
						if (value != xpaths[xpath]) {
							// console.log( "DATA: ", data );
							return callback( new Error("Data Mismatch: " + key + ": " + xpath + ": " + value + " != " + xpaths[xpath]) );
						}
					}
					
					callback();
				}); // get
			},
			callback
		);
	},
	
	multiIndexSearch: function(map, index_config, test, callback) {
		// perform multiple index searches in series, add assertions to test
		var self = this;
		
		async.forEachOfLimit( map, 1,
			function(expected, squery, callback) {
				// search records
				self.storage.searchRecords( squery, index_config, function(err, results) {
					if (expected === false) {
						test.ok( !!err, "Error expected with query: " + squery );
						return callback();
					}
					
					test.ok( !err, "No error searching record: " + err );
					
					test.debug("Search: "+squery+" -- results:", results);
					test.ok( !!results, "Got results from search" );
					test.ok( typeof(results) == 'object', "Results is an object: " + typeof(results) );
					
					var keys = Object.keys(results);
					test.ok( keys.length == Object.keys(expected).length, "Found correct number of records: " + keys.length );
					
					for (var key in expected) {
						test.ok( !!results[key], "Found record " + key + " in results" );
					}
					
					callback();
				} );
			},
			callback
		);
	}
};
```


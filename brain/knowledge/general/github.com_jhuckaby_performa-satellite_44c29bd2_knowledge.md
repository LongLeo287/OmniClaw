---
id: github.com-jhuckaby-performa-satellite-44c29bd2-kn
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:15.280388
---

# KNOWLEDGE EXTRACT: github.com_jhuckaby_performa-satellite_44c29bd2
> **Extracted on:** 2026-04-01 11:06:20
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007521235/github.com_jhuckaby_performa-satellite_44c29bd2

---

## File: `.npmignore`
```
.gitignore
node_modules/
dist/
work/
```

## File: `LICENSE.md`
```markdown
# License

**The MIT License (MIT)**

*Copyright (c) 2019 - 2024 Joseph Huckaby*

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `README.md`
```markdown
# Overview

This module is a companion to the [Performa](https://github.com/jhuckaby/performa) monitoring system.  It is the data collector, which can be installed on all your servers.  It collects metrics and sends them to the central Performa server every minute, and is activated by [cron](https://en.wikipedia.org/wiki/Cron).  It is shipped as a precompiled binary and thus has no dependencies.

# Installation

The easiest way to install Performa Satellite is to use one of our precompiled binaries.  It can live anywhere on the filesystem, but for these examples we place it into the `/opt/performa` directory.  Make sure you are `root` (superuser) to install this.

```
mkdir /opt/performa
curl -L https://github.com/jhuckaby/performa-satellite/releases/latest/download/performa-satellite-linux-x64 > /opt/performa/satellite.bin
chmod 755 /opt/performa/satellite.bin
/opt/performa/satellite.bin --install
```

Note that in this case you will have to select the correct binary for your platform.  The static binary flavors available are:

- `performa-satellite-linux-arm64`
- `performa-satellite-linux-x64`
- `performa-satellite-macos-arm64`
- `performa-satellite-macos-x64`

The `performa-satellite-linux-x86` binary should work on any 64-bit Linux OS on x86 hardware, including RedHat/CentOS and Debian/Ubuntu.  Change `x86` to `arm64` if you are running Linux on ARM (e.g. Raspberry Pi).  If you are installing on macOS, replace `linux` with `macos`, but note your Mac's architecture (`x64` or `arm64` a.k.a. Apple Silicon).

Running the binary with the `--install` argument will add it to [cron](https://en.wikipedia.org/wiki/Cron), specifically in `/etc/cron.d/performa-satellite`, which is set to run once per minute.  It also creates a default configuration file, if one doesn't exist.

# Configuration

Performa Satellite expects a JSON formatted configuration file to live in the same directory as the binary executable, and named `config.json`.  Here is an example file:

```json
{
	"enabled": true,
	"host": "performa.local:5511",
	"secret_key": "CHANGE_ME",
	"group": ""
}
```

Here are descriptions of the properties you can put in the file:

| Property Name | Type | Description |
|---------------|------|-------------|
| `enabled` | Boolean | This enables or disables Performa Satellite.  Set this to `false` to pause metrics collection. |
| `host` | String | Set this to the hostname and port of your Performa master server, e.g. `performa.mycompany.com:5511`.  The default port for Performa is `5511`. |
| `secret_key` | String | Set this to the same secret key string on your Performa master server.  See [Secret Key](https://github.com/jhuckaby/performa#secret_key) for details. |
| `group` | String | **(Optional)** The group ID is optional, and only needed if you have servers with indeterminate hostnames (i.e. serverless, autoscale, etc.).  See [Groups](https://github.com/jhuckaby/performa#groups) for details. |
| `proto` | String | **(Optional)** If you have configured your Performa master server with HTTPS, Satellite can send metrics securely by setting this property to `https:`. |
| `socket_opts` | Object | **(Optional)** Optionally configure the options passed to the Node.js HTTP library.  A potential use case is for SSL self-signed certs (see below). |
| `max_sleep_ms` | Number | **(Optional)** Set the maximum random sleep time.  Defaults to 5000 ms.  See [Scalability](#scalability) below for details. |

To connect with HTTPS and allow self-signed certs, add the `proto` and `socket_opts` properties to your `config.json` file:

```json
{
	"enabled": true,
	"host": "performa.local:5511",
	"secret_key": "CHANGE_ME",
	"group": "",
	"proto": "https:",
	"socket_opts": {
		"rejectUnauthorized": false
	}
}
```

## Command-Line Arguments

The Performa Satellite binary executable accepts the following command-line arguments:

| Argument | Description |
|----------|-------------|
| `--install` | This runs first-time installation tasks such as creating the cron job and a sample configuration file. |
| `--uninstall` | This removes the cron job and deletes the config file, if one is found. |
| `--config` | Optionally specify a custom location on disk for the configuration file. |
| `--debug` | Setting this flag runs the collector in debug mode, causing it to emit raw stats on the console rather than submitting them to the server. |
| `--nosleep` | This disables the random sleep that Satellite performs before collecting and sending metrics. |
| `--hostname` | This allows you to specify a custom local hostname, to use in place of the actual server hostname. |
| `--fake` | Setting this flag will generate "fake" (semi-random) metrics data.  Used for testing purposes. |
| `--quiet` | This silences all output from Satellite, even fatal errors. |

# Scalability

Performa Satellite is designed to run on many servers, and will randomly delay sending metrics by up to 5 seconds (by default) at the start of each new minute, so not all your servers contact the central master server at the same instant.  The same random seed is used for each server (it is based on the hostname) to insure that the metrics collection happens exactly 1 minute apart on each server.

If you have a setup with hundreds of thousands of servers all reporting to the same Performa central server, it is recommended that you increase the max delay from 5 seconds up to 30 seconds.  To do this, edit your Performa Satellite `config.json` file and add a top-level JSON property named `max_sleep_ms`.  This value is in milliseconds, so set it to `30000` for 30 seconds.

You can disable the sleep feature by adding the `--nosleep` command-line argument.

# Development

You can install the Performa Satellite source code by using [Git](https://en.wikipedia.org/wiki/Git) ([Node.js](https://nodejs.org/) is also required):

```
git clone https://github.com/jhuckaby/performa-satellite.git
cd performa-satellite
npm install
```

You can then run it in debug mode by issuing this command:

```
node index.js --debug
```

To repackage the binary executables for Linux, macOS and Windows, run this command:

```
npm run package
```

# License (MIT)

**The MIT License**

*Copyright (c) 2019 - 2024 Joseph Huckaby.*

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

## File: `config.json`
```json
{
	"enabled": true,
	"host": "performa.local:5511",
	"secret_key": "CHANGE_ME",
	"group": ""
}
```

## File: `index.js`
```javascript
#!/usr/bin/env node

// Performa Satellite
// Gathers metrics and submits them to a Performa master server
// Install via crontab to run every minute
// See: https://github.com/jhuckaby/performa-satellite
// Copyright (c) 2019 - 2024 Joseph Huckaby, MIT License

var fs = require('fs');
var os = require('os');
var cp = require('child_process');
var Path = require('path');
var XML = require('pixl-xml');
var Request = require('pixl-request');
var cli = require('pixl-cli');
var si = require('systeminformation');
var sqparse = require('shell-quote').parse;

var request = new Request("Performa-Satellite/1.1.4");
request.setTimeout( 5 * 1000 ); // 3 seconds
request.setAutoError( true );
request.setRetries( 5 );
request.setAutoContentLength( false );
request.setKeepAlive( true );
request.retryMatch = /^[45]\d\d$/;

cli.global();
var Tools = cli.Tools;
var args = cli.args;
var async = Tools.async;
var self_bin = Path.resolve( process.argv[0] );
var config_file = Path.join( Path.dirname( self_bin ), 'config.json' );
var config = {};

if (args.install || (args.other && (args.other[0] == 'install'))) {
	// first time installation, add self to crontab
	var raw_tab = "";
	raw_tab += "# Run Performa Satellite data collector once per minute.\n";
	raw_tab += "# See: https://github.com/jhuckaby/performa-satellite\n";
	raw_tab += "PATH=$PATH:/usr/bin:/bin:/usr/local/bin:/usr/sbin:/sbin:/usr/local/sbin\n";
	raw_tab += '* * * * * root ' + self_bin + " --quiet\n";
	
	var cron_file = '/etc/cron.d/performa-satellite';
	fs.writeFileSync( cron_file, raw_tab, { mode: 0o644 } );
	// try to give crond a hint that it needs to reload
	if (fs.existsSync('/etc/crontab')) fs.utimesSync( '/etc/crontab', new Date(), new Date() );
	if (fs.existsSync('/var/spool/cron')) fs.utimesSync( '/var/spool/cron', new Date(), new Date() );
	print("\nPerforma Satellite has been installed to cron:\n\t" + cron_file + "\n");
	
	if (!fs.existsSync(config_file)) {
		config = { enabled: true, host: "performa.local:5511", secret_key: "CHANGE_ME", group: "" };
		var raw_config = JSON.stringify( config, null, "\t" );
		fs.writeFileSync( config_file, raw_config, { mode: 0o600 } );
		print("\nA sample config file has been created: " + config_file + ":\n");
		print( raw_config + "\n" );
	}
	
	print("\n");
	process.exit(0);
}
else if (args.uninstall || (args.other && (args.other[0] == 'uninstall'))) {
	// remove from cron and exit
	var cron_file = '/etc/cron.d/performa-satellite';
	if (!fs.existsSync(cron_file)) die("\nPerforma Satellite is not currently installed, so just delete this file and it's super gone.\n\n");
	fs.unlinkSync( cron_file );
	
	// also cleanup legacy cron.d filename if applicable
	if (fs.existsSync(cron_file + '.cron')) fs.unlinkSync(cron_file + '.cron');
	
	// try to give crond a hint that it needs to reload
	if (fs.existsSync('/etc/crontab')) fs.utimesSync( '/etc/crontab', new Date(), new Date() );
	if (fs.existsSync('/var/spool/cron')) fs.utimesSync( '/var/spool/cron', new Date(), new Date() );
	if (fs.existsSync(config_file)) fs.unlinkSync( config_file );
	print("\nPerforma Satellite has been removed.\n");
	print("To complete the uninstall, simply delete this file.\n");
	print("\n");
	process.exit(0);
}

// optional config file, in same dir as executable or custom location
if (args.config && fs.existsSync(args.config)) {
	config = JSON.parse( fs.readFileSync(args.config, 'utf8') );
}
else if (fs.existsSync(config_file)) {
	config = JSON.parse( fs.readFileSync(config_file, 'utf8') );
}
else if (fs.existsSync( Path.join(__dirname, 'config.json') )) {
	config = JSON.parse( fs.readFileSync(Path.join(__dirname, 'config.json'), 'utf8') );
}

// exit quietly if not enabled
if (!config.enabled && !args.enabled && !process.env['PERFORMA_ENABLED'] && !args.debug) process.exit(0);

// optionally switch users
if (!args.debug && config.uid && (process.getuid() == 0)) {
	var user = Tools.getpwnam( config.uid );
	if (user) process.setuid( user.uid );
}

// determine hostname to submit metrics to
var api_host = args.host || process.env['PERFORMA_HOST'] || config.host || 'performa.local:5511';
var api_proto = args.proto || process.env['PERFORMA_PROTO'] || config.proto || 'http:';

// allow server to specify its own group (i.e. for auto-scaling)
var group_id = args.group || process.env['PERFORMA_GROUP'] || config.group || '';

// start building JSON structure
var info = {
	version: "1.0",
	date: (new Date()).getTime() / 1000,
	hostname: args.hostname || os.hostname(),
	auth: Tools.digestHex('' + Math.floor(Tools.timeNow(true) / 60) + config.secret_key, 'sha256'),
	data: {
		uptime_sec: os.uptime(),
		arch: os.arch(),
		platform: os.platform(),
		release: os.release(),
		load: os.loadavg(),
		// cpus: os.cpus(),
		stats: {}
	}
};
if (group_id) info.group = group_id;

var commands = [];
var host_hash = Tools.digestHex( info.hostname, 'md5' );
var host_id = parseInt( host_hash.substring(0, 8), 16 ); // 32-bit numerical hash
var state_file = Path.join( os.tmpdir(), "performa-satellite-temp.json" );
var state = {};

var snapshot = { 
	auth: info.auth,
	network: {}, 
	processes: {}, 
	files: { list: [] } 
};

if (config.use_curl) {
	// use curl instead of pixl-request
	var curl_bin = (config.use_curl === true) ? '/usr/bin/curl' : config.use_curl;
	
	request.json = function(url, data, callback) {
		var data_file = Path.join( os.tmpdir(), "performa-satellite-data.json" );
		fs.writeFileSync( data_file, JSON.stringify(data) + "\n" );
		
		var cmd = curl_bin + ' -s -m 5 -H "Content-Type: application/json" -d "@' + data_file + '" "' + url + '"';
		cp.exec( cmd, { timeout: 6 * 1000 }, function(err, stdout, stderr) {
			if (err) return callback(err);
			if (stderr.match(/\S/)) return callback( new Error(stderr) );
			
			var json = null;
			try { json = JSON.parse( ''+stdout ); }
			catch (err) {
				return callback(err);
			}
			
			callback(false, {}, json, {});
		} ); // cp.exec
	}; // request.json
} // curl

async.series([
	function(callback) {
		// sleep for N seconds based on hash of hostname
		// this is to avoid multiple servers from submitting metrics at the same instant
		if (args.debug || args.nosleep) return process.nextTick(callback);
		
		var max_sleep_ms = config.max_sleep_ms || 5000;
		var sleep_ms = 1000 + (host_id % max_sleep_ms);
		setTimeout( function() { callback(); }, sleep_ms );
	},
	function(callback) {
		// load state data if cache file exists
		fs.readFile( state_file, 'utf8', function(err, data) {
			if (err || !data) return callback();
			try { state = JSON.parse(data); }
			catch (e) {;}
			callback();
		});
	},
	function(callback) {
		// first call home to say hello and gs list of custom commands to run, if any
		if (!config.secret_key) die("ERROR: No secret key found in config.json file.\n");
		
		var url = api_proto + "//" + api_host + "/api/app/hello";
		var opts = config.socket_opts || {};
		
		var hello = {
			version: info.version, 
			hostname: info.hostname, 
			group: info.group || ''
		};
		
		request.json( url, hello, opts, function(err, resp, data, perf) {
			// check for error, fatal unless in debug mode
			var err_msg = '';
			if (err) err_msg = "Performa Satellite Error: Failed to call home: " + err;
			else if (data.code) err_msg = "Performa Satellite Error: API returned: " + data.description;
			else if (!data.version || (data.version !== 2)) err_msg = "Incompatible API Version: Please upgrade both Performa and Performa Satellite to the latest stable release.";
			
			if (err_msg) {
				var err_file = Path.join( os.tmpdir(), "performa-satellite-error.txt" );
				fs.writeFileSync( err_file, [
					"Date/Time: " + (new Date()).toString(),
					"URL: " + url,
					"Error: " + err_msg,
					"Data:",
					JSON.stringify(hello)
				].join("\n") + "\n" );
				
				if (args.debug) {
					warn( "Warning: " + err_msg + "\n" );
					return callback();
				}
				else die( err_msg + "\n" );
			}
			
			commands = data.commands || [];
			callback();
		});
	},
	function(callback) {
		// operating system
		si.osInfo( function(data) {
			data.platform = Tools.ucfirst( data.platform );
			info.data.os = data;
			callback();
		} );
	},
	function(callback) {
		// system memory
		si.mem( function(data) {
			info.data.memory = data;
			callback();
		} );
	},
	function(callback) {
		// cpu info
		si.cpu( function(data) {
			info.data.cpu = data;
			callback();
		} );
	},
	function(callback) {
		// cpu load
		si.currentLoad( function(data) {
			Tools.mergeHashInto( info.data.cpu, data );
			delete info.data.cpu.cpus;
			callback();
		} );
	},
	function(callback) {
		// file systems
		si.fsSize( function(data) {
			info.data.mounts = {};
			data.forEach( function(item) {
				var key = item.mount.replace(/^\//, '').replace(/\W+/g, '_') || 'root';
				info.data.mounts[key] = item;
			});
			callback();
		} );
	},
	/*function(callback) {
		// block devices
		si.blockDevices( function(data) {
			info.data.devices = data;
			callback();
		} );
	},*/
	function(callback) {
		// disk IO
		si.disksIO( function(data) {
			info.data.stats.io = data;
			callback();
		} );
	},
	function(callback) {
		// filesystem stats
		si.fsStats( function(data) {
			info.data.stats.fs = data;
			callback();
		} );
	},
	/*function(callback) {
		// network interfaces
		si.networkInterfaces( function(data) {
			info.data.interfaces = data;
			callback();
		} );
	},*/
	function(callback) {
		// network stats (first external interface)
		si.networkStats( function(data) {
			info.data.stats.network = data[0];
			callback();
		} );
	},
	function(callback) {
		// count open network sockets
		si.networkConnections( function(data) {
			if (!data) data = [];
			info.data.stats.network.conns = data.length;
			info.data.stats.network.states = { established: 0 };
			data.forEach( function(conn) {
				if (conn.state) {
					var key = conn.state.toLowerCase();
					if (!info.data.stats.network.states[key]) info.data.stats.network.states[key] = 0;
					info.data.stats.network.states[key]++;
				}
			});
			snapshot.network.connections = data;
			callback();
		} );
	},
	function(callback) {
		// all processes
		si.processes( function(data) {
			info.data.processes = data;
			snapshot.processes.list = info.data.processes.list;
			delete info.data.processes.list;
			callback();
		} );
	},
	function(callback) {
		// try to calculate iowait % (linux only)
		// borrowed from: https://github.com/cgoldberg/linux-metrics/blob/master/linux_metrics/cpu_stat.py
		if ((process.platform != 'linux') || !fs.existsSync('/proc/stat')) return process.nextTick( callback );
		
		info.data.cpu.cpus = {};
		
		var proc_lines = fs.readFileSync( '/proc/stat', 'utf8' ).trim().split(/\n/);
		proc_lines.forEach( function(line) {
			if (line.match(/^\s*(cpu\d*)\s+(.+)$/)) {
				var cpu_key = RegExp.$1;
				var cpu_values = RegExp.$2.trim().split(/\s+/).map( function(value) { return parseInt(value); } );
				
				if (cpu_values.length && state.proc_stat && state.proc_stat[cpu_key]) {
					var cpu_deltas = cpu_values.map( function(value, idx) {
						return Math.max( 0, value - state.proc_stat[cpu_key][idx] );
					});
					
					var delta_total = 0;
					cpu_deltas.forEach( function(delta) { delta_total += delta; } );
					if (!delta_total) delta_total = 1; // prevent divide-by-zero
					
					// convert each to percentage of total
					var percents = cpu_deltas.map( function(delta) {
						return Tools.shortFloat( 100 - (100 * ((delta_total - delta) / delta_total)) );
					});
					
					// format for JSON
					var pct_fmt = {
						'user': percents[0],
						'nice': percents[1],
						'system': percents[2],
						'idle': percents[3],
						'iowait': percents[4],
						'irq': percents[5],
						'softirq': percents[6]
					};
					
					if (cpu_key == 'cpu') info.data.cpu.totals = pct_fmt;
					else info.data.cpu.cpus[cpu_key] = pct_fmt;
				} // found state
				else {
					// fill with zeroes for now
					var pct_fmt = { user:0, nice:0, system:0, idle:100, iowait:0, irq:0, softirq:0 };
					if (cpu_key == 'cpu') info.data.cpu.totals = pct_fmt;
					else info.data.cpu.cpus[cpu_key] = pct_fmt;
				}
				
				if (!state.proc_stat) state.proc_stat = {};
				state.proc_stat[cpu_key] = cpu_values;
			}
		}); // foreach line
		
		// cleanup old mess
		if (state.proc_stat) {
			delete state.proc_stat.date;
			delete state.proc_stat.cpu_values;
		}
		
		process.nextTick( callback );
	},
	function(callback) {
		// write state data back out to cache file on disk
		fs.writeFile( state_file, JSON.stringify(state), callback );
	},
	function(callback) {
		// custom commands
		if (!commands.length) return process.nextTick( callback );
		info.data.commands = {};
		
		async.eachSeries( commands,
			function(command, callback) {
				// exec single command
				if (!command.timeout) command.timeout = 5; // default 5 sec
				
				var child_opts = { 
					// timeout: command.timeout * 1000,
					windowsHide: true,
					env: Tools.copyHash( process.env ),
					stdio: ['pipe', 'pipe', 'ignore']
				};
				if (command.uid && (command.uid != 0)) {
					var user_info = Tools.getpwnam( command.uid, true );
					if (user_info) {
						child_opts.uid = parseInt( user_info.uid );
						child_opts.gid = parseInt( user_info.gid );
						child_opts.env.USER = child_opts.env.USERNAME = user_info.username;
						child_opts.env.HOME = user_info.dir;
						child_opts.env.SHELL = user_info.shell;
					}
					else {
						info.data.commands[ command.id ] = "Error: Could not determine user information for: " + command.uid;
						return process.nextTick( callback );
					}
				}
				
				var child = null;
				var child_cmd = command.exec;
				var child_args = [];
				var child_output = '';
				var child_timeout_err_msg = '';
				var callback_fired = false;
				
				// if command has cli args, parse using shell-quote
				if (child_cmd.match(/\s+(.+)$/)) {
					var cargs_raw = RegExp.$1;
					child_cmd = child_cmd.replace(/\s+(.+)$/, '');
					child_args = sqparse( cargs_raw, child_opts.env );
				}
				
				var child_timer = setTimeout( function() {
					// timed out
					child_timeout_err_msg = "Command timed out after " + command.timeout + " seconds";
					child.kill(); // should fire exit event
				}, command.timeout * 1000 );
				
				// spawn child
				try {
					child = cp.spawn( child_cmd, child_args, child_opts );
				}
				catch (err) {
					clearTimeout( child_timer );
					info.data.commands[ command.id ] = "Error: Could not execute command: " + child_cmd + ": " + Tools.getErrorDescription(err);
					if (!callback_fired) { callback_fired = true; callback(); }
				}
				
				child.on('error', function (err) {
					// child error
					clearTimeout( child_timer );
					info.data.commands[ command.id ] = "Error: Could not execute command: " + child_cmd + ": " + Tools.getErrorDescription(err);
					if (!callback_fired) { callback_fired = true; callback(); }
				} );
				
				child.on('exit', function (code, signal) {
					// child exited
					clearTimeout( child_timer );
					var result = child_timeout_err_msg || child_output;
					
					// automatically parse JSON or XML
					if ((command.format == 'json') && result.match(/(\{|\[)/)) {
						// attempt to parse JSON
						var json = null;
						try { json = JSON.parse(result); }
						catch (err) { result = 'JSON Parser Error: ' + err; }
						if (json) result = json;
					}
					else if ((command.format == 'xml') && result.match(/\</)) {
						// attempt to parse XML
						var xml = null;
						try { xml = XML.parse(result); }
						catch (err) { result = "XML Parser Error: " + err; }
						if (xml) result = xml;
					}
					else {
						// plain text, trim whitespace
						result = result.trim();
					}
					
					info.data.commands[ command.id ] = result;
					if (!callback_fired) { callback_fired = true; callback(); }
				});
				
				if (child.stdout) {
					child.stdout.on('data', function(data) {
						child_output += data.toString();
						if (child_output.length > 32 * 1024) child.kill(); // sanity
					});
				}
				
				if (child.stdin && command.script) {
					child.stdin.write( command.script + "\n" );
				}
				child.stdin.end();
			},
			callback
		);
	},
	function(callback) {
		// all done
		
		if (args.fake) {
			// fake up metrics based on host ID hash and timestamp
			// used for testing purposes
			var data_paths = [
				'load/0',
				'memory/used',
				'memory/available',
				'stats/network/conns',
				'mounts/root/use',
				'stats/fs/rx',
				'stats/fs/wx',
				'stats/io/tIO',
				'commands/open_files',
				'stats/network/rx_bytes',
				'stats/network/tx_bytes',
				'processes/all'
			];
			data_paths.forEach( function(path) {
				var now = Tools.timeNow(true);
				var id1 = parseInt( host_hash.substring(0, 16), 16 );
				var id2 = parseInt( host_hash.substring(16), 16 );
				var cycle_len = (id1 % 90) + 10; // between 10 and 99 minutes
				var cycle_half = Math.floor( cycle_len / 2 );
				var cycle_idx = Math.floor(now / 60) % cycle_len;
				var adj1 = ((id1 % 10000) / 10000) + 0.5; // 0.5 to 1.5
				var adj2 = ((id2 % 10000) / 10000) + 0.5; // 0.5 to 1.5
				var orig_value = Tools.getPath( info.data, path ) || 0;
				var value1 = orig_value * adj1;
				var value2 = orig_value * adj2;
				var value = 0;
				var mode = 'EaseInOut';
				var algo = 'Quadratic';
				
				if (cycle_idx <= cycle_half) {
					value = Tools.tween( value1, value2, cycle_idx / cycle_half, mode, algo );
				}
				else {
					value = Tools.tween( value2, value1, (cycle_idx - cycle_half) / cycle_half, mode, algo );
				}
				if (orig_value == Math.floor(orig_value)) value = Math.floor(value);
				else value = Tools.shortFloat( value );
				
				Tools.setPath( info.data, path, value );
				
				// rehash md5 for next item
				host_hash = Tools.digestHex( host_hash, 'md5' );
			});
		} // fake
		
		if (args.debug) {
			// if debug mode is set, dump all metrics to console and exit (no submit)
			print( JSON.stringify(info, null, "\t") + "\n" );
			process.exit(0);
		}
		
		// submit metrics to Performa central server via JSON HTTP POST
		var url = api_proto + "//" + api_host + "/api/app/submit";
		var opts = config.socket_opts || {};
		
		request.json( url, info, opts, function(err, resp, data, perf) {
			if (err) {
				var err_file = Path.join( os.tmpdir(), "performa-satellite-error.txt" );
				fs.writeFileSync( err_file, [
					"Date/Time: " + (new Date()).toString(),
					"URL: " + url,
					"Error: " + err,
					"Data:",
					JSON.stringify(info)
				].join("\n") + "\n" );
				
				die("Performa Satellite Error: Failed to submit data: " + err + "\n");
			}
			
			if (data.take_snapshot && data.time_code) {
				// server has requested a snapshot
				// (includes all running procs and open conns)
				snapshot.version = "1.0";
				snapshot.hostname = info.hostname;
				snapshot.source = data.snapshot_source;
				snapshot.time_code = data.time_code;
				url = api_proto + "//" + api_host + "/api/app/snapshot";
				
				// the process CPU values from systeminformation are incorrect, so we have to grab them ourselves
				// this works on at least: OS X, Fedora, Ubuntu and CentOS
				var ps_cmd = '/bin/ps -eo "ppid pid %cpu rss"';
				cp.exec( ps_cmd, { timeout: 5 * 1000 }, function(err, stdout, stderr) {
					if (err) die("Performa Satellite Error: Failed to exec ps: " + err + "\n");
					
					var lines = stdout.split(/\n/);
					var pids = {};
					
					// process each line from ps response
					for (var idx = 0, len = lines.length; idx < len; idx++) {
						var line = lines[idx];
						if (line.match(/(\d+)\s+(\d+)\s+([\d\.]+)\s+(\d+)/)) {
							var ppid = parseInt( RegExp.$1 );
							var pid = parseInt( RegExp.$2 );
							var cpu = parseFloat( RegExp.$3 );
							var mem = parseInt( RegExp.$4 ); // Note: This is in KB
							pids[ pid ] = { ppid: ppid, cpu: cpu, mem: mem };
						} // good line
					} // foreach line
					
					snapshot.processes.list.forEach( function(process) {
						if (pids[process.pid]) {
							process.pcpu = pids[process.pid].cpu;
							process.mem_rss = pids[process.pid].mem;
						}
					} ); 
					
					// add all open files to the snap
					getOpenFiles( function(err) {
						// ignore error (not much we can do about it here)
						var opts = config.socket_opts || {};
						
						// now send the snapshot to the server
						request.json( url, snapshot, opts, function(err, resp, data, perf) {
							if (err) {
								var err_file = Path.join( os.tmpdir(), "performa-satellite-error.txt" );
								fs.writeFileSync( err_file, [
									"Date/Time: " + (new Date()).toString(),
									"URL: " + url,
									"Error: " + err,
									"Data:",
									JSON.stringify(snapshot)
								].join("\n") + "\n" );
								
								die("Performa Satellite Error: Failed to submit snapshot data: " + err + "\n");
							}
							callback();
						}); // request.json
					}); // getOpenFiles
				}); // cp.exec
			} // snapshot
			else callback();
		}); // request.json
	} // done
]); // async.series

function getOpenFiles(callback) {
	// use lsof to include all open files to the snap
	var cmd = Tools.findBinSync('lsof');
	if (!cmd) return callback( new Error("Cannot locate lsof binary.") );
	
	// linux only: prevent duplicate files for threads
	if (process.platform == 'linux') cmd += ' -Ki';
	
	// rest of lsof CLI options are universal:
	// machine-readable output, skip blocking ops, formatting opts
	cmd += ' -RPn -F Ttpfn';
	
	cp.exec( cmd, { timeout: 10 * 1000 }, function(err, stdout, stderr) {
		if (err) return callback(err);
		
		// parse lsof output
		var files = [];
		var cur_proc = null;
		var cur_file = null;
		
		stdout.split(/\n/).forEach( function(line) {
			if (!line.match(/^(\w)(.+)$/)) return;
			var code = RegExp.$1;
			var value = RegExp.$2;
			
			switch (code) {
				case 'p':
					// new process
					if (cur_proc && cur_file) files.push( Tools.mergeHashes(cur_proc, cur_file) );
					cur_proc = { pid: parseInt(value) };
					cur_file = null;
				break;
				
				case 'f':
					// new file
					if (cur_proc && cur_file) files.push( Tools.mergeHashes(cur_proc, cur_file) );
					cur_file = { desc: value };
				break;
				
				case 't':
					// file type
					if (cur_file) cur_file.type = value;
				break;
				
				case 'n':
					// file path
					if (cur_file) cur_file.path = value;
				break;
				
				case 'T':
					// TCP socket info (append if applicable)
					if (cur_file && cur_file.path && value.match(/ST\=(.+)$/)) {
						cur_file.path += ' (' + RegExp.$1 + ')';
					}
				break;
			} // switch code
		} ); // foreach line
		
		if (cur_proc && cur_file) files.push( Tools.mergeHashes(cur_proc, cur_file) );
		
		snapshot.files.list = files;
		callback();
		
	}); // cp.exec
};
```

## File: `package.json`
```json
{
	"name": "performa-satellite",
	"version": "1.1.6",
	"description": "Remote data collector for Performa.",
	"author": "Joseph Huckaby <jhuckaby@gmail.com>",
	"homepage": "https://github.com/jhuckaby/performa-satellite",
	"license": "MIT",
	"main": "index.js",
	"bin": "index.js",
	"repository": {
		"type": "git",
		"url": "https://github.com/jhuckaby/performa-satellite"
	},
	"bugs": {
		"url": "https://github.com/jhuckaby/performa-satellite/issues"
	},
	"keywords": [
		"performa"
	],
	"scripts": {
		"package": "mkdir -p dist && pkg --compress GZip ."
	},
	"pkg": {
		"targets": [ "node18-linux-x64", "node18-linux-arm64", "node18-macos-x64", "node18-macos-arm64" ],
    	"outputPath": "dist"
	},
	"dependencies": {
		"pixl-cli": "^1.0.0",
		"pixl-request": "^2.0.0",
		"pixl-xml": "^1.0.0",
		"systeminformation": "4.34.11",
		"shell-quote": "1.7.3"
	},
	"devDependencies": {
		"pkg": "5.8.1"
	}
}
```


---
id: mscdex-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:09.928708
---

# KNOWLEDGE EXTRACT: mscdex
> **Extracted on:** 2026-03-30 17:43:07
> **Source:** mscdex

---

## File: `node-imap.md`
```markdown
# 📦 mscdex/node-imap [🔖 PENDING/APPROVE]
🔗 https://github.com/mscdex/node-imap


## Meta
- **Stars:** ⭐ 2228 | **Forks:** 🍴 387
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
An IMAP client module for node.js.

## README (trích đầu)
```
Description
===========

node-imap is an IMAP client module for [node.js](http://nodejs.org/).

This module does not perform any magic such as auto-decoding of messages/attachments or parsing of email addresses (node-imap leaves all mail header values as-is).

An upgrade guide from node-imap v0.7.x to v0.8.x can be found [here](https://github.com/mscdex/node-imap/wiki/API-changes-between-v0.7-and-v0.8).


Requirements
============

* [node.js](http://nodejs.org/) -- v10.0.0 or newer

* An IMAP server to connect to -- tested with gmail


Installation
============

    npm install imap

Examples
========

* Fetch the 'date', 'from', 'to', 'subject' message headers and the message structure of the first 3 messages in the Inbox:

```javascript
var Imap = require('imap'),
    inspect = require('util').inspect;

var imap = new Imap({
  user: 'mygmailname@gmail.com',
  PASSWORD='[REDACTED_PASSWORD]',
  host: 'imap.gmail.com',
  port: 993,
  tls: true
});

function openInbox(cb) {
  imap.openBox('INBOX', true, cb);
}

imap.once('ready', function() {
  openInbox(function(err, box) {
    if (err) throw err;
    var f = imap.seq.fetch('1:3', {
      bodies: 'HEADER.FIELDS (FROM TO SUBJECT DATE)',
      struct: true
    });
    f.on('message', function(msg, seqno) {
      console.log('Message #%d', seqno);
      var prefix = '(#' + seqno + ') ';
      msg.on('body', function(stream, info) {
        var buffer = '';
        stream.on('data', function(chunk) {
          buffer += chunk.toString('utf8');
        });
        stream.once('end', function() {
          console.log(prefix + 'Parsed header: %s', inspect(Imap.parseHeader(buffer)));
        });
      });
      msg.once('attributes', function(attrs) {
        console.log(prefix + 'Attributes: %s', inspect(attrs, false, 8));
      });
      msg.once('end', function() {
        console.log(prefix + 'Finished');
      });
    });
    f.once('error', function(err) {
      console.log('Fetch error: ' + err);
    });
    f.once('end', function() {
      console.log('Done fetching all messages!');
      imap.end();
    });
  });
});

imap.once('error', function(err) {
  console.log(err);
});

imap.once('end', function() {
  console.log('Connection ended');
});

imap.connect();
```

* Retrieve the 'from' header and buffer the entire body of the newest message:

```javascript
// using the functions and variables already defined in the first example ...

openInbox(function(err, box) {
  if (err) throw err;
  var f = imap.seq.fetch(box.messages.total + ':*', { bodies: ['HEADER.FIELDS (FROM)','TEXT'] });
  f.on('message', function(msg, seqno) {
    console.log('Message #%d', seqno);
    var prefix = '(#' + seqno + ') ';
    msg.on('body', function(stream, info) {
      if (info.which === 'TEXT')
        console.log(prefix + 'Body [%s] found, %d total bytes', inspect(info.which), info.size);
      var buffer = '', count = 0;
      stream.on('data', function(chunk) {
        count += chunk.length;
        buffer += chun
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


---
layout: post
title: Offline First
slug: offline-first
lang: en
author: Martin Thoma
date: 2020-04-25 20:00
category: My bits and bytes
tags: Web Development, Software Architecture, Software Engineering
featured_image: logos/star.png
status: draft
---
Most web applications treat the network as always available. When the train
enters a tunnel, the app shows a spinner, then an error, and whatever you just
typed is gone. *Offline first* turns this around: the application is built so
that it works without a connection, and the network is used to synchronize when
it is there.

The idea is old for native apps (an email client always kept a local copy of
your mailbox), but for web applications it became practical only when browsers
got the building blocks for it.


## Why it matters

* **Unreliable connections are normal.** Trains, elevators, basements, rural
  areas, overloaded conference Wi-Fi, flight mode. "Offline" is not the edge
  case, "slow and flaky" is the common one.
* **Speed.** If the data is already on the device, the app shows it
  immediately. Every request to the server is a request the user waits for.
* **No lost work.** Input is stored locally first, so a failed request doesn't
  throw away what the user typed.
* **Less load on the server.** Static assets and data that didn't change are
  served from the local cache.


## The building blocks

<dl>
    <dt>Service Worker</dt>
    <dd>A script that the browser runs in the background, between the web
    application and the network. It can intercept requests and answer them from
    a cache. This is what makes a web application load without a connection
    (<a href="https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API">MDN</a>).</dd>
    <dt>Cache API</dt>
    <dd>Storage for request/response pairs. The service worker puts the HTML,
    CSS, JavaScript and images of the application into it when it is
    installed.</dd>
    <dt>IndexedDB</dt>
    <dd>A database in the browser for structured data, for example the
    documents, messages or to-do items of the user
    (<a href="https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API">MDN</a>).</dd>
    <dt>Background Sync</dt>
    <dd>Lets the service worker retry sending data once the connection is back,
    even if the user already closed the tab
    (<a href="https://developer.mozilla.org/en-US/docs/Web/API/Background_Synchronization_API">MDN</a>;
    not supported by all browsers).</dd>
</dl>

A typical caching strategy for the application shell is *cache first*: answer
from the cache, fall back to the network. For data, *network first* or
*stale-while-revalidate* is more common: show the cached version immediately,
fetch the new one in the background and update the view when it arrives.


## The hard part: synchronization

Reading offline is easy. Writing offline is where it gets interesting, because
two devices can change the same data while they can't talk to each other.
When they reconnect, someone has to decide what the result is:

* **Last write wins.** The newest change overwrites the older one. Simple, but
  it silently loses data.
* **Ask the user.** Show both versions and let the user merge them. Correct, but
  annoying if it happens often.
* **Merge automatically.** For many data types there are merge rules that always
  work, for example adding items to a set or appending to a list.
  [Conflict-free replicated data types (CRDTs)](https://crdt.tech/) generalize
  this: every replica can be changed independently, and all replicas end up in
  the same state once they have seen the same changes.

Libraries take a lot of this work away. [PouchDB](https://pouchdb.com/) stores
data in the browser and synchronizes it with a CouchDB server; Automerge and
Yjs are CRDT libraries for collaborative documents.

The essay [Local-first software](https://www.inkandswitch.com/local-first/) by
Ink & Switch takes the idea further: the data lives primarily on the user's
devices, the server is only a helper for syncing and backup.


## Design for it

Offline first is also a user-interface question:

* Show the state honestly: "saved on this device", "synchronized", "offline".
* Don't block input while a request is running.
* Queue actions instead of rejecting them, and tell the user if one fails
  permanently.
* Decide early which features really need the server (payments, searching data
  that isn't on the device) and make them fail gracefully.


## See also

* [alistapart.com/article/offline-first](https://alistapart.com/article/offline-first/)
* [offlinefirst.org](http://offlinefirst.org/)
* [itstillworks.com/build-own-website-offline-676922…](https://itstillworks.com/build-own-website-offline-6769224.html)

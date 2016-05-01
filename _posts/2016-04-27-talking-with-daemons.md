---
layout: post
title: Talking with Daemons
author: Martin Thoma
date: 2016-04-27 23:26
category: Programming
tags: Python, RPC, daemon
featured_image: logos/daemon.png
---
Everybody knows that training big machine learning models takes a lot of
computing power. However, it takes much less computing power to evaluate the
model for a single instance. One important factor when measuring the time
of a program which only runs one image classification is the time for loading
the model itself. Only the reading / structuring of the computational graph.
We don't want to load the model often.

One possible way around this is making a web service. The user connects to it,
uploads an image and gets the result. But the model is loaded all the time and
the web service is running all the time.

One problem with this approach is that you might want to work on the web
interface and not having to reload the machine learning part all the time. I
also think this might be one of the most inefficient ways to realize
<abbr title="inter process communication">IPC</abbr>.

Today, it came to my mind that there might be a cleaner approach. I thought
about creating a daemon and using RPCs.

**Credits to [codeape](http://stackoverflow.com/a/658156/562769). He provided the basis for the examples below.**


## RPC basics

RPC is short for <i>remote procedure call</i>. It is a call to a function which
is not in the same address space as the calling function. So basically code in
program A calls code from program B.

In Python, this is actually pretty easy to use with
[Pyro](https://pythonhosted.org/Pyro4/).


## Server

Create a file `summon_daemon.py`:

```python
#!/usr/bin/env python

"""The server."""

import Pyro.core


class Bartimaeus(Pyro.core.ObjBase):
    """The called class."""

    def __init__(self):
        """Constructor."""
        Pyro.core.ObjBase.__init__(self)
        self.counter = 0

    def count(self, up):
        """Count up."""
        self.counter += up
        return "I was called {count} times.".format(count=self.counter)

Pyro.core.initServer()
daemon = Pyro.core.Daemon()
uri = daemon.connect(Bartimaeus(), "bartid")

print("The daemon runs on port: {port}".format(port=daemon.port))
print("The object's uri is: {uri}".format(uri=uri))

daemon.requestLoop()
```

## Client

And a `call_daemon.py`:

```python
#!/usr/bin/env python

"""Talk with the daemon."""

import Pyro.core

# you have to change the URI below to match your own host/port.
bartimaeus = Pyro.core.getProxyForURI("PYROLOC://localhost:7766/bartid")

print(bartimaeus.count(1))
```


## Timing

I was interested how fast this is locally. So I made a tiny test:

Server (`summon_daemon.py`):

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The server."""

import logging
import sys
import Pyro.core

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG,
                    stream=sys.stdout)


class Bartimaeus(Pyro.core.ObjBase):
    """The called class."""

    def __init__(self):
        """Constructor."""
        Pyro.core.ObjBase.__init__(self)
        self.counter = 0

    def count(self, up):
        """Count up."""
        logging.info("new up: %i", up)
        self.counter += up
        return "I was called {count} times.".format(count=self.counter)

Pyro.core.initServer()
daemon = Pyro.core.Daemon()
uri = daemon.connect(Bartimaeus(), "bartid")

print("The daemon runs on port: {port}".format(port=daemon.port))
print("The object's uri is: {uri}".format(uri=uri))

daemon.requestLoop()
```


Client (`call_daemon.py`):

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Talk with the daemon."""

import logging
import sys
import Pyro.core

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG,
                    stream=sys.stdout)


def main(up):
    """Do something with bartimaeus - who lives in another realm."""
    # you have to change the URI below to match your own host/port.
    logging.info("Send up: %i", up)
    bartimaeus = Pyro.core.getProxyForURI("PYROLOC://localhost:7766/bartid")
    print(bartimaeus.count(up))


def get_parser():
    """Get parser object for call_demon.py."""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-n",
                        dest="up",
                        default=1,
                        type=int,
                        help="count up")
    return parser


if __name__ == "__main__":
    args = get_parser().parse_args()
    main(args.up)

```

resulting in about 0.004s from sending to receiving.

{% caption align="aligncenter" width="500" alt="About 0.004s from sending to receiving" text="About 0.004s from sending to receiving" url="../images/2016/04/daemon.png" %}


## A small chat

You could implement a very simple chat with this. I only have version 3.16 of
[Pyro](https://pythonhosted.org/Pyro4/) which seems not to have
[callbacks](https://pythonhosted.org/Pyro4/clientcode.html#pyro-callbacks) so
that the server can inform the client when a new message is there. This means
the following toy implementation expects the user to send messages to receive
the current ones. Not nice, but I just wanted to give it a try:

Server:

```python
#!/usr/bin/env python

"""A chat server."""

import Pyro.core


class Chat(Pyro.core.ObjBase):
    """The called class."""

    def __init__(self):
        """Constructor."""
        Pyro.core.ObjBase.__init__(self)
        self.msgs = []
        self.clients = []

    def receive(self, sender, msg, last_msg):
        """Receive a message."""
        self.msgs.append((sender, msg))
        print("[{sender}] {msg}".format(sender=sender, msg=msg))
        return (self.msgs[last_msg:], len(self.msgs))

Pyro.core.initServer()
daemon = Pyro.core.Daemon()
uri = daemon.connect(Chat(), "chat")

print("The daemon runs on port: {port}".format(port=daemon.port))
print("The object's uri is: {uri}".format(uri=uri))

daemon.requestLoop()
```

Client:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A chat client."""

import logging
import sys
import Pyro.core

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG,
                    stream=sys.stdout)


def main(server, name):
    """Run the chat."""
    chat_server = Pyro.core.getProxyForURI(server)
    last_msg_id = 0
    print("*"*80)
    print("* Chat started. You are called '{name}'.".format(name=name))
    print("*"*80)
    while True:
        msg = raw_input()
        new_msgs, last_msg_id = chat_server.receive(name, msg, last_msg_id)
        for sender, msg in new_msgs:
            print("[{sender}] {msg}".format(sender=sender, msg=msg))


def get_parser():
    """Get parser object for chat_client.py."""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("--server",
                        dest="server",
                        required=True,
                        help="starts with PYRO://")
    parser.add_argument("--name",
                        required=True,
                        help="what others see")
    return parser


if __name__ == "__main__":
    args = get_parser().parse_args()
    main(args.server, args.name)

```


## Daemons

A [daemon](https://en.wikipedia.org/wiki/Daemon_(computing)) is a computer
program that runs as a background process, rather than being under the direct
control of an interactive user.

You can [create a simple daemon](http://stackoverflow.com/a/16420140/562769),
too.


## See also

* [Web Service for IPC: Pros and Cons?](https://www.reddit.com/r/learnprogramming/comments/4gq8mn/web_service_for_ipc_pros_and_cons/)
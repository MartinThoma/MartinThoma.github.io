---
layout: post
title: JavaScript development
author: Martin Thoma
date: 2014-02-17
categories:
- Code
tags:
- JavaScript
- development
- best practice
featured_image:
---
The possibilities you have today with JavaScript are fantastic. It's not even
close to what you could do with JS in 2005. The speed increased A LOT and hence
programs got more complex. Hence developers had the need to make development 
easier.

## Node Package Manager
One way to speed up development is using the node package manager (short: npm). It allows
you to install JavaScript libraries. I'd say it is comparable to Rubys `gem` 
command.

### Installation
Unfortunately, the npm version in the debian repositories is quite outdated. So
you should install it yourself like this:

Clone the Git repository. This is about 75 MB:

```bash
git clone https://github.com/joyent/node.git
cd node
```

Compile and install npm. That took about 5 minutes for me:

```bash
./configure
make
sudo make install
```

Check if everything went fine:

```bash
node -v
```

### Usage

The command 

```bash
sudo npm install jslint -g
```

will install `jslint` globally.

## JSLint
A code linter is marks code that might be wrong. It's not only syntax checking,
but also checking for code smell. The name "linter" comes from "lint" which
was a program that flagged non-portable constructs in C-code ([source](https://en.wikipedia.org/wiki/Lint_(software))).

It can be installed like this

```bash
npm install jslint
```

An alternative is jshint.

## Sublime Text

### Shortcuts
* <kbd>Ctrl</kbd> + <kbd>r</kbd>: Get a function list

### Packages
* DocBlockr: Simply type `/**` and press <kbd>Enter</kbd> to get a nice template
  for JavaDocs :-)

## Weblinks
* [jshint.com](http://www.jshint.com/about/)
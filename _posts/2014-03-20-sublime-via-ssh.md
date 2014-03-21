---
layout: post
title: How to use Sublime Text via SSH
author: Martin Thoma
date: 2014-03-20 21:09
categories:
- Code
tags:
- Sublime Text
- SSH
featured_image: logos/sublime-text.png
---

Sublime Text is the best editor I have ever used. One argument for vim and against
SSH could be that you can't simply use Sublime Text when you're accessing a
computer via SSH. But there is a way!

In the following, I will expain the simplest way how to remote edit files with
Sublime Text.

## Preparation on your computer

<ol>
    <li>Install and start Sublime Text.</li>
    <li>Install the <code>rsub</code> package via Package Controll.</li>
    <li>Open <code>~/.ssh/config</code>. Create it if id does not exist yet. Add 
        the code from below.</li>
    <li>Start SSH with <code>ssh myname</code>.</li>
</ol>

This is how the `config` file should look like:

```text
Host myname
  Hostname pc123.your.network.com
  RemoteForward 52698 127.0.0.1:52698
```

 You can add more information like `User yourusername` to this file.

## Server-Side steps

<ol start="5">
    <li>Download the <code>rmate</code> script:<br/>
<code>curl https://raw.github.com/aurora/rmate/master/rmate &gt; rmate</code>
    </li>
    <li>Execute <code>./rmate yourfile</code>. It will open in your local Sublime Text!</li>
</ol>

## Improvements

These steps have to be done server-side.

### With Root access
It's not so nice to open files with `~/rmate filename` all the time. You can
use `rmate filename` after executing this command:

```bash
# This creates a symlink
sudo ln -s ~/rmate /usr/local/bin/
```

You can use other paths than `/usr/local/bin/`. Look at your `PATH` for candidates:

```bash
echo $PATH
```

### Without Root access
When you don't have root access, you can't create a symlink for most (eventually even all)
folders in your `PATH`. But you can expand your `PATH`:

```bash
mkdir -p ~/bin        # create folder if it doesn't exist
ln -s ~/rmate ~/bin/  # create symlink
```

Now expand your `PATH` so that it includes `~/bin`. There are at least two ways
to do so:

* You can directly edit your shells `.rc` file (e. g. `.bashrc`, `.zshrc`, `.cshrc`, ...) or
* you can edit your `.profile`

As many shells source `.profile` I'll explain this way. First, open `~/.profile`.
Then add

```bash
# First check if that folder exists
if [ -d "$HOME/bin" ] ; then
    # Add your home folder to the end of the current path
    PATH="$PATH:$HOME/bin"
fi
```

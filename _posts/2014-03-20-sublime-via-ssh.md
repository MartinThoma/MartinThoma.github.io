---
layout: post
title: How to use Sublime Text via SSH
author: Martin Thoma
date: 2014-03-20 21:09
categories:
- Code
tags:
- Sublime Text
featured_image: logos/sublime-text.png
---

Sublime Text is the best editor I have ever used. One argument for vim and against
SSH could be that you can't simply use Sublime Text when you're accessing a
computer via SSH. But there is a way!

In the following, I will expain the simplest way how to remote edit files with
Sublime Text.

## Preparation on your computer

1. Install and start Sublime Text
2. Open `~/.ssh/config`. Create it if id does not exist yet. Add this:

```text
Host myname
  Hostname pc123.your.network.com
  User mthoma
  RemoteForward 52698 127.0.0.1:52698
```

You can add more information like `User yourusername`.

3. Start SSH with `ssh myname`.

## Server-Side steps

4. Download the `rmate` script:

```bash
curl https://raw.github.com/aurora/rmate/master/rmate > rmate
```

5. Execute `./rmate yourfile`. It will open in your local Sublime Text!
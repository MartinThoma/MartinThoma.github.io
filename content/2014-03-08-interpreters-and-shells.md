---
layout: post
title: Interpreters and Shells
author: Martin Thoma
date: 2014-03-08 11:49
category: Code
tags: Shell
featured_image: 2011/09/Gnome-Terminal.png
---
Should you ever be in the position to write a shell or interpreter I hope you
will make sure the following things work. Take it as a quality guide. They
are ordered by level of importance. The first thing is the most basic one that
has to work, the last one is less necessary, but much cooler if you support it.

In the following, I'll only talk about shells. But most of it will also apply 
to interpreters.

## Level 0: Robustness
A shell has to be robust. Users rely on it when GUI doesn't work. This means
it should definitely not fail. Never.

And just to make sure that you get me correct. Commands get "Entered". So the
user pushes "enter" when he wants something to happen. Everything the shell does
meanwhile should not change the system (except for shell-related stuff) and not
be able to slow down / crash the system.

## Level 1: Speed
I expect a shell to start without recognizable delay. I'm not too sure how fast 'without recognizable delay' means. In the most extreme case it would be about 1/100 of a second, because when monitors have 100Hz they are said to be flicker free. You could not even see that. But I think it is not necessary.

Another measure would be reaction time. I've just did an online test and saw that
my reaction time is about 0.2 seconds. So a shell should be ready for user input
after this time.

## Level 2: Left / Right arrow keys
When I enter a command, it happens that I forget something. In this case I want
to be able to navigate with left / right arrow keys through the console.

## Level 3: History with up / down arrow keys
When you use the up-array, you should get the last command you've entered.
When you press it twice, you get the second last command...
So the shell should save your last commands in a so called "history". This 
history should be at least

## Level 4: Customization
* Promt
* History length

## Level 5: Path autocompletion
The path should autocomplete when you hit <kbd>Tab</kbd>. The autocomplete should
work as follows:

1. The autocomplete should never get farer than one folder.
2. If there are multiple possibilities to autocomplete, then it should only
  autocomplete what is in common. After a second <kbd>Tab</kbd> it should display
  the possibilities and after a third <kbd>Tab</kbd> the shell should go to the
  first possibility so that you can hit enter to use this possibility.

## Level 6: Command autocompletion
The autocomplete function should also complete commands.

## Level 7: Fuzzy autocompletion
When you make a typo in a path and hit <kbd>Tab</kbd> the shell should correct
the typo if possible.

## Additional stuff
Some stuff is nice to have, but not really essential:

* Some default commands like `help`, `time`, `pwd`, `cd` and `echo`.
* <kbd>Ctrl</kbd> + <kbd>D</kbd> as a shortcut for exiting.
* <kbd>Ctrl</kbd> + <kbd>C</kbd> should stop the current command.
* The configuration file should be stored in the home folder of the user and it should be called `.[name]rc`. The dot makes the file invisible by convention and 'rc' means 'resource configuration'.
* The prompt configuration should be easy. Some patterns that are used quite often are 
  * `\w` for the working directory, where `$HOME` gets abbreviated with `~`
  * `\u` the username
  * `\h` the hostname
  * Using colors for different parts
* Navigation with <kbd>Pos 1</kbd> and <kbd>End</kbd> should work.

## Ranking
Here is how some shells rank. Please note, that it's very difficult to check
if a shell is robust. :

**Level 0**: Windows XP / Windows 7 default shell; Windows Power shell<br/>
The shell is too slow. I don't know if this is still a problem in Windows 8, but
I guess so.

The `scala` interactive interpreter is slow.

**Level 1**: `csh` prints "^[[D" when I press the left arrow and "^[[C" when 
I press the right arrow. When I press <kbd>Tab</kbd> it only prints tab. What
a crap.

**Level 3**: `python` seems to have possibilities to execute arbitrary python code at
startup by specifying the environment variable `PYTHONSTARTUP`, but somehow this
does not work on my system.<br/>
However, customizing the prompt is fairly easy:

```python
import sys

sys.ps1 = "-->"
```

**Level 4**: `GHCi`, a Haskell compiler, has mastered level 4. The prompt can be
configured via `~/.ghci` by adding `:set prompt "ghci> "`.

If you want to show the current path, you can do it like this ([source](http://stackoverflow.com/a/11263118/562769)):

```haskell
let cur fill = do { cwd <- System.Directory.getCurrentDirectory; return (":set prompt \"" ++ cwd ++ fill ++ " \""); }
:def doprompt (\_ -> cur ">")
:def mycd (\dir -> System.Directory.setCurrentDirectory dir >> cur ">")
:doprompt
```

**Level 4.5**: `bash` is robust, takes about 0.11 seconds to start, has a history of 
500 lines as you can verify with `echo $HISTSIZE`, is customizable with `.bashrc`.

`tcsh` takes about 0.02 seconds to start, has a default history size of 100 lines
as you can verify with `echo $history`, is customizable with `.tcshrc` and `.cshrc`.

Rubys interactive interpreter `irb` seems to be fast enough, has a history,
the prompt can be configured in `~/.riplrc` ([source](http://stackoverflow.com/a/6097629/562769)). I don't know if the history length is limited and can be adjusted.

All shells in this level have path autocompletion as described in 5.1, but do not have autocompletion as described in 5.2.

**Level 7**: ZSH is the best shell I have ever used. Especially with [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh).

## Additional resources
* [How to change your shell prompt](http://www.understudy.net/custom.html):
  A list of files and commands that might be useful.

---
layout: post
title: Install and configure computer
author: Martin Thoma
date: 2014-01-25 10:14
categories:
- Cyberculture
tags:
- Linux
featured_image: 2011/11/computer-fix-it-guy.jpg
---
When I reinstall my computer, I usually do these following steps:

1. Copy all data to an external HDD
2. Write down all WLAN configurations (eventually with screenshots; NOT ONLY PASSWORDS!)
3. Write down all programs that I use.
  1. Export configuration of those programs.
4. Wait a week or a month and see if someting is missing in the lists from above.
5. Drop the old system and install a new one

## Software I usually install ##
If possible, I will give the debian package names in the following list:

* [LaTeX](../how-to-install-the-latest-latex-version/) and scientific writing
  * [`jabref`](http://martin-thoma.com/reference-management-with-jabref/): A reference manager
  * `gnuplot`
  * `pdf2svg`
  * `aspell` and `aspell-de`
* [Google Chrome](https://www.google.com/intl/de/chrome/browser/)
* Multimedia
  * [`vlc`](http://www.videolan.org/vlc/): A very good DVD player
  * [OnlineTvRecorder](http://wiki.ubuntuusers.de/OnlineTvRecorder) and especially [OTR-Verwaltung](http://wiki.ubuntuusers.de/OTR-Verwaltung)
     * `avidemux wine mplayer`
  * `sudo add-apt-repository ppa:clipgrab-team && sudo apt-get update && sudo apt-get install clipgrab`
* Graphics
  * [`gimp`](http://www.gimp.org/)
  * [`inkscape`](http://www.inkscape.org/)
  * `dia`
  * [`imagemagick`](http://www.imagemagick.org/script/index.php)
  * `pdf2svg librsvg2-bin`
* Programming
  * `vim`
  * `python python3 python-numpy python-setuptools python-mysqldb`
  * `ruby ruby-sqlite3 ruby-mysql`
  * `gcc g++ cmake build-essential`
  * OpenGL: `xorg-dev libglu1-mesa-dev freeglut3 freeglut3-dev libglew1.5 libglew1.5-dev libglu1-mesa libglu1-mesa-dev libgl1-mesa-glx libgl1-mesa-dev`
  * `apache2 php5 php5-mysql`
  * `zsh` and [Oh-my-zsh](../working-terminal/)
  * `eclipse`
  * `sqlitebrowser`
  * `tcl`
  * `phpmyadmin selfhtml`
  * `meld diffpdf`
  * [`virtualbox`](https://wiki.ubuntuusers.de/virtualbox)
* Themes
  * Balazan-Theme from [bisigi-project](http://www.bisigi-project.org/?page_id=8&lang=en) (simply download it.)
* Other
  * [`sublime_text`](http://martin-thoma.com/sublime-text/)
  * `libreoffice`
  * `curl`
* DRM-caused (I want to watch DVDs!)
  * `ubuntu-restricted-extras libdvd-pkg libdvdread4 libdvdnav4`, then run
    `sudo dpkg-reconfigure libdvd-pkg`
  * `totem banshee mplayer rythmbox`

## Configure ##

### Set standards

```bash
update-alternatives --config editor
update-alternatives --config x-www-browser
```

### MATE

See [issues/262](https://github.com/mate-desktop/caja/issues/262):

```bash
mv ~/.config/gtk-3.0/bookmarks ~/.config/gtk-3.0/bookmarks-backup
ln -s ~/.gtk-bookmarks ~/.config/gtk-3.0/bookmarks
```

### GUI

I like the old menu bar quite a lot. It opens instantly and is customizable:


{% caption align="aligncenter" width="500" alt="Old menu bar" text="Old menu bar" url="../images/2014/03/mate-old-menu.png" %}

You can get it back in MATE by doing a right-click on the menu. Then click on
"add to panel":

{% caption align="aligncenter" width="287" alt="Add to panel" text="Add to panel" url="../images/2014/03/mate-add-to-panel.png" %}

After that, the following dialog will pop up. Choose "Menu Bar"

{% caption align="aligncenter" width="500" alt="Add menu bar" text="Add menu bar" url="../images/2014/03/mate-add-menu-bar.png" %}

### DRM-Stuff ###
```bash
sudo /usr/share/doc/libdvdread4/install-css.sh
sudo regionset #use that with caution
```

### dotfiles ###
See [github.com/MartinThoma/dotfiles](https://github.com/MartinThoma/dotfiles).

## Data
Download / copy all data back from GitHub / external HDDs to my internal HDD.
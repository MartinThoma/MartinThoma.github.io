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

* [LaTeX](../how-to-install-the-latest-latex-version/)
  * gnuplot
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
* Programming
  * `vim`
  * `python python3 python-numpy python-setuptools python-mysqldb`
  * `ruby ruby-sqlite3 ruby-mysql`
  * `gcc g++`
  * `apache2 php5 php5-mysql`
  * `zsh` and [Oh-my-zsh](../working-terminal/)
  * `eclipse`
  * `sqlitebrowser`
  * `tcl`
  * `phpmyadmin selfhtml`
  * `meld diffpdf`
* Themes
  * Balazan-Theme from [bisigi-project](http://www.bisigi-project.org/?page_id=8&lang=en)
  * `sudo add-apt-repository ppa:bisigi && sudo apt-get update`
  * `sudo apt-get install bisigi-themes`
  * `sudo apt-get install balanzan-theme`
* Other
  * [`sublime_text`](http://martin-thoma.com/sublime-text/)
  * `libreoffice`
  * `curl`
* DRM-caused (I want to watch DVDs!)
  * `ubuntu-restricted-extras libdvdcss2 libdvdread4 libdvdnav4 w32codecs`
  * `totem banshee mplayer rythmbox`

## Configure ##

### Set standards

```bash
update-alternatives --config editor
update-alternatives --config x-www-browser
```

### GUI

I like the old menu bar quite a lot. It opens instantly and is customizable:


{% caption align="aligncenter" width="500" alt="Old menu bar" text="Old menu bar" url="../images/2014/03/mate-old-menu.png" %}

You can get it back in MATE by doing a right-click on the menu. Then click on
"add to panel":

{% caption align="aligncenter" width="500" alt="Add to panel" text="Add to panel" url="../images/2014/03/mate-add-to-panel.png" %}

After that, the following dialog will pop up. Choose "Menu Bar"

{% caption align="aligncenter" width="500" alt="Add menu bar" text="Add menu bar" url="../images/2014/03/mate-add-menu-bar.png" %}

### DRM-Stuff ###
```bash
sudo /usr/share/doc/libdvdread4/install-css.sh
sudo regionset #use that with caution
```

### vim ###
.vimrc:

```vim
set t_Co=256
set shell=bash
set shellquote= 
set shellxquote= 
set noshelltemp 

syntax on	" enable syntax highlighting
filetype on	" enable file type detection
colorscheme default

" Set some nice character listings, then activate list
set list listchars=tab:⟶\ ,trail:·,extends:>,precedes:<,nbsp:%
set list

" 1 tab == 4 spaces
set shiftwidth=4
set tabstop=4
set expandtab " use spaces instead of tabs
autocmd FileType make setlocal noexpandtab " Makefiles always need tabs

set number " turn on line numbers
set showmatch " show matching brackets

" Highlight current line
set cursorline
" hi CursorLine cterm=NONE ctermbg=187

" Show when lines get too long
set textwidth=80
set colorcolumn=+1
highlight OverLength ctermbg=red ctermfg=white guibg=#592929
match OverLength /\%81v.\+/

set autoindent " keep intendation level

hi SpecialKey   ctermfg=white    ctermbg=none       cterm=none " make tab sign grey

" highlight LineNr ctermfg=0 ctermbg=187
set statusline+=%F " Add full file path to your existing statusline
set laststatus=2

" execute make
map <C-m> :make
autocmd BufWritePost *.cpp execute '!astyle --style=java --indent=spaces %'
```

### Git ###
.gitconfig

```text
[user]
	name = Martin Thoma
	email = info@martin-thoma.de
[diff]
	external = git-meld

[diff "pdfdiff"]
	command = diffpdf

[core]
	attributesfile = ~/.gitattributes
```

.gitattributes

```text
*.pdf diff=pdfdiff
```

## Data
Download / copy all data back from GitHub / external HDDs to my internal HDD.
---
layout: post
title: Git Bundle
slug: git-bundle
author: Martin Thoma
date: 2017-04-02 20:00
category: Code
tags: git
featured_image: logos/git.png
---

Sometimes you need to share code via E-Mail / stick. If the code you need to
share is a git repository, creating a bundle is a pretty good way to do it.


You can create a bundle with

```
$ git bundle create repository-name.bundle --all
```

Then you can restore the repository by cloning:

```
$ git clone repository-name.bundle
```

You can also use a bundle as a remote. Hence

```
$ git fetch origin
$ git pull
```


## Docs

* [git-scm.com/docs/git-bundle](https://git-scm.com/docs/git-bundle)
* [How to use git-bundle for keeping development in sync?](http://stackoverflow.com/q/3635952/562769)

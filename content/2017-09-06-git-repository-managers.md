---
layout: post
title: Git Repository Managers
slug: git-repository-managers
author: Martin Thoma
status: draft
date: 2017-09-06 20:00
category: Code
tags: git, repository, Gitlab
featured_image: logos/git.png
---
Git is likely todays most important version control system. It is used for
Linux, actively developed and stable.


## Git Basics

Git is a decentralized version control system. This means has interesting
implications on your workflow:

* You can commit locally. It doesn't matter if you are online or offline as git
  is on your local machine.
* The maintainance of the "main" code base is only convention. This comes from
  the OpenSource world where you might want to fork a project.
* You can have multiple branches of code. You usually have the `master` which
  should be relatively stable and several feature branches. As soon as a
  feature is ready it can be merged into the master. This keeps keeps the
  version history of the master cleaner as it is possible that you might go
  back and decide not to include a feature.

See [Pro Git](https://git-scm.com/book/en/v2) for more information.


## Repository Managers

Although you don't necessarily need anything else, a repositry manager is
helpful for collaborative development. You want others in your organization be
able to easily **find**, **comment** and **contribute** to your codebase.

Without a repository manager, others have to know that your project exits.
You can comment and contribute via e-mail. For example, [`git bundle`](https://git-scm.com/docs/git-bundle) allows you to
share complete repositories, but you can also [share patches with git](https://www.devroom.io/2009/10/26/how-to-create-and-apply-a-patch-with-git/).

<table class="table">
    <tr>
        <th></th>
        <th>GitLab</th>
        <th><a href="https://en.wikipedia.org/wiki/Bitbucket_Server_(software)">Bitbucket Server</a></th>
        <th>Gogs</th>
        <th>Gitea</th>
    </tr>
    <tr>
        <td>Other names</td>
        <td></td>
        <td>Stash</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Comment</td>
        <td></td>
        <td></td>
        <td></td>
        <td>Fork of Gogs</td>
    </tr>
    <tr>
        <td>License</td>
        <td></td>
        <td>non-free</td>
        <td>MIT</td>
        <td></td>
    </tr>
    <tr>
        <td>On-premises vs Cloud</td>
        <td>Both</td>
        <td><a href="https://bitbucket.org/product/pricing?tab=host-in-the-cloud">Both</a></td>
        <td>on-premises</td>
        <td>on-premises</td>
    </tr>
    <tr>
        <td>Source</td>
        <td><a href="https://github.com/gitlabhq/gitlabhq">github.com/gitlabhq</a></td>
        <td>?</td>
        <td><a href="https://github.com/gogits/gogs">github.com/gogits</a></td>
        <td><a href="https://github.com/go-gitea/gitea">github.com/go-gitea</a></td>
    </tr>
    <tr>
        <td>Written in</td>
        <td>Ruby + Go</td>
        <td>Java</td>
        <td>Go</td>
        <td>Go</td>
    </tr>
    <tr>
        <td>Last change</td>
        <td></td>
        <td>2017-08-24</td>
        <td>2017-08-16</td>
        <td>2017-09-05</td>
    </tr>
    <tr>
        <td>Developers</td>
        <td>GitLab Inc.</td>
        <td>Atlassian Inc.</td>
        <td>2 project members</td>
        <td>18 maintainers</td>
    </tr>
    <tr>
        <td>Github Stars</td>
        <td>19790</td>
        <td>-</td>
        <td>20717</td>
        <td>3505</td>
    </tr>
    <tr>
        <td>Github Forks</td>
        <td>5281</td>
        <td>-</td>
        <td>2393</td>
        <td>376</td>
    </tr>
    <tr>
        <td>Open Github Issues</td>
        <td><a href="https://gitlab.com/gitlab-org/gitlab-ce/issues">8830</a></td>
        <td>-</td>
        <td>496</td>
        <td>447</td>
    </tr>
    <tr>
        <td>Contributors</td>
        <td>1360</td>
        <td>-</td>
        <td>346</td>
        <td>364</td>
    </tr>
    <tr>
        <td>Minimum Hardware requirements</td>
        <td>?</td>
        <td>?</td>
        <td>Raspberry Pi</td>
        <td>Raspberry Pi</td>
    </tr>
    <tr>
        <td>Issue Tracker</td>
        <td>?</td>
        <td>?</td>
        <td>?</td>
        <td>?</td>
    </tr>
    <tr>
        <td>Pull Requests</td>
        <td>?</td>
        <td>?</td>
        <td>?</td>
        <td>?</td>
    </tr>
    <tr>
        <td>Wiki</td>
        <td>?</td>
        <td>?</td>
        <td>?</td>
        <td>?</td>
    </tr>
    <tr>
        <td><a href="https://git-lfs.github.com/">Git LFS</a></td>
        <td>?</td>
        <td>?</td>
        <td>?</td>
        <td>?</td>
    </tr>
    <tr>
        <td><a href="https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol">LDAP</a></td>
        <td>Yes</td>
        <td>?</td>
        <td>?</td>
        <td>?</td>
    </tr>
</table>


## See also

* [Gitlab vs Bitbucket Server vs Gitea vs Gogs](https://www.reddit.com/r/git/comments/6y68vr/gitlab_vs_bitbucket_server_vs_gitea_vs_gogs/)
* [GitHub Enterprise](https://enterprise.github.com/home)

---
layout: post
title: Automatic Deployment
author: Martin Thoma
date: 2014-11-22 17:19
categories:
- The Web
tags:
- Hosting
- Deployment
- GitHub
- DigitalOcean
featured_image: logos/GitHub.png
---
[write-math.com](http://write-math.com) is the web service I've build for my
bachelors thesis (see [write-math article](http://martin-thoma.com/write-math/)
for more information). It was only build to get enough training data to run
experiments. It was extended quite a lot. I've added some meta data, ways to
have a look at the data and share it. I noticed that there are a lot of wrong
labels, so I've added possibilities to fix them.

I build the web service with the knowledge I got about 9 years ago. Back in
2004, there were not so many options for web hosting. Especially if you don't
have much money (meaning I was not willing to pay more than 3 Euro/month for
web hosting - including a TLD).

Now I have much more money and there are much neater possibilites. One of them
is [DigitalOcean](https://www.digitalocean.com/?refcode=b5dd0c5d61b9). They
make it super-simple to get your own server within about 5 minutes. You pay per
minute (the cheapest one is about 5 Dollar/month - not including a TLD) and you
get SSH access. (I can recommend [namecheap](https://www.namecheap.com/) if
you need a TLD).

As I have more money and more technologies / languages, I would like to
re-write the back end of write-math. It should have a nice, clearly defined,
REST API. And it should be deployed in a better way than copying via FTP.

## The Workflow

This is the workflow I wish to have:

1. Development via GitHub. There is a master branch which should always be in
   sync with write-math.
2. Newly developed features get their own branches.
3. The master branch has to have some code quality properties:
    * PEP8 conformance, if it is written with Python
    * Tests (for example via test coverage?)
    * Documentation (enforcing docstrings / automatically building the docs
      after each commit)
4. If merging a development branch into the master would violate one of those
   quality constraints, the merge should be rejected automatically.
5. A new commit on the master should automatically trigger deployment to the
   website.
6. The version running on the website should behave exactly like my local
   version. I don't want to have issues with missing packages / libraries.


## Docker

[Docker](https://www.docker.com/) is a container format / service. You can
define what you want via a so called `Dockerfile`:

```text
FROM python
MAINTAINER Martin Thoma <info@martin-thoma.de>

RUN git clone https://github.com/MartinThoma/write-math-py.git
RUN pip install -r /write-math-py/requirements.txt

EXPOSE 5000

CMD ["/write-math-py/main.py"]
```

This file says I want an image which is based on another image called
[`python`](https://registry.hub.docker.com/_/python/). I continue with cloning
my GitHub repository, exposing port 5000 for later usage and defining which
script should be run when I want to run the container.

Using docker makes sure that I can test how my application would behave online,
without having to put it online.


## Docker Hub

Docker has a repository of images, similar to GitHub. You can have public and
private images.


## Docker-Hook

[`docker-hook`](https://github.com/schickling/docker-hook)
is a very simple script you can put on your web server to listen for new
changes. You can add a so called "web hook" to a docker image on Docker Hub.
This means Docker Hub will call the website when one image gets an update. The
`docker-hook` script simply creates a web server and waits for such a
notification. When it arrives, the web server (where `write-math` will run)
knows it needs to update its docker image. It automatically downloads the new
image, stops the old container and runs the new one.


## Conclusion

From commit to deployment in about 6 minutes. Automatically. Although I think
this should be less than a minute, it's still quite nice :-)
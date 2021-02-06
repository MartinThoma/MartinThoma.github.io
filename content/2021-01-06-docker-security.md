---
layout: post
title: Docker Security 😇
subtitle: A hands-on guide to security for Docker
slug: docker-security
url: https://levelup.gitconnected.com/docker-security-5f4df118948c
author: Martin Thoma
status: draft
date: 2021-02-06 20:00
category: Security
tags: Docker, AppSec
featured_image: logos/docker.png
---
![Photo by [Andrey Sharpilo](https://unsplash.com/@sharpiloa?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/9600/0*r4ZMVDm0J0WtgNKQ)*Photo by [Andrey Sharpilo](https://unsplash.com/@sharpiloa?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*

Most companies I have seen deploy Docker images in at least one project or service. Docker is great because it makes stuff reproducible by specifying the environment to a big degree. However, you still have to think about security. Let’s have a closer look!

## Host Security

All Docker containers run on a host system. The host needs to be secure AND the container needs to be secure.

There are various vulnerability scanning, auditing, and hardening tools for Linux systems:

* [Lynis](https://cisofy.com/lynis/): Executesudo apt-get install lynis && sudo lynis audit system and wait for a couple of minutes and you get a pretty nice report indicating what you can do to harden your system.
* [SELinux](https://en.wikipedia.org/wiki/Security-Enhanced_Linux): Provides Mandatory Access Control (MAC) as a kernel-module. Thomas Cameron gave an [introduction to SELinux](https://www.youtube.com/watch?v=_WOKRaM-HI4). The key point for SELinux and AppArmor is the Access control policy. Linux, by default, uses Discretionary Access Control (DAC). SELinux and AppArmor enforce MAC. [Learn more about the differences](https://levelup.gitconnected.com/effective-access-control-331f883cb0ff). [Luc Juggery](undefined) gave a nice introduction to [SELinux & Docker](https://medium.com/lucjuggery/docker-selinux-30-000-foot-view-30f6ef7f621).
* [AppArmor](https://en.wikipedia.org/wiki/AppArmor): Provides MAC as a service. It distinguishes unconfined and confined processes. It ignores unconfined processes. Confined processes may only do what they are allowed to do according to the AppArmor profile of that process. [Seth Arnold](http://sarnold.org/resume/sarnold.html) gave a nice talk about [AppArmor 3.0](https://www.youtube.com/watch?v=PRZ59lxLlOY). Again, [Luc Juggery](undefined) wrote a hands-on guide for [AppArmor & Docker](https://medium.com/lucjuggery/docker-apparmor-30-000-foot-view-60c5a5deb7b).
* Docker Daemon: Run the daemon as a non-privileged user. Especially not as root.

You should run regular checks against vulnerability databases. If they find an
issue, you need an effective way to get notified, e.g. by posting to a Slack
channel.

You could also use an OS that is optimized for containers, e.g. [Googles
Container-Optimized OS](https://cloud.google.com/container-optimized-os)
(COS).

There are many more things to say about the host system, but that is not the
focus of this article. If you’re interested, I’ll write a follow-up 🙂

## Base Image

The base image is the foundation of your docker image. Within your Dockerfile,
you define the base image with FROM . For me, it typically is
[python:3.8.7-slim-buster](https://hub.docker.com/_/python) or similar. You
need to ask yourself:

* Do I trust the base images’ author to have good intentions?
* Do I trust the base images’ author to have a secure development setup so that malware isn’t uploaded unintentionally, e.g. by leaking the credentials to the account or password re-use?

You should also scan your base image for vulnerabilities. Even for very
standard images, there are often vulnerabilities. Some can be fixed by
directly running an update (e.g. RUN apt-get update && apt-get upgrade),
others don’t have an update within the repository. But pretty often you also
don’t need all the installed stuff.

Be aware that alpine does only share vulnerabilities that they have already
fixed. So the scan might look better for them, although they are not better.
Alpine images are smaller, though. So the attack surface is smaller.

## Harden Your Image

Hardening is the process of reducing the attack surface or increasing the
difficulty to find and use existing vulnerability. It reduces the blast radius
any ticking bomb in your system could have.

### Copy only necessary files

You can use the
[.dockerignore](https://docs.docker.com/engine/reference/builder/#dockerignore-file)
file to make sure that some files are not added.

### Run non-privileged user in the container

By default, the code you execute within a docker container runs with the user
ID 0 — with root. It is recommended not to do that. You can change that in
multiple ways:

Within the Dockerfile — I prefer that one:

```dockerfile
RUN groupadd -r noroot && useradd -r -g noroot noroot
USER noroot
```

When you start the container:

```bash
$ docker run -u 1000 -it python:3.9.1-buster bash
I have no name!@a70ba4f24042:/$ echo $UID
1000
```

In Kubernetes via RunAsUser in the securityContext
([docs](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)).

### Multi-Stage Builds

If an attacker gets access to your container, you want them to have as few tools there as possible. Use [multi-stage builds](https://docs.docker.com/develop/develop-images/multistage-build/) for that. Build your code in a build-container and use the built artifact in another container. As a bonus, your image size will be smaller.

The [Docker docs](https://docs.docker.com/develop/develop-images/multistage-build/) give a very good example:

```dockerfile
FROM golang:1.7.3
WORKDIR /go/src/github.com/alexellis/href-counter/
RUN go get -d -v golang.org/x/net/html
COPY app.go .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY **--from=0** /go/src/github.com/alexellis/href-counter/app .
CMD ["./app"]
```

## Harden Your Containers

### Read-Only Root File System

This depends on how you run the docker image, but if you use docker run you can add the [--read-only flag](https://docs.docker.com/engine/reference/commandline/run/). This makes the root file system read-only. This means if an attacker gets into the system, they cannot store anything on disk or change any of the executables. They can still change the memory.

You should also be aware that some pretty standard tasks like creating a temporary file obviously don’t work anymore:

```bash
$ sudo docker run -it --read-only python:3.9.1-buster
Python 3.9.1 (default, Jan 12 2021, 16:45:25)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tempfile
>>> a = tempfile.mkdtemp()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.9/tempfile.py", line 348, in mkdtemp
    prefix, suffix, dir, output_type = _sanitize_params(prefix, suffix, dir)
  File "/usr/local/lib/python3.9/tempfile.py", line 118, in _sanitize_params
    dir = gettempdir()
  File "/usr/local/lib/python3.9/tempfile.py", line 287, in gettempdir
    tempdir = _get_default_tempdir()
  File "/usr/local/lib/python3.9/tempfile.py", line 219, in _get_default_tempdir
    raise FileNotFoundError(_errno.ENOENT,
FileNotFoundError: [Errno 2] No usable temporary directory found in ['/tmp', '/var/tmp', '/usr/tmp', '/']
```

You can work around this issue by mounting /tmp as a volume:

```bash
$ sudo docker run -it --mount source=myvol2,target=/tmp --read-only python:3.9.1-buster
Python 3.9.1 (default, Jan 12 2021, 16:45:25)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tempfile; a = tempfile.mkdtemp()


$ sudo docker run --rm -i -v=myvol2:/tmp/v busybox find /tmp/v
/tmp/v
/tmp/v/tmpbhw8djco
```

Even better is using the host's temporary file system:

```bash
$ sudo docker run -it **--tmpfs /tmp** --read-only python:3.9.1-buster
```

### Limit Capabilities

You can limit the [Linux kernel capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html):

```bash
$ docker run **--cap-drop all** -it python:3.9.1-buster bash
root@3c568219116e:/# groupadd -r noroot
**groupadd: failure while writing changes to /etc/gshadow**
```

You can then grant the ones your application needs:

```bash
$ docker run --cap-drop all --cap-add CHOWN -it python:3.9.1-buster bash
root@3c568219116e:/# groupadd -r noroot
groupadd: failure while writing changes to /etc/gshadow
```

In Kubernetes, this is done via capabilities in the securityContext
([docs](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)).

### no-new-privileges

You might want to always set --security-opt=no-new-privileges . It disables
container processes from gaining new privileges
([docs](https://docs.docker.com/engine/reference/run/#security-configuration)).
In Kubernetes, this is called allowPrivilegeEscalation
([docs](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)).

### Scanning for vulnerabilities

[Clair](https://github.com/quay/clair) by quay seems to be a commonly used
[tool to scan containers for vulnerabilities. I haven’t used it so far,
[though.

## Inter Container Communication

A key thought of “defense in depth” is to make every single step as hard as
possible for an attacker. If something is not strictly necessary for the
application to run, it is not allowed. Restricting the way the containers
communicate with other containers is one part of that.

![Scenario how an attacker is blocked by a controlled network communication / inter container communication. Image by Martin Thoma](https://cdn-images-1.medium.com/max/3972/1*t8W3Hpw3xa89r9j8JNScWw.png)*Scenario how an attacker is blocked by a controlled network communication / inter container communication. Image by Martin Thoma*

Most companies have a lot of different microservices running in containers.
Some of the containers need to communicate, others don’t need it. Maybe two
have vulnerabilities as shown in the image above. The backend has a
vulnerability that allows the attacker to get into the container and another
service might suffer from the same issue. But there is no direct way the
attacker can communicate with the other vulnerable service and thus harm is
prevented.

Have a look at [Docker container
networking](https://docs.docker.com/config/containers/container-networking/)
or [Kubernetes network
policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/).

## Conclusion

Container Security is an extremely broad field. The [NIST Application
Container Security
Guide](https://www.nist.gov/publications/application-container-security-guide)
is way more extensive than this article, the [OWASP Docker Cheat
Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)
is of similar length. Tsvi Korren made a pretty good presentation container
security:

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/_5uZnM1yv0Y" frameborder="0" allowfullscreen></iframe></center>

In security, it is hard to recommend what to do. For maximum security, you want to do everything. But a very short and actionable guide would be:

* Make sure you use a well-known, trusted, maintained base image.
* Install only software you need, copy only files you use. Try multi-stage builds if you need software to build the software.
* Use a non-root user.
* Restrict privileges / inter container communication.
* Use a read-only file system.
* Get a workflow that automatically scans for vulnerabilities and alerts you if anything new was found.

## What’s next?

In this series about application security (AppSec) we already explained some of the techniques of the attackers 😈 and also techniques of the defenders 😇:

* Part 1: [SQL Injections](https://medium.com/faun/sql-injections-e8bc9a14c95) 😈
* Part 2: [Don’t leak Secrets](https://levelup.gitconnected.com/leaking-secrets-240a3484cb80) 😇
* Part 3: [Cross-Site Scripting (XSS)](https://levelup.gitconnected.com/cross-site-scripting-xss-fd374ce71b2f) 😈
* Part 4: [Password Hashing](https://levelup.gitconnected.com/password-hashing-eb3b97684636) 😇
* Part 5: [ZIP Bombs](https://medium.com/bugbountywriteup/zip-bombs-30337a1b0112) 😈
* Part 6: [CAPTCHA](https://medium.com/plain-and-simple/captcha-500991bd90a3) 😇
* Part 7: [Email Spoofing](https://medium.com/bugbountywriteup/email-spoofing-9da8d33406bf) 😈
* Part 8: [Software Composition Analysis](https://medium.com/python-in-plain-english/software-composition-analysis-sca-7e573214a98e) (SCA) 😇
* Part 9: [XXE attacks](https://medium.com/faun/xxe-attacks-750e91448e8f) 😈
* Part 10: [Effective Access Control](https://levelup.gitconnected.com/effective-access-control-331f883cb0ff) 😇
* Part 11: [DOS via a Billion Laughs](https://medium.com/bugbountywriteup/dos-via-a-billion-laughs-9a79be96e139) 😈
* Part 12: [Full Disk Encryption](https://medium.com/faun/full-disk-encryption-2090489f9760) 😇
* Part 13: [Insecure Deserialization](https://medium.com/bugbountywriteup/insecure-deserialization-5c64e9943f0e) 😈
* Part 14: [Docker Security](https://levelup.gitconnected.com/docker-security-5f4df118948c) 😇

And this is about to come:

* CSRF 😈
* DOS 😈
* ReDoS 😈
* Credential Stuffing 😈
* Cryptojacking 😈
* Single-Sign-On 😇
* Two-Factor Authentication 😇
* Backups 😇

Let me know if you are interested in more articles around AppSec / InfoSec!

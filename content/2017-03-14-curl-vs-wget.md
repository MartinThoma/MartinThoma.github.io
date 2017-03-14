---
layout: post
title: curl vs wget
slug: curl-vs-wget
author: Martin Thoma
status: draft
date: 2017-03-14 20:00
category: Cyberculture
tags: curl, wget, download
featured_image: logos/star.png
---
I recently had to download large files (see [post](https://martin-thoma.com/download-data/)).
Before I used a download helper, I used `curl`. It is a standard tool for downloading
files. But there is another standard tool: `wget`. Let's see what I find in the
first 10 Google hits about their differences.

<table>
    <tr>
        <th></th>
        <th><a href="https://en.wikipedia.org/wiki/CURL">curl</a></th>
        <th><a href="https://en.wikipedia.org/wiki/Wget">wget</a></th>
    </tr>
    <tr>
        <td>Initial Release</td>
        <td>1997</td>
        <td>1996</td>
    </tr>
    <tr>
        <td>License</td>
        <td>MIT/X derivate&nbsp;</td>
        <td>GNUv3</td>
    </tr>
    <tr>
        <td>Written in</td>
        <td>C</td>
        <td>C</td>
    </tr>
    <tr>
        <td>OS</td>
        <td>cross-platform</td>
        <td>cross-platform</td>
    </tr>
    <tr>
        <td>Protocols</td>
        <td>FTP, FTPS, Gopher, HTTP, HTTPS, SCP, SFTP, TFTP, TELNET, DICT, LDAP, LDAPS, FILE, POP3, IMAP, SMB/CIFS, SMTP, RTMP, RTSP</td>
        <td>HTTP, HTTPS, FTP</td>
    </tr>
    <tr>
        <td>Usage</td>
        <td>`curl -O [URL]`</td>
        <td>`wget [url]`</td>
    </tr>
</table>


## curl strengths

* curl supports much more protocols and platforms (OS/400, TPF - never heard of them before)
* curl supports more authentication methods
* curl supports gzip and deflate Content-Encoding and does automatic decompression

## wget strengths

* Recursive! Wget's major strong side compared to curl is its ability to
  download recursively, or even just download everything that is referred to
  from a remote resource, be it a HTML page or a FTP directory listing.
* wget can recover from a prematurely broken transfer and continue downloading.
* Wget enables more features by default: cookies, redirect-following, time
  stamping from the remote resource etc. With curl most of those features need
  to be explicitly enabled.

## Interesting wget options

* `-b`: Put the download in background. Interersting for large downloads.
* `--user-agent="Mozilla/5.0"`
* `-i [filename]`: Specify a filename with newline separated URLs to download
* `--mirror -p`: Download a webpage
* `--convert-links`: Convert links for offline viewing
* `-P ./LOCAL-DIR`: where to store the webpage
* `--reject=gif`: Don't download gif files
* `-Q5m`: Stop downloading when the file size exceeds 5 MB


## Conclusiong

Use `wget` when you want to download a single file or a website. Use `curl`
for more fancy stuff.


## See also

* Daniel Stenberg: [curl vs Wget](https://daniel.haxx.se/docs/curl-vs-wget.html)
* Unix.SE: [What is the difference between curl and wget?](http://unix.stackexchange.com/q/47434/4784)
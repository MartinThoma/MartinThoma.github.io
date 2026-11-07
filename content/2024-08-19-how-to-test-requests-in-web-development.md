---
layout: post
title: How to test Requests in Web Development
slug: how-to-test-requests-in-web-development
lang: en
author: Martin Thoma
date: 2024-08-19 08:01
category: Code
tags: Web Development, Testing
featured_image: logos/development.png
summary: A small local web server that prints all requests it receives
medium_url: https://medium.com/@martinthoma/how-to-test-requests-in-web-development-9c7f531f5efb
status: draft
---
<figure>
    <a href="../images/2024/08/how-to-test-requests-in-web-development-1.png"><img src="../images/2024/08/how-to-test-requests-in-web-development-1.png" alt="Terminal output of postbin: it starts a server on port 5000 and prints a received POST request with its headers in a table and the JSON payload" width="800" height="282"></a>
</figure>

As a backend developer, I sometimes have the need to check which requests are sent, including the headers and the payload. It’s enormously useful to have a local tool which can check that.

I’ve just released [postbin](https://pypi.org/project/postbin/): A simple small webserver which receives requests and prints them, including the headers.

## Alternatives

I have used websites for that in the past, but in a professional context this might not be a good option in case you could leak private information. I also had issues with those websites, e.g. not all types of requests would be received/printed.

I’ve seen similar projects, but haven’t tried them:

* [httpbin](https://github.com/psf/httpbin): That looks pretty good. I have only found it once I started writing this blog post
* [rusqbin](https://github.com/lloydmeta/rusqbin)

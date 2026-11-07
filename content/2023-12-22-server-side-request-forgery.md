---
layout: post
title: Server-Side Request Forgery 😈
slug: server-side-request-forgery
lang: en
author: Martin Thoma
date: 2023-12-22 21:34
category: Security
tags: Security, AppSec
featured_image: logos/cybersecurity.png
summary: What are SSRFs, how do they work, how do they harm
medium_url: https://medium.com/@martinthoma/server-side-request-forgery-c55ed743557b
status: draft
---
<figure class="ai-generated">
    <a href="../images/2023/12/server-side-request-forgery-1.jpg"><img src="../images/2023/12/server-side-request-forgery-1.jpg" alt="A hooded man with glasses typing on a laptop in front of screens full of network diagrams and lock symbols" width="800" height="800"></a>
    <figcaption>Created with AI</figcaption>
</figure>

Server-Side Request Forgery (SSRF) is a type of web application security vulnerability that allows attackers to manipulate server-side requests, potentially gaining unauthorized access to internal resources and sensitive data. As organizations increasingly rely on web applications for business-critical operations, understanding and mitigating the risk posed by SSRF has become increasingly important.

In this article, we will explore the mechanics of SSRF and its potential impact on affected systems. We will also discuss best practices and strategies for identifying and preventing SSRF vulnerabilities, equipping you with the knowledge and tools necessary to safeguard your web applications from this threat.

## Why should I care?

* [**Capital One Data Breach (2019)**](https://edition.cnn.com/2019/07/29/business/capital-one-data-breach/index.html): A hacker exploited an SSRF vulnerability in a misconfigured AWS Web Application Firewall to gain access to sensitive data of over 100 million Capital One customers. The attacker was able to access Social Security numbers, bank account numbers, and other personal information ([source](https://krebsonsecurity.com/2019/08/what-we-can-learn-from-the-capital-one-hack/)).
* [**Grafana SSRF Vulnerability (2016 — 2020)**](https://grafana.com/blog/2020/06/03/grafana-6.7.4-and-7.0.2-released-with-important-security-fix/): An SSRF vulnerability was discovered in Grafana, an open-source analytics and monitoring platform. Attackers could exploit the vulnerability to access internal networks and steal sensitive data. Grafana released a security update to fix the issue.
* [**GitLab SSRF Vulnerability (2021)**](https://portswigger.net/daily-swig/gitlab-fixes-serious-ssrf-flaw-that-exposed-orgs-internal-servers): GitLab, a popular web-based DevOps platform, disclosed an SSRF vulnerability that exposed orgs’ internal servers.
* [**Microsoft Exchange Server (2023)**](https://threatprotect.qualys.com/2023/11/17/microsoft-exchange-server-authenticated-ssrf-vulnerability-zero-day/): The mail server allows attaching files not only from your local disk but also from an URL. This could be used for arbitrary code execution.

## How are SSRF attacks executed?

Server-Side Request Forgery (SSRF) attacks are executed by exploiting vulnerabilities in a web application that allow an attacker to forge server-side requests.

Typically, the attacker manipulates user input or API calls to create malicious requests, which are then sent by the server. The server has code that executes requests on behalf of the user, but the type of request or the target is changed by the attacker. These requests executed by the server can bypass security measures, such as firewalls or IP whitelisting, as they originate from the vulnerable server itself. Consequently, attackers can access restricted resources, read sensitive files, or interact with internal services that should not be exposed to external users.

In some cases, SSRF attacks can even lead to remote code execution or lateral movement within the target organization’s network.

## Example Vulnerability and Attack

Think about a mail service like Microsoft Exchange or Gmail. You can upload attachments, but it’s annoying that you have to download an image and upload it again if you want to share it via e-mail. It would be more convenient if you could just click on a button to add the image given by the URL.

If the code allows arbitrary file paths, the user could set the path to `file:///etc/passwd` to get the web server’s local users. Once the local users are known, `file:///home/user/.ssh/id_rsa` can be used to get the private SSH key. `/home/user/.bash_history` might reveal interesting services that can be accessed with that key.

## How can I prevent SSRF attacks?

Preventing Server-Side Request Forgery (SSRF) attacks involves a combination of secure coding practices and input validation.

First, ensure that your web application follows the **principle of least privilege**, meaning it only has the necessary permissions and access to required resources.

Next, perform strict **input validation and sanitization** on all user-supplied data to prevent malicious payloads from being injected into server-side requests. Whitelisting allowed URLs, protocols, and IP addresses can help restrict outbound requests to trusted sources only.

Other secure coding practices that can help are **security audits**, **code reviews**, and **educating your development team** about SSRF attacks. The main reason to fall for this attack is not being aware that it exists.

<!-- series: appsec -->

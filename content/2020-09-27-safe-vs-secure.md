---
layout: post
title: Safe vs Secure
slug: safe-vs-secure
URL: https://medium.com/plain-and-simple/safe-vs-secure-456ba5ebe95b
author: Martin Thoma
date: 2020-09-27 20:00
category: My bits and bytes
tags: Terminology, English, InfoSec, AppSec, Security, Safety, SRE, DevOps, DevSecOps
featured_image: logos/star.png
---
When I hear “safety” in the context of software development, I’m always
reminded that I need to automate my backup solution. The potential harm most
software developers have to deal with is luckily only data loss due to hardware
failures.

> # Safety is resilience against accidential harm to people, property, or the environment.

Aspects of safety in software development and operations include:

* **Availability**: A single server could be cut off the internet by
  construction workers, a hard drive could reach its end of life, a fire could
  break out, an earthquake could hit the region.
* **Scalability**: Web services might go down when they are too successful.
  It’s sometimes called the
  “[hug of death](https://en.wikipedia.org/wiki/Slashdot_effect)” when a huge
  website links to a small one. Or just when you have a successful marketing
  campaign.
* **Integrity**: All ways to send data are prone to errors. Package loss or
  bit-flips happen. We have error-correcting protocols to deal with that.

Software can also be safety-critical, for example when you think about airbags.
A defect there can put lives under risk
([example](https://www.businessinsider.com/r-gm-recalls-43-million-vehicles-worldwide-for-software-defect-2016-9?r=DE&IR=T)).
Other examples of **safety-critical software** include traffic lights,
life-support systems, software managing the electrical power grids, industrial
software which is used in machines that produce medicine, pacemakers, and many
more.

When we are talking about security in software development, we are thinking
about hackers. [Wikipedia](https://en.wikipedia.org/wiki/Security) has a pretty
nice explanation:

> # Security is resilience against harm caused by others.

Aspects of security in software development and operations include:

* **Accountability**: You want to have a log of changes. This includes source
  code. In the version control system git, you can even cryptographically sign
  the changes so that others cannot tamper with your changes.
* **Availability**: An attacker might run a
  [Denial-of-Service attack](https://en.wikipedia.org/wiki/Denial-of-service_attack) (DOS).
* **Confidentiality**:
  [Man-in-the-middle](https://en.wikipedia.org/wiki/Man-in-the-middle_attack)
  (MITM) attacks that apply packet sniffing come to my mind. [Dharmil
  Chhadva](undefined) wrote [a nice
  article](https://levelup.gitconnected.com/man-in-the-middle-attack-mitm-part-2-packet-sniffer-82f0a121c58d)
  about this topic.
* **Integrity**: Think of a bank account. An attacker wants to increase the
  money on one account.
  [Cryptojacking](https://www.wired.com/story/cryptojacking-took-over-internet/)
  is an example where not data, but the software is affected.

Measures to increase security include:

* Code Reviews and Unit Tests: Anything that improves overall code quality
* Software Composition Analysis (SCA), e.g. by
  [safety](https://pypi.org/project/safety/),
  [VeraCode](https://www.veracode.com/products/software-composition-analysis),
  [WhiteSource](https://www.whitesourcesoftware.com/how-to-choose-a-software-composition-analysis-solution/),
  [BlackDuck](https://www.synopsys.com/software-integrity/security-testing/software-composition-analysis.html),
  and
  [many more](https://owasp.org/www-community/Free_for_Open_Source_Application_Security_Tools).
* Static Application Security Testing (SAST), e.g. by
  [bandit](https://pypi.org/project/bandit/),
  [Coverity](https://www.synopsys.com/software-integrity/security-testing/static-analysis-sast.html),
  and [many
  more](https://owasp.org/www-community/Free_for_Open_Source_Application_Security_Tools).
* Dynamic Application Security Testing (DAST), e.g. supported by
  [OWASP ZAP](https://www.zaproxy.org/),
  [Arachni Scanner](https://www.arachni-scanner.com/),
  [Synopsys](https://www.synopsys.com/software-integrity/application-security-testing-services/dynamic-analysis-dast.html),
  and
  [many more](https://owasp.org/www-community/Free_for_Open_Source_Application_Security_Tools).

## TL;DR: Differences between Safety and Security

<table class="table table-striped table-sm" style="width: 60%">
    <tr>
        <th></th>
        <th>Safety</th>
        <th>Security</th>
    </tr>
    <tr>
        <td>What to fear</td>
        <td>Hazard</td>
        <td>Threat</td>
    </tr>
    <tr>
        <td>Cause is</td>
        <td>Accidential</td>
        <td>Malicious</td>
    </tr>
    <tr>
        <td>Measures are</td>
        <td>Backups, Redundancy</td>
        <td>SAST, DAST, CAS, HTTPS, ...</td>
    </tr>
    <tr>
        <td>When things go wrong, it's called a ...</td>
        <td>Failure</td>
        <td>Incident</td>
    </tr>
    <tr>
        <td>Roles</td>
        <td>Site Reliability Engineer</td>
        <td>AppSec Engineer, Penetration Tester</td>
    </tr>
</table>

## See also

* [IEC 61508](https://en.wikipedia.org/wiki/IEC_61508): “Functional Safety of […] Programmable Electronic Safety-related Systems”.
* [IEEE STD-1228](https://ieeexplore.ieee.org/document/467427):
* OmniSecu: [Types of Network Attacks against Confidentiality, Integrity and Avilability](https://www.omnisecu.com/ccna-security/types-of-network-attacks.php)

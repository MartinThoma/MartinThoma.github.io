---
layout: post
title: Watermarks, Digital Signatures, and Fingerprinting
slug: watermarks-digital-signatures-and-fingerprinting
lang: en
author: Martin Thoma
date: 2023-01-07 22:56
category: Security
tags: Security, Cryptography
featured_image: logos/cybersecurity.png
summary: Watermarks are hard to remove, signatures are hard to forge, fingerprints trace people against their will
medium_url: https://medium.com/@martinthoma/watermarks-digital-signatures-and-fingerprinting-86c4ade984f1
---
I see the terms watermark and digital signature being used interchangeably, but they are different:

> Good **watermarks** **are hard to remove**, but might be easy to forge. Watermarks help the person who created the work to be able to prove they did it.

> **Fingerprints** are used to trace people against their will. The person who created them didn’t create them on purpose.

> Good (**digital) signatures** **are hard to forge**, but might be easy to remove. Signatures help the person who received the signature to prove agreement of the signer — typically to a contract, but also to certificates.

## How is it done in the physical world?

There are two ways to **sign documents**. You can either write your name or you can use a stamp. In former times, a seal was created. All ways are extremely insecure as you essentially only need to see the original to be able to forge a physical signature / stamp / seal.

Creating watermarks is more time intensive. I also don’t know any way to remove a watermark from a physical document.

<iframe width="560" height="315" src="https://www.youtube.com/embed/orSFE-bJniw" title="YouTube video player" frameborder="0" allowfullscreen></iframe>

Fingerprints are known to everybody, but did you know that your printer might add them as well? It’s called [machine identification code](https://en.wikipedia.org/wiki/Machine_Identification_Code) or tracking dots. Those are tiny yellow dots that some printers leave on the page in order to make it identifiable.

## How is it done in the digital world?

Digital signatures use public key cryptography like the [RSA cryptosystem](https://en.wikipedia.org/wiki/RSA_%28cryptosystem%29) and [ECDSA](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm). If implemented right, state-of-the-art digital signatures are impossible to forge. It’s hard to explain how they work, but Computerphile does a good job:

<iframe width="560" height="315" src="https://www.youtube.com/embed/s22eJ1eVLTU" title="YouTube video player" frameborder="0" allowfullscreen></iframe>

Watermarks are trickier. How do you ensure that somebody does not remove the information that you created some work from the work?

The simplest way to add a watermark to a file is by changing metadata. However, that is typically easy to remove. For pure images / audio / video, the user could simply take a screenshot / redirect the audio output / record the screen.

A solution for images that worked for a while was to add an overlay over a key part of the image. However, with recent AI improvements that doesn’t help so well anymore.

For audio, you could also add beats in a certain pattern. The key part is that they must be clear to hear.

Fingerprints also exist for devices. You can identify browsers by a lot more than just the user agent, see:

[**Device fingerprint - Wikipedia** *A device fingerprint or machine fingerprint is information collected about the software and hardware of a remote…*](https://en.wikipedia.org/wiki/Device_fingerprint)

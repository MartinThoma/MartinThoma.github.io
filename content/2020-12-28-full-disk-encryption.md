---
layout: post
title: Full Disk Encryption 😇
subtitle: Keep your data private, even if you lose your device
slug: full-disk-encryption
URL: https://medium.com/faun/full-disk-encryption-2090489f9760
author: Martin Thoma
date: 2020-12-28 20:00
category: Security
tags: Security, Cybersecurity, IT Security, InfoSec
featured_image: logos/star.png
---
Having an attacker with physical access to your device is one of the worst
scenarios. If the data is not encrypted on the disk, then the attacker can
simply disassemble your device, get the HDD/SDD, put it in his machine, and
read the data. For this reason, encrypting your data is crucial.

There are so many things you want to protect that it makes sense to just
encrypt the complete hard drive. For example, you might have valuable data on
your swap partition or within temporary files. So just encrypt the whole drive.
This is called **F**ull **D**isk **E**ncryption, or **FDE** in short. Let’s
talk about how it works, different implementations of it, and the weaknesses.

## Why it Matters

* **2009**: According to “The Cost of a Lost Laptop” by Ponemon Institute, the
  average damage organizations suffer due to lost laptops is **$49,246**.
  Please note that this includes the hardware, the damage done by leaked
  confidential data, and the damage done by lost work.
* **2015**: “Nearly 41% of all data breach events from 2005 through 2015 were
  caused by lost devices such as laptops, tablets, and smartphones.”
  ([source](https://www.forbes.com/sites/steveolenski/2017/12/08/is-the-data-on-your-business-digital-devices-safe/?sh=22fc1c014c6a))

## FDE does not solve…

* … lost data: You need to make backups for that
* … leaking data through memory: FDE is about protecting data at rest. When
  your computer is turned off. Not about protecting data in memory or in
  transit. [Subash SN](undefined) shows this beautifully in his article
  [Breaking Full Disk Encryption from a Memory
  Dump](https://blog.appsecco.com/breaking-full-disk-encryption-from-a-memory-dump-5a868c4fc81e).
* … leaking data through the internet: If an attacker gets live access to your
  computer, e.g. by convincing you to install some software to make a remote
  fix on your machine (phishing), FDE does not help at all.
* … [rubber-hose
  cryptanalysis](https://en.wikipedia.org/wiki/Rubber-hose_cryptanalysis):
  Torturing you to give your password away.
* … [hardware keyloggers](https://en.wikipedia.org/wiki/Keystroke_logging): If
  the attacker can record all your keystrokes, they will also get the password
  you’re using to decrypt the drive.

## How FDE Works

Full disk encryption (FDE) works on a very low level. It is below the file
system which also means it’s compatible with every file system. It uses a
symmetric encryption algorithm that operates on blocks of data, e.g. 128-bit.
Those blocks are automatically encrypted when they are written and
automatically decrypted when they are requested. The program typically keeps
the key in memory.

A typical choice is a **block size of 128-bit**, the **AES block cipher** with
a **256-bit key **and** CBC operation mode**. Block ciphers operate on blocks
of an exact size (e.g. 128-bit). They get this size as input and give the same
size in output. The operation mode — or short “mode” — is the rule that is
applied to deal with other block sizes. The simplest mode is ECB
(**e**lectronic **c**ode**b**ook). That mode just splits the plain text into
blocks of the desired size, pads the last message with zeros, and applies the
cipher to every block independently. This is a bad idea as it shows repeating
patterns clearly. XTS is a common mode explained by [Prof Bill Buchanan
OBE](undefined) in his article [Who Needs a Tweak? Meet Full Disk
Encryption](https://medium.com/asecuritysite-when-bob-met-alice/who-needs-a-tweak-meet-full-disk-encryption-437e720879ac).
Computerphile has a nice explanation of the modes:

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/Rk0NIQfEXBA" frameborder="0" allowfullscreen></iframe></center>

The key has to be stored on the device to encrypt the data. This means the key
needs to be secure. Additionally, one may not store the key in plaintext on the
machine and one needs to prevent brute-forcing of the key. What the user
memorizes is the passphrase. This passphrase is run through a cryptographic
hash function to generate the key. This “cryptographic” means that it is
computationally heavy — you have to spend that computation every time you
unlock your computer. But the attacker also has to do it. Meaning if you need
e.g. 1 second to run this, the attacker would need one second for every single
attempt. A typical **key derivation function** is **PBKDF2** and a typical
**cryptographic hash function** is **SHA-512**. After the key has been derived,
it is stored securely in memory.

Instead of using a password, you could also give your users a physical token
such as a Yubikey
([example](https://www.yubico.com/works-with-yubikey/catalog/secure-disk-for-bitlocker/))
or similar solutions. Or you simply put the key file on a USB stick. The
advantage of such tokens is that users cannot give them away. But this is a
topic for another article.

All of that is not worth anything if you have a keylogger running. Hardware
keyloggers need extra considerations, but for software keyloggers, we want to
ensure the integrity of the boot path. This is where TPM can help. TPM is a
piece of hardware that ensures that no tampering happened to the hardware or
essential parts of the software, namely the BIOS

## What is Secure?

NIST is the US national institute of standards and technology. Their
recommendations are widely followed. The German BSI is also interesting to look
at.

[NIST 800–38E](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=904691)
(2010) approves the XTS-AES mode with either 256-bit keys (XTS-AES-128; 128 is
the block size here) or **512-bit keys** for a **256-bit block size** using the
**AES cipher** in **XTS mode**. Please note that AES-128 refers to a block size
of 128-bit, not to the length of the key.

[BSI
TR-02102–1](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR-02102.pdf?__blob=publicationFile)
(2020) recommends using one of those block-ciphers: AES-128, AES-192, AES-256.
They say CCM, GCM, CBC, CTR are acceptable. Interestingly, they do not mention
XTS here. In another part of the document, they mention potential issues of
this mode for backups.

## FDE Solutions

### Windows: BitLocker

[BitLocker](https://en.wikipedia.org/wiki/BitLocker) is an FDE feature included
with Microsoft Windows since 2007. By default, it uses AES in CBC mode with a
128-bit key. It can be configured to use XTS mode and/or a 256-bit key. It can
use a [TPM](https://en.wikipedia.org/wiki/Trusted_Platform_Module) to validate
the integrity of boot and system files before decrypting a protected volume.

Here is a guide on how to set BitLocker up on Windows: [**Setting up BitLocker
Drive Encryption on Windows 10** *When you store sensitive data on your
computer, it's crucial that you take the necessary steps to protect that
data…*www.windowscentral.com](https://www.windowscentral.com/how-use-bitlocker-encryption-windows-10)

### Linux: dm-crypt using LUKS2

dm-crypt using LUKS is the default way to do FDE on Linux since 2004. dm-crypt
supports XTS, but the default cipher string specification is
aes-cbc-essiv:sha256
([source](http://manpages.ubuntu.com/manpages/bionic/man8/cryptsetup.8.html)).
You can use cryptsetup and cryptmount to manage your dm-crypt .

You can use GRUBs cryptodisk feature to secure your boot path.

Detailed instructions can be found here:
[**Full_Disk_Encryption_Howto_2019**
*Further support may be available from Freenode IRC channel #ubuntu. This page is an up-to-date guide to comprehensive…*help.ubuntu.com](https://help.ubuntu.com/community/Full_Disk_Encryption_Howto_2019)

### Mac: FileVault 2

[FileVault](https://en.wikipedia.org/wiki/FileVault) is the FDE program that was introduced for Mac in 2003. By default, it uses XTS-AES with 128-bit blocks and a 256-bit key.

Here is a guide on how to turn on FileVault on Mac:
[**Use FileVault to encrypt the startup disk on your Mac**
*FileVault 2 is available in OS X Lion or later. When FileVault is turned on, your Mac always requires that you log in…*support.apple.com](https://support.apple.com/en-us/HT204837)

### Android

Only Android 7.0 to 9 support FDE. Android 10 only supports file-based
encryption
([source](https://source.android.com/security/encryption/full-disk)). Some
speculations why the FDE was removed are issues with alarm clocks and support
options in case of forgotten passwords
([source](https://www.reddit.com/r/Android/comments/gt3ib8/why_was_fulldisk_encryption_removeddisallowed_in/)).
As a phone is typically running all the time and rather easy to unlock, disk
encryption is actually not enough. The memory needs to be protected as well.

The supported Android versions used dm-crypt .

In my Samsung S10, the setting to enable FDE on Android is called “Strong Protection”. You find a guide here:
[**How to encrypt your Android device**
*There's little doubt that keeping your personal data secure these days is pretty important, so it is fortunate that…*www.androidauthority.com](https://www.androidauthority.com/how-to-encrypt-android-device-326700/)

### Honorable Mentions

* GnuPG (Linux) is a free replacement for PGP released in 1999. It received 250k DM in 1995 which would be equivalent to 350k € or $427k USD in 2019.
* PGP (Linux): Pretty Good Privacy (PGP) from Symantec (now NortonLifeLock) calls the concept **W**hole **D**isk **E**ncryption (**WDE**) instead of FDE. WDE was introduced in 2014 to PGP. It uses a password as authentication before the rest of the operating system can boot. This means you can use it for Windows and Linux.
* VeraCrypt (former TrueCrypt): If you’re interested in how to use it, have a look at [Andrew Douma](undefined)s article [Full Disk Encryption with VeraCrypt](https://medium.com/@securitystreak/veracrypt-full-disk-drive-encryption-fde-157eacbf0b61).

## Lost Device Policy

Having FDE on all your devices is not enough. On the one hand, you need to make
sure that the employees use strong passwords and that those passwords are not
written on the device.

But even that should not be it. You should have a documented way how to handle
lost devices. You need a Lost Device Policy. This can include:

* Block all accounts of that employee. Even if the laptop gets compromised, at least the remaining accounts cannot be used to steal more data.
* Try to get the laptop again by calling lost&found stations (e.g. for the taxi/airport/hotel)
* Inform the police that the laptop was stolen. You should have a model name and the serial number at hand. Maybe even something that makes the laptop unique?

## See also

While searching for references for this article, I came across some very good resources.

* ArchLinux: [Data-at-rest encryption](https://wiki.archlinux.org/index.php/Data-at-rest_encryption)
* ArchLinux: [dmcrypt/Encrypting an entire system](https://wiki.archlinux.org/index.php/Dm-crypt/Encrypting_an_entire_system)
* Security.SE: [How secure is Ubuntu’s default full-disk encryption?](https://security.stackexchange.com/questions/39306/how-secure-is-ubuntus-default-full-disk-encryption)

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

And this is about to come:

* CSRF 😈
* DOS 😈
* Credential Stuffing 😈
* Cryptojacking 😈
* Single-Sign-On 😇
* Two-Factor Authentication 😇
* Backups 😇

Let me know if you are interested in more articles around AppSec / InfoSec!

---
layout: post
title: Dreamspark SDM Odysee
author: Martin Thoma
date: 2015-03-24 13:04
categories:
- Cyberculture
tags:
- Microsoft
- Dreamspark
- Windows 7
- Windows 8.1
featured_image: logos/microsoft.png
---
I need to have Windows for work. As a student I *should* have free access to
it. But when I try to download it, I have to use Microsofts
"Secure Download Manager" (SDM). As a Ubuntu (Linux) user, this is easier
said than done.

## TL;DR

You need a Windows PC to download Windows. Ask a friend to download it. That
might be the easiest way. If you have a Windows PC and get the same error as I
get, you might need to re-install the system. (No, rebooting does not help.)

What I've tried and what does not work:

* Wine
* VMs
* Avoiding SDM

What I am currently trying: Installing Windows 7 on another computer.*argh*


## The problem

Using the Windows 8 systems at my university gives:

{% caption align="aligncenter" width="500" alt="Error message when trying to install SDM" text="Error message when trying to install SDM" url="../images/2015/03/windows-sdm-screenshot.png" %}

> Das Feature, das Sie verwenden möchten, befindet sich auf einer Netzressource,
> die nicht zur Verfügung steht.
>
> Klicken Sie auf "OK", um den Vorgang zu wiederholen. Oder geben Sie in das
> untenstehende Feld den Pfad zu einem anderen Ordner ein, der das
> Installationspaket "SDM_DE.msi" enthält.

(Sorry, I only get the German error message.)

When I give the path of the SDM_DE.msi I get:

> Die Datei "Z:\sdm\SDM_DE.msi" ist kein gültiges Installationspaket für das
> Produkt "Secure Download Manager". Suchen Sie das Installationspaket
> "SDM_DE.msi" in einem Order, von dem aus Sie
> "Secure Download Manager" installieren können.

Then I got desperate and followed [threadsofscience.wordpress.com/2013/02/13/downloading-dreamspark-microsoft-windows-on-ubuntu](https://threadsofscience.wordpress.com/2013/02/13/downloading-dreamspark-microsoft-windows-on-ubuntu/) (similar: http://boris-spinner.de/secure-download-manager-sdm-unter-linux-ausfuehren/).

It seems as if I need Linux to emulate Windows to get Windows ... it's a
strange world.

> wine: Bad EXE format for Z:\home\moose\Downloads\SDM_EN.msi.

Seems to be a 32-bit / 64-bit problem ...

* http://wiki.winehq.org/FAQ#32_bit_wineprefix
* https://appdb.winehq.org/objectManager.php?sClass=version&iId=31542


After trying to fix it, I get

> err:msidb:get_tablecolumns column 1 out of range
> err:msidb:get_tablecolumns column 2 out of range
> fixme:storage:create_storagefile Storage share mode not implemented.
> err:msidb:get_tablecolumns column 1 out of range
> err:msidb:get_tablecolumns column 2 out of range
> err:msidb:get_tablecolumns column 1 out of range
> err:msidb:get_tablecolumns column 2 out of range
> err:msidb:get_tablecolumns column 1 out of range
> err:msidb:get_tablecolumns column 2 out of range
> err:msidb:get_tablecolumns column 3 out of range
> err:msidb:get_tablecolumns column 1 out of range
> err:msidb:get_tablecolumns column 2 out of range
> err:msidb:get_tablecolumns column 3 out of range
> err:msidb:get_tablecolumns column 1 out of range
> err:msidb:get_tablecolumns column 2 out of range
> err:msidb:get_tablecolumns column 3 out of range
> err:msidb:get_tablecolumns column 1 out of range
> err:msidb:get_tablecolumns column 2 out of range
> err:msidb:get_tablecolumns column 3 out of range


## Reverse Engineering ... a little bit

Taking a look at the `1234567890ab.sdx` file reveals that it contains only a single url:

```text
http://kit.onthehub.com/WebStore/Account/SdmAuthorize.aspx?o=12345678-1234-1234-123a-12234567890a&ws=12345678-1234-1234-1234-1234567890ab&uid=12345678-1234-1234-1234-1234567890ab&abc=5
```

(I've replaced the numbers by 123... to avoid problems with other people using
my link to download stuff)

However, I cannot simply download it there. There is a page with two downloads,
but when I click on download nothing happens.

{% caption align="aligncenter" width="500" alt="SDM download page" text="SDM download page" url="../images/2015/03/sdm-download-page.png" %}

So I use Chrome developer tools
(<kbd>Ctrl</kbd>+<kbd>shift</kbd>+<kbd>i</kbd>) to see the request.

It's a GET request which gets the response:

```xml
<information>
    <oiopua>12345678-1234-1234-1234-1234567890ab</oiopua>
    <edv>1234567890^^1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789</edv>
    <linkAvailable>1</linkAvailable>
    <errorTextKey />
    <invokeExternalDownload>0</invokeExternalDownload>
    <fileURL>http://software.dreamspark.com/dreamspark/GERMAN/de_windows_8.1_with_update_x64_dvd_4048209.01.sdc</fileURL>
</information>
```

Although I can download the `.sdc` file, I cannot use it. It is an encrypted
file (which would give the `.iso`, but I don't know how to encrypt it.).

If you are interested in the file format, you might want to read
[Secure Digital Container](https://en.wikipedia.org/wiki/Secure_Digital_Container)


## VMs

Another try is installing a VM. You can download some at
https://www.modern.ie/en-us/virtualization-tools#downloads

I downloaded IE11, Win 8.1. Importing the VM took about 15 minutes on my computer.
Then I got another error:

{% caption align="aligncenter" width="500" alt="VM import error" text="VM import error" url="../images/2015/03/vm-critical-error.png" %}


## Installing Windows 7

12:50 I fortunately had a Windows 7 DVD lying around. Installing it will
probably take another 2 hours or so...

13:23 - *argh* ... I just found another reason to hate Windows. I've just
installed Windows 7. Cable-based network does not work out of the box.
I have to install drivers from http://www.helpjet.net/files-Acer-TravelMate-5735Z.html#ANetwork



## Related

* [Install Windows 8.1 from Dreamspark download on Ubuntu](http://superuser.com/questions/734924/install-windows-8-1-from-dreamspark-download-on-ubuntu)
* [Why are Microsoft products so User unfriendly?](http://martin-thoma.com/why-are-microsoft-products-so-user-unfriendly/)
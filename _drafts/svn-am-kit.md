---
layout: post
title: SVN am KIT
author: Martin Thoma
date: 2012-04-26 01:33:01
categories: 
- Cyberculture
tags: 
- KIT
- svn
- SWT I
featured_image: 
---
Jeder Student mit einem <a href="http://www.atis.uka.de/">ATIS-Account</a> kann <a href="http://www.atis.uka.de/1422.php">hier</a> einen SVN-Zugang beantragen. Ich werde nun kurz erklären, wie man ihn mit der Konsole benutzt.

<h2>Import</h2>
Syntax (<a href="http://svnbook.red-bean.com/en/1.6/svn.ref.svn.c.import.html">Hilfe</a>):
[bash]svn import [PATH] URL[/bash]

Beispiel:
[bash]svn import -m &quot;Initial import of the BankAccountReader project.&quot; /home/swt-user/BankAccountReader https://svnserver.informatik.kit.edu/stud/svn/s_thoma/trunk/BankAccountReader[/bash]

<h2>Checkout</h2>
Syntax (<a href="http://svnbook.red-bean.com/en/1.6/svn.ref.svn.c.checkout.html">Hilfe</a>):
[bash]svn checkout URL[@REV]... [PATH][/bash]

Beispiel:
[bash]svn co https://svnserver.informatik.kit.edu/stud/svn/s_thoma/trunk --username s_thoma[/bash]

<h2>Copy, Move, Delete</h2>
<strong>Copy</strong> (<a href="http://svnbook.red-bean.com/en/1.6/svn.ref.svn.c.copy.html">Hilfe</a>):
[bash]svn copy SRC[@REV]... DST[/bash]

Beispiel:
[bash]svn copy mySoureFile.java folder/myDestFile.java[/bash]

<strong>Move</strong> (<a href="http://svnbook.red-bean.com/en/1.6/svn.ref.svn.c.move.html">Hilfe</a>):
[bash]svn move SRC... DST[/bash]

<strong>Delete</strong> (<a href="http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.delete.html">Help</a>):
[bash]svn delete PATH...[/bash]

Für delete gibt es einige synonyme Befehle:
[bash]svn rm myFile.java[/bash]

Anders als der standard Linux <a href="http://linux.die.net/man/1/rm">rm-Befehl</a> ist der von SVN rekursiv!

<h2>status</h2>
Syntax (<a href="http://svnbook.red-bean.com/en/1.6/svn.ref.svn.c.status.html">Hilfe</a>):
[bash]svn status [PATH...][/bash]

Beispiel:
[bash]svn status

D       src
D       src/Tests.in
D       src/Tests.out
D       src/banking
D       src/banking/Status.java
D       src/banking/AccountNumber.java
D       src/banking/Shell.java
D       src/banking/Terminal.java
D       src/svn-commit.tmp
A  +    BankAccountReader
D       BankAccountReader/svn-commit.tmp[/bash]

<h2>commit</h2>
Syntax (<a href="http://svnbook.red-bean.com/en/1.6/svn.ref.svn.c.commit.html">Hilfe</a>):
[bash]svn commit [PATH...][/bash]

Beispiel:
[bash]svn commit -m &quot;restructuring directory structure&quot;
Adding         BankAccountReader
Deleting       BankAccountReader/svn-commit.tmp
Deleting       src

Committed revision 3.[/bash]

<h2>Siehe auch</h2>
<a href="http://svnbook.red-bean.com/en/1.6/svn.ref.html">Subversion complete reference</a>
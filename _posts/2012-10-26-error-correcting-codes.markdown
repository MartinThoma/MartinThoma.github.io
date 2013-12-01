---
layout: post
status: publish
published: true
title: Error correcting Codes
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 47471
wordpress_url: http://martin-thoma.com/?p=47471
date: 2012-10-26 22:29:51.000000000 +02:00
categories:
- My bits and bytes
tags:
- mathematics
- coding theory
comments:
- id: 353581
  author: Keba
  author_email: why@web.de
  author_url: ''
  date: !binary |-
    MjAxMi0xMC0zMSAxOTo1Njo0NSArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0xMC0zMSAxNzo1Njo0NSArMDEwMA==
  content: ! "You&lsquo;re bad at googling: \r\n\r\nEnglish Wikipedia: http://en.wikipedia.org/wiki/Hamming_code#Construction_of_G_and_H
    &ndash; \r\nGerman Wikipedia: http://en.wikipedia.org/wiki/Hamming_code#Construction_of_G_and_H\r\n\r\nWhat
    the hack did you type into the google search field? ;)\r\n\r\nNevertheless, thanks
    for the article. Though I&lsquo;m not (yet) an Informatics student, it&lsquo;s
    an interesting topic. :)\r\n\r\nRegards, Keba"
- id: 353591
  author: Keba
  author_email: why@web.de
  author_url: ''
  date: !binary |-
    MjAxMi0xMC0zMSAxOTo1NzoyOSArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0xMC0zMSAxNzo1NzoyOSArMDEwMA==
  content: ! 'Nah, and I&lsquo;m bad at copy-pasting. Link to German Wikipedia: http://de.wikipedia.org/wiki/Hamming-Code#Linearit.C3.A4t'
- id: 353601
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMi0xMC0zMSAyMDoxOTo0MiArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0xMC0zMSAxODoxOTo0MiArMDEwMA==
  content: ! "Hi Keba,\r\n\r\nI did read this article, but I don't think it really
    answers the question how the matrix G can be obtained.\r\nIf you understood how
    to generate the matrix G, could you tell me how it would look like for a (15,
    2048, 3)-Hamming Code?\r\n\r\nCheers,\r\nMartin"
---
<div class="info">This blogpost is strongly related to <a href="http://page.math.tu-berlin.de/~felsner/DMSWe/Aufgaben/codes.pdf">this germand PDF</a> of a pupils' competition in which I have participated in 2008.</div>

Today, we have a lot of data that is stored or transferred in a binary way. Once in a while an error occurs and single bits get switched from 0 to 1 or the other way around. <a href="http://en.wikipedia.org/wiki/Coding_theory">Coding theory</a> tries to find algorithms with which you can <strong>detect</strong> and <strong>correct</strong> errors.

<h2>Introduction</h2>
To keep it simple, we make a small example. We have $2^3 = 8$ valid messages:

Message A: (0, 0, 0)
Message B: (0, 0, 1)
Message C: (0, 1, 0)
Message D: (0, 1, 1)
Message E: (1, 0, 0)
Message F: (1, 0, 1)
Message G: (1, 1, 0)
Message H: (1, 1, 1)

I will call the set $c_1 := \{A, B, C, D, E, F, G, H\}$ of those messages a <strong>code</strong>.

Now Alice wants to send message A to Bob. If one error occurs, Bob receives either message B, message C or message E. As all of those are valid messages, he might not notice that an error occurred (and even more not be able to correct the error).

How could Alice and Bob solve this problem? 

<h2>Redundancy</h2>
Well, a simple solution would be to send the message twice. Or, almost the same, sending once a message with redundant information. So the new messages are:

Message A': (0, 0, 0, 0, 0, 0)
Message B': (0, 0, 1, 0, 0, 1)
Message C': (0, 1, 0, 0, 1, 0)
Message D': (0, 1, 1, 0, 1, 1)
Message E': (1, 0, 0, 1, 0, 0)
Message F': (1, 0, 1, 1, 0, 1)
Message G': (1, 1, 0, 1, 1, 0)
Message H': (1, 1, 1, 1, 1, 1)

$c_2 := \{A', B', C', D', E', F', G', H'\}$

If Bob gets a message with only one error, he can detect it. But he still isn't able to correct it:
Alice send Message A and an error occurred at the first (most significant) bit. Bob can see that this is not a valid message, but if he thinks that only one error occurred, it is equally likely that Alice sent message A or message E.

Can we do better?

<h2>Hamming distance</h2>
A useful tool is the so called "<a href="http://en.wikipedia.org/wiki/Hamming_distance">Hamming distance</a>". 

The set of all 0/1 tuples of the length $n$ is called $\mathcal{F}_n$. 

Examples: 
$\begin{align}
    \{A, B, C, D, E, F, G, H\}     &= \mathcal{F}_3\\
\{A', B', C', D', E', F', G', H'\} &\subsetneq \mathcal{F}_8
\end{align}$

$A[i]$ is the $i$-th bit of a message $A$ with $i \in \{0, \dots, (n-1)\}$

$\oplus : \{0,1\} \times \{0,1\} \rightarrow \{0,1\}$ defined as $\oplus(a, b) := 
\begin{cases}
 0 & \text{, if } a = b\\
 1 & \text{, if } a \neq b\\
\end{cases}$.
($\oplus$ is XOR).

The Hamming distance is a function $h: \mathcal{F}_n \times \mathcal{F}_n \rightarrow \mathbb{N}_0$ defined as:
$\displaystyle h(A, B) := \sum_{i=0}A[i] \oplus B[i]$

The minimum Hamming distance is defined as:
$\displaystyle h_\text{min}(\text{code}) = \min(\{h(A, B) | A, B \in \text{code}, A \neq B\})$

<h3>First example</h3>


<table class="wikitable">
<tr>
  <th>&nbsp;</th>
  <th>A</th>
  <th>B</th>
  <th>C</th>
  <th>D</th>
  <th>E</th>
  <th>F</th>
  <th>G</th>
  <th>H</th>
</tr>
<tr>
  <th>A</th>
  <td>0</td>
  <td>1</td>
  <td>1</td>
  <td>2</td>
  <td>1</td>
  <td>2</td>
  <td>2</td>
  <td>3</td>
</tr>
<tr>
  <th>B</th>
  <td>1</td>
  <td>0</td>
  <td>2</td>
  <td>1</td>
  <td>2</td>
  <td>1</td>
  <td>3</td>
  <td>2</td>
</tr>
<tr>
  <th>C</th>
  <td>1</td>
  <td>2</td>
  <td>0</td>
  <td>1</td>
  <td>2</td>
  <td>3</td>
  <td>2</td>
  <td>2</td>
</tr>
<tr>
  <th>D</th>
  <td>2</td>
  <td>1</td>
  <td>1</td>
  <td>0</td>
  <td>3</td>
  <td>2</td>
  <td>2</td>
  <td>1</td>
</tr>
<tr>
  <th>E</th>
  <td>1</td>
  <td>2</td>
  <td>2</td>
  <td>3</td>
  <td>0</td>
  <td>1</td>
  <td>1</td>
  <td>2</td>
</tr>
<tr>
  <th>F</th>
  <td>2</td>
  <td>1</td>
  <td>3</td>
  <td>2</td>
  <td>1</td>
  <td>0</td>
  <td>2</td>
  <td>1</td>
</tr>
<tr>
  <th>G</th>
  <td>2</td>
  <td>3</td>
  <td>1</td>
  <td>2</td>
  <td>1</td>
  <td>1</td>
  <td>0</td>
  <td>1</td>
</tr>
<tr>
  <th>H</th>
  <td>3</td>
  <td>2</td>
  <td>2</td>
  <td>1</td>
  <td>2</td>
  <td>1</td>
  <td>1</td>
  <td>0</td>
</tr>
</table>

$h_\text{min}(c_1) = 1$

<h3>Second example</h3>
<table class="wikitable">
<tr>
  <th>&nbsp;</th>
  <th>A'</th>
  <th>B'</th>
  <th>C'</th>
  <th>D'</th>
  <th>E'</th>
  <th>F'</th>
  <th>G'</th>
  <th>H'</th>
</tr>
<tr>
  <th>A'</th>
  <td>0</td>
  <td>2</td>
  <td>2</td>
  <td>4</td>
  <td>2</td>
  <td>4</td>
  <td>4</td>
  <td>6</td>
</tr>
<tr>
  <th>B'</th>
  <td>2</td>
  <td>0</td>
  <td>4</td>
  <td>2</td>
  <td>4</td>
  <td>2</td>
  <td>6</td>
  <td>4</td>
</tr>
<tr>
  <th>C'</th>
  <td>2</td>
  <td>4</td>
  <td>0</td>
  <td>2</td>
  <td>4</td>
  <td>6</td>
  <td>2</td>
  <td>4</td>
</tr>
<tr>
  <th>D</th>
  <td>4</td>
  <td>2</td>
  <td>2</td>
  <td>0</td>
  <td>6</td>
  <td>4</td>
  <td>4</td>
  <td>2</td>
</tr>
<tr>
  <th>E'</th>
  <td>2</td>
  <td>4</td>
  <td>4</td>
  <td>6</td>
  <td>0</td>
  <td>2</td>
  <td>2</td>
  <td>4</td>
</tr>
<tr>
  <th>F'</th>
  <td>4</td>
  <td>2</td>
  <td>6</td>
  <td>4</td>
  <td>2</td>
  <td>0</td>
  <td>4</td>
  <td>2</td>
</tr>
<tr>
  <th>G'</th>
  <td>4</td>
  <td>6</td>
  <td>2</td>
  <td>4</td>
  <td>2</td>
  <td>4</td>
  <td>0</td>
  <td>2</td>
</tr>
<tr>
  <th>H'</th>
  <td>6</td>
  <td>4</td>
  <td>4</td>
  <td>2</td>
  <td>4</td>
  <td>2</td>
  <td>2</td>
  <td>0</td>
</tr>
</table>

$h_\text{min}(c_2) = 2$

<h2>Detection and correction of errors</h2>
If I didn't make a typo, those tables should be symmetrical (as XOR is symmetrical) and the hamming distance of a message to itself is 0. 

The higher the minimum hamming distance of a code is, the more errors can be detected and corrected. In fact, you can quite easily quantise the relationship:

<div class="definition">Let $c$ be a code with $h_\text{min}(c) = 2e + 1 \quad e \in \mathbb{N}^+$.

$2e$ is the maximum number of errors that can be detected and $e$ is the maximum number of errors that can be corrected.</div>


A code with length $n$ which has $M$ elements and a minimum Hamming distance of $d$ is called a $(n, M, d)$-Code.

Example: $c_1$ is a $(3, 8, 1)$ code and $c_2$ is a $(6, 8, 2)$ code.

The task of coding thery is:
You're given a $n$ and a $d$ and you should find the code words so that M is as high as possible.

<h3>Example of a (6, 8, 3)-Code</h3>
$\begin{align}
c_3 = \{&(1,1,1,1,1,1),\\
&(0,0,0,0,1,1),\\
&(0,0,1,1,0,0),\\
&(0,1,0,1,0,1),\\
&(0,1,1,0,1,0),\\
&(1,0,0,1,1,0),\\
&(1,0,1,0,0,1),\\
&(1,1,0,0,0,0)\}
\end{align}
$

<h2>Hamming codes</h2>
<a href="http://en.wikipedia.org/wiki/Hamming_code">Hamming codes</a> are a family of $(2^k - 1, 2^{(2^k -1)-k}, 3), \quad k \geq 2$ codes. This means, every hamming code can only correct one error.

The idea behind Hamming codes is to save in one bit if the number of a fixed set of positions of the message is even or odd. This is called parity and done with XOR. The parity-bit is saved at the end of the message (or, just another point of view: the positions that are powers of two (1, 2, 4, 8, ...) of each message are only parity bits. This are obviously $\lceil \log_2(\text{length of code}) \rceil = \lceil \log(2^k - 1) \rceil = k$).

Wikipedia has a really nice image for that:
[caption id="attachment_47691" align="aligncenter" width="500"]<a href="http://martin-thoma.com/wp-content/uploads/2012/10/hamming-code-parity.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/10/hamming-code-parity.png" alt="Parity-bits and data bits in a Hamming codeword" title="Parity-bits and data bits in a Hamming codeword" width="500" height="95" class="size-full wp-image-47691" /></a> Parity-bits and data bits in a Hamming codeword[/caption]

Now, how are the parity-bits calculated?
Well, think of each messages as a vector in $\{0,1\}^{(2^k - 1) - k}$. Then you define a matrix $G \in \{0,1\}^{2^k - 1} \times \{0,1\}^{(2^k - 1) - k}$. Now you can get the codewords $c$ by multiplying the datawords $d$ (messages) with $G$:
$c = G \cdot d$.
This is the reason why Hamming-Codes are called "linear codes". They can be obtained by a linear function.

How do I get the generator-matrix $G$?
I don't know it and my internet searches didn't reveal any solution. Do you know one?

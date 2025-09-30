---
layout: post
lang: en
title: How many Homomorphisms exist between Z/nZ and Z/mZ?
slug: how-many-homomorphisms-exist-between-znz-and-zmz
author: Martin Thoma
date: 2013-08-27 15:26:38.000000000 +02:00
category: Mathematics
tags: Algebra
featured_image: 2013/08/algebra-thumb.jpg
---
Today I've wondered how many homomorphisms are between the groups $(\mathbb{Z}/n\mathbb{Z},+)$ and $(\mathbb{Z}/m\mathbb{Z},+)$ with $m, n \geq 2$. Does it make a difference if I use + or $\cdot$ as operators?

Let $M := (\mathbb{Z}/m\mathbb{Z},+)$ and $N := (\mathbb{Z}/n\mathbb{Z},+)$ be groups and $\varphi: M \rightarrow N$ be a group homomorphism.
Let $H := \{\varphi: M \rightarrow N\}$

Some fundamental theorems (which I'm not going to prove) are:
<ol class="roman">
  <li>$\varphi(M)$ is a group.</li>
  <li>$K_\varphi := \{m \in M | \varphi(m) = e_N\}$ is a group.</li>
  <li><a href="http://en.wikipedia.org/wiki/Lagrange%27s_theorem_(group_theory)">Lagrange's theorem</a>: $H \leq G \Rightarrow \#H | \# G$</li>
  <li>$\varphi(1)$ defines the complete homomorphism as $\varphi(n) = \varphi(1 + (n-1)) = \varphi(1) + \varphi(n-1)$</li>
  <li>$\varphi(1) = 0$ is always a homomorphism (that maps everything to 0).</li>
</ol>

<h2>$m = n$</h2>
<strong>Theorem</strong>: $n=m \Rightarrow |H|=n$
<strong>Proof</strong>:
You can map $1$ to $n$ values $\stackrel{(IV)}{\Rightarrow}$ there can't be more than $n$ homomorphisms.

For every $i \in \{0, \dots, n-1\}$ exists an homomorphism $\varphi_i(1) = i$:

\begin{align}
\varphi(a) + \varphi(b) &= (ai \mod n) + (bi \mod n)\\
&= ai + bi \mod n\\
&= (a+b)i \mod n\\
&= \varphi(a+b)
\end{align}

This means, that all of them are actually homomorphisms. For different $i,j \in \{0, \dots, n-1\}$ the homomorphisms $\varphi_i$ and $\varphi_j$ are different. So we really have $n$ homomorphisms $\blacksquare$


My first thought was that it's only a permutation, but
<table>
<tr><th>$m \in M$</th>	     <td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr>
<tr><th>$\varphi(m) \in N$</th><td>0</td><td>3</td><td>0</td><td>3</td><td>0</td><td>3</td></tr>
</table>

is not a permutation, but a homomorphism.

<h2>Distinct primes</h2>
<strong>Theorem</strong>: $n, m \in \mathbb{P}, n \neq m \Rightarrow |H| = 1$
<strong>Proof</strong>:

Let $n, m \in \mathbb{P}, n \neq m$.

<u>Part 1</u>: $1 \leq |H|$

This follows directly from (V).

<u>Part 2</u>: $|H| \leq 1$

We know that
\begin{align}
\stackrel{(I)+(III)}{\Rightarrow}        &\# \varphi(M) | \# N\\
\stackrel{n \in \mathbb{P}}{\Rightarrow} &\# \varphi(M) \in \{1, n\}
\end{align}

and

\begin{align}
\stackrel{(II)+(III)}{\Rightarrow}       &\# K_\varphi | \# M\\
\stackrel{m \in \mathbb{P}}{\Rightarrow} &\# K_\varphi \in \{1, m\}
\end{align}

Case 1: $m > n$

Now the kernel can't be trivial anymore, so $\# K_\varphi = m$. This means that everything is mapped to 0. There is only one homomorphism that does so.

Case 2: $m < n$

Now the image $\varphi(M)$ can't be all of $N$. This means $\varphi(M) = 1$ which is again the 0-mapping $\blacksquare$

<h2>Any $n$ and $m$</h2>
<strong>Theorem</strong>: $|H| = gcd(n, m)$
<strong>Proof</strong>:

First a sanity check: The theorems above are special cases of this theorem.
Let's try to prove it.

Let $n$ be composed of primes $p_1, \dots, p_x$ (where $p_i = p_j$ is allowed).
Then $N = \mathbb{Z}/n\mathbb{Z} \cong \mathbb{Z}/p_1\mathbb{Z} \times \mathbb{Z}/p_2\mathbb{Z} \times \cdots \times \mathbb{Z}/p_x\mathbb{Z}$ according to the <a href="http://en.wikipedia.org/wiki/Chinese_remainder_theorem">Chinese remainder theorem</a>. The same is true for $M$.
As there are $p_i$ homomorphisms between $\mathbb{Z}/p_i\mathbb{Z}$ and $\mathbb{Z}/p_j\mathbb{Z}$ with $p_i = p_j$ and as you can take a $p_i$ from the left and a $p_j$ from the right you can combine the different homomorphisms. So it is basically a combinatoric problem. As everything (except for same primes) will only have 1 homomorphism, you have to multiply the number of homomophisms for each pair $(p_i, p_j)$. But this is simply the gcd $\blacksquare$

<h2>$(\mathbb{Z}/n\mathbb{Z}, \cdot)$</h2>
What changes when we use $(\mathbb{Z}/n\mathbb{Z}, \cdot)$ and $(\mathbb{Z}/m\mathbb{Z}, \cdot)$?

Well, first of all $m$ and $n$ have to be primes. Otherwise, not every element would have an inverse. Second, you have to exclude 0. Which means we only use units:

$(\mathbb{Z}/n\mathbb{Z}, \cdot)^\times$ and $(\mathbb{Z}/m\mathbb{Z}, \cdot)^\times$

According to the German Wikipedia (<a href="http://de.wikipedia.org/wiki/Prime_Restklassengruppe">source</a>):


<blockquote>$(\mathbb{Z}/n\mathbb{Z})^\times$ is cyclic $:\Leftrightarrow n \in \{p^r, 2p^r | p \in \mathbb{P}, r \in \mathbb{N}_{\geq 1}\}$</blockquote>

So there is no simple way to reduce it to the same proofs.
But I've created a little <a href="https://gist.github.com/MartinThoma/6353473">script that automatically finds homomorphisms</a>.

<h2>Related</h2>
<ul>
  <li><a href="http://math.stackexchange.com/q/45663/6876">Quick way to find the number of the group homomorphisms ϕ:Z3&rarr;Z6?</a></li>
</ul>

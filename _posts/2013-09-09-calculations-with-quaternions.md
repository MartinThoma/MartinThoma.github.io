---
layout: post
title: Calculations with quaternions
author: Martin Thoma
date: 2013-09-09 14:45:17.000000000 +02:00
categories:
- Mathematics
tags:
- quaternions
featured_image: 2013/08/algebra-thumb.jpg
---
<a href="https://en.wikipedia.org/wiki/Quaternion">Quaternions</a> are an expansion of the concept of complex numbers on structures with four (instead of two) components. A quaterion $h$ can be written as a vector or in the form of $h = h_0 + ih_1 + j h_2 + kh_3$, where $i, j$ and $k$ are related to the $i$ in complex numbers. Accordingly $h_0$ is often called real part and h_1, h_2, h_3 are called imaginary part of a quaternion. 

For $i, j$ and $k$ the following rules are applied:

$i^2 = j^2 = k^2 = -1$
and
$ijk=-1$

<h2>Basic rules</h2>
From these rules follows:
$\begin{align} ij &= k\\ ji &= -k\\ jk &= i\\ kj &= -i\\ ki &= j\\ ik &= -j \end{align}$

(<a href="http://math.stackexchange.com/q/487245/6876">proof</a>)

<h2>Multiplication</h2>
Now, obviously quaternions multiplication is not commutative: $ij = k \neq -k = ji$

But for numbers in $\mathbb{R}$, it is commutative (<a href="http://math.stackexchange.com/q/488271/6876">proof</a>).

The multiplication is:

$\begin{align}
x  y 
&=( x_0 y_0 - x_1 y_1 - x_2 y_2 - x_3 y_3)\\
&+( x_0 y_1 + x_1 y_0 + x_2 y_3 - x_3 y_2) \mathrm i\\
&+( x_0 y_2 - x_1 y_3 + x_2 y_0 + x_3 y_1) \mathrm j\\
&+( x_0 y_3 + x_1 y_2 - x_2 y_1 + x_3 y_0) \mathrm k
\end{align}$

<h3>Calculating multiplicative inverse</h3>
This means, when you're given an element $x = x_0 + x_1 \mathrm i + x_2 \mathrm j + x_3 \mathrm k$ its inverse $y$ can be calculated by solving the following linear system of equations:

$\begin{align}
x_0 y_0 - x_1 y_1 - x_2 y_2 - x_3 y_3 &= 1\\
x_0 y_1 + x_1 y_0 + x_2 y_3 - x_3 y_2 &= 0\\
x_0 y_2 - x_1 y_3 + x_2 y_0 + x_3 y_1 &= 0\\ 
x_0 y_3 + x_1 y_2 - x_2 y_1 + x_3 y_0 &= 0\\
\end{align}$

which can be written as:

$\left(\begin{array}{cccc|c} 
    x_0 & -x_1 & -x_2 & -x_3 & 1\\
    x_1 &  x_0 & -x_3 &  x_2 & 0\\
    x_2 &  x_3 &  x_0 & -x_1 & 0\\
    x_3 & -x_2 &  x_1 &  x_0 & 0
  \end{array}\right).$

According to <a href="http://www.mathworks.de/de/help/aeroblks/quaternioninverse.html">mathworks</a> it is 

$y = \frac{x_0 - \mathrm i x_1 - \mathrm j x_2 - \mathrm k x_3}{x_0^2 + x_1^2 + x_2^2 + x_3^2}$

<h2>More</h2>
<h3>Conjugate</h3>
Just like the complex conjugate is defined as

$\overline{z} = a - ib$ with $z=a+ib$

the conjugate of quaternions is defined as

$\bar x := x_0-x_1\mathrm i-x_2\mathrm j-x_3\mathrm k$ with $x=x_0+x_1\mathrm i+x_2\mathrm j+x_3\mathrm k$

<h3>Rotating points</h3>
Quaternions can be used to rotate points. It works like this:

$x' = q x \overline{q}$

Pretty simple, isn't it?

For example, if you had the point (2,0,0) and you wanted to rotated it by $q = (\frac{\sqrt{2}}{2}, 0, \frac{\sqrt{2}}{2}, 0)$ you would transform (2,0,0) to (2i+0k+0j) and calculate

$\begin{align}
x' &= q x \overline{q}\\
&= (\frac{\sqrt{2}}{2}+\frac{\sqrt{2}}{2} \mathrm j) \cdot 2 \mathrm i \cdot (\frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2} \mathrm j)\\
&= (\sqrt{2} \mathrm i + \sqrt{2} \mathrm{ji}) \cdot (\frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2} \mathrm j)\\
&= (\sqrt{2} \mathrm i - \sqrt{2} \mathrm k) \cdot (\frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2} \mathrm j)\\
&= \mathrm i - \mathrm{ij} - \mathrm k + \mathrm{kj}\\
&= \mathrm{i - k -k - i}\\
&= -2 \mathrm k\\
&\Rightarrow x' = (0,0,-2)
\end{align}$

<h3>Rotation matrix to quaternion</h3>
Let $M$ be a rotation matrix and $m_{ij}$ be an entry of this matrix.

<h4>General rule</h4>

\begin{align}
s &= \frac{1}{2} \sqrt{1 + \sum_{i=1}^3 m_{ii}}\\
x &= \frac{m_{32} - m_{23}}{4s}\\
y &= \frac{m_{13} - m_{31}}{4s}\\
z &= \frac{m_{21} - m_{12}}{4s}
\end{align}

resulting in the quaternion $(s, x, y, z)$.

<h4>Special rule</h4>
A rotation matrix

$R_y = \begin{pmatrix}
\cos(\theta)  & 0 & \sin(\theta)\\
0             & 1 & 0\\
-\sin(\theta) & 0 & \cos(\theta)
\end{pmatrix}$

can be transformed to a quaternion

$q = (\cos(\frac{\theta}{2}), \vec u \sin (\frac{\theta}{2}))$

where $\vec u$ describes the axis you rotate by.

In this case $R_y$ is the y-axis, so $\vec u = \begin{pmatrix}0\\1\\0\end{pmatrix}$.


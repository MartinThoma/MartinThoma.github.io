---
layout: post
title: Why everybody should know about conditional probability
author: Martin Thoma
date: 2013-07-23 15:37:39.000000000 +02:00
category: Mathematics
tags: Stochastic, probability
featured_image: 2013/07/probability-tree.png
---
Probability theory is difficult, but I think everybody should be taught basics in this subject. Why? Because it is relevant for everybody.

Suppose you go to the doctor to make a cancer test. The test is positive. That means you have cancer, right? Wrong!

<h2>Basics</h2>
A probability is a numerical value in [0, 1] that is assigned to events (or lets rather say outcomes of an experiment). A probability can never be less than zero and never be more than one.

The sum of all probabilities of all outcomes of one experiment is always 1.

Example: Your experiment $x$ could be throwing a coin. The outcome of your experiment is either head or tails. So if
$Pr[x = \text{head}] = 0.6$, then $Pr[x = \text{tail}] = 0.4$.

Now you might argue that the coin can also stand on its border. This would result in a different model of the situation with different probabilities, e.g.:

$Pr[x = \text{head}] = 0.559$, $Pr[x = \text{border}] = 0.001$ and $Pr[x = \text{tail}] = 0.4$.

Another very important rule is Bayes rule:

$Pr[A|B] = \frac{Pr[B|A] \cdot Pr[A]}{Pr[B]}$

This works also with more variables:

$Pr[A|BC] = \frac{Pr[B|AC] \cdot Pr[A|C]}{Pr[B|C]}$

<h2>Cancer</h2>
Lets say the probability of having cancer is $Pr[C] = 0.01$. This means the probability of not having cancer is $Pr[\neg C] = 0.99$.

Now you have cancer tests. They can either be positive (+) which means they say you have cancer. Or they are negative (-), which means according to the test, you don't have cancer.

They are not always working as expected. So you get so called "false positives" and "false negatives".

A false positive is a positive result, while it should be negative. So the test says you have cancer, while you don't have cancer. It is denoted by $Pr[+ | \neg C] = 0.2$.

A false negative is a negative result, while it should be positive. So the test says you don't have cancer, but you actually have cancer. It is denoted by $Pr[- | C] = 0.1$.

You should note that $Pr[+ | \neg C] + Pr[- | C] = 0.2 + 0.1 = 0.3 \neq 1$. Why is this the case? Because the test might also not be related at all to you having cancer.

But $Pr[+ | \neg C] + Pr[- | \neg C]$ has to be 1 and $Pr[+ | C] + Pr[- | C]$ also has to be one.

So you can draw this table:

<table class="wikitable" style="width:auto;">
<tr>
  <th>$Pr[\text{Testresult}|\text{Cancer}]$</th>
  <th>$C$</th>
  <th>$\neg C$</th>
</tr>
<tr>
  <th>$+$</th>
  <td style="background-color:lime;">$0.9$</td>
  <td style="background-color:red;">$0.2$</td>
</tr>
<tr>
  <th>$-$</th>
  <td style="background-color:red;">$0.1$</td>
  <td style="background-color:lime;">$0.8$</td>
</tr>
</table>

You can see that the correct results are much more likely than the wrong ones.

<h2>Some intermediate results</h2>
How likely is a positive / negative test result?
\begin{align}
Pr[+] &= Pr[+|C] \cdot Pr[C] + Pr[+| \neg C] \cdot Pr[\neg C] = 0.207\\
Pr[-] &= Pr[-|C] \cdot Pr[C] + Pr[-| \neg C] \cdot Pr[\neg C] = 0.793
\end{align}

How likely are the combinations? (This time you don't know if you have cancer):

<table class="wikitable" style="width:auto;">
<tr>
  <th>$Pr[\text{Testresult}, \text{Cancer}]$</th>
  <th>$C$</th>
  <th>$\neg C$</th>
</tr>
<tr>
  <th>$+$</th>
  <td>$0.009$</td>
  <td>$0.198$</td>
</tr>
<tr>
  <th>$-$</th>
  <td>$0.001$</td>
  <td>$0.792$</td>
</tr>
</table>



<h2>Reversing it</h2>
It is quite likely that you would like to know how likely it is that you have cancer. Without a test, you know:

\begin{align}
Pr[C]      &= 0.01\\
Pr[\neg C] &= 0.99
\end{align}


Now you get a positive test result. How likely is it that you have cancer? In other words: Calculate $Pr[C|+]$

\begin{align}
Pr[C|+]      &= \frac{Pr[C, +]}{Pr[+]} = \frac{0.009}{0.207} = \frac{1}{23} \approx 0.043\\
Pr[\neg C|+] &= 1 - \frac{1}{23} = \frac{22}{23} \approx 0.957\\
Pr[C|-]      &= \frac{0.001}{0.793} = \frac{1}{793} \approx 0.001\\
Pr[\neg C|-] &= 1 - \frac{1}{793} = \frac{792}{793} \approx 0.999
\end{align}

How would you interpret these results? I'd say:
When you get a positive result you shouldn't really worry. But perhaps you should make other tests.
When you get a negative results you can be very sure that you don't have cancer.

<h2>Testing again</h2>
A very natural approach to a positive test result might be taking the same test again. How does this influence the probability?

There are four possibilities what could have happened:
<ul>
  <li>You have cancer:
    <ul>
      <li>Second test was negative</li>
      <li>Second test was positive</li>
    </ul>
  </li>
  <li>You don't have cancer:
    <ul>
      <li>Second test was negative</li>
      <li>Second test was positive</li>
    </ul>
  </li>
</ul>

First of all, I compare some intermediate results

\begin{align}
Pr[++] &= Pr[C] \cdot Pr[+|C] \cdot Pr[+|C] + Pr[\neg C] \cdot Pr[+|\neg C] \cdot Pr[+|\neg C]\\
       &= 0.477 \neq 0.042849 = 0.207^2 = (Pr[+])^2\\
Pr[+-] &= Pr[C] \cdot Pr[+|C] \cdot Pr[-|C] + Pr[\neg C] \cdot Pr[+|\neg C] \cdot Pr[-|\neg C] \\
       &= 0.01 \cdot 0.9 \cdot 0.1 + 0.99 \cdot 0.2 \cdot 0.8\\
       &= 0.1593\\
Pr[C,+,+] &= Pr[C] \cdot Pr[+ | C]^2 = 0.01 \cdot 0.9^2 = 0.0081\\
Pr[C,+,-] &= Pr[C] \cdot Pr[+ | C] \cdot Pr[-|C] = 0.01 \cdot 0.9 \cdot 0.1 = 0.0009\\
Pr[C|++] &= \frac{Pr[C,+,+]}{Pr[++]} = \frac{0.0081}{0.207^2} = \frac{9}{530} \approx 0.170\\
Pr[C|+-] &= \frac{Pr[C,+,-]}{Pr[+-]} = \frac{0.0009}{0.1593} = \frac{1}{177} \approx 0.006
\end{align}

Woooha! So if one test says you have cancer, don't worry. When two tests say you have cancer, you have a 17% chance of having cancer.

On the other hand: One negative and one positive test is better than no test at all, because without a test you have a probability of 0.01 to have cancer. With both tests, you only have a probability of 0.006.

<h2>Why probability is important for you</h2>
As you might have seen, your intuition about probability is wrong. But we hear numbers all the time. It is important for us to understand them, so we should drop our intuition and learn how to use those numbers.

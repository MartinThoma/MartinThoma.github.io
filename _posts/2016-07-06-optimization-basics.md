---
layout: post
title: Optimization Basics
slug: optimization-basics
author: Martin Thoma
date: 2016-07-06 20:00
category: Machine Learning
tags: Machine Learning, optimization, gradient descent
featured_image: logos/ai.png
---
Optimization is a subfield of mathematics / computer science which deals with finding the best solution. Typically, problems in optimization are stated like this:

$$
\begin{align}
&\underset{x}{\operatorname{minimize}}& & f(x) \\
&\operatorname{subject\;to}
& &g_i(x) \leq 0, \quad i = 1,\dots,m \\
&&&h_i(x) = 0, \quad i = 1, \dots,p
\end{align}
$$

where

* $f(x): \mathbb{R}^n \to \mathbb{R}$ is the **loss function (objective function)** to be minimized over the variable $x$,
* $g_i(x) \leq 0$ are called **inequality constraints**, and
* $h_i(x) = 0$ are called **equality constraints**.

By convention, the standard form defines a **minimization problem**. A
**maximization problem** can be treated by negating the objective function.

(That was copied from [en.wikipedia.org/w/Optimization_problem](https://en.wikipedia.org/w/index.php?title=Optimization_problem&oldid=715562612#Continuous_optimization_problem) and only slightly edited.)


I'm now going to explain some very basic techniques which are used for finding good solutions to optimization problems. Please note that there are also discrete optimization problems where you have to finde a solution $x \in \mathbb{N}^n$. I will only focus on continuous optimization problems.


## Simulated Annealing

Simulated Annealing is a heuristical optimization algorithm. It starts at a
random point $x \in \mathbb{R}^n$. Then it takes a random point $y$ of the
environment of $x$:

$$y \in U(x)$$

If $f(y) \leq f(x)$, then the current position $x$ is overwritten with $y$:

$$x \leftarrow y$$

Otherwise, it might be overwritten with probability $\exp \left (-\frac{f(y)-f(x)}{T(t)} \right )$ where $T: \mathbb{N}_0 \rightarrow \mathbb{R}_{> 0}$ is called the temperature at time $t$.

So the optimization algorithm is:

<ol>
    <li>Take a random point $x \in \mathbb{R}^n$</li>
    <li>Take a random point $y \in U(x)$</li>
    <li>$$x \leftarrow \begin{cases}y &\text{if } f(y) \leq f(x)\\
                          y &\text{if } \operatorname{rand}(0,1) < \exp \left (-\frac{f(y)-f(x)}{T(t)} \right )\\
                          x &\text{otherwise}\end{cases}$$</li>
    <li>Go to step 2.</li>
</ol>




See also my [German description](https://martin-thoma.com/neuronale-netze-vorlesung/#simulated-annealing).


## Gradient descent

The gradient descent algorithm can easily be applied when the optimization problem has no constraints and the objective function $f$ is differentiable.
The idea is to just take a random starting point $x \in \mathbb{R}^n$ and
iteratively improve it. There are many algorithms which follow this approach (Simulated annealing, L-BFGS, Newton's method, Quasi-Newtonian, Conjugate Gradient, ...).

Instead of randomly going in other directions, the
gradient $\nabla f$ is calculated at the position $x$. The gradient points
in the direction of maximum increase, so we go in the opposite direction:

$$x_{\text{new}} = x - \nabla f(x)$$

The problem with this approach is that the surface of the objective function
might first go down in the direction of $\nabla f(x)$, but if you go a bit
further it can go up by a lot. So we want to make very small steps. To achive
this, we multiply the gradient with a factor $\eta \in (0, 1]$. In machine
learining, this $\eta$ is called the *learning rate* and typically one
chooses $\eta = 0.01$. However, there are [learning rate scheduling algorithms](https://martin-thoma.com/neuronale-netze-vorlesung/#learning-rate-scheduling) which adapt this parameter during training.

The update rule is:

$$x_{\text{new}} = x - \eta \nabla f(x)$$


### Iterative Descent

A more general formulation of the Gradient descent algorithm is called
iterative descent. The idea is to start at some arbitrary $x_0$ and iteratively
update the current guess of the minimum to

$$x_{k+1} = x_k + \eta \cdot d_k$$

where $\eta \in (0, 1]$ is the step length (learning rate) and

$$d_k = -D_k \nabla f(x_k)$$

is the direction of the descent. The direction depends on the Gradient
$\nabla f(x_k)$, but also on a matrix $D_k$:

<ul>
    <li>$D_k = I$: Gradient descent</li>
    <li>$D_k = H_f^{-1}(x_k)$: Newtons method, where $H_f$ is the <a href="https://en.wikipedia.org/wiki/Hessian_matrix">Hessian matrix</a> of $f$</li>
</ul>


## Linear Regression with MSE

In linear regression one is given a list of $n$ points $(x, y)$ with $x \in \mathbb{R}^m$ and $y \in \mathbb{R}$. The task is to find a matrix $A \in \mathbb{1 \times m}$ such that the predicted value $\hat{y}$ of the linear model

$$\hat{y}(x) = A \cdot x$$

minimizes the term

$$\text{MSE} = \sum_{i=1}^n (y_i - \hat{y}(x_i))^2$$

For convenience, one can write the list of points as a matrix $\mathbf{X} \in \mathbb{R}^{n \times m}$ and
a vector $\mathbf{y} \in \mathbb{R}^n$:

$$\text{MSE} = \|\mathbf{y} - \mathbf{X} A^T\|_2$$

with the Euclidean norm

$$\| v \|_2 := \sqrt{ ( v_1 )^2 + ( v_2 )^2 + \dotsb + ( v_n )^2 } = \left( \sum_{i=1}^n ( v_i )^2 \right)^{1/2}$$

Every part of the sum is non-negative, so exponentiating the Euclidean norm
with a positive factor will not change the result of the minimization:

$$\operatorname{minimize}_{A} \|\mathbf{y} - \mathbf{X} A^T\|_2^2$$

Now we can see that this is every element of the vector squared. So we can
get rid of the norm and then use distributivity:

$$
\begin{align}
\operatorname{minimize}_{A}&(\mathbf{y} - \mathbf{X} A^T)^T \cdot (\mathbf{y} - \mathbf{X} A^T)\\
\Leftrightarrow \operatorname{minimize}_{A}&(\mathbf{y}^T - A \mathbf{X}^T) \cdot (\mathbf{y} - \mathbf{X} A^T)\\
\Leftrightarrow \operatorname{minimize}_{A}&\mathbf{y}^T \mathbf{y} - A \mathbf{X}^T \mathbf{y} - \mathbf{y}^T \mathbf{X} A^T + A\mathbf{X}^T \mathbf{X} A^T\\
\end{align}
$$

You need to know that

$$
\begin{align}
A \mathbf{X}^T \mathbf{y} &= ((A \mathbf{X}^T \mathbf{y})^T)^T\\
&= (\mathbf{y}^T \mathbf{X} A^T)^T\\
&= \mathbf{y}^T \mathbf{X} A^T\\
\end{align}
$$

You can get rid of the last transposing operation, because
$$(\mathbf{y}^T \mathbf{X} A^T) \in \mathbb{R}^{1 \times 1}$$

This simplifies the optimization problem to

$$\operatorname{minimize}_{A}\underbrace{\mathbf{y}^T \mathbf{y} - 2 A \mathbf{X}^T \mathbf{y} + A\mathbf{X}^T \mathbf{X} A^T}_{E_{X, y}(A)}$$

Now you can calculate the gradient of this term with respect to $A$:

$$\nabla E_{X, y}(A) = 2 X^T X A^T - X^T y - X^T y = 2 X^T (X A^T - y)$$

A necessary condition of a minimum is the gradient to be 0:

$$
\begin{align}
\nabla E_{X, y}(A) &\overset{!}{=} 0\\
\Leftrightarrow 0 &\overset{!}{=} 2 X^T (X A^T - y)\\
\Leftrightarrow 0 &\overset{!}{=} X^T X A^T - X^T y\\
\Leftrightarrow A &\overset{!}{=} ((X^T X)^{-1} X^T y)^T\\
\end{align}
$$

As $H_{E_{X, y}} = \nabla^2 E_{X, y}(A) = 2 X^T X$ is positive definite, this is a minimum. Hence, the optimal solution to this problem is:

$$A = ((X^T X)^{-1} X^T y)^T$$


## Lagrange multipliers

Lagrange multipliers are a trick in optimization problems with constraints.
They can be used to get rid of the constraints.

The Lagrange function has the form

$$\mathcal{L} (x, \lambda_1, \dots, \lambda_n) = f(x) + \sum_{j=1}^n \lambda_j h_j(x)$$
with the *Lagrange multipliers* $\lambda_j \in \mathbb{R}$ and $h_j$ are equality constraints.<br/>
<br/>
Necessary conditions for a minimum $x^*$ is:

<ul>
    <li>$\nabla_x \mathcal{L} = \nabla_x f(x^*) + \sum_{j=1}^n \lambda_j \nabla_x h_j(x^*) \overset{!}{=} 0$</li>
    <li>$\frac{\partial}{\partial \lambda_j} \mathcal{L} = h_j(x^*) \overset{!}{=} 0, \quad j=1, \dots, $</li>
</ul>

See [<a href="#ref-smi04" name="ref-smi04-anchor">Smi04</a>] for many examples.


## Optimization Problem characteristics

There are some properties of optimization problems which make it easier / harder
to solve:

<table>
    <tr>
        <th>Property</th>
        <th>Easy</th>
        <th>Hard</th>
    </tr>
    <tr>
        <td>Objective</td>
        <td>linear</td>
        <td>non-linear</td>
    </tr>
    <tr>
        <td>Optimization Variable</td>
        <td>small discrete, continuous</td>
        <td>large discrete</td>
    </tr>
    <tr>
        <td>Constraints</td>
        <td>No Constraints</td>
        <td>Constraints</td>
    </tr>
</table>


## Resources

* Reddit: [Overview of Optimization Algorithms](https://www.reddit.com/r/MachineLearning/comments/4582s0/overview_of_optimization_algorithms/)


## References

* [<a href="#ref-smi04-anchor" name="ref-smi04">Smi04</a>] B. T. Smith, “Lagrange multipliers tutorial in the context of support
  vector machines,” Memorial University of Newfoundland St. John’s,
  Newfoundland, Canada, Jun. 2004.

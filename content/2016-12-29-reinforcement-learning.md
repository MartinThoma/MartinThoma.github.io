---
layout: post
lang: en
title: Reinforcement Learning
slug: reinforcement-learning
author: Martin Thoma
date: 2016-12-29 20:00
category: Machine Learning
tags: Machine Learning, RL
featured_image: logos/ml.png
---
Reinforcement learning is a sub-field of mathematics and computer science. It
deals with the following kind of problems: You're given a set of states
$\mathcal{X} \subseteq \mathbb{R}^n$ and a starting state $x_0 \in \mathcal{X}$.
For every time step $k = 0, 1, 2, \dots$ you have a set of possible actions,
depending on your current state:
$$\mathcal{A}_k(x_k)$$
Depending on what your action and your current state is, the new state is
$$P(x_k, a_k, x_{k+1}) \in [0, 1]$$
So the transition from state $x_k$ to state $x_{k+1}$ with action $a_k$ is
stochastic.

For some states $x_k$, actions $a_k$ at time $k$, you receive rewards:

$$r_k(x_k, a_k) \in \mathbb{R}$$

Your goal is to maximize

$$\mathbb{E}(\sum_{k=0}^\infty \gamma^k \cdot r_k(x_k, a_k))$$

where $\gamma in (0, 1)$ is a discounting factor which makes sure we don't get
infinite rewards. $\gamma = 0.99$ is a typical choice.


## Applications

This very general problem description can be applied in almost any scenario:

* Learning automatically to play games
* Learning to control robots


## Why RL is difficult

* Credit assignment: In chess, you only get a reward (positiv or negative) at
  the end of the game. How to you tell which move was good or bad?
* [Exploration vs. exploitation](https://martin-thoma.com/probabilistische-planung/#exporation-exploitation):
  When should you stick to what you know and when should you try something new?
* State equivalence: Typically, your state is very high-dimensional. For example
  when learning very old computer games from raw pixels you have
  $$210 \cdot 160 \cdot 3 = 100800$$
  dimensions in your feature vector. But the relevant game states might be
  much less.


## Approaches

A **policy network** gets the state as input and outputs the action. It learns
by executing many episodes (e.g. a complete game; from start until you reach a
final state or at least a state with reward) and labels all actions before with
the received reward. There might be many which were good even in a lost game,
but in average you expect to punish bad decisions and encourage good decisions.


## Resources

If you are a student at KIT, I can recommend to visit the lecture
[Probabilistic Planning](https://martin-thoma.com/probabilistische-planung/).

Other resources you might want to have a look at:

* [Deep Reinforcement Learning: Pong from Pixels](http://karpathy.github.io/2016/05/31/rl/)
    * [Pong example](https://gist.github.com/karpathy/a4166c7fe253700972fcbc77e4ea32c5)
* [Guest Post (Part I): Demystifying Deep Reinforcement Learning](https://www.nervanasys.com/demystifying-deep-reinforcement-learning/)
* [Human-level control through deep reinforcement learning](http://www.nature.com/nature/journal/v518/n7540/pdf/nature14236.pdf) by V. Mnih et al.
    * [Playing Atari with Deep Reinforcement Learning](http://arxiv.org/abs/1312.5602) on arXiv
* [Deterministic Policy Gradient Algorithms](http://jmlr.org/proceedings/papers/v32/silver14.pdf)

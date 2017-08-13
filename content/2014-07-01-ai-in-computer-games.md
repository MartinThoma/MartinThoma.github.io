---
layout: post
title: A.I. in Computer Games
author: Martin Thoma
date: 2014-07-01 23:52
category: Machine Learning
tags: AI, games, Machine Learning
featured_image: logos/ai.png
---

Artificial Intelligences (A.I.s) are computer programs that are able to adjust
their behaviour according to data they see. So A.I.s are able to adjust to
the data a human player generates.

<figure>
    <img src="http://imgs.xkcd.com/comics/game_ais.png" alt="Game A.I.s">
    <figcaption>Game A.I.s</figcaption>
</figure>


## Solved games

There is a number of games which are definitely solved. That means the A.I.
plays perfectly:

* Tic-Tac-Toe
* Connect Four: [A Knowledge-based Approach of Connect-Four](http://www.informatik.uni-trier.de/~fernau/DSL0607/Masterthesis-Viergewinnt.pdf). Amsterdam, 1988. Victor Allis.
* Checkers:

See also: [Solved Game](https://en.wikipedia.org/wiki/Solved_game)

## Computers win always

A second category are games in which A.I.s always win against human players, but
they don't have a perfect strategy. Or at least we have not proven that they
have a perfect strategy:

* Chess
* Go on a 5×5 board
* Reversi on a 4×4 board


Update: There are advances on the 19×19 field:

* [Paper](https://storage.googleapis.com/deepmind-data/assets/papers/deepmind-mastering-go.pdf)
* Nature: [Mastering the game of Go with deep neural networks and tree search](http://www.nature.com/nature/journal/v529/n7587/full/nature16961.html)
* YouTube by nature: [The computer that mastered Go](https://www.youtube.com/watch?v=g-dKXOlsf98)
* Google Blog: [AlphaGo: using machine learning to master the ancient game of Go](https://googleblog.blogspot.de/2016/01/alphago-machine-learning-game-go.html)


## Unspecialized Game A.I.s

The following video is an explanation and demo of software Tom Murphy VII wrote that learns how to play a Nintendo Entertainment System game and then automatically plays it.
It's called "learnfun" (for learn function).

You might want to skip to 6:13 for the demo:

<iframe width="512" height="288" src="//www.youtube.com/embed/xOCurBYI_gY" frameborder="0" allowfullscreen></iframe>

Interesting parts:

* `09:46` - Ridiculous Super Mario move
* `14:20` - Super packman move
* `15:57` - Tetris: The best move is not to play

Research paper published in SIGBOVIK 2013: "[The first level of Super Mario Bros. is easy with lexicographic ordering a and time travel ...after that it gets a little tricky](http://tom7.org/mario/mario.pdf)."

There is a follow-up video with Zelda, Punch-Out, Dr. Mario (10:27), Contra
(12:10), Wall Street Kid (14:30) and Russian Attack (18:10):

<iframe width="512" height="288" src="//www.youtube.com/embed/YGJHR9Ovszs?list=UU3azLjQuz9s5qk76KEXaTvA" frameborder="0" allowfullscreen></iframe>

Interesting parts:

* `10:25` - Exploiting a Random number generator in Dr. Mario
* `18:15` - Russian Attack: Finding a save spot
* `20:58` - Russian Attack: Fight fast

And a third episode with Super Mario, Gradius (4:06), Mega Man 2 (8:30), Pro
Wrestling, Color a Dinosaur, Nintendo Pinball (13:40), Cliffhanger (15:20),
Arkanoid (16:33), Double Dare (19:22), Ice hockey (21:44):

<iframe width="512" height="288" src="//www.youtube.com/embed/Q-WgQcnessA" frameborder="0" allowfullscreen></iframe>

Interesting parts:

* `04:45`: Playing Gradius like a YoLo-Pro
* `05:42`: Gradius - Insta-Kill the Boss
* `10:04`: Mega Man 2 - Manipulate the random number generator
* `16:33`: Arkanoid (Break Out) - Manipulate the random number generator

## Super Mario A.I. Competition

<iframe width="512" height="288" src="//www.youtube.com/embed/bBZ7kEphv3s?start=385" frameborder="0" allowfullscreen></iframe>

## DOTA: Dendi vs. OpenAI

<iframe width="512" height="288" src="https://www.youtube.com/embed/wiOopO9jTZw" frameborder="0" allowfullscreen></iframe>
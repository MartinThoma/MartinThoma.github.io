---
layout: post
title: How well can ChatGPT play Code Names?
slug: how-well-can-chatgpt-play-code-names
lang: en
author: Martin Thoma
date: 2023-08-01 18:44
category: Machine Learning
tags: AI, Board Game
featured_image: logos/ai.png
summary: Experiment how well ChatGPT can play the association game “Code Names” (2023 Edition)
medium_url: https://medium.com/@martinthoma/how-well-can-chatgpt-play-code-names-9c3af9e52b4c
---
<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-1.jpg"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-1.jpg" alt="The Codenames board with 25 word cards, colored in red, blue, neutral and one black card (BOIL)" width="800" height="521"></a>
</figure>

You are playing the association game “Code Names”. The words are:

* Blue: ski, star, fish, blind, tip, file, cotton, scarecrow
* Red: bond, sound, park, penny, bee, tokyo, walrus, hospital, scuba diver
* Black: boil
* neutral: angel, captain, bass, casino, day, goldilocks, field

You are the red spy master. It’s your turn. Give a single word hint for your team.

Red Spy master:

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-2.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-2.png" alt="ChatGPT as the red spymaster gives the hint “underwater” and, when asked, the number 2" width="800" height="381" loading="lazy"></a>
</figure>

Red Team:

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-3.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-3.png" alt="Prompt with the Codenames board and the hint “Underwater, 2” for the red team; ChatGPT guesses “scuba diver”" width="800" height="410" loading="lazy"></a>
</figure>

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-4.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-4.png" alt="ChatGPT continues with the guess “fish”, which is a blue card, so the blue team’s turn begins" width="800" height="306" loading="lazy"></a>
</figure>

Blue spy master:

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-5.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-5.png" alt="Prompt with all words by color for the blue spymaster; ChatGPT gives the hint “winter, 2”" width="800" height="385" loading="lazy"></a>
</figure>

Blue team:

<div class="gallery">
    <figure>
        <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-6.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-6.png" alt="ChatGPT as the blue team guesses “ski” for the hint “winter, 2”" width="800" height="114" loading="lazy"></a>
    </figure>
    <figure>
        <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-7.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-7.png" alt="Prompt with the remaining board; ChatGPT as the blue team continues with the guess “penny” for “winter, 2”" width="800" height="459" loading="lazy"></a>
    </figure>
    <figure>
        <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-8.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-8.png" alt="Meme face with the text “Penny comes to your mind when you think about winter? Before star or angel?”" width="416" height="489" loading="lazy"></a>
    </figure>
</div>

Board:

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-9.jpg"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-9.jpg" alt="The Codenames board after the first round: scuba diver, fish, ski and penny are revealed" width="800" height="521" loading="lazy"></a>
</figure>

Red Spy master:

<div class="gallery">
    <figure>
        <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-10.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-10.png" alt="Prompt with the remaining words for the red spymaster; ChatGPT gives the hint “day, 2”, although day is a word on the board" width="800" height="399" loading="lazy"></a>
    </figure>
    <figure>
        <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-11.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-11.png" alt="After the reminder not to use words from the board, ChatGPT gives the hint “cornfield, 2”" width="800" height="179" loading="lazy"></a>
    </figure>
    <figure>
        <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-12.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-12.png" alt="Meme of a confused man holding his head: “Cornfield? You know that scarecrow is your opponent’s word?”" width="420" height="333" loading="lazy"></a>
    </figure>
</div>

Red Team:

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-13.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-13.png" alt="Jup. Super reasonable. Scarecrow is the opponent’s word and field is neutral. Awesome." width="800" height="550" loading="lazy"></a>
    <figcaption>Jup. Super reasonable. Scarecrow is the opponent’s word and field is neutral. Awesome.</figcaption>
</figure>

Blue Spy master:

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-14.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-14.png" alt="Prompt with the remaining cards for the blue spymaster; ChatGPT gives the hint “movie, 2”" width="800" height="538" loading="lazy"></a>
</figure>

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-15.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-15.png" alt="Angry meme face: “Movie?!?! Your opponent has Bond and Tokyo”" width="402" height="408" loading="lazy"></a>
</figure>

Blue Team

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-16.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-16.png" alt="At least the team is reasonable now" width="800" height="386" loading="lazy"></a>
    <figcaption>At least the team is reasonable now</figcaption>
</figure>

Board:

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-17.jpg"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-17.jpg" alt="The Codenames board after the second round: bond and scarecrow are revealed as well" width="800" height="521" loading="lazy"></a>
</figure>

Red Spy master:

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-18.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-18.png" alt="Prompt asking for a word associated with as many red words as possible and none of the others; ChatGPT answers “Arctic”" width="800" height="335" loading="lazy"></a>
</figure>

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-19.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-19.png" alt="Asked which words the team should guess, ChatGPT as the red spymaster expects only “walrus” for the hint “Arctic”" width="800" height="367" loading="lazy"></a>
</figure>

Red Team:

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-20.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-20.png" alt="Prompt with the remaining board and the hint “Arctic, 1”; ChatGPT as the team guesses “walrus”" width="800" height="381" loading="lazy"></a>
</figure>

Blue Spy master

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-21.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-21.png" alt="Prompt with the remaining cards for the blue spymaster; ChatGPT gives the hint “constellation, 3”" width="800" height="298" loading="lazy"></a>
</figure>

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-22.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-22.png" alt="That is the type of hint I was hoping for!" width="800" height="341" loading="lazy"></a>
    <figcaption>That is the type of hint I was hoping for!</figcaption>
</figure>

Blue Team:

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-23.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-23.png" alt="Interesting thoughts — if only your spy master was thinking the same way." width="800" height="367" loading="lazy"></a>
    <figcaption>Interesting thoughts — if only your spy master was thinking the same way.</figcaption>
</figure>

Board:

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-24.jpg"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-24.jpg" alt="The Codenames board after the third round, with walrus, star and blind revealed" width="800" height="520" loading="lazy"></a>
</figure>

Red Spy Master

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-25.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-25.png" alt="ChatGPT as the red spymaster gives the hint “Metropolis” and wants the team to guess Tokyo, hospital and sound" width="800" height="573" loading="lazy"></a>
</figure>

Red team:

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-26.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-26.png" alt="For the hint “Metropolis, 3”, ChatGPT as the red team guesses angel, Tokyo and casino" width="800" height="448" loading="lazy"></a>
</figure>

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-27.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-27.png" alt="I’m speechless. The first guess should have been Tokyo for sure." width="409" height="406" loading="lazy"></a>
    <figcaption>I’m speechless. The first guess should have been Tokyo for sure.</figcaption>
</figure>

Blue Spy master:

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-28.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-28.png" alt="ChatGPT as the blue spymaster gives the hint “document, 2” for file and cotton, because cotton is used to make paper" width="800" height="560" loading="lazy"></a>
</figure>

Blue Team:

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-29.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-29.png" alt="For the hint “document, 2”, ChatGPT as the blue team guesses file and then hospital" width="800" height="487" loading="lazy"></a>
</figure>

Board:

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-30.jpg"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-30.jpg" alt="The Codenames board after the fourth round, with angel, file and hospital revealed as well" width="800" height="524" loading="lazy"></a>
</figure>

Red Spy Master:

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-31.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-31.png" alt="ChatGPT as the red spymaster gives the hint “Buzz” for sound, bee and Tokyo" width="800" height="416" loading="lazy"></a>
</figure>

Red Team:

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-32.png"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-32.png" alt="For the hint “buzz, 3”, ChatGPT as the red team guesses bee, sound and the black card boil" width="800" height="388" loading="lazy"></a>
</figure>

<figure>
    <a href="../images/2023/08/how-well-can-chatgpt-play-code-names-33.jpg"><img src="../images/2023/08/how-well-can-chatgpt-play-code-names-33.jpg" alt="The final Codenames board: the red team guessed the black card boil and lost" width="800" height="520" loading="lazy"></a>
</figure>

This small experiment was disappointing. As so often, letting ChatGPT explain itself improved the situation. Likely I could have given it better prompts, e.g. by repeating more of the past. But not getting the first one right is a rare occasion in my playing rounds. And there it was the norm.

Maybe we should start making “Human against the Machine” tournaments with Code Names 😄

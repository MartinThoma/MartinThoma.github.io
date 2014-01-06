---
layout: post
title: Password Changing Services
author: Martin Thoma
date: 2011-10-17 08:10:43.000000000 +02:00
categories:
- The Web
tags:
- Web Development
- IT-Security
- password
featured_image: 2011/10/password-checker.png
---
Today I've changed my PayPal password, because I thought it was time to do so. Now I know that the password changing service of PayPal can be improved quite a lot. I had to type the password about twelve times! This is the reason why I thought it was time to create some principles for good password chaning services:

<strong>User authentification</strong>: It is important that only the user can change the password. You have to force the user to type in his old password again. This should be done as a first step in the authentification. Nothing is more frustrating than beeing forced to type in your old password again and again as your new password wasn't valid. You could check if he typed in his old password less than a minute ago.

<strong>Eliminate typos</strong>: Like every good service, PayPal wants you to type the password and the verification. It would be good, if two symbols were added to the textbox. One for the activiation of <a href="http://en.wikipedia.org/wiki/Caps_lock">caps lock</a> and one for <a href="http://en.wikipedia.org/wiki/Num_lock">num lock</a>. I think this has to be done by the browser.

<strong>Clientside validation</strong>: The first time, I used a password which was considered as weak. A JavaScript informed me that it was weak, but I could submit the form. The form should be validated on the client. If it is not valid, don't let him submit the form. (The password has to be validated also on the server, of course.)

<strong>Allow all characters</strong>: I was very negatively surprised as I was informed that PayPal doesn't allow "non-printable characters" like spaces. They informed me after I submitted, of course.
It does make sense to warn the user if he uses special characters which might be difficult to type on other systems, like german umlauts (&auml;&ouml;&uuml;&Auml;&Ouml;&Uuml;&szlig;). But why the hell do they force me to use underscores instead of spaces? Do they print my password? Do they want that I print my password?


<strong>Allow "weak" passwords</strong>: 
You should not allow weak passwords, of course. But you should have a good definition of weak. Less than 6 characters is weak. I wanted to use a 26-character password with upper- and lower case letters, spaces and one special character. This was considered as weak. If you read <a href="../md5-cracking/" title="MD5 cracking">my post about MD5 cracking</a> you have probably noticed, that it is much harder to crack a 26-character password with only lower case letters than a 8 character password with lower case, upper case and numbers. About $10^{22}$ times as much passwords are possible with 26 characters and 26 letters than with a character-space of 62 elements but only 8 places (see <a href="http://www.wolframalpha.com/input/?i=26^26%2F%2826*2%2B10%29^8">Wolfram|Alpha</a>). You can easily build a password if you use a sentence, not a word. This will be long and will quite possibly only have lower case letters, spaces and one upper case letter, but it is possible to remember it.
{% caption align="aligncenter" width="740" caption="Password Strength" url="http://imgs.xkcd.com/comics/password_strength.png" alt="Password Strength"  height="601" class="size-medium" %}

<strong>Allow long passwords</strong>: As the passwords should not be stored as plaintext, but hashed it doesn't really matter how long they are. If you use MD5, it will always take 32 characters. Why should you limit a user to only 20 characters (like PayPal does)? If the 26 character password is easier to remember, why do you want to restrict him to a shorter password which is easier to crack?

I made the same annoying experiences with the password of my students account for university. They forced me to use a short password with a lower case and upper case letters, digits and special characters.

Do you have some more suggestions for good passwords? Which websites have a very good password changing service?

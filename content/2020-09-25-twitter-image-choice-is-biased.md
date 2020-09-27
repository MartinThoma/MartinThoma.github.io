---
layout: post
title: How Twitter’s Image Choice is Biase
slug: twitter-image-choice-is-biased
URL: https://towardsdatascience.com/how-twitters-image-choice-is-biased-8d3f0ba63379
author: Martin Thoma
date: 2020-09-25 20:00
category: My bits and bytes
tags: Twitter, Technology, Machine Learning, Social Media, Artificial Intelligence
featured_image: logos/star.png
---
![Photo by [Ravi Sharma](https://unsplash.com/@ravinepz?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/10368/0*zuJRjBe7Su-ygZMJ)*Photo by [Ravi Sharma](https://unsplash.com/@ravinepz?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*

Twitter shows preview-images of shared images. If the aspect ratio is not the wanted one, the image needs to be cropped for the preview.

The way the cropping is done is supposedly not random. People seem to think that it is “smart” in the sense that it chooses an interesting or reasonable part of the image. Maybe a crop is chosen that maximizes clicks.

So far, so good. But now there is this:

<iframe src="https://medium.com/media/2bb8dd06753f3b0f9e91f064ac8371bc" frameborder=0></iframe>

You might not be able to see it, but there are two times two images: One of Senator McConnell and one of the former president Obama. Twitter chose to show McConnel for both images.

The German comedian Abdelkarim was pointing to Twitter showing preferably blonde people:

<iframe src="https://medium.com/media/afc725dd42bbd294aa937786e3914e16" frameborder=0></iframe>

There are [many](https://twitter.com/_jsimonovski/status/1307542747197239296) [tweets](https://twitter.com/JefCaine/status/1307441209338544148) like this. For many, the impression seems to be that this bias towards some pictures is racist.

## Are white people shown more often than black people in Twitter previews?

The [follow-up tweets](https://twitter.com/bascule/status/1307440596668182528) are for sure very interesting and indicate that there could be an issue. From an outsider’s perspective, it’s pretty hard to tell. Twitter certainly receives many thousands of images and creates previews for them. A reasonable objective for a company is to maximize clicks. For example, Twitter could simply change the preview image depending on the user. This would mean that Twitter tries to estimate which users click more often on which types of images. If the user clicks more often on white people, then it shows more often white people.

I’m not saying that this is what happens, but it could be.

Let’s assume it’s not. Let’s assume everybody sees the same preview images in all cases. Then you could still optimize globally for click rates. If the Twitter population clicks more often on white people, the Twitter population get’s to see white people.

## Biased Data Leads to Biased Results

In 2016, the Guardian published a very related article about an AI judging beauty and preferring white people:
[**A beauty contest was judged by AI and the robots didn’t like dark skin**
*The first international beauty contest judged by “machines” was supposed to use objective factors such as facial…*www.theguardian.com](https://www.theguardian.com/technology/2016/sep/08/artificial-intelligence-beauty-contest-doesnt-like-black-people)

There is a key takeaway in this article:
> # Machine Learning systems need data. If the data has issues, the Machine Learning system has issues.

The AI was trained on a dataset with few black people. The generalization the machine learning algorithm took from that is that being black does not correlate well with winning this contest. Which is correct. The gap where it becomes problematic is that it was used to judge “objective” beauty. It’s a machine, it can’t be biased. Right?

## Bias and Racism

This for sure is interesting trivia, but does it have a bigger effect? Is the effect of less exposure on Twitter even negative?

It’s weird for sure, it should be fixed for sure. I wouldn’t call it racist, though. In my opinion, it’s very unlikely that some Twitter developers had the evil master plan to harm black people by preferring to show white people in case two image crops are possible. Calling this racist distracts from the [many](https://www.theguardian.com/us-news/2020/aug/27/white-supremacists-militias-infiltrate-us-police-report) [real](https://www.nytimes.com/2020/05/27/opinion/racism-white-women.html) [racist](https://abcnews.go.com/US/bbq-becky-golfcart-gail-list-unnecessary-911-calls/story?id=58584961) [cases](https://en.wikipedia.org/wiki/Killing_of_George_Floyd) we have seen in the past few months. Events where one knows that the actors were aware of the effects their actions can have. Events where the effect was death.

A software developer writing a slightly smarter algorithm for image cropping than just taking a random crop is not racist. If the following statement is correct, it’s simply sloppy work.

I’ve also tried this myself by uploading an image with the four Teletubbies. You could now be outraged that it shows a white-only image or just conclude that the algorithm is pretty bad:

<iframe src="https://medium.com/media/2a9d93a6d8cbc33b3df83c1a465f8bea" frameborder=0></iframe>

## What can we do against biased AI products?

One simple reason why the algorithm might be biased is class imbalance. This can also be combined with a mismatch of the training data compared to the production data. One class is just represented way more often in the training dataset. One technique to deal with more frequent classes is to over-sample the less frequent ones or to under-sample the more frequent ones. Meaning the algorithm gets to see the training data of the under-represented class more often.

Very often, it is also possible to find application-specific solutions. For example, Twitter could simply not show preview images at all. Or show a random crop. Letting the user choose the crop would also be an option. Google also chose a drastic option when they faced bias issues in a machine learning product:
[**Google’s solution to accidental algorithmic racism: ban gorillas**
*After Google was criticized in 2015 for an image-recognition algorithm that auto-tagged pictures of black people as…*www.theguardian.com](https://www.theguardian.com/technology/2018/jan/12/google-racism-ban-gorilla-black-people)

Post-processing is another option. If you notice that two candidates for good crops both contain faces, flip a coin which face to show. You can also try to be super smart about it, recognize famous people, and rank them according to their amount of Hashtags/mentions in the last 24 hours.

There are way more things to consider. If you’re interested, I encourage you to read one of the following articles.

## See also

* Jiayuan Huang, Alexander J. Smola, Arthur Gretton, Karsten M. Borgwardt, Bernhard Scholkopf: [Correcting Sample Selection Bias by Unlabeled Data](https://papers.nips.cc/paper/3075-correcting-sample-selection-bias-by-unlabeled-data.pdf)
* [Jaspreet Sandhu](https://www.linkedin.com/in/jaspreetsan/?originalSubdomain=fr): [Understanding and Reducing Bias in Machine Learning](https://towardsdatascience.com/understanding-and-reducing-bias-in-machine-learning-6565e23900ac)
* [Salma Ghoneim](https://www.linkedin.com/in/salma-ghoneim/): [5 Types of bias & how to eliminate them in your machine learning project](https://towardsdatascience.com/5-types-of-bias-how-to-eliminate-them-in-your-machine-learning-project-75959af9d3a0)

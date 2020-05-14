---
layout: post
title: How I reduced my Hosting Costs
slug: reduce-hosting-costs
author: Martin Thoma
status: draft
date: 2020-03-15 20:00
category: My bits and bytes
tags: Code, CMS
featured_image: logos/star.png
---
Recently, the provider which I used for many years and which I was happy enough
to not touch martin-thoma.de, moved. I had to change all my database
credentials, so during the migration everything broke. And they just left a
notice "by the way, you have to pay 12x the price as you use too much space in
the MySQL database".

So I talked with a good friend about it and realized that I might not need
the database at all anymore.

In this article, I document how I moved.


## Wiki

I had an internal MediaWiki which I used to store notes. Nothing fancy, it was
public in the beginning and started with notes for school. Back then, I didn't
know git and I'm not quite sure if GitHub existed back then.

This wiki always caused me headaches:

* **Security**: Almost all things in there were no issue at all of anybody sees
  them, but some I would prefer to stay private. So I need to make sure that
  the overall system is save.
* **Stability**: Can I keep this thing running? What happens if my provider
  updates the PHP version? Remember, that thing was pretty old and I had to
  update the MediaWiki version once. That was not so nice. Also, how can I make
  backups? In the beginning, I couldn't access the database with the `mysql`
  client (might have bin lacking knowledge; I don't remember)
* **Media**
    * **Bugs**: I had one or two big images (over 2000px x 2000px) which were
      only partially uploaded. I will never get them back.
    * **Time**: Uploading actually is a bit time consuming as you have to do it
      file by file
* **Markup**: I don't like the Wiki-Markup. I prefer Github Flavored Markdown
  with HTML for anything more complex.

The solution now seemed simple: **Migrate the content to a git repository!**

This way I can back it up like I do with other local files, I don't have it
online so the risk of it being exposed is way smaller, I can use markdown,
uploading Media is only copying a file. I like it 🙂

During the migration I've also realized that his Wiki has a big overlap with my
blog. Only that I can very easily see the contents of my blog. And a lot of the
content was super outdated or even riddiculous. For example, I listed a lot of
Open Source software with their licenses once. I have no idea why.

Most pages I've linked to were dead - the domains still existed, but the page
was moved. Astonishingly, the student pages seemed to be quite reliable.
YouTube, in contrast, was almost always unavailable. So much about "the
internet does not forget".

In total, it was 30 MB of data in 256 files. Lots of them were low-resolution
images.


### Interesting Stuff I found

> How do crazy people go through the forest? They take the Psychopath!
>
> How do you get holy water? You boil the Hell out of it!

---

In 2010 I already described how newspapers work nowadays:

* Have a website with a subscription model
* Build a profile of readers
* Recommend articles
* Let people also pay for single articles

I'm not 100% certain, but I think this was either uncommon or didn't exist back
then.


---


There is another reason I used the wiki. Sometimes I needed to see diffs
and I didn't know [meld](https://meldmerge.org/) then 😄


## write-math.com

I had a bit weird solution here:

* 5.00 USD / month for a Digital Ocean Droplet where the machine learning stuff was running
* 13.16 USD / year for [.com domain renewal at namecheap](https://www.namecheap.com/domains/registration/gtld/com/)
* 30.73 EUR / year for the database - this is the one I used for multiple things and also the one I want to get rid of

So you could say that I paid about 100 EUR / year for write-math.com.

I switched to Namecheap "Stellar" shared server hosting. They use [cPanel and
3.7.3](https://www.namecheap.com/support/knowledgebase/article.aspx/129/22/what-version-of-the-software-is-used-on-your-servers). This way I can remove the Digital Ocean droplet and instead run it at Namecheap. I removed the need for the database entirely.

Now I pay 17.28 USD/year for the hosting and 13.16 USD for the domain. So 30.44 USD / year or about 28 EUR / year.


### SSH

First thing to do was to add my SSH key - only the public one ([docs](https://www.namecheap.com/support/knowledgebase/article.aspx/9428/89/how-to-connect-via-ssh-using-keys)). Then go to the
"Manage Shell" part, "Enable SSH access" and "authorize" the added key.

Now you can access it via

```bash
ssh USER@SERVER --port=PORT
```

* USER: cPanel username
* SERVER: hostname/IP of the server you are connecting to
* PORT: 21098 for a Shared server

### Python

Setting up a [Python app via cPanel](https://www.namecheap.com/support/knowledgebase/article.aspx/10048/2182/how-to-work-with-python-app/) is easy. Basically it
creates a virtual environment for you. They use an Apache Webserver with
[Phusion Passenger](https://en.wikipedia.org/wiki/Phusion_Passenger)


There is a `passengar_wsgi.py`

See also:

* https://help.krystal.uk/python/creating-a-python-app-using-the-django-framework
* https://www.internetivo.com/clients/knowledgebase/99/Start-your-Python-Django-app-on-cPanel.html
* https://help.dreamhost.com/hc/en-us/articles/215769548-Passenger-and-Python-WSGI
* https://docs.cpanel.net/knowledge-base/web-services/how-to-install-a-python-wsgi-application/
* https://www.phusionpassenger.com/library/walkthroughs/start/python.html
* https://www.phusionpassenger.com/docs/tutorials/quickstart/python/

I was a bit confused because there was a wsgi.py automatically created which
overwrote my wsgi.py. Luckily, I use git and could simply run `git checkout .`

## AWS

If you want to run the website on AWS, you have to pay at least one EC2 instance.
With `t2.small`, this would be 0.023 USD/h which means 10.08 USD / month
([EC2 prices](https://aws.amazon.com/de/ec2/instance-types/t2/)). You might
also want to use AWS RDS which is pretty expensive. You can also [register
domains via AWS Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register-update.html).
It's 9 USD / year for .de domains and 12 USD / year for .com domains

A [guide by AWS](https://aws.amazon.com/de/getting-started/projects/build-wordpress-website/services-costs/)
would lead to 450 USD/month for hosting a Wordpress blog.


[Craigerson](https://www.youtube.com/watch?v=IFeA0jh36WQ) says that he pays
only around 11 USD per month.

## Other Hosting Services

They differ in:

* Time to first byte: That is pretty high for namecheap
* Price per month
* Availability

See:

* https://www.hostinger.com/web-hosting
* https://www.bluehost.com/hosting/shared
* https://docs.google.com/spreadsheets/d/e/2PACX-1vTXQ11WibUUePRjr4k2HAFS3t0P_mRJVLLQgvKCdisiEUZS8jg3Z2eSLB9uBbsNzOJ2MLdkr9jWPQpC/pubhtml?fbclid=IwAR1wpUGuQr4kb3HcSMUsKG4-ywB7uIgWR3OngKQJomRM71GOkB1a5plyUkg

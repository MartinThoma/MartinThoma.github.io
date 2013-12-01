---
layout: post
status: publish
published: true
title: OpenID autodiscovery
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 9741
wordpress_url: http://martin-thoma.com/?p=9741
date: 2011-12-10 11:08:56.000000000 +01:00
categories:
- The Web
tags:
- OpenID
comments: []
featured_image: 2011/10/OpenID.png
---
<a href="http://martin-thoma.com/5-web-technologies-which-should-be-used-more-often/#OpenID">OpenID</a> is a web technology that gives the users the possibility to use one website for authentification on another web service. The <em>OpenID Attribute Exchange</em> makes registration processes simpler, as the user can automatically allow the website to get some information like the Email-adress, the gender and the full name.

The next step to an even simpler login process would be autodiscovery. This means there would be no need to do anything for logging in. You simply have to go to the website and be logged at your OpenID provider (e.g. Google). This is quite easily possible if the user was logged in before. You leave a cookie that gives you the information which OpenID he uses. So you simply don't let him logout. I don't know if it is a good idea to do so.

The registration process is much trickier. Due to the <a href="http://en.wikipedia.org/wiki/Same_origin_policy">same origin policy</a>, you can't read other cookies than those you have set. So you can't check if there is a cookie from Google, Facebook or Yahoo.<br/>
You could try if the user has a Google account, as Google uses a discovery URL (https://www.google.com/accounts/o8/id) instead of the usual OpenID (something like https://me.yahoo.com/martinthoma). So, by chance you will be able to let a user register without forcing him to interact in any way with your website. He has to allow your website to get his data at his OpenID provider, though.

<h2>Futher reading</h2>
<ul>
<li>Wikipedia:
<ul>
<li><a href="http://en.wikipedia.org/wiki/OpenID">OpenID</a>: an open standard that describes how users can be authenticated in a decentralized manner, eliminating the need for services to provide their own ad hoc systems and allowing users to consolidate their digital identities</li>
<li><a href="http://en.wikipedia.org/wiki/Yadis">Yadis</a>: a communications protocol for discovery of services such as OpenID, OAuth, and XDI connected to a Yadis ID</li>
</ul>
</li>
<li><a href="http://openid.net/specs/openid-attribute-exchange-1_0.html">OpenID Attribute Exchange 1.0</a>: Specification</li>
<li><a href="https://docs.google.com/document/pub?id=1O7jyQLb7dW6EnJrFsWZDyh0Yq0aFJU5UJ4i5QzYlTjU&pli=1">Guide to Running a User Account System</a>: by Eric Sachs of Google&rsquo;s Identity team</li>
</ul>

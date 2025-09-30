---
layout: post
lang: en
title: Subscribe via Email
slug: email-subscription
author: Martin Thoma
date: 2011-09-20 20:00
category: My bits and bytes
tags: subscribe
featured_image: logos/star.png
disable_comments: true
---
The subscription is done via [Authory](https://authory.com/MartinThoma):

<script>
function mySubmitFunction() {
  $.ajax({
      type: "POST",
      url: "https://api-production.authory.com/subscribe/MartinThoma",
      data: {"email": document.getElementById('email').value},
      success: function(data) {alert("You've subscribed");return false;},
      error: function(e) {console.log(e);}
  });
  return false;
}
</script>

<form onsubmit="event.preventDefault();return mySubmitFunction()">
    <label for="email">E-Mail</label>
    <input type="email" name="email" id="email" />
    <button type="button" onclick="mySubmitFunction(); return false;">Subscribe</button>
</form>

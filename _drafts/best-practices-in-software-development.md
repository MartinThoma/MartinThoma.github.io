---
layout: post
title: Best Practices in Software Development
author: Martin Thoma
date: 2011-11-10 04:26:19
categories: 
- Cyberculture
tags: 
- Best Practice
- Software Development
featured_image: 
---
<h2>General Organisation</h2>
<h3>People</h3>
One needs to have an overview who is working on what and which problems occur. He has to know exactly what features need to be implemented and whats only nice to have.

<h3>Documentation</h3>
I recommend MediaWiki.

<h3>Bugtracking</h3>
Redmine could be used. I like the Google Code issue tracker.

<h3>Clean Code</h3>
In Java you've got checkstyle, in PHP phpcs. Some tools to do automatic checks if the code is nicely formatted are very helpful.

<h2>Software Design Patterns</h2>
<ul>
  <li>Model-View-Controller: Use a template engine</li>
  <li>One file for <a href="http://en.wikipedia.org/wiki/Internationalization_and_localization">internationalization and localization</a></li>
  <li>Use Subversion or another versioning system</li>
  <li>Atomic changes in PHP / Python; Class or issue related changes in Java</li>
</ul>
<h3>Object Orientation</h3>
If you use OOP, please use the key language features:
<ul>
    <li><strong>Getter and Setter</strong>: No class variables should be written directly from outside of the class. Imagine you decide that the change of one variable has to trigger a method or it might affect another variable or you want to make checks to the changes. In those cases, everybody who has already used your class has to change his code.</li>
    <li><strong>Inheritance</strong>: Use it when it is logical. That means you should only use it, if the child is a special case of its parent.</li>
</ul>
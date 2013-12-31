---
layout: post
title: PHP Template Engines
author: Martin Thoma
date: 2011-10-02 12:52:01
categories: 
- Code
- The Web
tags: 
- PHP
featured_image: 
---
Template engines help to separate code and design. This concept is known as <a href="http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller">Model-view-controller</a> (MVC).

<h2>Why should I use a template engine?</h2>
Separating code and design is good for the following reasons:
<ul>
  <li><strong>Parallel working</strong>: You can tell a designer which special tags he can use and which kind of data will be in those tags, so he can start designing. If you change your code, the template isn't affected. While you change your code, the designer can change the design. You work on two different files, so you don't get into trouble.</li>
  <li><strong>Readability</strong>: In most cases it is much easier to read code when the design is done elsewhere.</li>
  <li><strong>Keep focus</strong>: You know which values are needed for the output. Just take a look at those values and try to compute them. The list you've previously made for the designer might help you to keep focus on the important information and how to get there.</li>
</ul>

<h2>Which template engines are used in big projects?</h2>
<ul>
  <li><a href="http://en.wikipedia.org/wiki/MediaWiki">MediaWiki</a>: </li>
  <li><a href="http://en.wikipedia.org/wiki/WordPress">WordPress</a>: They seem to have an own template engine. A very detailed description of <a href="http://codex.wordpress.org/Templates">WordPress templates</a> and the <a href="http://wordpress.org/download/svn/">source code</a> are online.</li>
  <li><a href="http://en.wikipedia.org/wiki/PhpBB">phpBB</a>: <a href="http://area51.phpbb.com/docs/30x/coding-guidelines.html#templating">phpBB template guidelines</a></li>
  <li><a href="http://en.wikipedia.org/wiki/TYPO3">TYPO3</a>: Fluid template engine (<a href="http://typo3.org/documentation/document-library/references/doc_core_tsref/4.5.0/view/1/7/#id2642042">notes</a>)</li>
  <li><a href="http://en.wikipedia.org/wiki/Drupal">Drupal</a>: PHPTemplate</li>
  <li><a href="http://en.wikipedia.org/wiki/PhpMyAdmin">phpMyAdmin</a>: own template engine</li>
</ul>

<h2>Which template engines could be used?</h2>

<h2>Further reading</h2>
http://docwiki.embarcadero.com/RadPHP/en/Component_Writer's_Guide_::_Template_Engines
http://en.wikipedia.org/wiki/Template_engine_(web)
http://gonzalo123.wordpress.com/2011/01/17/php-template-engine-comparison/
http://stackoverflow.com/questions/tagged/template-engine
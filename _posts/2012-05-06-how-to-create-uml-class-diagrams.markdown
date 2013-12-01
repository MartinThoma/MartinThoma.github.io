---
layout: post
status: publish
published: true
title: How to create UML class diagrams
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 24161
wordpress_url: http://martin-thoma.com/?p=24161
date: 2012-05-06 20:38:01.000000000 +02:00
categories:
- My bits and bytes
tags:
- LaTeX
- MetaUML
- UML
- Dia
comments:
- id: 126401
  author: i42n
  author_email: g@web.de
  author_url: ''
  date: !binary |-
    MjAxMi0wNS0wNiAyMDo0NTozMSArMDIwMA==
  date_gmt: !binary |-
    MjAxMi0wNS0wNiAxODo0NTozMSArMDIwMA==
  content: Wenn du die Dia Diagramme als svg exportierst und in ikscape ein pdf draus
    machst, dann kannst du so beliebig skalierbarbin latex einbinden.
---
<h2>Dia</h2>
Creating UML diagrams with Dia works like a charm! It provides some default tools. You should simply try it. Dia is a free tool.

Take a look at these screenshots:
[caption id="attachment_24211" align="aligncenter" width="231" caption="Create a class for a class diagram in Dia"]<a href="http://martin-thoma.com/wp-content/uploads/2012/05/dia-create-class.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/05/dia-create-class.png" alt="Create a class for a class diagram in Dia" title="Create a class for a class diagram in Dia" width="231" height="611" class="size-full wp-image-24211" /></a>[/caption]

[caption id="attachment_24221" align="aligncenter" width="676" caption="Edit class properties in Dia"]<a href="http://martin-thoma.com/wp-content/uploads/2012/05/dia-class-properties.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/05/dia-class-properties.png" alt="Edit class properties in Dia" title="Edit class properties in Dia" width="676" height="589" class="size-full wp-image-24221" /></a>[/caption]

[caption id="attachment_24231" align="aligncenter" width="454" caption="Customizing associations in Dia - adding multiplicities is so much easier in Dia than in MetaUML!"]<a href="http://martin-thoma.com/wp-content/uploads/2012/05/dia-association.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/05/dia-association.png" alt="Customizing associations in Dia" title="Customizing associations in Dia" width="454" height="447" class="size-full wp-image-24231" /></a>[/caption]

[caption id="attachment_24251" align="aligncenter" width="519" caption="A quick example for a class diagram created with Dia"]<a href="http://martin-thoma.com/wp-content/uploads/2012/05/Dia-ClassDiagram.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/05/Dia-ClassDiagram.png" alt="A quick example for a class diagram created with Dia" title="A quick example for a class diagram created with Dia" width="519" height="104" class="size-full wp-image-24251" /></a>[/caption]

<h2>LaTeX</h2>
I only know MetaUML for creating class diagrams entirely in LaTeX. Does anybody know something different? 

Of course, you can include a diagram created with Dia:
<ol>
  <li>Export the diagram as PNG (antialized)</li>
  <li>Add something like that to your tex-file: \includegraphics[width=180mm]{myDiagramm.png}</li>
</ol>


<h3>MetaUML</h3>
A MetaUML class diagram looks like that in code (saved as myMetaDiagram.mp):

{% highlight text %}input metauml;
beginfig(1);
	Class.World("World")
		   ("-age: int",
			"#ressources: List") 
		   ("+sayHello(): void");

	Class.NoHuman("Human")
		   ("-birthday: Date",
			"-nickname: String",
			"-secret: String") 
		   ("+code(language: Language): Program");

	leftToRight(50)(World, NoHuman);
	drawObjects(World, NoHuman);

	link(aggregation)(NoHuman.w -- World.e);
	item(iAssoc)("1")(obj.n     = .2[World.e,NoHuman.w]);
	item(iAssoc)("has >")(obj.n = .5[World.e,NoHuman.w]);
	item(iAssoc)("0..*")(obj.n  = .8[World.e,NoHuman.w]);

endfig;
end{% endhighlight %}

You have to execute mpost before you can compile LaTeX. A working example is in this <a href='http://martin-thoma.com/wp-content/uploads/2012/05/UML.zip'>UML Archive</a>.

It looks like that in your generated PDF file:
[caption id="attachment_24271" align="aligncenter" width="676" caption="MetaUML class diagram"]<a href="http://martin-thoma.com/wp-content/uploads/2012/05/MetaUML-class-diagram.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/05/MetaUML-class-diagram.png" alt="MetaUML class diagram" title="MetaUML class diagram" width="676" height="161" class="size-full wp-image-24271" /></a>[/caption]

<h2>See also</h2>
<ul>
  <li>Wikipedia: <a href="http://en.wikipedia.org/wiki/Class_diagram">Class diagram</a>, <a href="http://en.wikipedia.org/wiki/Dia_(software)">Dia</a></li>
  <li>Dia:  <a href="http://www.wspiegel.de/infogk12/oops/dia_einf.html#py16_2">Dia und UML</a></li>
  <li><a href="http://ftp.fernuni-hagen.de/ftp-dir/pub/mirrors/www.ctan.org/graphics/metapost/contrib/macros/metauml/doc/metauml_manual_0.2.5.pdf">MetaUML: Tutorial, Reference and Test Suite</a></li>
  <li>Freies Magazin, Mai 2012: <a href="http://www.freiesmagazin.de/freiesMagazin-2012-05">Astah &ndash; Kurzvorstellung des UML-Programms</a> (German)</li>
</ul>

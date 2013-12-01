---
layout: post
status: publish
published: true
title: C++ Preprocessor Snippets
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 28561
wordpress_url: http://martin-thoma.com/?p=28561
date: 2012-12-25 19:32:31.000000000 +01:00
categories:
- Code
tags:
- C
- Preprocessor
comments: []
featured_image: 2012/05/CPP-thumb.png
---
The C++ Preprocessor - which is in fact the same as the C Preprocessor - provides some very basic, but powerful abilities. I haven't used them quite often, but I have seen some nice examples. So here are some C++ Preprocessor Snippets:
<h2>Maximum / Minimum</h2>
If you want to find the maximum / minimum of two elements, no matter of which type, you can do something like this:

{% highlight cpp %}#include <iostream>

#define MAX(a, b) ((a < b) ? b : a)

using namespace std;

int main() {
	cout << MAX(42, 1337) << endl;
	cout << MAX(1337, 42) << endl;
	cout << MAX(-1337, 42) << endl;
	cout << MAX(1337.0, 42) << endl;
	return 0;
}{% endhighlight %}

<h2>Absolute Value</h2>
You can get the absolute value like this:
{% highlight cpp %}#include <iostream>

#define ABS(a) (a < 0 ? -(a) : a)

using namespace std;

int main() {
	int a = 42, b = -43, c = 0, d = -1337;

	cout << ABS(a) << endl;
	cout << ABS(b) << endl;
	cout << ABS(c) << endl;
	cout << ABS(d) << endl;
	return 0;
}{% endhighlight %}

By the way, brackets around <code>a</code> are important, because without them you could get:

{% highlight text %}a=1,b=3
ABS(a-b) = ABS(1-3) = (1-3 < 0 ? -1-3 : 1-3) = -2 < 0 ? -4 : -2 = -4{% endhighlight %}

<h2>Swap variable content</h2>
This is an example for a multiline replacement.

{% highlight cpp %}#include <iostream>

#define SWAP(a, b)  {	int tmp; \
						tmp = b; \
						b = a;   \
						a = tmp; \
					}

using namespace std;

int main() {
	int a = 42, b = 1337;
	swap(a, b);
	cout << a << endl;
	cout << b << endl;
	return 0;
}{% endhighlight %}
<h2>See also</h2>
<ul>
	<li>Wikipedia: <a href="http://en.wikipedia.org/wiki/C_preprocessor">C preprocessor</a></li>
    <li>Tips and tricks using the preprocessor: <a href="http://www.iar.com/Global/Resources/Developers_Toolbox/C_Cplusplus_Programming/Tips%20and%20tricks%20using%20the%20preprocessor%20(part%20one).pdf">Part one</a> - <a href="http://www.iar.com/Global/Resources/Developers_Toolbox/C_Cplusplus_Programming/Tips%20and%20tricks%20using%20the%20preprocessor%20(part%20two).pdf">part two</a><br/>
A very good article about the meaning of #import, #error, #pragma. It is written very well and has some examples.</li>
    <li>Obfuscated C: <a href="http://www.cise.ufl.edu/~manuel/obfuscate/pi.c">Calculate PI</a></li>
</ul>

Do you know more preprocessor snippets that are used very often or which are interesting?

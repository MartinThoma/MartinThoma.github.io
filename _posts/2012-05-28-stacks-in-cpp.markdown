---
layout: post
title: Stacks in C++
author: Martin Thoma
date: 2012-05-28 11:45:40.000000000 +02:00
categories:
- Code
tags:
- C
- Stack
- STL
featured_image: 2012/05/CPP-thumb.png
---
<h2>Minimum Example</h2>
```c++
#include <iostream>
#include <stack>

using namespace std;



int main(){
	stack<int> myStack;

	myStack.push(5);
	cout << "Size of stack: " << myStack.size() << endl;

	myStack.push(4);
	
	// get the element on the top
	cout << "Top: " << myStack.top() << endl;

	// it does NOT automatically pop!
	cout << "Top: " << myStack.top() << endl;

	// pop has NO return value!
	myStack.pop();

	cout << "Top: " << myStack.top() << endl;

    return 0;
}
```

<h2>Maximum number of elements</h2>
{% highlight cpp %}
#include <iostream>
#include <stack>

using namespace std;

int main() {
	stack<int> s;
	for (unsigned int i=0; i < 1000000; i++) {
		for (unsigned int j=0; j < 100; j++) {
			s.push(i);
		}
	}

	cout << "Size of stack: " << s.size() << endl;
}
{% endhighlight %}

{% highlight bash %}
Size of stack: 100000000
{% endhighlight %}
100,000,000 could be added without any problems.

<h2>See also</h2>
<ul>
  <li>C++ Reference: <a href="http://www.cplusplus.com/reference/stl/stack/">general information</a> and <a href="http://www.cplusplus.com/reference/stl/stack/stack/">example</a></li>
  <li><a href="http://en.wikipedia.org/wiki/Stack_(data_structure)">General information about the datastructure stack</a></li>
</ul>

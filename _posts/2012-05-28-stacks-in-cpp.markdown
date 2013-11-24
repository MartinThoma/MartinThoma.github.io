---
layout: post
status: publish
published: true
title: Stacks in C++
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 25201
wordpress_url: http://martin-thoma.com/?p=25201
date: 2012-05-28 11:45:40.000000000 +02:00
categories:
- Code
tags:
- C
- Stack
- STL
comments: []
---
<h2>Minimum Example</h2>
[cpp]#include <iostream>
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
}[/cpp]

<h2>Maximum number of elements</h2>
[cpp]#include <iostream>
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
}[/cpp]

[bash]Size of stack: 100000000[/bash]
100,000,000 could be added without any problems.

<h2>See also</h2>
<ul>
  <li>C++ Reference: <a href="http://www.cplusplus.com/reference/stl/stack/">general information</a> and <a href="http://www.cplusplus.com/reference/stl/stack/stack/">example</a></li>
  <li><a href="http://en.wikipedia.org/wiki/Stack_(data_structure)">General information about the datastructure stack</a></li>
</ul>

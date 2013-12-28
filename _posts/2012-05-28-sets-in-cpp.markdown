---
layout: post
title: Sets in C++
author: Martin Thoma
date: 2012-05-28 12:08:58.000000000 +02:00
categories:
- Code
tags:
- STL
- Set
- CPP
featured_image: 2012/05/CPP-thumb.png
---
``` cpp
#include <iostream>
#include <set>
#include <iterator>

using namespace std;

int main() {
	// create an empty set of integers
	set<int> mySet;

	// insert one element
	mySet.insert(5);
	
	// insert another element
	mySet.insert(4);

	// insert more elements
	mySet.insert(1337);
	mySet.insert(42);
	mySet.insert(31415);

	// insert an element which was there before
	mySet.insert(5);

	// check if 4 is in set
	bool is_in = mySet.find(4) != mySet.end();
	cout << "4 is in mySet: " << is_in << endl;

	is_in = mySet.find(6) != mySet.end();
	cout << "6 is in mySet: " << is_in << endl;

	// iterate over the set
	set<int>::iterator myIt;
	for(myIt=mySet.begin(); myIt != mySet.end(); myIt++){
		cout << *myIt << " ";
	}

	return 0;
}
```

As find is logarithmic in `size()` (source: <a href="http://www.cplusplus.com/reference/stl/set/find/">C++ Reference</a>), the membership test is also in ${\cal O}(log(n))$.

<h2>Sets of structs</h2>
If you want to create a set of structs, you have to create a comperator:

{% highlight cpp %}
bool operator<(const Edge&amp; left, const Edge&amp; right)
{
    return left.uniqueEdge < right.uniqueEdge;
}
{% endhighlight %}
<h2>See also</h2>
<ul>
  <li>C++ Reference: <a href="http://www.cplusplus.com/reference/stl/set/">general information</a> and <a href="http://www.cplusplus.com/reference/stl/set/set/">example</a></li>
  <li><a href="http://stackoverflow.com/questions/1701067/how-to-check-that-an-element-is-in-a-stdset">How to check that an element is in a std::set?</a></li>
</ul>

---
layout: post
title: Vectors in C++
author: Martin Thoma
date: 2012-05-28 12:40:52.000000000 +02:00
categories:
- Code
tags:
- C
- STL
- Vector
featured_image: 2012/05/CPP-thumb.png
---
<h2>Minimal Example</h2>
{% highlight cpp %}#include <iostream>
#include <vector>
#include <algorithm>
 
using namespace std;
 
int main() {
    // create an empty vector
    vector<int> myVector;
 
    // insert one element
    myVector.push_back(5);
 
    // insert another element
    myVector.push_back(4);
 
    // insert more elements
    myVector.push_back(1337);
    myVector.push_back(42);
    myVector.push_back(31415);
 
    // insert an element which was there before
    myVector.push_back(5);
 
    // get the third element
    cout << "third element: " << myVector[2] << endl;
 
    // removes the element at position number 6
    myVector.erase (myVector.begin()+5);
 
    // removes the element with the value 4
    myVector.erase(remove(myVector.begin(), myVector.end(), 4), 
					myVector.end());
 
    // iterate over the vector
    vector<int>::iterator myIt;
    for(myIt=myVector.begin(); myIt != myVector.end(); myIt++){
        cout << *myIt << " ";
    }
	cout << endl;
 
    return 0;
}{% endhighlight %}

Output:
{% highlight bash %}
third element: 1337
5 1337 42 31415 
{% endhighlight %}

<h2>Vector initialization</h2>
{% highlight cpp %}// create a vector with 100 zeroes
vector<int> myVector (100);{% endhighlight %}

{% highlight cpp %}// create a vector which has 42 times the integer 100
vector<int> myVector (42, 100);{% endhighlight %}

<h2>Nested Vectors</h2>
{% highlight cpp %}#include <iostream>
#include <vector>

using namespace std;

int main() {
	// create an empty vector
	vector< vector<int> > myVector (4);

	// add elements
	myVector[0].push_back(1);
	myVector[0].push_back(2);
	myVector[1].push_back(3);

    // iterate over the vector
    vector< vector<int> >::iterator myIt;
	vector<int>::iterator innerIt;
    for(myIt=myVector.begin(); myIt != myVector.end(); myIt++){
		cout << "Inner vector: ";
		for (innerIt=myIt->begin();innerIt!=myIt->end();innerIt++) {
			cout << *innerIt << " ";
		}
		cout << endl;
    }

	return 0;
}{% endhighlight %}
Output:
{% highlight bash %}Inner vector: 1 2 
Inner vector: 3 
Inner vector: 
Inner vector: {% endhighlight %}

<h3>Initialize nested vectors</h3>
{% highlight cpp %}vector<int> myInnerVector(5, 3);
vector<vector<int> > myVector(8,myInnerVector);{% endhighlight %}
Output with the script above:
{% highlight bash %}Inner vector: 3 3 3 3 3 
Inner vector: 3 3 3 3 3 
Inner vector: 3 3 3 3 3 
Inner vector: 3 3 3 3 3 
Inner vector: 3 3 3 3 3 
Inner vector: 3 3 3 3 3 
Inner vector: 3 3 3 3 3 
Inner vector: 3 3 3 3 3 {% endhighlight %}

You could also do it this way:
{% highlight cpp %}vector< vector<int> > myVector(8, vector<int>(5, 3));{% endhighlight %}

<h2>Some more</h2>
<h3>Reverse the order</h3>
With reverse (<a href="http://www.cplusplus.com/reference/algorithm/reverse/">source</a>):
{% highlight cpp %}#include <algorithm>
#include <vector>

using namespace std;

int main () {
  vector<int> myvector;
  vector<int>::iterator it;

  // set some values:
  for (int i=1; i<10; ++i) myVector.push_back(i); // 1 2 3 4 5 6 7 8 9

  reverse(myVector.begin(),myVector.end());       // 9 8 7 6 5 4 3 2 1

  // print out content:
  cout << "myVector contains:";
  for (it=myVector.begin(); it!=myVector.end(); ++it)
    cout << " " << *it;

  cout << endl;

  return 0;
}{% endhighlight %}

<h2>See also</h2>
<ul>
  <li>C++ Reference: <a href="http://www.cplusplus.com/reference/stl/vector/">General information</a> and <a href="http://www.cplusplus.com/reference/stl/vector/vector/">example</a></li>
  <li><a href="http://stackoverflow.com/questions/3131991/iterating-over-2-dimensional-stl-vector-c">Iterating over 2-dimensional STL vector C++</a></li>
</ul>

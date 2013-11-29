---
layout: post
status: publish
published: true
title: Maps in C++
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 66091
wordpress_url: http://martin-thoma.com/?p=66091
date: 2013-05-16 08:52:54.000000000 +02:00
categories:
- Code
tags:
- C
- STL
- datastructure
- map
comments: []
---
Maps are one of the most useful datastructures in C++ and there is no excuse for not knowing it.

Here is a basic example that shows how you can use it:

{% highlight cpp %}
#include <iostream> // cout
#include <string>

#include <map>

using namespace std;

int main() {
    map<string, string> phonebook;

    // Put some stuff in it
    phonebook["Martin"] = "(0123) 45 678";
    phonebook["Alice"] = "+(13) 37 0000";
    phonebook["Bob"]   = "+(13) 37 0000";
    phonebook["Charlie"] = "Alice";

    // Look stuff up
    cout << "The phone number of Alice is " 
         << phonebook["Alice"] << endl;

    cout << "Number of phone book entries: "
         << phonebook.size() << endl;

    // Print everything
    cout << "Iterate over all phonebook entries: " << endl;
    for(map<string,string>::iterator it=phonebook.begin(); 
        it!=phonebook.end(); ++it) {
        cout << "\t" << (*it).first << ": " << (*it).second << endl;
    }

    // Check if entry exists:
    string person = "Bob";
    cout << "Does " << person << " have a phone number ?" << endl;
    map<string,string>::iterator it = phonebook.find(person);
    if(it != phonebook.end()) {
        //element found:
        cout << "\t" << "Yes! His number is: " << it->second << endl;
    } else {
        cout << "\t" << "No." << endl;
    }
}
{% endhighlight %}

<h2>See also</h2>
<ul>
  <li>Wikipedia: <a href="http://en.wikipedia.org/wiki/Map_(computer_science)">Map (Computer Science)</a></li>
  <li>C++ Reference: <a href="http://www.cplusplus.com/reference/map/map/">general information</a> and <a href="http://www.cplusplus.com/reference/map/map/map/">example</a></li>
  <li>Map is ordered collection (<a href="http://stackoverflow.com/a/4562771/562769">source</a>)</li>
</ul>

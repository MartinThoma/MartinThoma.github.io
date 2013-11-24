---
layout: post
status: publish
published: true
title: How to sort with Java
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 53391
wordpress_url: http://martin-thoma.com/?p=53391
date: 2013-01-08 21:49:47.000000000 +01:00
categories:
- Code
tags:
- Programming
- Java
- sorting
comments:
- id: 1119551
  author: Amedar Consulting
  author_email: ''
  author_url: http://amedar.pl
  date: !binary |-
    MjAxMy0wMS0xMyAxMjo0MDowNiArMDEwMA==
  date_gmt: !binary |-
    MjAxMy0wMS0xMyAxMTo0MDowNiArMDEwMA==
  content: ! '<strong>Blog...</strong>


    Somebody essentially lend a hand to make significantly articles I might state.
    That is the very first time I frequented your web page and to this point? I surprised
    with the research you made to create this actual post amazing. Magnificent process!...'
---
Sorting is a very basic task that every programmer should be able to solve. In Python, you have sort and sorted. In C++, you can use <a href="http://martin-thoma.com/c-operator-overloading/#Sorting">operator overloading</a>. I'll now tell you how to do basic sorting with Java. I will not write about <a href="http://www.codinghorror.com/blog/2007/12/sorting-for-humans-natural-sort-order.html">natural language sorting</a> or language-aware sorting. This is only about simple sorting with Java.

<h2>Sorting without programming</h2>
First of all, you have to make sure that you understand how sorting works - without Java, just in the real world.

What you need:
<ul>
  <li>A container $C$ of objects</li>
  <li>A way to compare two objects of the list at a time. The comparison, lets call it $\leq$ needs to satisfy the following conditions:
     <ul>
       <li><a href="http://en.wikipedia.org/wiki/Total_relation">totality</a>: $\forall x, y \in C: x \leq y \lor y \leq x$</li>
       <li><a href="http://en.wikipedia.org/wiki/Antisymmetric_relation">antisymmetry</a>: $\forall x,y \in C: x \leq y \land y \leq x \Rightarrow x = y$</li>
       <li><a href="http://en.wikipedia.org/wiki/Transitive_relation">transitivity</a>: $\forall x,y,z \in C: x \leq y \land y \leq z \Rightarrow x \leq z$</li>
     </ul>
  </li>
</ul>

Just think about what you sort in your everyday life:
<ul>
  <li>Numbers</li>
  <li>Words</li>
  <li><a href="http://en.wikipedia.org/wiki/List_of_countries_by_population">Contries by population</a></li>
  <li>Playing cards</li>
</ul>

You can apply different algorithms like <a href="http://en.wikipedia.org/wiki/Selection_sort">selection sort</a> which you would use for numbers or <a href="http://en.wikipedia.org/wiki/Insertion_sort">insertion sort</a> which you would use for card games. No matter what algorithm you use, you need to be able to compare the elements. 

Note that you can compare some objects, like countries, by many measures. You could look at the population, the birth rate or the area. No matter what you use to compare, the this will not influence the way you sort.

<h2>Collections</h2>
One way to sort is to implement the interface <a href="http://docs.oracle.com/javase/7/docs/api/java/util/List.html">List</a>. For all datastructures, that implement the interface List or one of its sub-interfaces you can use <a href="http://docs.oracle.com/javase/7/docs/api/java/util/Collections.html">Collections</a> an go on like this:

[java]import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> myList = new LinkedList<String>();
        myList.add("I");
        myList.add("think");
        myList.add("therefore");
        myList.add("I");
        myList.add("am");
        System.out.println(myList);
        Collections.sort(myList);
        System.out.println(myList);
    }
}[/java]

Output:
[bash]
[I, think, therefore, I, am]
[I, I, am, therefore, think]
[/bash]

Note that I didn't write a Comparator or implement Comparable as String has one by default.
Don't mix <a href="http://docs.oracle.com/javase/7/docs/api/java/util/Collections.html">Collections</a> and <a href="http://docs.oracle.com/javase/7/docs/api/java/util/Collection.html">Collection</a>! A Set is a Collection, but it is not sortable. Collections is a class that you can use for sorting. Like <a href="http://docs.oracle.com/javase/7/docs/api/java/lang/Math.html">Math</a>, that has utilities like <a href="http://docs.oracle.com/javase/7/docs/api/java/lang/Math.html#sqrt(double)">sqrt</a>

<h2>Arrays</h2>
[java]
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        String[] myStrings = new String[5];
        myStrings[0] = "I";
        myStrings[1] = "think";
        myStrings[2] = "therefore";
        myStrings[3] = "I";
        myStrings[4] = "am";

        System.out.println(Arrays.asList(myStrings));
        Arrays.sort(myStrings);
        System.out.println(Arrays.asList(myStrings));
    }
}
[/java]

<h2>Interface Comparable</h2>
This is an example how you could implement <a href="http://docs.oracle.com/javase/7/docs/api/java/lang/Comparable.html">Comparable</a>.

Country.java
[java]
public class Country implements Comparable<Country> {
    int population;
    double area;
    String name;

    public Country(int population, double area, String name) {
        this.population = population;
        this.area = area;
        this.name = name;
    }

    @Override
    public int compareTo(Country o) {
        // a negative integer, zero, or a positive integer as this
        // object is less than, equal to, or greater than the
        // specified object.
        return this.name.compareTo(o.name);
    }

    @Override
    public String toString() {
        return name + ": " + population;
    }
}
[/java]

Main.java
[java]
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Country> europe = new ArrayList<Country>();
        europe.add(new Country(82000000,350000,"Germany"));
        europe.add(new Country(60000000,360000, "France"));
        europe.add(new Country(20000000,100000, "Norway"));
        europe.add(new Country(30000000,500000, "Sweden"));
        europe.add(new Country(50000000,123000, "Spain"));
        System.out.println(europe);
        Collections.sort(europe);
        System.out.println(europe);
    }
}
[/java]

Output:
[bash]
[Germany: 81903000, France: 64667000, Norway: 4985900, Sweden: 9514406, Spain: 47212990, Switzerland: 8014000, Monaco: 36371]
[France: 64667000, Germany: 81903000, Monaco: 36371, Norway: 4985900, Spain: 47212990, Sweden: 9514406, Switzerland: 8014000]
[/bash]

You should definitely add JavaDoc and comment what you've compared.
Note that it would sort the list in reverse order if you switched <code>this.population - o.population;</code> to <code>o.population - this.population;</code>. This would be bad style, as the JavaDoc of Comparable define the order. If you would like to sort in reverse, you should use <code>Collections.reverse(europe);</code>.

You can also use compareTo() within compareTo():
[java]
    @Override
    public int compareTo(Country o) {
        return this.name.compareTo(o.name);
    }
[/java]

<h2>Comparator</h2>
If you need to compare objects in multiple ways, you might need to implement <a href="http://docs.oracle.com/javase/7/docs/api/java/util/Comparator.html#compare(T, T)">Comperator</a>. If you only have to compare objects in one way, I would always use the Interface Comparable. It's easier to use.

<h3>External Comparator</h3>
An external Comperator PopulationDensityComperator.java could look like this:
[java]
import java.util.Comparator;

public class PopulationDensityComperator implements
        Comparator<Country> {

    @Override
    public int compare(Country o1, Country o2) {
        double o1Density = o1.population / o1.area;
        double o2Density = o2.population / o2.area;

        if (Math.abs(o1Density - o2Density) < 0.00001) {
            return 0;
        } else {
            return o1Density - o2Density;
        }
    }

}
[/java]

and you would use it like this in the Main.java:
[java]
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Country> europe = new ArrayList<Country>();
        europe.add(new Country(81903000,357121.41,"Germany"));
        europe.add(new Country(64667000,668763, "France"));
        europe.add(new Country( 4985900,385199, "Norway"));
        europe.add(new Country( 9514406,450295, "Sweden"));
        europe.add(new Country(47212990,504645, "Spain"));
        europe.add(new Country( 8014000, 41285, "Switzerland"));
        europe.add(new Country(   36371,     2.02, "Monaco"));
        System.out.println(europe);
        Collections.sort(europe);
        System.out.println(europe);
        Collections.sort(europe, new PopulationDensityComperator());
        System.out.println(europe);
    }
}
[/java]

Your output would be:
[bash]
[Germany: 81903000, France: 64667000, Norway: 4985900, Sweden: 9514406, Spain: 47212990, Switzerland: 8014000, Monaco: 36371]
[France: 64667000, Germany: 81903000, Monaco: 36371, Norway: 4985900, Spain: 47212990, Sweden: 9514406, Switzerland: 8014000]
[Norway: 4985900, Sweden: 9514406, Spain: 47212990, France: 64667000, Switzerland: 8014000, Germany: 81903000, Monaco: 36371]
[/bash]

<h3>Internal (anonymous) Comparator</h3>
You can also directly implement the comperator where you need it:
[java]
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Country> europe = new ArrayList<Country>();
        europe.add(new Country(81903000,357121.41,"Germany"));
        europe.add(new Country(64667000,668763, "France"));
        europe.add(new Country( 4985900,385199, "Norway"));
        europe.add(new Country( 9514406,450295, "Sweden"));
        europe.add(new Country(47212990,504645, "Spain"));
        europe.add(new Country( 8014000, 41285, "Switzerland"));
        europe.add(new Country(   36371,     2.02, "Monaco"));
        System.out.println(europe);
        Collections.sort(europe);
        System.out.println(europe);
        Collections.sort(europe, new Comparator<Country>(){
            @Override
            public int compare(Country o1, Country o2) {
                double o1Density = o1.population / o1.area;
                double o2Density = o2.population / o2.area;

                if (Math.abs(o1Density - o2Density) < 0.00001) {
                    return 0;
                } else if (o1Density > o2Density) {
                    return 1;
                } else {
                    return -1;
                }
            }
        });
        System.out.println(europe);
    }
}
[/java]

Your output would be:
[bash]
[Germany: 81903000, France: 64667000, Norway: 4985900, Sweden: 9514406, Spain: 47212990, Switzerland: 8014000, Monaco: 36371]
[France: 64667000, Germany: 81903000, Monaco: 36371, Norway: 4985900, Spain: 47212990, Sweden: 9514406, Switzerland: 8014000]
[Norway: 4985900, Sweden: 9514406, Spain: 47212990, France: 64667000, Switzerland: 8014000, Germany: 81903000, Monaco: 36371]
[/bash]

I don't recommend this way for some reasons:
<ul>
  <li>It is more likely that your code gets more difficult to read</li>
  <li>It's more difficult to reuse your code (you can't use the same Comparator in another location)</li>
  <li>It's more difficult to extend your code</li>
</ul>

An argument for such an Comparator might be, that it is easier to read. But this is only an argument if the Comparator is very short.

<h2>More examples</h2>
<ul>
  <li>StackOverflow: <a href="http://stackoverflow.com/q/3718383/562769">java class implements comparable</a></li>
</ul>

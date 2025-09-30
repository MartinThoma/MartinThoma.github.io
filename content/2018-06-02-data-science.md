---
layout: post
lang: en
title: Data Science - An Overview
slug: data-science
author: Martin Thoma
date: 2018-06-02 20:00
category: Machine Learning
tags: Machine Learning
featured_image: logos/data-science.png
---
Data Science recently became popular. Currently are 154 open job positions on
Indeed.com for Data Scientists in Munich. To put it into context: There are 186
Android developer positions open, 527 Dev Ops, 753 frontend, 812 backend. So
it's still fairly small, but in the same ballpark.

I wanted to have a data-based answer to what a data scientist actually is and
created a list of the skill set employers ask for, but it turns out that this
would lead to a lengthy and hard to digest blog post.

I don't really like the term "data science" as it is too vague to me, but here
is how I would define it: A data scientist is a person who applies data
science. Data science is an academic field which deals with the extraction of
knowledge and insights from data.

<figure class="wp-caption aligncenter img-thumbnail">
    <a href="../images/2018/06/data-science-ngram.png"><img src="../images/2018/06/data-science-ngram.png" alt="Popularity of Data Science and related terms in books." style="width: 512px;"/></a>
    <figcaption class="text-center">Popularity of Data Science and related terms in books. One can see a linear increase for "machine learning" since about 1975, the term "data mining" exploded from 1992 to 2003. Other related terms like "big data", "deep learning", "information extraction" and "data science" are much less popular in books.</figcaption>
</figure>

I would also say it is a term used much more often in industry than in
academia. The requirements between different job postings differ, but there are
some general themes:

<figure class="wp-caption aligncenter img-thumbnail">
    <a href="../images/2018/06/word-cloud-skillset.png"><img src="../images/2018/06/word-cloud-skillset.png" alt="Word Cloud of the Skillset in 10 different Data Scientist job postings" style="width: 512px;"/></a>
    <figcaption class="text-center">Word Cloud of the Skillset in 10 different Data Scientist job postings. If you're interested how to create word clouds, look <a href="https://gist.github.com/MartinThoma/d325e3cdc2fd68133241efa21d3205b4">here</a>.</figcaption>
</figure>


Some of the requirements are typical senior software developer skills, such as
knowledge in Scrum and Waterfall and good knowledge of spoken and written
English and German. And some are rather special such as several skills around
machine learning (sklearn, scipy, nltk, Theno / Tensorflow / Keras / MXNet) or
Big Data (AWS, Hadoop, Spark).

I've also asked some friends and collegues which kind of tasks they have seen
so far. I gave them a list of six possible responses and asked for more if
there is something that didn't match an entry in the list. I didn't get any answer
outside of it. Here are the answers:

<figure class="wp-caption aligncenter img-thumbnail">
    <a href="../images/2018/06/data-science-projects.png"><img src="../images/2018/06/data-science-projects.png" alt="Data Science project types" style="width: 512px;"/></a>
    <figcaption class="text-center">Data Science project types. EDA is short for "Exploratory Data Analysis". The bar chart was created with <a href="https://www.rapidtables.com/tools/bar-graph.html">rapidtables.com</a></figcaption>
</figure>

Let's first explain the differnt project types:

1. **Forecasts**: Given a time series of the past, predict the future
2. **Classification (and regression)**: For example, detect if an e-mail is spam or not
3. **EDA**: Exploratory Data Analysis. Here is the data - now find something interesting. This is a very unspecific task.
4. **Visualizations**: Data Science can also be a bit about story telling. You
   found something which can be explained with exact terminology and words, but
   it has to be made clear to stakeholders what you found in an simple,
   intuitive, fast way.
5. **A/B tests (and hypothesis testing)**
6. **Clustering**: Which types of customers do we have? (Customer segmenation)

Now, back to the bar chart: You can see that bar charts are much more visible /
stick better to peoples mind, although the other tasks are more common. And you
can see that people tend to make too quick conclusions from seeing a pattern in
small numbers 😉

From personal experience, I would say that forecasts, clustering and regression
are relative common tasks. Of course, one has often to start with exploratory
data analysis.

I try to avoid clustering and pure EDA tasks as they are ill-defined. You can't
say when you are ready which makes it hard to get satisfying results.


## Data Science vs Business Analytics

Both, data science and business analytics are closely related. They certainly
have big overlaps. Here are some differences:

<table>
    <tr>
        <th></th>
        <th>Business Intelligence</th>
        <th>Data Science</th>
    </tr>
    <tr>
        <th>Tasks</th>
        <td>Reports</td>
        <td>Predictive models</td>
    </tr>
    <tr>
        <td>Tool</td>
        <td>Qlickview, SAP</td>
        <td>Pandas, sklearn, Jupiter notebooks, Tensorflow, Keras, XGBoost, scipy, numpy</td>
    </tr>
</table>


## Data Scientist vs Data Engineer

Both, data scientists and data engineers, deal with data. While the engineer
has more ETL-tasks (extract, transform, load), the scientists has more model
creation and analysis tasks.


<table>
    <tr>
        <th></th>
        <th>Data Engineer</th>
        <th>Data Scientists</th>
    </tr>
    <tr>
        <td>Typical Background</td>
        <td>Computer Science + Software Engineering</td>
        <td>Computer Science + Mathematics</td>
    </tr>
    <tr>
        <td>Tasks</td>
        <td>Collect and Transform Data (<abbr title="Extract, Transform, Load">ETL</abbr>), Data Warehousing</td>
        <td>Generate Insights from Data; Machine Learning</td>
    </tr>
    <tr>
        <td>Typical Frameworks</td>
        <td><a href="https://en.wikipedia.org/wiki/Apache_Hadoop">Hadoop</a>, <a href="https://en.wikipedia.org/wiki/Apache_Spark">Spark</a>, <a href="https://en.wikipedia.org/wiki/Apache_Cassandra">Cassandra</a>, <a href="https://en.wikipedia.org/wiki/Apache_Drill">Apache Drill</a>, CouchDB, talend, mongoDB, neo4j, MariaDB</td>
        <td><a href="https://en.wikipedia.org/wiki/Pandas_(software)">Pandas</a>, <a href="https://en.wikipedia.org/wiki/NumPy">Numpy</a>, <a href="https://en.wikipedia.org/wiki/SciPy">Scipy</a>, <a href="https://en.wikipedia.org/wiki/Scikit-learn">scikit-learn</a></td>
    </tr>
</table>


## Data Scientist vs Data Analyst

Data Scientists and Data Analysts are pretty similar compared to Data Engineers.
I would say that Data Scientists should also know about Machine Learning algorithms
and Frameworks while I would not expect it from a Data Analyst.


## Data Science vs ML vs AI

David Robinson made a really nice quote ([source](https://dzone.com/articles/the-difference-between-data-science-machine-learni)):

> So in this post, I'm proposing an oversimplified definition of the difference
> between the three fields:
>
> * Data science produces **insights**.
> * Machine learning produces **predictions**.
> * Artificial intelligence produces **actions**.

Usually, I said that ML is a strict subset of AI:

<figure class="wp-caption aligncenter img-thumbnail">
    <img src="../images/2018/06/ai-ml-deep-learning.png" alt="AI vs ML vs Deep Learning" style="width: 512px;"/>
    <figcaption class="text-center">AI vs ML vs Deep Learning</figcaption>
</figure>

David Robinsons statement is not a contradiction to mine. I would say you need
predictions about the future to take smart actions in a changing world.

<figure class="wp-caption aligncenter img-thumbnail">
    <img src="../images/2018/06/ds-ml-ai.png" alt="A more detailed view of Data Science, Machine Learning, and AI" style="width: 512px;"/>
    <figcaption class="text-center">A more detailed view of Data Science, Machine Learning, and AI</figcaption>
</figure>


## See also

Now that it is clear what kinds of tasks are common in data science, will
continue with blog posts how to make those projects sucessful.

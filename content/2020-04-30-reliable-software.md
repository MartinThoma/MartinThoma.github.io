---
layout: post
lang: en
title: How to build reliable Software
slug: reliable-software
author: Martin Thoma
date: 2020-04-30 20:00
category: Code
tags: Software Engineering
featured_image: logos/star.png
---
Reliability in software development is an ambiguous term. Without thinking much
about it, most people would call a system reliable if *it just works*. When
reading specifications, you might read some of the following terms:

<dl>
    <dt><dfn>Availability</dfn></dt>
    <dd>For (web) services, availability is the probability that at a random
        time the service is working. It is usually calculated over a year as
        availability = uptime / (uptime + downtime). If a web service has an
        availability of 99.9% over a year, it means there were 57 minutes in
        total in which the service was not usable.</dd>
    <dt><a href="https://en.wikipedia.org/wiki/Robustness_(computer_science)"><dfn>Robustness</dfn></a></dt>
    <dd>How much diversion from the specification can you take before things
        start to break? I connect this with validation of user input,
        used services not responding, parts of the hardware failing.</dd>
    <dt><dfn>Stability</dfn></dt>
    <dd>How long can you operate without failures? The connected measure is
        <a href="https://en.wikipedia.org/wiki/Mean_time_between_failures">Mean Time Between Failures</a>
        (<abbr title="Mean Time Between Failures">MTBF</abbr>).</dd>
    <dt><dfn>Resilience</dfn></dt>
    <dd>How long does it take to recover? Resilience is the ability of software
        to handle unexpected situations without the user noticing or at least
        with graceful degradation. When working on it, the <a href="https://en.wikipedia.org/wiki/Mean_time_to_recovery">Mean time to recovery</a> (MTTR)
        is reduced.</dd>
</dl>

ANSI/IEEE 1991 defines reliability as "the probability of failure-free software
operation for a specified period of time in a specified environment". That sounds
pretty much like my definition of availability.

There are also different words for bugs like failure, fault or error.
For this article, I don't distinguish them. I was curious if other people do
and got [mixed answers](https://twitter.com/themoosemind/status/1252992387338719239).
Definitions are given in [^1].

In this article, I try to show some good practices which help to built software
people can rely on. I will not talk about anything security related. So
integrity agains an attacker and confidentiality will not be discussed.


## Issue Types

Please note that reliability is not only about bugs. For example, think of the
e-commerce website Amazon. Even if it is bug-free, it could be that so many
people go on amazon.com on a black-friday sale that the servers (the hardware)
can't handle the load. Either all people get a super slow experience or some
just don't get an answer. This is not a bug, but it for sure is an issue.

Having a clear understanding of what can go wrong helps to prevent the issue or
at least deal with it in a good way.

Looking at the effect on the system, you can distinguish those:

* **Crash Failures**: The system is down
* **Ommision Failures**: (response, brittle)
* **Timing Failures**: System responses, but too late
* **Response Failures**: System responses, but the response is wrong


### Hardware Issues

* Disk failure
* Power outage
* Network
    * Loss of network connection, e.g. cable was cut
    * Package loss
* Bug within the Hardware, e.g. [Pentium FDIV bug](https://en.wikipedia.org/wiki/Pentium_FDIV_bug)


### Bugs

A bug is a mistake made by the programmers. Besides some [well-documented single bugs](https://en.wikipedia.org/wiki/List_of_software_bugs)
there are groups of issues which occur often. For some of them, it depends on
the programming language if they are possible at all.

* **Typos**: Especially when entering strings, this can easily happen.
* **[Off-by-one errors](https://en.wikipedia.org/wiki/Off-by-one_error)** (also: greater / smaller than, greater or greater-equal) are either just typos or a missunderstanding by the developers, because they didn't think thoroughly about it.
* **Partial Change**: You adjusted one part, but you needed to make the same change somewhere else. For example, this could happen when you define on which port your application should run. You change it in the application code, but not in the Dockerfile / docker-compose.yml
* **Unicode**: [Bush hid the facts](https://en.wikipedia.org/wiki/Bush_hid_the_facts)
* **Timezones**: Which timezone was used? What is the difference between a timezon and an offset? Can I use UTC everywere? Those questions are answered in <a href="https://zenodo.org/record/1443533#.XqCJcvIzYdg">What every developer should know about time</a>. As a very brief guideline: Usually it is fine to use UTC in ISO-8601 format for server-side events. For client-side events it is often desirable that you store the local time in ISO-8601 with the timezone as a string in two fields.
* **Floating-point comparisons**: Don't use <code>if (a == b)</code>, but <code>if (abs(a-b) < epsilon)</code>. See <a href="https://www.itu.dk/~sestoft/bachelor/IEEE754_article.pdf">What Every Computer Scientist Should Know About Floating-Point Arithmetic</a>
* **Type missmatches**:
    * Null: You expect an object of class Foo, but got a NULL pointer.
    * Sub-ranges: You expect a positive integer, but got zero.
    * Stringly typed: You expected either the string "ADMIN" or "USER", but got "user". Use Enums.
* **Buffer Overflow**
* Inter-system communication and changing systems
* [**Resource Leaks**](https://en.wikipedia.org/wiki/Resource_leak): The program asks for a resource, but never gives it back.
    * [**Memory Leak**](https://en.wikipedia.org/wiki/Memory_leak): Memory which is no longer needed is never released.
    * [**Handle Leak**](https://en.wikipedia.org/wiki/Handle_leak): Files are opened, but never closed. This means even if they are marked for deletion, they are not deleted. [Happened to me](https://stackoverflow.com/questions/60852105/what-is-the-os-level-handle-of-tempfile-mkstemp-good-for).
* [Infinite Loop](https://en.wikipedia.org/wiki/Infinite_loop)
* [Deadlock](https://en.wikipedia.org/wiki/Deadlock)
* [Dangling pointer](https://en.wikipedia.org/wiki/Dangling_pointer)
* [Race condition](https://en.wikipedia.org/wiki/Race_condition)


### Scalability

There is the famous [hug of death](https://en.wikipedia.org/wiki/Slashdot_effect),
when a famous website links to a small one. Or when a new service is mentioned
in big media. The issue is that humans don't have a feeling for big numbers.
A single request on a website is typically handled so fast that we tend to
think that we can handle arbitrary numbers of users. And for most websites
and most times this is practically true - there are simply not so many people
comming to the website. But once you get from a few dozend parallel users to
thousands or maybe even millions, things start to look different. You need to
think about the amount of resources you need.

There are two aspects to this:

* Big-O notation: How does the amount of resources grow with growing demand?
  In many cases, you want **linear growth** or less.
* Infrastructure: Do you need bigger machines (vertical scaling) or can you
  just buy more machines (**horizontal scaling**).

You really want all things you do to be linear or sub-linear. This means in the
worst case when you have double as many users you just have double as much
needs for resources. And you really want horizontal scaling, because then
double as much resources just means double the price.

As an example: Assume you have a DNA matching website. You tell your customers
that you will keep track of the latest research and tell them if that might
lead to new insights about you. Something like finding markers that indicate
risk for cancer. The resources you need are in $\mathcal{O}(n)$ where $n$ is
the number of users. Once you get new research, you need to check all $n$
users. If the users double, you need to do double the work. And you can do it
on different machines, hence you can scale horizontally.

Now assume you would say that you apply the latest research for finding the
optimal partner. Once you get new insights in the DNA, you need to compare
every pair of DNA. This is in $\mathcal{O}(n^2)$, meaning if you double your
userbase you might have 4x the need of infrastrucutre!
Now assume you would do it all on the same machine and you had a fixed time
limit. Then you would need to buy faster machines. At some point, this is just
physically not possible anymore. Then you need to change the algorithm to
run on multiple machines. But with quadratic growth, you might hit limits there
as well.


### Third-Party Issues

You might call another service to get parts you need. What could happen:

* **No answer**
* **To slow answer**: Maybe the answer you got is not relevant anymore. Think
  of a portal where you can trade stocks. You want to know the current price.
  If the service needs 5 minutes to answer, the price will have changed. So
  even if you get the answer eventually, it is useless.
* **Wrong parameters**: The function you called needs other parameters. Maybe it
  was a bug on your side, but maybe also the service just changed its behaviour.
* **Wrong format**: You received an answer and it is correct, but the format of
  it is unexpected. For example, I once say floating points from a database
  having the German decimal separator (a comma instead of a point). And being
  stored as a string instead of a float / decimal is a story of its own.
* **Wrong answer**: The data just being plain wrong. Again, using a database
  I've had a look at the birth dates and found somebody being born in the year
  zero.


## Issue Prevention

It's nice if nothing goes wrong, right? So how can we avoid issues?

There are so many things to write here, I guess I will move this to its own article.
Here are some points:

<table class="table">
    <thead>
    <tr>
        <th>Issue</th>
        <th>Prevention / Mitigation</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>Type missmatches</td>
        <td>Use a typed language or type annotations and a type checker (mypy for Python, TypeScript for JavaScript)</td>
    </tr>
    <tr>
        <td>Partial Change</td>
        <td>Use constants instead of <a href="https://en.wikipedia.org/wiki/Magic_number_(programming)">magic values</a> (typically numbers or strings)</td>
    </tr>
    <tr>
        <td>Infinite Wait for Response</td>
        <td>Timeout: If a synchronous call does not get an answer, don't keep asking forever.</td>
    </tr>
    <tr>
        <td>Unnecessary repeats</td>
        <td>Circuit Breaker: Don't repeat stuff infinitely. [Hystrix](https://github.com/Netflix/Hystrix) would be a Java solution for that.</td>
    </tr>
    <tr>
        <td>Infinite Loop</td>
        <td>Use foreach-loops over while / for loops</td>
    </tr>
    </tbody>
</table>

* Fault-prevention patterns


### Code reviews
Thorough code reviews can potentially prevent any bug. Of course, you
don't have any guaranteed. But two people might catch more than one
person.

### Type Checking
Some languages require that you state the type for everything, for example Java.
Other languages, like Rust, support type inference ([example](https://doc.rust-lang.org/stable/rust-by-example/types/inference.html)).
Then there are languages and language extensions like TypeScript and type annotations
for Python. There you don't need to annotate the types. If you do, you can
run a static type checker over your code. They support incremental changes,
meaning you can support some parts and the type checker tries to do its best.

* type safe: Subtypes (integer sub-ranges, enums)

If you want compile-time type checking, you need to have a look at
[`mypy`](http://mypy-lang.org/). mypy is a big project known by all relevant
members of Python. Less known is
[`pydantic`](https://pydantic-docs.helpmanual.io/). pydantic can support with
run-time type checking. There are way more things to say about type checking
in Python. Maybe I'll do that in another article.


### Input Checking

It sounds obvious, but check your input. Especially common are null values, e.g. when you
get data from a database. Files might not exist on all platforms or they can be corrupted.
APIs could change the format in which they return stuff.

For APIs, schema validation is your friend. If that doesn't work, sanity checks and Regular Expressions (RegEx)
might get you close enough.

However, most schema validations are not super rigid. One simple check I miss in most
cases is value ranges. For example, when I have a "day of birth" field for a current user, I can
easily say tht anything which is more than 150 years in the past is wrong. Also, days of birth
which are less than 12 years in the past might indicate an issue in most applications.

Maybe I'll write an article about schema validation as well.


### Finding Code Smells

The more code you write, the more possibilities you have to make mistakes. The more complex the
code is, the more likely you mess something up.

Just looking at the lines of code and the code complexity (e.g. cyclomatic complexity) might
point you to places where errors could be likely.

Looking at line test coverage / branch test coverage are two ways to find places where you might
want to have a closer look.

There are also linters like [pylint](https://pypi.org/project/pylint/) and [flake8](https://pypi.org/project/flake8/).
They mostly capture minor stylistic things which can be automatically fixed by
code formatters like [black](https://pypi.org/project/black/).

pylint, for example, can help you to detect duplicate code:

```bash
pylint --disable=all --enable=duplicate-code,similarities
```


### Dependencies

Dependencies can break in two ways:

1. Breaking changes in new versions
2. Availability of Dependencies

Version pinning solves the first issue, but not the second one. A notable case was [left-pad in npm](https://en.wikipedia.org/wiki/Npm_(software)#Notable_breakages). Removing a single dependency killed a lot of the ecosystem.

You can avoid this by storing the depenencies, e.g. by having your own artifactory.


### Testing

There are lots of different things you can tests:

* Feature Tests
* Load-Tests
* Regression Tests: check if things still work. TODO: difference to unit tests / feature or load tests?
* Unit Tests
* Integration Tests
* End-to-End Tests
* Acceptance tests: Preconditions, postconditions, and assertions

Don't get confused by that. Tools like `pytest` can have exactly the same structure for an
unit test and an integration test.  They look the same. The difference is that an integration
tests doesn't only look at your code in isolation, but at the way your code works with an external
system.

Testing is a huge topic. I covered a bit of it in [Testing in Python](https://martin-thoma.com/testing-python-code/),
but there is certainly way more to write.

## Fault Tolerance

There are some issues we cannot prevent, but we can design systems that can deal with them.

<table class="table">
    <tr>
        <th>Fault</th>
        <th>Measure</th>
    </tr>
    <tr>
        <td>Harware outage</td>
        <td>Redundancy. In most cases, I would recommend to simply take a cloud provider so that you don't have to deal with those issues</td>
    </tr>
    <tr>
        <td>Disk Failure</td>
        <td>Replication (e.g. <a href="https://en.wikipedia.org/wiki/RAID">RAID</a>)</td>
    </tr>
    <tr>
        <td>Network Transmission Errors</td>
        <td>Error-correcting codes; checksums. Some protocols like <a href="https://en.wikipedia.org/wiki/Transmission_Control_Protocol">TCP</a> do this automatically. Others, like <a href="https://en.wikipedia.org/wiki/User_Datagram_Protocol">UDP</a>, don't do it.</td>
    </tr>
    <tr>
        <td>Too high usage</td>
        <td>Graceful Degradation: It might be that you get so many users, you have to shut things down. You might then, for example, just switch off the computationally expensive features. For example, if you have an interactive service you could instead serve a static version of it.</td>
    </tr>
</table>


## Fault Detection

Some faults slip through your system and cause an issue which can be seen by the customer. You can't prevent or tolerate every fault.

But at least you can make sure that you notice when things go wrong. You can add logging to your service / application.
When you use structured logging (JSON line log messages), you can easily create dashboards.

Several services also make this visible to their customers in form of a status page ([Azure](https://status.azure.com/de-de/status), [AWS](https://status.aws.amazon.com/), [GitHub](https://www.githubstatus.com/), ...)

For severe cases, you also want alerting: A slack notification, an e-mail or an SMS.

By releasing the software first to a small group of beta-testers you can make sure that issues are less
severe. For web serivces, this is called a canary release / canary deployment.


## Incidence Management


Jeff Atwood has written [Not All Bugs Are Worth
Fixing](https://blog.codinghorror.com/not-all-bugs-are-worth-fixing/) in which
he mentions the bug triage:

> Eric lists four questions that need to be answered during triage to decide
> whether a bug should be fixed or not:
>
> * **Severity**: When this bug happens, how bad is the impact?
> * **Frequency**: How often does this bug happen?
> * **Cost**: How much effort would be required to fix this bug?
> * **Risk**: What is the risk of fixing this bug?

To estimate severity, risk and cost, you need to know something about the system.
For the severity, you have to be able to estimate the consequences.

In order to estimate frequency, logs can help.

Once you've answered those questions and decided that the incidence actually is
severe enough to take further action, you might want to escalate it. First, get
everybody who is important for that in your organization in one (chat) room to
discuss it. This might be developers of several teams, people from user support
who might get questions about that problem, maybe even external companies.

Once the incident is resolved or at least all of the information is on the table,
you should write an [incidence postmortem](https://www.atlassian.com/incident-management/postmortem).
This is a document intendet to give transparency to everybody and to prevent
similar things from happening again. It is NOT about blaming people. You might
even want to publish them. Here are a couple of incident postmortems which
were made public:

* Microsoft: [Performance Issues and failures in VSTS West Europe, 2018-02-07](https://devblogs.microsoft.com/devopsservice/?p=16295) ([archive](https://devblogs.microsoft.com/devopsservice/?cat=2))
* Cloudflare: [Cloudflare outage, 2019-07-02](https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/)
* Facebook: [Configuration, 2015-01-29](https://blog.thousandeyes.com/facebook-outage-deep-dive/)
* Google: [Configuration, 2014-01-24](https://googleblog.blogspot.com/2014/01/todays-outage-for-several-google.html)
* AWS: [DynamoDB Service Disruption and Related Impacts the US-East](https://aws.amazon.com/de/message/5467D2/)
* [many more](https://github.com/danluu/post-mortems)

See also:

* Google: [Postmortem Culture: Learning from Failure](https://landing.google.com/sre/sre-book/chapters/postmortem-culture/)
* Atlassian: [Incident Postmortem Template](https://www.atlassian.com/incident-management/postmortem/templates)


## Maintenance

Every software system needs maintenance. For example, you might need
to update a timezone database. You might need to apply security patches of
third-party dependencies you use. Upgrading the dependencies regularly makes
it easier to upgrade. Look for deprecation warnings. Upgrading a single
dependency when you have a good test suite is no big deal. Upgrading
a lot of dependencies after years is not so fun.

And you might have ticking bombs. This is part of the software that is expected
to fail. It's usually a decision which was made to simplify the work for the
moment, but is expected to be fixed in future. Many time-related things
like the [Year 2000 problem](https://en.wikipedia.org/wiki/Year_2000_problem)
or the [Year 2038 problem](https://en.wikipedia.org/wiki/Year_2038_problem)
are in this category.

## Checklists

Here are a few simple questions that might lead to more reliable software.

### Software Development Process

This checklist focuses on your software development process. It is pretty
general and is intendet to not depend on the specific software you're
developing.

1. Do you use Software Versioning (e.g git)?
2. Do you have Pull Requests (Merge Requests) and Reviews?
3. Testing
    1. Do you have (enough) unit tests? (Line coverage, branch coverage)
    2. Do you have (enough) integration tests?
    3. Did you run load tests?
    4. Did you let users run your software?
4. Do you have log messages so that you can figure out what happened in case of
   a failure?
5. Do you have a blame-free incident management process with post-mortems for
   severe cases?
6. Do you have a CI/CD system in place? (e.g. [Gitlab CI/CD](https://docs.gitlab.com/ee/ci/pipelines/) and [many more](https://github.com/marketplace/category/continuous-integration))

### Web Services

A web service is anything that runs continuously in the web. It needs to be
available and deal with different changing load. It could be a website or
an API.

1. Do you have a `dev`, `stg` and `prd` environment?
2. Do you specify your infrastructure as code? (see
   [IaC](https://en.wikipedia.org/wiki/Infrastructure_as_code), e.g. [AWS
   CloudFormation](https://aws.amazon.com/de/cloudformation/))
3. Do you have a [load balancer](https://en.wikipedia.org/wiki/Load_balancing_(computing))? (e.g.
   [nginx](https://en.wikipedia.org/wiki/Nginx) or [AWS ELB](https://aws.amazon.com/de/elasticloadbalancing/))
4. Can you scale your infrastructure horizontally? (e.g. [AWS Auto Scaling](https://aws.amazon.com/de/autoscaling/))
5. Do you have [canary releases](https://en.wikipedia.org/wiki/Feature_toggle#Canary_release)?
6. Monitoring
    1. Do you have a health check in place which is independant of your current system?
    2. Do you show relevant system metrics (e.g. CPU and memory usage) in an easily accessible way (e.g. a Dashboard)?
    3. Do you show relevant business metrics (e.g. number of users) in an easily accessible way?
    4. Do you have a clear system who is on-call? Are those people able to fix issues? Did you train and try error cases?
7. Alerting: Do you have alerts for severe issues to trigger immediate attention?
8. Backups:
    1. Do you create backups of critical data regularly?
    2. Do you always have at least two independent backups?


Hardware:

1. Do you have redundant network connections?
2. Do you have redundant power supply?

If it is an API:

1. Did you add a specification? (e.g. [OpenAPI](https://en.wikipedia.org/wiki/OpenAPI_Specification))
2. Did you version the API?

### Applications

1. Do you have an update mechanism in place?
2. Did you run it on all platforms you want to support?
3. Is it clear to the customer where and how they can get support / report issues?

## See also

* Sazzad Hissain Khan: [Distinguishing System Robustness, Resilience, Stability, Flexibility and Performance](https://medium.com/@hissain.khan/distinguishing-system-robustness-resilience-stability-flexibility-and-performance-f509e87bcc49) on Medium, May 2019.
* Wikipedia:
    * [Reliability, availability and serviceability](https://en.wikipedia.org/wiki/Reliability,_availability_and_serviceability)
    * [Infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_code)
    * [Fault tolerance](https://en.wikipedia.org/wiki/Fault_tolerance)
* Stack Exchange:
    * [Understanding what Fault, Error and Failure mean](https://stackoverflow.com/q/6323049/562769)
* Algirdas Avizienis, Jean-Claude Laprie, Brian Randell, and Carl Landwehr: [Basic Concepts and Taxonomy of Dependable and Secure Computing](https://www.nasa.gov/pdf/636745main_day_3-algirdas_avizienis.pdf) in IEEE Transactions on Dependable and Secure Computing, 2004.
* Igor Perikov: [5 patterns to make your microservice fault-tolerant](https://itnext.io/5-patterns-to-make-your-microservice-fault-tolerant-f3a1c73547b3), 2020-01-08.

## Footnotes

[^1]: Avizienis, Algirdas, Jean-Claude Laprie, and Brian Randell: [Fundamental Concepts of Dependability](https://www.cs.rutgers.edu/~rmartin/teaching/spring03/cs553/readings/avizienis00.pdf), 2001.

---
layout: post
title: API Design
slug: api-design
author: Martin Thoma
date: 2018-03-07 20:00
category: The Web
tags: API, Web, Design
featured_image: logos/development.png
---
Today, I gave API design a little bit of thought. Web APIs to be more specific.
So here are some good practices I've seen. Feel free to add more in the
comments 😊


## General Thoughts

An API is written because you want to make a public interface to your
application. You will not know who is using your service. For this reason, you
have to keep things running for quite a while. Changes in an endpoint could
potentialy cause another service to crash. You want your stuff to be reliable,
so think about that in advance.

Oh, and JSON is likely the most common way to return information in the web.
So make sure your responses are valid JSON and you include
`Content-Type: application/json` in the header. Consequently, you can expect
the payload to be valid JSON as well.


### Character Sets

Use UTF8. Always. Everywhere.

See also: [Should character encodings besides UTF-8 (and maybe UTF-16/UTF-32) be deprecated?](https://softwareengineering.stackexchange.com/q/40063/25699)


### Monitoring

You offer a service, so please make sure it is available. You could use services
like [Runscope](https://www.runscope.com/api-monitoring) which ping your
endpoints regularly.

To give your users a way to check if things look normal, you could create a
status page. A popular choice is [statuspage.io](https://www.statuspage.io).
Some examples of status pages:

* [status.aws.amazon.com(http://status.aws.amazon.com)
* [status.github.com](https://status.github.com/messages)
* [status.bitbucket.org](https://status.bitbucket.org)


### Server Time

Make sure your server time is not too off. This makes comparing logs of
different systems easier. And it could be that you use the system time directly
or indirectly as an API output. You can use an [NTP server](https://en.wikipedia.org/wiki/Network_Time_Protocol)
to sync the time.

For manual checking.

```
$ ntpq -pn
     remote           refid      st t when poll reach   delay   offset  jitter
==============================================================================
 0.ubuntu.pool.n .POOL.          16 p    -   64    0    0.000    0.000   0.000
 1.ubuntu.pool.n .POOL.          16 p    -   64    0    0.000    0.000   0.000
 2.ubuntu.pool.n .POOL.          16 p    -   64    0    0.000    0.000   0.000
 3.ubuntu.pool.n .POOL.          16 p    -   64    0    0.000    0.000   0.000
 ntp.ubuntu.com  .POOL.          16 p    -   64    0    0.000    0.000   0.000
+92.222.82.98    130.149.17.8     2 u   75  128  377   24.430   -0.043   1.522
*185.51.192.34   46.243.26.34     2 u   44  128  377   27.447   -0.319   1.120
-212.18.3.19     212.18.1.106     2 u   61  128  377   16.443   -0.317   1.454
+88.159.1.196    193.190.230.66   2 u   47  128  377   29.346    0.564   1.828
-192.33.96.102   .PPS.            1 u  113  128  377   40.525    3.008   2.11
```


## Naming
Suppose we would have an API which lets us create / delete / receive users. I
would expect the following:

* GET `domain.io/api/users`: Returns a list of all users
* GET `domain.io/api/users/42`: Returns the user with ID 42
* POST `domain.io/api/users`: Creates a new user
* DELETE `domain.io/api/users/42`: Deletes the user with ID 42

This kind of logic should be consistent through the complete API.

For the filed names, I suggest to use **camelCase** as it is usually done with
JSON.

For the names, I suggest to use **plural forms**. The main point is to be
consistent.


## Versioning

Having an URL structure like `domain.io/api/v1/foobar` is really nice. This
allows you to change some of the practices and be consistent. So you could
follow some naming schemas vor `/v1/*` and others for `/v2/*`. Or change the
authentication.


## List-returning Endpoints

**Please note**: You might want to read [Web API Pagination with the 'Timestamp_Offset_Checksum' Continuation Token](https://blog.philipphauer.de/web-api-pagination-continuation-token/#offset-pagination) - don't take the following as the best option for granted!

Always when you return lists, make it paginated. Add a **default sorting**
and an **offset parameter**. You could also add an **order** and a **limit** parameter.

The endpoint should return

```
{"continue": 100,
 "data": FOOBAR}
```

where the value of `continue` is the next index to continue. So in case you
decide that an limit of 100 returned elements is enough / reasonable, the
the first query that has more than 100 elements would return the `continue` of
100. A call with an `offset=142` wuld have an `"continue": 242` in the
response, if there are at least 242 elements.

It is done similar in the [MediaWiki API](https://www.mediawiki.org/wiki/API:Query).


## Documentation

Add an `format` parameter to every `GET` query. If it is not specified, then
you can return documentation and/or a formatted response.

See [MediaWiki as an example](https://en.wikipedia.org/w/api.php?action=query&generator=allpages&gaplimit=3&gapfrom=Ba&prop=links%7Ccategories&format=jsonfm&formatversion=2).

Also, you should be really careful about units:

* **Prices**: Always document the currency. I suggest to use cents so that you
  can use integers and don't have to deal with floating point precision
  problems.
* **Dates**: There are timezones. I suggest to use the [ISO 8601](https://de.wikipedia.org/wiki/ISO_8601) with
  datetime as used for ECMA consistently: `YYYY-MM-DDTHH:mm:ss+00:00` (UTC), e.g `2018-03-07T21:37:24+00:00`.
* **SI Units**: Use [SI units](https://en.wikipedia.org/wiki/International_System_of_Units) as a default. If you don't use them, make a big warning sign.


## Errors

Help your API users by making nice error messages. Something like

```
HTTP Status 400

{
    "errors": [
        {
            "status": 400,
            "error": "FIELDS_VALIDATION_ERROR",
            "detail": "Invalid country 'German'.",
            "fields": {
                "country": "Invalid country. See ISO 3166 ALPHA-3 for valid values."
            },
            "code": 1337,
            "links": {
                "docs": "http://domain.io/docs",
                "errors": "http://domain.io/docs/errors#1337"
            }
        }
    ]
}
```


## Security

### HTTPS

Use HTTPS.


### Authentication

Give an concrete example how one should authenticate. Most likely, there will
be a token system. Be absolutely clear when the tokens expire.

If loosing the token could lead to people not being able to access your service
for a while, make sure they know it! This could be the case if one account may
only have one active token.


See also:

* [Authentication versus Authorization](https://stackoverflow.com/q/6556522/562769)
* [Introduction to JSON Web Tokens](https://jwt.io/introduction/)

### Input Validation

Don't let users input go directly to the database / be part of the execution.

See [SQL injection](https://en.wikipedia.org/wiki/SQL_injection)


## Other Stuff

There are a couple of other rules, but I'm not sure how important they actually
are:

### HTTP Methods

Copied from [developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods):

* `GET`: [...] Requests using GET should only retrieve data.
* `POST`: The POST method is used to submit an entity to the specified
  resource, often causing a change in state or side effects on the server
* `PUT`: The PUT method replaces all current representations of the target
  resource with the request payload.
* `PATCH`: The PATCH method is used to apply partial modifications to a
  resource.
* `DELETE`: The DELETE method deletes the specified resource.


### HTTP Response Status codes:

#### Success: 2XX

* 200 OK: Successful GET, PUT, PATCH
* 201 Created: Successful POST
* 204 No Content: For successful DELETE

#### Client Errors: 4XX

* 400 Bad Request: E.g. the parameters are invalid
* 401 Unauthorized
* 403 Forbidden: Authenticated, but the client may not access the endpoint
* 404 Not Found
* 410 Gone: For deprecation

#### Server Errors: 5XX

* 500 Internal Server Error
* 503 Service Unavailable: Maintenance


## See also

* [GraphQL](http://graphql.org/learn/): A data query language developed internally by Facebook which is an alternative to REST, see [GraphQL vs REST](https://philsturgeon.uk/api/2017/01/24/graphql-vs-rest-overview/)
* [RESTful API Design. Best Practices in a Nutshell.](https://blog.philipphauer.de/restful-api-design-best-practices/)
* [jsonapi.org](http://jsonapi.org/format/#status)

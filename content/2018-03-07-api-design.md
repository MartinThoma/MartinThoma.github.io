---
layout: post
title: API Design
slug: api-design
lang: en
author: Martin Thoma
date: 2018-03-07 20:00
category: The Web
tags: API, Web, Design
featured_image: logos/development.png
---
Today, I gave API design a little bit of thought. Web APIs to be more specific.
So here are some good practices I've seen.


## General Thoughts

Once others use your API, every change can break their software. For a public
API, you don't even know who they are. So you have to keep things running for
quite a while, and changes need a plan (see [Versioning](#versioning)). You want
your stuff to be reliable, so think about that in advance.

Oh, and JSON is likely the most common way to return information on the web.
So make sure your responses are valid JSON and you include
`Content-Type: application/json` in the header. Don't assume that requests are
valid JSON, though: validate every payload. Answer with `400 Bad Request` if it
is broken and with `415 Unsupported Media Type` if the client sends something
else.


### Character Sets

Use UTF-8. Always. Everywhere.

See also: [Should character encodings besides UTF-8 (and maybe UTF-16/UTF-32) be deprecated?](https://softwareengineering.stackexchange.com/q/40063/25699)


### Monitoring

You offer a service, so please make sure it is available. You could use services
like [Runscope](https://www.runscope.com/api-monitoring) which call your
endpoints regularly.

To give your users a way to check if things look normal, you could create a
status page. Popular choices are [statuspage.io](https://www.statuspage.io) and [Atlassian Statuspage](https://www.atlassian.com/software/statuspage).
Some examples of status pages:

* [health.aws.amazon.com](https://health.aws.amazon.com/health/status)
* [githubstatus.com](https://www.githubstatus.com/)
* [bitbucket.status.atlassian.com](https://bitbucket.status.atlassian.com/)


### Server Time

Make sure your server time is not too far off. This makes comparing logs of
different systems easier. And it could be that you use the system time directly
or indirectly as an API output. You can use an [NTP server](https://en.wikipedia.org/wiki/Network_Time_Protocol)
to sync the time.

For manual checking: on current Linux systems, `timedatectl` shows
`System clock synchronized: yes` if the clock is synced. If you run ntpd,
`ntpq -pn` shows the details:

```shell
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
Suppose we have an API which lets us create / retrieve / update / delete users.
I would expect the following:

* GET `example.com/api/users`: Returns a list of all users
* GET `example.com/api/users/42`: Returns the user with ID 42
* POST `example.com/api/users`: Creates a new user
* PUT `example.com/api/users/42`: Replaces the user with ID 42 (PATCH: changes
  only the fields that are sent)
* DELETE `example.com/api/users/42`: Deletes the user with ID 42

This kind of logic should be consistent through the complete API.

For the field names, pick one style and use it everywhere. JSON itself does not
prescribe one: **camelCase** is common in the JavaScript world, but many large
APIs use **snake_case**, for example `created_at` in the
[GitHub REST API](https://docs.github.com/en/rest).

For the resource names, I suggest using **plural forms** (`/users`, not
`/user`). The main point is to be consistent.

And, of course, there is the actual value of IDs. Sequential IDs tell others how
many users you have and let them iterate through your data. Random IDs such as
UUIDs (version 4) avoid that. But they are no access control: every endpoint
still has to check whether the caller may access the requested object. Missing
these checks is the first risk in the
[OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/).


## Versioning

Having a URL structure like `example.com/api/v1/foobar` is really nice. This
allows you to change some of the practices and be consistent. So you could
follow some naming schemes for `/v1/*` and others for `/v2/*`. Or change the
authentication.

Not every change needs a new version. Adding an endpoint or an optional field is
backwards compatible, as long as clients ignore fields they don't know; tell them
to do so. Removing or renaming a field, changing its type or meaning, or making
a parameter required breaks clients and needs a new version.

When you plan to remove an old version, announce it early. The `Deprecation`
header ([RFC 9745](https://www.rfc-editor.org/rfc/rfc9745)) and the `Sunset`
header ([RFC 8594](https://www.rfc-editor.org/rfc/rfc8594)) tell clients in every
response that an endpoint is deprecated and when it will go away.


## List-returning Endpoints

**Please note**: You might want to read [Web API Pagination with the 'Timestamp_Offset_Checksum' Continuation Token](https://phauer.com/2017/web-api-pagination-continuation-token/#offset-pagination) - don't take the following as the best option for granted!

Whenever you return lists, make them paginated. Add a **default sorting**
and an **offset parameter**. You could also add an **order** and a **limit** parameter.

The endpoint should return:

```json
{"continue": 100, "data": [...]}
```

where the value of `continue` is the offset of the next page. So in case you
decide that a limit of 100 returned elements is enough / reasonable,
the first query that has more than 100 elements would return the `continue` of
100. A call with an `offset=142` would have a `"continue": 242` in the
response, if there are more than 242 elements. On the last page, `continue` is
missing.

It is done similarly in the [MediaWiki API](https://www.mediawiki.org/wiki/API:Query).

[Django REST framework](https://www.django-rest-framework.org/api-guide/pagination/)
uses this format for its page number and limit/offset pagination, here for
`?limit=100&offset=100`:

```json
{
    "count": 1023,
    "next": "https://example.com/api/users?limit=100&offset=200",
    "previous": "https://example.com/api/users?limit=100",
    "results": [...]
}
```

`count` is the total number of elements. `next` and `previous` are complete URLs,
so clients don't have to build them; they are `null` on the last and on the
first page. The cursor pagination of Django REST framework returns the same
format without `count`.

Offset pagination has two weaknesses: if elements are inserted or deleted while a
client pages through the list, it skips or repeats elements, and large offsets
are slow in many databases. A continuation token (see the note above) avoids both.


## Documentation

Describe your API in an [OpenAPI](https://www.openapis.org/) document. It is the
de-facto standard: tools generate interactive documentation, client libraries and
tests from it. Give a working example request and response for every endpoint.

A nice addition for humans: MediaWiki has a `format=jsonfm` parameter that shows
the response as a formatted HTML page in the browser. See
[MediaWiki as an example](https://en.wikipedia.org/w/api.php?action=query&generator=allpages&gaplimit=3&gapfrom=Ba&prop=links%7Ccategories&format=jsonfm&formatversion=2).

Also, you should be really careful about units:

* **Prices**: Never send a price as a bare number. I suggest an object with
  three fields: `{"amount": 1999, "digits": 2, "currency": "EUR"}` means
  19.99 EUR (1999 / 100). `amount` is an integer, so you don't have to deal
  with floating point precision problems. `digits` says how many decimal places
  the amount has, and `currency` is the
  [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code. Because `digits` is
  part of the value, clients don't need a table of currencies, and not every
  currency has 100 subunits: the Japanese yen has none
  (`{"amount": 500, "digits": 0, "currency": "JPY"}`), the Kuwaiti dinar has
  1000 fils (`{"amount": 1250, "digits": 3, "currency": "KWD"}` is
  1.250 KWD). `digits` also covers prices that are more precise than the
  currency, like fuel at 1.799 EUR per liter
  (`{"amount": 1799, "digits": 3, "currency": "EUR"}`).
  [Stripe](https://docs.stripe.com/currencies) also sends integer amounts, but
  without `digits`: clients have to know from its documentation which currencies
  have no decimal places.
* **Dates**: There are timezones. I suggest using
  [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339), a strict profile of
  [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601), in UTC:
  `2018-03-07T21:37:24Z`. JavaScript's `toISOString()` produces this format with
  milliseconds: `2018-03-07T21:37:24.000Z`. For a date without a time, use
  `2018-03-07`. See also my article about [datetime](../datetime/).
* **SI Units**: Use [SI units](https://en.wikipedia.org/wiki/International_System_of_Units) as a default. If you don't use them, make a big warning sign.


## Errors

Help your API users by making nice error messages. Something like:

```text
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
                "docs": "https://example.com/docs",
                "errors": "https://example.com/docs/errors#1337"
            }
        }
    ]
}
```


## Security

### HTTPS

Use HTTPS. Redirecting plain HTTP to HTTPS does not help much for an API: a
client that sent its token over plain HTTP has already exposed it. Better reject
plain HTTP requests.


### Authentication

Give a concrete example of how one should authenticate. Most likely, there will
be a token system. Be absolutely clear when the tokens expire.

Clients should send the token in the `Authorization` header, never in the URL:
URLs end up in server logs, proxy logs and the browser history.

If losing the token could lead to people not being able to access your service
for a while, make sure they know it! This could be the case if one account may
only have one active token.


See also:

* [Authentication versus Authorization](https://stackoverflow.com/q/6556522/562769)
* [Introduction to JSON Web Tokens](https://jwt.io/introduction/)

### Input Validation

Validate all input: types, lengths, ranges and allowed values. Validation alone
does not prevent injections, though. Never build database queries from user input
by string concatenation; use parameterized queries.

See [SQL injection](https://en.wikipedia.org/wiki/SQL_injection) and my article
about [SQL injections](../sql-injections/).


### Rate Limiting

Limit how many requests a client may make, so that one client cannot take down
the service for everyone. Answer with `429 Too Many Requests`
([RFC 6585](https://www.rfc-editor.org/rfc/rfc6585)) and a `Retry-After` header
that says when the client may try again.


## HTTP Methods and Status Codes

### HTTP Methods

Copied from [developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods):

* `GET`: [...] Requests using GET should only retrieve data.
* `POST`: The POST method is used to submit an entity to the specified
  resource, often causing a change in state or side effects on the server
* `PUT`: The PUT method replaces all current representations of the target
  resource with the request payload.
* `PATCH`: The PATCH method is used to apply partial modifications to a
  resource.
* `DELETE`: The DELETE method deletes the specified resource.

One property matters for clients that retry after a timeout: `GET`, `PUT` and
`DELETE` are *idempotent*
([RFC 9110](https://www.rfc-editor.org/rfc/rfc9110#section-9.2.2)), sending the
same request twice has the same effect as sending it once. `POST` and `PATCH`
are not. If a `POST` times out, the client cannot know whether the user was
created. Stripe solves this with an
[idempotency key](https://docs.stripe.com/api/idempotent_requests): the client
sends a unique key with the request, and the server performs a request with a
known key only once.


### HTTP Response Status codes

#### Success: 2XX

* 200 OK: Successful GET, PUT, PATCH
* 201 Created: A POST created a resource; its URL goes into the `Location` header
* 202 Accepted: The request was accepted and will be processed later
* 204 No Content: Success without a response body, e.g. for a DELETE

#### Client Errors: 4XX

* 400 Bad Request: E.g. the parameters are invalid
* 401 Unauthorized: Despite the name, the client is not *authenticated*: the
  token is missing or invalid
* 403 Forbidden: Authenticated, but the client may not access the resource
* 404 Not Found
* 409 Conflict: The request conflicts with the current state, e.g. the user
  already exists
* 410 Gone: The resource existed, but was removed for good, e.g. an endpoint
  after its sunset date
* 415 Unsupported Media Type: E.g. the body is not JSON
* 422 Unprocessable Content: The JSON is valid, but the values are not (some APIs
  use 400 for this)
* 429 Too Many Requests: The client exceeded the rate limit

#### Server Errors: 5XX

* 500 Internal Server Error
* 503 Service Unavailable: E.g. maintenance or overload; add a `Retry-After`
  header


## GraphQL

This article was mainly about REST-like APIs. [GraphQL](https://graphql.org/learn/) is a query language for APIs which Facebook developed internally and published in 2015; today the [GraphQL Foundation](https://graphql.org/foundation/) maintains it. It is an alternative to REST, see [GraphQL vs REST](https://philsturgeon.com/graphql-vs-rest-overview/).

A GraphQL API has a typed schema that clients can query, so tools can show all
types and fields automatically. You still have to document what the fields
mean. You buy that advantage with overhead in writing
[the resolvers](https://graphql.org/learn/execution/), and with new problems:
HTTP caching is harder because all queries go to one endpoint, and clients can
send very expensive queries, so you need limits for query depth and complexity.

## See also

* My article about [REST](../rest/)
* [RESTful API Design. Best Practices in a Nutshell.](https://phauer.com/2015/restful-api-design-best-practices/)
* [jsonapi.org](https://jsonapi.org/format/#status)
* [OWASP API Security Top 10](https://owasp.org/API-Security/)

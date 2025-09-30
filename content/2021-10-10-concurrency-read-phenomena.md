---
layout: post
lang: en
title: Database Read Phenomena
slug: db-read-phenomena
author: Martin Thoma
status: draft
date: 2021-05-31 20:00
category: Cyberculture
tags: Rating
featured_image: logos/star.png
---
We have seen phenomenal improvements in the hardware in the last 30 years. Moore observed that the number of transistors in a dense integrated circuit (IC) doubles roughly every two years, the CPU clock rate increased from 740 kHz in 1970 to 4.9 GHz in 2021, and the types of instructions CPUs can execute got more complex over time. But there are limits to increasing the clock rate and adding more complex instructions. Instead of doing that, CPU manufacturers added the possibility to execute more stuff concurrently. This comes with its own set of problems.

To me, the most interesting ones are in the context of web services. And most prominently, there are interactions with a central database and are related to transaction isolation. In this article, you will learn what the 3 best-known read phenomena are and which transaction isolation levels fix them. Let's start!

## The Basics

Databases organize multiple operations in transactions. You can imagine a database as a sequence of transactions. If a transaction is part of the database, we say it is committed. If a transaction fails, a rollback is executed. The transaction is undone.

We want transactions to be atomic. If a transaction fails, the database is left in a consistent state. If a transaction succeeds, the database is left in a consistent state. If a transaction is not committed, the database is left in a consistent state. If a transaction is not committed, the database is left in a consistent state.

We also want transaction isolation - concurrent executions of transaction don't lead to different results than serial executions. It should not matter if transactions are executed one after each other or in parallel.

The problems with concurrent execution are:

The problems we will investigate in this article are called read phenomena and they occur when the isolation property is broken. Having a stronger isolation comes at a cost. The tradeoff is speed versus guarantees that certain problems don't occur. These guarantees are called transaction isolation levels. Controlling the issues is also called concurrency control. There is optimistic and pessimistic concurrency control. Optimistic concurrency control uses

<table>
    <tr>
        <th>Isolation Level</th>
        <th>Dirty Read</th>
        <th>Non-repeatable Read</th>
        <th>Phantom Read</th>
    </tr>
    <tr>
        <td>READ_UNCOMMITTED</td>
        <td style="text-align: center;">💩</td>
        <td style="text-align: center;">💩</td>
        <td style="text-align: center;">💩</td>
    </tr>
    <tr>
        <td>READ_COMMITTED</td>
        <td style="text-align: center;">✅</td>
        <td style="text-align: center;">💩</td>
        <td style="text-align: center;">💩</td>
    </tr>
    <tr>
        <td>REPEATABLE_READ</td>
        <td style="text-align: center;">✅</td>
        <td style="text-align: center;">✅</td>
        <td style="text-align: center;">💩</td>
    </tr>
    <tr>
        <td>SERIALIZABLE</td>
        <td style="text-align: center;">✅</td>
        <td style="text-align: center;">✅</td>
        <td style="text-align: center;">✅</td>
    </tr>
</table>

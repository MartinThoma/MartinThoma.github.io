---
layout: post
lang: en
title: The Blockchain
subtitle: An Introduction to Blockchain, Bitcoin ₿, and related concepts
slug: blockchain
URL: https://medium.com/coinmonks/the-blockchain-473aac352e5
author: Martin Thoma
date: 2021-01-13 20:00
category: Blockchain
tags: Blockchain
featured_image: logos/star.png
---
![An example of a blockchain. Image by Martin Thoma.](https://cdn-images-1.medium.com/max/3606/1*PnKV_yIgbdLZMehrIlM1ZQ.png)*An example of a blockchain. Image by Martin Thoma.*

Bitcoin crossed $40,000 USD for the first time recently, so it’s again in the news. Bitcoin is just the most-known **cryptocurrency**. It is one application using a **blockchain**. In this article, I will walk you through some core concepts of blockchain and cryptocurrencies. This article is written for beginners and a bit fluffy in some areas. There will be follow-up articles to address that. Let’s start!

## The Idea of a Ledger

![German Ledger from 1828 (Source: [RaphaelQS](https://commons.wikimedia.org/wiki/File:Ledger.png))](https://cdn-images-1.medium.com/max/3412/1*FTMD4L4J-UYMwVAjGP65UQ.png)*German Ledger from 1828 (Source: [RaphaelQS](https://commons.wikimedia.org/wiki/File:Ledger.png))*

Suppose we lived in a simpler world without credits and with only one bank. Everybody just owns a non-negative amount of money. The bank keeps track of transactions. Let’s say we have three students living in the same shared apartment: Anna, Bob, and Charlie. They all put $100 USD in their bank account:

```text
Date             | Sender    | Receiver |  Amount
-------------------------------------------------
2021-01-01 06:00 | (Deposit) | Anna     |    $100
2021-01-01 06:01 | (Deposit) | Bob      |    $100
2021-01-01 06:08 | (Deposit) | Charlie  |    $100
```

Now they make a few transactions. Before the bank's system accepts any transaction, it checks if the account balance would still be non-negative. To get the account balance, they can sum up all previous transactions. To make it a bit easier to follow, I will shorten the “Date” to just a number counting up and add the balance after the transaction is executed for **A**nna, **B**ob, and **C**harlie to the table. The ABC columns are just for you to keep track of; they are not necessary:

```text
Date | Sender   | Receiver | Amount |       A  |  B   |  C
------------------------------------|     ------------------
1    | (Deposit)| Anna     | $100   |     $100 |   $0 |   $0
2    | (Deposit)| Bob      | $100   |     $100 | $100 |   $0
3    | (Deposit)| Charlie  | $100   |     $100 | $100 | $100
4    | Bob      | Charlie  |  $20   |     $100 |  $80 | $120
5    | Bob      | Anna     |  $30   |     $130 |  $50 | $120
6    | Anna     | Bob      | $130   |     $0   | $180 | $120
```

Hence the ledger is just a database of all transactions.

(I’m simplifying a lot here. If you’re interested in [Accounting Stuff](https://www.youtube.com/channel/UCYJLdSmyKoXCbnd-pklMn5Q), James Hearle summarized those ideas and more, including double-entry accounting in the linked channel.)

## How to get rid of the Bank

![Photo by [the blowup](https://unsplash.com/@theblowup?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/9832/0*CpxtEZdU4BBJgDa8)*Photo by [the blowup](https://unsplash.com/@theblowup?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*

Anna, Bob, and Charlie are unhappy with their bank. They don’t like that it takes typically two working days until the booked transaction actually takes place. They are unhappy with paying fees. They wonder what would happen if their bank suddenly closed or maybe even manipulated the numbers.

As Anna, Bob, and Charlie live in the same apartment and they spent their money on stuff for the apartment (soap, toilet paper, dishwasher tabs, …), they put a list on the fridge. They simply make it public who made which transaction. They don’t have complete trust in each other, though.

For example, Bob might write in the ledger that he got $20 from Charlie — although Charlie never approved that. To make sure **only the account owners can send money** from their accounts, every new transaction needs the **signature** of the sender. To make sure that **everybody only sends money they have**, the **remaining participants check the balance of the sender**. If an invalid balance is seen, the transaction is rejected.

They also want to make sure that **nobody can erase any transaction**. The solution is simple: Every transaction gets an incrementing transaction number.

## Let’s make it digital!

![Photo by [Joshua Sortino](https://unsplash.com/@sortino?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/8390/0*KWahhiN2IJx8UXSR)*Photo by [Joshua Sortino](https://unsplash.com/@sortino?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*

Anna, Bob, and Charlie want to be certain they will never lose their ledger. Instead of having a single central ledger, they decide to **distribute** it. They all want to have a copy of it.

Being young students, all of them happen to have a website. So they come up with this protocol which they all want to follow:

1. If anybody wants to make a new transaction, they add the transaction to the copy of the ledger they have on their website.

1. Everybody regularly checks if there are newer transactions in any of the other ledgers.

1. If there is just one ledger with at least one new transaction, they just copy the newer transactions.

Then they notice two problems. The first one is the signature. Luckily, one of them heard of Public-Key Cryptography and digital signatures. They quickly realized that for any transaction, they can easily make a digital version of a signature that cannot be forged. The **digital signature** does not only prove who made the transaction but also makes sure that the content of the transaction is not modified. As the content of the transaction contains the transaction number it is also not possible to delete a single transaction. As the longest list of transactions is shared, one cannot simply crop a whole lot of transactions off at the end.

![Anna sees new transactions from Bob and Charlie. They all have the same green blocks, but bob discarded the blue blocks in which he sent money to charlie. He created the red and the yellow ones to fool Anna. Image by Martin Thoma](https://cdn-images-1.medium.com/max/3786/1*l_g-X3q0xEVBskHQQsrSQA.png)*Anna sees new transactions from Bob and Charlie. They all have the same green blocks, but bob discarded the blue blocks in which he sent money to charlie. He created the red and the yellow ones to fool Anna. Image by Martin Thoma*

What happens if Anna sees a new transaction from Bob and a new transaction from Charlie? Let’s say Anna has already confirmed that both, Bob and Charlie, have the same indices up to #42. Bob and Charlie had a lot of transactions after that and the correct latest transaction #60. But Bob doesn’t like that he had to send quite a bit of money to Charlie in transactions #43 to #60, so he simply writes 10 transactions after #42. Charlie still receives some money, but less than he should. Anna sees that Charlie has already transaction number #70 and ignores what Charlie has.

To prevent this, they make it more difficult to create a transaction. They have heard of [Hashcash](https://en.wikipedia.org/wiki/Hashcash) to prevent spammers from sending too many emails. The idea is to make the Email sender (the potential spammer) execute a computationally heavy function. The result of that function is easy to verify, but there is no way to speed the execution of the function up in the first place. The result is then called **Proof of Work**. The specific kind of proof of work that is typically used is called a **nonce**: Number only used once. Finding such a nonce is intentionally computationally intensive. This is what **mining** is. Alice, Bob, and Charlie agree to add the proof of work to each transaction. Thus re-calculating a lot of transactions is just not worth it anymore.

![Anna sees the same number of new transactions from Bob and Charlie, but transaction #43 is different. Bob tries to tamper with the amount he sent Charlie. Image by Martin Thoma](https://cdn-images-1.medium.com/max/3066/1*y7lcxfcKXW5GMUf8lq-aFw.png)*Anna sees the same number of new transactions from Bob and Charlie, but transaction #43 is different. Bob tries to tamper with the amount he sent Charlie. Image by Martin Thoma*

However, there is one big flaw: If they just store the transaction number, one could replace transactions in the middle. If Bob is unhappy that he has sent $100 to Charlie in transaction #43, he could just craft another transaction #43. So instead of storing the transaction number, they agree to store an identifier that is unique to the content of the previous transaction. A so-called **hash value**.

Let’s summarize:

* **Digital signatures** prevent **transaction forgery.**
* Storing the previous transactions' **hash value** prevents **dropping existing transactions** by the sender. It also prevents **duplication attacks**.
* Storing a **proof of work** per transaction prevents **re-computation of many transactions** at the end of the ledger.
* Having the chain of transactions, the ledger, **distributed** among all participants makes the current state **transparent**. It’s a pre-requisite of preventing the re-computation.

You might already have guessed it: A transaction in this example is pretty close to a block in the blockchain. In our example, a transaction contains:

* The hash value of the previous block
* Amount of transaction
* Sender
* Receiver

Those four elements are signed.

There is one special case: The first block. It does not have a previous block
and thus there cannot be a hash value of a previous block. The first block is
called the **genesis block**.

## Example vs Bitcoin

One part I haven’t addressed at all is how the users of Bitcoin interact. We
didn’t talk about the network at all. Just to be clear: It’s NOT the case that
everybody adds their own website and everybody else has to know and check. That
was just a simplification. There is a
[Peer-To-Peer](https://en.wikipedia.org/wiki/Peer-to-peer) protocol in place.

An important element of Bitcoin is the **consensus algorithm** which decides
what the latest block is. The network members check new data before it’s added
with a consensus mechanism. The consensus algorithm has two elements. One
consensus mechanism is **proof of work**. The proof of work mechanism uses the
computing capacity of the members to validate work. In the example, I made it
constant. It’s more complicated. The other element of the consensus algorithm
is that in the case of a draw, if multiple parties have created a new block at
exactly the same time, one waits until one of the chains gets longer. **The
longer chain wins**.

Bitcoin also does not store the account balance. [It’s more
complicated](https://bitcoin.stackexchange.com/q/29780/6721). It stores a
sequence of transactions. A transaction consists of inputs and outputs. The sum
of inputs must be greater than or equal to the sum of outputs. This way, the
double-spending problem is solved. The inputs must be associated with the
signature of the transaction — only the owner is allowed to send money. This
structure is the reason why you typically have two outputs: The receiver of the
money and your own address for the change. You can imagine every input as a
coin. Coins can only be split by having multiple outputs in a transaction, not
by taking a part of a coin as input. You can also join coins by having just one
output.

It took me quite a while and the help of [Rene
Pickhardt](https://www.rene-pickhardt.de/) to understand that Bitcoin is
actually NOT account-based, but everything that really matters is the
transactions. It’s not verified that the account is a non-negative balance, but
that a transaction spends only available money. That is a crucial difference!
Rene is an awesome educator; check out his [introductory video about electronic
cash](https://www.youtube.com/watch?v=TrF9RmfyLbw).

## Bitcoin vs Blockchain

![Photo by [Thought Catalog](https://unsplash.com/@thoughtcatalog?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/14934/0*IN19QU1F182EeISq)*Photo by [Thought Catalog](https://unsplash.com/@thoughtcatalog?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*

Bitcoin is an application that uses the blockchain. As an analogy, think of
email. Email is an application that uses the internet.

Blockchain Technology combines 4 concepts:

* Cryptography to ensure messages cannot be faked
* A Consensus Algorithm
* A data structure for storage
* Distribution via Peer-to-Peer protocols

For Bitcoin, those choices are:

* **Cryptography**: Bitcoin uses ECDSA for signatures, double SHA-256 for hashing
* **Consensus Algorithm**: Proof of Work (Proof of Stake would be an alternative)
* **Storage**: Merkle Tree
* **Distribution**: A TCP-based peer-to-peer protocol ([source 1](https://en.bitcoin.it/wiki/Protocol_documentation#cmpctblock), [source 2](https://developer.bitcoin.org/reference/p2p_networking.html))

## Blockchain vs DLT

Blockchain is a distributed ledger technology (DLT). Two other examples of DLT are [Tangle](https://en.wikipedia.org/wiki/IOTA_(technology)#The_Tangle) and [Hashgraph](https://hackernoon.com/demystifying-hashgraph-benefits-and-challenges-d605e5c0cee5).

## When is Blockchain useful?

As with every hype, people want to apply it everywhere. But where does it
actually make sense?

You can see the blockchain as a very special database. It only supports
insertions, but no deletions or edits. It’s **managed by the network**.
Depending on the protocol, this can mean that the data in the blockchain is
**immutable**. The data is **distributed**.

There are some properties where blockchain will never be able to compete with well-known database systems:

* **Insertion Speed**: Visa is able to handle 65k transactions/second
  ([source](https://usa.visa.com/dam/VCOM/download/corporate/media/visanet-technology/aboutvisafactsheet.pdf)),
  Bitcoin can only handle 7 transactions/second
  ([source](https://www.comp.nus.edu.sg/~prateeks/papers/Bitcoin-scaling.pdf)).
  That means, without the Bitcoin Lightning Network (BLN) extensions. With the
  BLN, the system can process over 10k transactions/second
  ([source](https://arxiv.org/pdf/2002.01374.pdf)).
* **Latency**: Probably less than 5 seconds for Visa, but about 1 hour for
  Bitcoin
  ([source](https://hackernoon.com/latency-and-finality-in-different-cryptocurrencies-a7182a06d07a)).
* **Queries**: We have lots of database types. Especially relational databases
  allow very complex queries. You will not have that with the blockchain.

Those alone already show that you want traditional database systems for a lot of problems. So let’s see where the Blockchain shines:

* **Cryptocurrencies **are probably the best-known examples of Blockchain
  technology as Bitcoin made the whole topic famous. The idea here is that you
  have a digital asset that cannot be forged. It’s impossible to create fake
  bitcoins. The government cannot decide to print new Bitcoins. The process is
  transparent and open to everybody: Every person and every organization.
  Privacy here is an interesting topic; if you’re interested I would write an
  own article about that. It also has challenges. For example, it’s impossible
  to get Bitcoin back if you lose your wallet. They are gone. For everybody.
  Forever. Or if somebody steals your computer and transfers them. If you get
  hacked. There is no court that can undo it.
* **Supply Chain Management**: Many brands nowadays want to make their supply
  chain more transparent. They want to prove to the customers where their
  product came from; “traceability” is the buzzword. They also want to make
  sure that counterfeits can be identified. So they upload data and about the
  origin of their products at every step. Those steps have timestamps and are
  very fine-granular. One problem the blockchain doesn’t solve is that all of
  the uploaded data could be faked. If you want to know more, get in touch with
  my friend [Peter Merkert](https://www.linkedin.com/in/petermerkert/). He
  built [retraced](https://retraced.co/), a company that supports the clothing
  industry in supply chain management. A big **thank you** also to him for
  proof-reading this article 🤗
* **Real Estate**: I know that in Germany we have pretty good maps of the
  country, of ownership of every single piece of land. The process of buying
  and selling land includes a trusted party — a
  [notary](https://en.wikipedia.org/wiki/Notary). The notary gets 1.5% of the
  amount you pay for the land. A square meter of land costs about 4000 EUR in
  Munich. A small house has about 300m² — so you would pay 1.2 million EUR for
  the land and thus 18k for the notary. This is a pretty good incentive to get
  rid of the notary, isn’t it? The other case is that you might not have such a
  process in all countries.
* **Capital Markets**: Blockchain-based digital securities provide cost
  advantages because they can be issued and exchanged without middlemen
  ([source](https://cashlink.de/cost-disruption/)). The numbers in this source
  are pretty crazy: [Cashlink](https://cashlink.de/) and Finoa estimate that
  cost savings from 35% to 65% for tokenization compared to traditional
  securitization are possible.
* **Energy** can be traded using blockchain. Read [When Energy Trading meets
  Blockchain in Electrical Power System: The State of the
  Art](https://arxiv.org/abs/1902.07233) to learn more.

A good sign that you might have a valid use case if there is **no trusted
middleman** or if you want to get rid of the middleman. Just look at the supply
chain case. If there is an organization that people trust, then you don’t need
to store the data in the blockchain. That organization just stores it in a
traditional database they control.

## What’s next

* Hashing: What it is, what cryptographic hashing is, what SHA / MD5 is
* Merkle Trees: What they are, how they work, and how they are used in Bitcoin
* Public-Key Cryptography and RSA: Public- and private keys, Digital Signatures, Trapdoor functions. What it is and why it’s so important
* Proof of Work: How it works, how difficult it is, and what Bitcoin / Ether / Stellar use.
* Smart contracts: What they are and how they work; e.g. with Etherium as an example
* [Initial Coin Offering](https://en.wikipedia.org/wiki/Initial_coin_offering) (ICO)
* Bitcoins consensus algorithm
* Bitcoin and the network: How do people connect?
* Bitcoin Wallets
* Peer-To-Peer Stuff: How Gossip Protocols work

Let me know what you’re interested in!

## See also

### Literature

* Satoshi Nakamoto: “[Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf)”, 2008.
* Gavin Wood: “[Ethereum: A secure decentralised generalised transaction ledger](http://gavwood.com/Paper.pdf)”, 2014
* [Patrick Schueffel](https://www.der-bank-blog.de/author/patrick-schueffel/): “[Alternative Distributed Ledger Technologies Blockchain vs. Tangle vs. Hashgraph — A High-Level Overview and Comparison](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3144241)”, 2017.

### Videos

Bosch created an awesome introductory video:

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/NKAanYdic9Q" frameborder="0" allowfullscreen></iframe></center>

And also 3Blue1Brown:

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/bBC-nXj3Ng4" frameborder="0" allowfullscreen></iframe></center>
> # Join Coinmonks [Telegram group](https://t.me/joinchat/EPmjKpNYwRMsBI4p) and learn about crypto trading and investing

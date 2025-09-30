---
layout: post
lang: en
title: How do hash functions work?
slug: how-do-hash-functions-work
author: Martin Thoma
date: 2013-05-11 20:07:07.000000000 +02:00
category: Code
tags: Programming, hash, C, datastructure, game tree, hashCode
featured_image: 2013/05/connect-four-thumb.gif
---
Everybody who has written a noticeable amount of Java code should know the method <code><a href="http://docs.oracle.com/javase/7/docs/api/java/lang/Object.html#hashCode()">hashCode</a>()</code>. But most beginners have difficulties to understand the significance of this little method. The following article gives you one small example with some impressions how much hash functions influence execution time.

<h2>Connect four</h2>
<blockquote>Connect Four [...] is a two-player game in which the players first choose a color and then take turns dropping colored discs from the top into a seven-column, six-row vertically-suspended grid. The pieces fall straight down, occupying the next available space within the column. The object of the game is to connect four of one's own discs of the same color next to each other vertically, horizontally, or diagonally before your opponent.
</blockquote>
<small>Source: <a href="http://en.wikipedia.org/wiki/Connect_Four">Wikipedia</a></small>

It looks like this:

<figure class="aligncenter">
            <a href="../images/2013/05/connect-four.gif"><img src="../images/2013/05/connect-four.gif" alt="Connect Four" style="max-width:320px;max-height:190px" class="size-full wp-image-65311"/></a>
            <figcaption class="text-center">Connect Four<br />Source: <a href='http://commons.wikimedia.org/wiki/File:Connect_Four.gif'>commons.wikimedia.org</a></figcaption>
        </figure>

<h2>The task</h2>
Imagine you would like to find a good strategy where to drop your disk. A simple brute-force method is to create a so called <a href="http://en.wikipedia.org/wiki/Game_tree">game tree</a>. This means you go through each possibility at each situation that could occur in the game for both players.

This approach has generally two problems:
<ol>
  <li>You have to know how to go through each situation. For connect four it is easy. Both players place their disks in turns and in every turn the current player has at most 7 possibilities. But it is impossible for games like <a href="http://en.wikipedia.org/wiki/Calvinball#Calvinball">Calvinball</a> or <a href="http://en.wikipedia.org/wiki/Mao_(card_game)">Mao</a>.</li>
  <li>The game tree might be HUGE. In this case, you can have $4,531,985,219,092 \approx 4.5 \cdot 10^{12}$ game situations (<a href="http://math.stackexchange.com/a/301128/6876">source</a>). Even if you would need only one bit for each situation, it would require 566.5 GB!</li>
</ol>

Anyway, lets say we want to store many unique game situations. Unique means, even if you have hundreds of possible paths to get to a given game situations, you will store this game situation only once.

<h2>Implementation</h2>
First of all, I would like to mention that you can <a href="#How_is_this_realated_to_hash_functions">skip the source code</a>. I've only included it to make it easier to understand what I'm talking about.

Lets say our game situation looks like this:

```c

struct gamesituation {
    /** How does the board currently look like? */
    char board[BOARD_WIDTH][BOARD_HEIGHT];

    /**
     * What are the next game situations that I can reach from this
     * board?
     * The next[i] means that the player dropped the disc at column i
     */
    int next[7];

    /* I could use a bitfield for this ... but it would make access
     * much more inconvenient.
     */
    unsigned char isEmpty;  // Is this gamesitatution already filled?
    unsigned char isFinished; // Is this game finished?
    unsigned char stalemate; // Was this game a stalemate?
    unsigned char winRed;   // Did red win?
    unsigned char winBlack; // Did black win?
};

```

You need a check if one player won:
```c

/*
 * Check if player has won by placing a disc on (x,y).
 * with direction (xDir, yDir)
 * @return 1 iff RED won, -1 iff BLACK won and 0 if nobody won
 */
signed char hasPlayerWon(char board[BOARD_WIDTH][BOARD_HEIGHT],
                  int x, int y, char xDir, char yDir) {
    char color = board[x][y];

    int tokensInRow = getTokensInRow(board, color, x, y, xDir, yDir)
              + getTokensInRow(board, color, x, y, -xDir, -yDir) - 1;

    if (tokensInRow >= WINNING_NR) {
        if (color == RED) {
            return 1;
        } else if (color == BLACK) {
            return -1;
        } else {
            perror("this color doesn't / shouldn't exist\n");
            exit(1);
        }
    }

    return 0;
}

/*
 * A new disc has been dropped. Check if this disc means that
 * somebody won.
 * @return 1 iff RED won, -1 iff BLACK won, otherwise NOT_FINISHED
 */
int isBoardFinished(char board[BOARD_WIDTH][BOARD_HEIGHT],
                    int x, int y) {
    signed char status;

    // check left-right
    status = hasPlayerWon(board, x, y, 1, 0);

    if (status != 0) {
        return status;
    }

    // top-down
    status = hasPlayerWon(board, x, y, 0, 1);

    if (status != 0) {
        return status;
    }

    // down-left to top-right
    status = hasPlayerWon(board, x, y, 1, 1);

    if (status != 0) {
        return status;
    }

    // top-left to down-right
    status = hasPlayerWon(board, x, y, -1, 1);

    if (status != 0) {
        return status;
    }

    return NOT_FINISHED;
}

```
If you need an explanation for this, you should read <a href="../check-x-in-a-row-for-board-games/" title="Check x-in-a-row for board games">this article</a>.

And you need a function that can mirror boards (to get rid of identical, but mirrored situations) and one that can compare boards:
```c

char isSameBoard(char a[BOARD_WIDTH][BOARD_HEIGHT],
                 char b[BOARD_WIDTH][BOARD_HEIGHT]) {
    for (int x = 0; x < BOARD_WIDTH; x++) {
        for (int y = 0; y < BOARD_HEIGHT; y++) {
            if (a[x][y] != b[x][y]) {
                return FALSE;
            }
        }
    }

    return TRUE;
}

void mirrorBoard(char board[BOARD_WIDTH][BOARD_HEIGHT],
                 char newBoard[BOARD_WIDTH][BOARD_HEIGHT]) {
    for (int x = 0; x < BOARD_WIDTH; x++) {
        for (int y = 0; y < BOARD_HEIGHT; y++) {
            newBoard[BOARD_WIDTH - x - 1][y] = board[x][y];
        }
    }
}

```

You need a function that makes all possible moves for the players:
```c


/*
 * Make all possible turns that the player can make in this
 * game situation.
 */
void makeTurns(char board[BOARD_WIDTH][BOARD_HEIGHT],
   char currentPlayer, unsigned int lastId, int recursion) {
    unsigned int insertID;
    int outcome;

    for (int column = 0; column < BOARD_WIDTH; column++) {
        // add to column
        int height = BOARD_HEIGHT - 1;

        // the disc falls down
        while (height >= 0 && board[column][height] == EMPTY) {
            height--;
        }
        height++;

        // this colum is full
        if (height == 6) {
            continue;
        }

        // place disc
        board[column][height] = currentPlayer;

        if (didBoardAlreadyOccur(board)) {
            // I've already got to this situation
            insertID = getBoardIndex(board);
            savePreviousID(insertID, lastId, column);
        } else {
            char mirrored[BOARD_WIDTH][BOARD_HEIGHT];
            mirrorBoard(board, mirrored);

            if (didBoardAlreadyOccur(mirrored)) {
                // I've already got this situation, but mirrored
                // so take care of symmetry at this point
                mirroredCounter++;
                insertID = getBoardIndex(mirrored);
                savePreviousID(insertID, lastId, column);
            } else {
                registeredSituations++;

                if (registeredSituations == MAXIMUM_SITUATIONS) {
                    giveCurrentInformation();
                    exit(MAXIMUM_SITUATIONS_REACHED_EXIT_STATUS);
                }

                if (REGISTERED_MOD > 0 &&
                    registeredSituations % REGISTERED_MOD == 0) {
                    giveCurrentInformation();
                }

                outcome = isBoardFinished(board, column, height);

                if (ABS(outcome) <= 1) {
                    // the game is finished
                    insertID = getNewIndex(board);
                    storeToDatabase(insertID, board, TRUE, outcome);
                    savePreviousID(insertID, lastId, column);
                } else {
                    // Switch players
                    if (currentPlayer == RED) {
                        currentPlayer = BLACK;
                    } else {
                        currentPlayer = RED;
                    }

                    insertID = getNewIndex(board);
                    setBoard(insertID, board);
                    savePreviousID(insertID, lastId, column);
                    char copy[BOARD_WIDTH][BOARD_HEIGHT];

                    for (int x = 0; x < BOARD_WIDTH; x++) {
                        for (int y = 0; y < BOARD_HEIGHT; y++) {
                            copy[x][y] = board[x][y];
                        }
                    }

                    makeTurns(copy, currentPlayer, insertID,
                              recursion + 1);
                }
            }
        }
    }
}

```

<h2>How is this realated to hash functions?</h2>
You might have noticed a few functions that I didn't explain by now:
<ul>
  <li><code>didBoardAlreadyOccur(board)</code>: Checks if a given board is stored in database.</li>
  <li><code>getBoardIndex(board)</code>: This is a function that takes a board and gives a non-negative integer which is characteristic for the given board.</li>
  <li><code>savePreviousID(insertID, lastId, column)</code>: store insertID as a possible next situation for lastId in database</li>
  <li><code>setBoard(insertID, board)</code>: Insert board into database at position insertID</li>
</ul>

How would you implement <code>didBoardAlreadyOccur(board)</code>? This function (or insertID) will be the slowest part of the code and will be called VERY often. So it needs to be as fast as possible.

<h2>A hash function</h2>
Most of the time you can create hash functions by mapping values to integers. In my case, I mapped the board - which is a two-dimensional char array - to one integer by thinking of it as a very long number. I think of a red disc as the digit 1, a black disc as the digit 2 and an empty field as 0:

```c

unsigned int charToInt(char x) {
    if (x == RED) {
        return 1;
    } else if (x == BLACK) {
        return 2;
    } else {
        return 0;
    }
}

```

When you want to get the board number, you can get it like this:
<figure class="aligncenter">
            <a href="../images/2013/05/connect-four-to-number.png"><img src="../images/2013/05/connect-four-to-number.png" alt="Empty=0, red=1, yellow=2" style="max-width:320px;max-height:380px" class="size-full wp-image-65761"/></a>
            <figcaption class="text-center">Empty=0, red=1, yellow=2<br />The board number is 00000000000000000210000211210112212</figcaption>
        </figure>

For most game situations, this number will be much too big to store it in an integer. Also, we would like to get an index for our array so that we know where to store this board. The simplest solution to this problem is to calculate <code>NUMBER % ARRAY_SIZE</code>:

```c
unsigned int getFirstIndex(char board[BOARD_WIDTH][BOARD_HEIGHT]) {
    unsigned int index = 0;

    for (int x = 0; x < BOARD_WIDTH; x++) {
        for (int y = 0; y < BOARD_HEIGHT; y++) {
            index += charToInt(board[x][y]) *
                     myPow(3, ((x + y * BOARD_WIDTH) % HASH_MODULO));
        }
    }

    index = index % MAXIMUM_SITUATIONS;
    return index;
}
```

The function <code>getFirstIndex</code> maps an char Array with BOARD_WIDTH * BOARD_HEIGHT = 7 * 6 = 42 elements to an integer interval [0, MAXIMUM_SITUATIONS] = [0, 20000000]. Although I only use three values for the char array, that is $3^{42} = 109418989131512359209 \approx 1.09 \cdot 10^{20}$. There are many game situation numbers that can never occur (e.g. two more red than black dists), but we still map a significantly larger space to [0,20000000]. You can't change that. You can probably find (much) better mappings, but as we know that there are $4.5 \cdot 10^{12}$ game situations, you will always have the problem that your codomain is much smaller than the domain of your hash function. That's a fundamental problem of hash functions.

This means, you will have two board situations that map to the same hash number. This is called a "hash collision". When you use the hash number directly as an index for your board, you will have to deal with hash collisions. Some solutions are:
<ul>
  <li>Ignoring the problem: That's boring and not always possible (but simple).</li>
  <li>Linear probing</li>
  <li>Quadratic probing</li>
</ul>

<h2>Linear probing</h2>
The idea of linear probing is very simple:

Inserting a new item:
<ol>
  <li>You look at the index $i$ that your hash function gave you.</li>
  <li>If this index is already full, you look at $i+1$</li>
  <li>When you took a look at all slots of your array, you can't insert the new item.</li>
</ol>

Searching for an already inserted item:
<ol>
  <li>You look at the index $i$ that your hash function gave you.</li>
  <li>If $i$ is empty, you're ready. The item was not inserted.</li>
  <li>If $i$ is not the item you've searched for, you have to look at $i+1$.</li>
  <li>Keep looking at the next item until you find your searched item, you've looked at all items or you find an empty slot.</li>
</ol>

Deleting is complicated. You have to look at all items after the deleted one, remove them from your array and insert them again. That's not good.

The problem of linear probing is <strong>clustering</strong>. When you have some hash values that are close together, you might get hash collisions faster. When you've got your first collisions, you resolve them by inserting the value close to the value where you originally wanted to save it. So you get one big cluster quite fast. When you want to insert an element in the cluster, you first have to search the end of the cluster. That's bad for performance.

An advantage of linear probing compared to quadratic probing is that you might get a better performance due to cache effects.

<h2>Quadratic probing</h2>
The idea of quadratic probing is the same as for linear probing, but you try to fix the clustering-problem by using a clever way to search for a free spot:

$h_i(x) = \left(h(x) + (-1)^{i+1} \cdot \left\lceil\frac{i}{2}\right\rceil^2\right) \bmod~m$

where $h$ is your hash function and $i$ is your i-th try to find a free spot while you have $m$ spots in total.

This one also suffers from clustering, but it's not as bad as with linear clustering.

<h2>Double hashing</h2>
This solution could be the best one, but also the hardest one to implement correctly. You could find a free spot by using a second hash function $h'$ like this:

$h_i(x) = (h(x)+h'(x)\cdot i) ~ \bmod ~ m$

BUT you have to make sure that $Pr[h(x)=h(y) \land h'(x)=h'(y)] = \frac{1}{m^2}$

<h2>Performance</h2>
You can use linear probing, quadratic probing and double hashing in my example and measure how many game situations get stored. The more game situations you can store in the same amount of time, the better:

<figure class="aligncenter">
            <a href="../images/2013/05/connectfour-probing.png"><img src="../images/2013/05/connectfour-probing.png" alt="Linear probing, quadratic probing and double hashing for connect four" style="max-width:512px;max-height:334px" class="size-full wp-image-65871"/></a>
            <figcaption class="text-center">Linear probing, quadratic probing and double hashing for connect four</figcaption>
        </figure>

You can see that linear probing performs much worse than quadratic probing and double hashing. When you compare quadratic probing with double hashing, there seems not to be a big difference. But note that my second hash function is almost the same as the first one. You could probably choose a better second hash function and get better results (suggestions are welcome).

<h2>Why are hash functions important?</h2>
Hash functions help you to map a big amount of data to a small space. They are important, because they are a relevant part of many datastructures. The better they are, the faster will operations on those datastructures work. Better means: Faster to compute or less collisions.

Some datastructures like this are:
<ul>
  <li><a href="http://docs.oracle.com/javase/7/docs/api/java/util/HashMap.html">HashMap</a> and <a href="http://docs.oracle.com/javase/7/docs/api/java/util/Hashtable.html">HashTable</a> (&rarr; <a href="http://stackoverflow.com/a/40878/562769">difference</a>)</li>
  <li><a href="http://docs.oracle.com/javase/7/docs/api/java/util/HashSet.html">HashSet</a></li>
</ul>

<h2>Final notes</h2>
Another resolution for hash collisions is creating a linked list. This means you will not suffer from clustering and you can insert in $\mathcal{O}(1)$. But searching for an element is still in $\mathcal{O}(n)$, where $n$ is the number of elements that were already inserted.

<h2>Resources</h2>
You can find the <a href="https://github.com/MartinThoma/connect-four/tree/master/C">code at GitHub</a>.

# Tennis Python Kata

[![Run on Replit](https://replit.com/badge/github/Coding-Cuddles/tennis-python-kata)](https://replit.com/new/github/Coding-Cuddles/tennis-python-kata)

## Overview

This kata complements [Clean Code: Fundamentals, Ep. 4 - Function Structure](https://cleancoders.com/episode/clean-code-episode-4).

Thre rules for scoring in tennis are as follows:

* If both players have the same number of points, the score is described as "Love-All",
  "Fifteen-All", "Thirty-All", or "Deuce" depending on the number of points scored.
* If one player has scored four or more points and has a two-point lead over the other player,
  the score is described as "Win for Player 1" or "Win for Player 2" depending on which
  player has won.
* If one player has scored four or more points and has a note-poins lead over the other
  player, the score is described as "Advantage Player 1" or "Advantage Player 2"
  depending on which plas has the advantage.
* If both players have scored less than four points, the score is described as "Love",
  "Fifteen", "Thirty", or "Forty" depending on the number of points scored by each player.

For more information on the rules of tennis, please see
the [official rules](https://www.itftennis.com/en/about-us/governance/rules-and-regulations/)
from International Tennis Federation.

## Instructions

To complete the kata, your code should include the following features:

* A function that keeps track of the score for each player: this function
  should be able to increment the score for a player when they win a point.
* A function that returns a string representation of the current score.

## Usage

You can import this project into [Replit](https://replit.com), and it will
handle all dependencies automatically.

### Prerequisites

* [Python 3.8+](https://www.python.org/)
* [pytest](https://pytest.org)

### Run main

```console
make run
```

### Run tests

```console
make test
```

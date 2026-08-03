# Tennis kata in Python

[![CI](https://github.com/Coding-Cuddles/tennis-python-kata/actions/workflows/main.yml/badge.svg)](https://github.com/Coding-Cuddles/tennis-python-kata/actions/workflows/main.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Implement tennis scoring with test-driven development. Setup is complete when the starter test suite
finishes without failures.

## Overview

This kata complements [Clean Code: Fundamentals, Ep. 4 - Function Structure](https://cleancoders.com/episode/clean-code-episode-4).

The rules of the tennis kata are as follows:

- The game is played by two players, called "Player 1" and "Player 2".
- The players start with a score of 0 points each.
- The players take turns hitting the ball over the net, with Player 1 serving
  first.
- The game continues until one of the players reaches a score of 4 points.
- If a player reaches a score of 4 points, they must have a lead of at least 2
  points over the other player in order to win the game. For example, if player
  1 has a score of 4 and player 2 has a score of 3, the game continues.
- If the scores are tied at 4 points each, the game enters the "Deuce" mode. In
  deuce mode, the players continue to play until one of them has a lead of 2
  points.

For more information on the rules of tennis, please see
the [official rules](https://www.itftennis.com/en/about-us/governance/rules-and-regulations/)
from International Tennis Federation.

## Instructions

To complete the kata, your code should include the following features:

- A function that keeps track of the score for each player: this function
  should be able to increment the score for a player when they win a point.
- A function that returns a string representation of the current score.

The rules for scoring representation are as follows:

- If both players have the same number of points, the score is described as
  "Love-All", "Fifteen-All", "Thirty-All", or "Deuce" depending on the number
  of points scored.
- If one player has scored four or more points and has a two-point lead over
  the other player, the score is described as "Win for Player 1" or "Win for
  Player 2" depending on which player has won.
- If one player has scored four or more points and has a one-point lead over
  the other player, the score is described as "Advantage Player 1" or
  "Advantage Player 2" depending on which player has the advantage.
- If both players have scored less than four points, the score is described as
  "Love", "Fifteen", "Thirty", or "Forty" depending on the number of points
  scored by each player.

## Prerequisites

Required:

- [Git](https://git-scm.com/downloads)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

Optional:

- [GNU Make](https://www.gnu.org/software/make/), for shorter commands. Every required task also
  has a direct `uv` command.

You do not need to install Python or pytest separately. `uv` installs a compatible Python version
and the locked project dependencies when needed.

## Set up the kata

1. Clone the repository:

   ```console
   git clone https://github.com/Coding-Cuddles/tennis-python-kata.git
   ```

2. Enter the repository directory:

   ```console
   cd tennis-python-kata
   ```

3. Run the starter test. Use Make when it is installed:

   ```console
   make test
   ```

   Otherwise, run pytest through `uv` directly:

   ```console
   uv run pytest
   ```

   The first run may install Python and the project dependencies. Setup is complete when pytest
   exits successfully; the unfinished starter implementation reports `1 xfailed`.

   If the command fails with `uv: command not found`, install
   [uv](https://docs.astral.sh/uv/getting-started/installation/) and repeat this step.

## Work on the kata

1. Implement the scoring behavior in `tennis.py`.

2. Run the tests after each change. Use Make when it is installed:

   ```console
   make test
   ```

   Otherwise, run pytest through `uv` directly:

   ```console
   uv run pytest
   ```

   Continue when the test run completes without failures.

## Make command reference

Make is optional. Run `make` or `make help` to list these commands in the terminal.

| Command             | Result                                  |
| ------------------- | --------------------------------------- |
| `make all`          | Run the test suite                      |
| `make help`         | Show the command reference              |
| `make test`         | Run the test suite                      |
| `make format`       | Format tracked Python files             |
| `make format-check` | Check formatting without changing files |
| `make clean`        | Remove generated caches                 |

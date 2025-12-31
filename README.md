# Rock Paper Scissors – Logic-Based Strategy  
**freeCodeCamp Machine Learning with Python Project**

---

## Overview

This project implements a **logic-based adaptive strategy** for the Rock Paper Scissors challenge from the **freeCodeCamp Machine Learning with Python curriculum**.

The objective of the challenge is to create a `player` function that can consistently defeat **four predefined bots** — Quincy, Abbey, Kris, and Mrugesh — by winning **at least 60% of the games against each bot**.

All logic is written inside `RPS.py`, strictly following the project rules. No changes were made to the game engine or test files.

---

## About My Solution

This solution does **not rely on randomness alone**.  
Instead, it **observes opponent behavior, detects patterns, and switches strategies dynamically**.

The bot maintains internal state across rounds and adapts once it identifies which opponent it is playing against.

### Bot-Specific Strategies

#### Quincy
- Follows a fixed repeating cycle: `R → R → P → P → S`
- The solution detects this cycle and predicts Quincy’s next move
- Plays the direct counter to that prediction

#### Abbey
- Predicts the opponent’s next move based on their **previous two moves**
- The solution tracks two-move transition frequencies
- Predicts Abbey’s expected move and counters it

#### Kris
- Always plays the move that beats the opponent’s **last move**
- The solution anticipates this behavior and plays the counter to Kris’s counter

#### Mrugesh
- Looks at the **last 10 moves** of the opponent
- Finds the most frequent move
- Plays the move that beats it
- The solution tracks frequency windows and plays a second-level counter

---

## How the Bot Works Internally

- Maintains:
  - Opponent move history
  - Own move history
  - Frequency counters
  - Transition tables
- Detects the opponent **once per match**
- Locks into the appropriate counter-strategy
- Avoids hard resets and works correctly with freeCodeCamp’s test harness

Although this project is part of an ML certification, the final solution demonstrates why this problem is **closer to reinforcement learning than simple hardcoding**, even though no formal RL libraries are used.

---

## Key Concepts Used

- Pattern detection
- Sliding window frequency analysis
- Markov-style transition tracking
- Strategy switching
- Counter-strategy reasoning (predict → counter → counter-the-counter)
- Stateful logic inside a function

---

## How to Run

All logic is implemented in **`RPS.py`**.

## To test locally using the provided tools:

python main.py

## To play against a specific bot:

play(player, quincy, 1000)
play(player, abbey, 1000)
play(player, kris, 1000)
play(player, mrugesh, 1000)


## To run the official tests, uncomment the test line in main.py.

## Results

Meets freeCodeCamp’s requirement of 60%+ win rate against all four bots

Achieves very high accuracy against deterministic opponents

Adapts correctly when bots are tested sequentially

## Notes & Learnings

Hardcoded logic alone becomes fragile when multiple strategies interact

Detection logic must be robust and pattern-based, not round-count based

This project highlighted the limits of static logic and why adaptive learning approaches (like Q-learning) are better suited for such problems

The solution evolved through multiple failed attempts, refinements, and debugging sessions

## Academic Honesty

This project is my own work.

I explored ideas shared by other freeCodeCamp learners to understand general detection strategies, but all logic was rewritten, adapted, and implemented independently.

By submitting this project, I affirm that the final implementation reflects my own understanding and effort.

## Reference

One repository that helped me understand opponent detection strategies conceptually:

https://github.com/Captainspockears/freecodecampMLprojects/blob/master/RockPaperScissor/RPS.py

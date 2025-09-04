# Rock Paper Scissors Logic-Based Strategy FreeCodeCamp Project

Overview

This project implements a logic-based strategy for the Rock Paper Scissors challenge from the FreeCodeCamp curriculum. The goal is to consistently defeat four predefined bots named Quincy, Abbey, Kris, and Mrugesh by analyzing their patterns and applying counter strategies.

About My Solution

The solution tracks the opponent’s moves and applies strategies tailored to each bot.

Quincy follows a fixed five-move cycle. The solution predicts her next move and plays the winning response.

Abbey uses a simple two-move Markov chain. The solution predicts her next move based on the frequency of recent plays.

Kris always counters the previous move. The solution anticipates this and counters accordingly.

Mrugesh predicts the most frequent move from the last ten rounds. The solution counters his prediction to maximize wins.

All code, logic, and improvements were written and implemented by me. I referred to several FreeCodeCamp users’ ideas for inspiration, and one solution in particular helped me understand detection strategies. I adapted the concepts and fully implemented them in my own way.

Academic Honesty

This project is my own work. Any inspiration from other FreeCodeCamp users is fully adapted and improved upon. By submitting this project, I pledge that I did not plagiarize and that all work reflects my own understanding and implementation.

Reference

The detection idea that influenced my project can be seen here: https://github.com/Captainspockears/freecodecampMLprojects/blob/master/RockPaperScissor/RPS.py

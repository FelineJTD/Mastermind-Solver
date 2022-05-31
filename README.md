# Mastermind Solver

## Overview
This repository contains two different mastermind solvers, one implementing the brute force algorithm and the other implementing the decrease and conquer algorithm. The two produces different results (brute force is faster but requires more moves, decrease and conquer is slower but a win is guaranteed in 8 moves) and can be run separately.

## Mastermind
Mastermind is a codebreaking board game featuring codes made of six different colours. To win, the codebreaker needs to guess the exact code that has been determined by the codemaker with the help of black and white pegs indicating correct and close guesses. Try playing the game at [gamesforthebrain.com](https://www.gamesforthebrain.com/game/guesscolors/) or [archimedes-lab.org](https://www.archimedes-lab.org/mastermind.html) (these websites are not mine).

## Mastermind in This Repository
This is how Mastermind is implemented here:
- The six different colours of code pegs are represented by“1”, “2”, “3”, “4”, “5”, and “6”. 
- The solution code has a length of four and is randomly generated. 
- Blanks are not allowed, but repetitions of colour are allowed. 
- For each round, the game will give feedback on the number of “black pegs” for exact matches (pegs that are correct in both colour and position) and the number of “white pegs” for close matches (pegs that are correct in colour but is wrongly positioned).

## Why You Should Check This Out
The algorithms described in this repository can be implemented in a real life Mastermind game by a human player. This also serves as a proof that yes, Mastermind can be won. It may also be used as a reference to create similar algorithms.

## Requirements
- Python 3
- Library:
  - itertools (to install, run `pip install itertools`)

## How to Run the Codes
1. Clone this repository to your machine and change directory to the resulting directory.
2. Change directory to `./src/brute_force` or `./src/decrease_and_conquer`.
3. There are two Python files which you can run in each folder:
    - `main.py`  
      A random solution code will be generated. The algorithm will make guesses to try and solve/uncover the previously generated solution code.  
      To run:
      ```
      python3 main.py
      ```
    - `analytics.py`  
      The algorithm will attempt to solve all 1,296 solution code possibilities (1111, 1112, 1113, ..., 6666) in a Mastermind game and return the execution time, the average number of guesses, and the maximum (worst-case scenario) number of guesses.  
      To run:
      ```
      python3 analytics.py
      ```

## Comparison Between the Two Algorithms
|                   | Brute Force | Decrease and Conquer |
| ----------------- | ----------- | -------------------- |
| Total time (s)    |	0.2082      |	18.6651              |
| Average guesses   | 12.8025     |	4.6597               |
| Worst case        |	30          |	8                    |

_*These statistics may differ in each run, especially the decrease and conquer stats since it involves random guesses_

## More Explanations
To understand the algorithms behind these programs, go read the paper in the `doc` directory ([A Comparative Study of Brute Force and   Decrease and Conquer Algorithm for Mastermind Puzzle Codebreaking](./doc/13520050_Felicia%20Sutandijo.pdf)) or watch the [Youtube video](https://youtu.be/vhfvBfylKWM).

## Status
This project is _completed_.

## Disclaimer
The codes are messy and not yet modular, but hey it works. A cleaner version may be updated if I have time.

## Author
Felicia Sutandijo (Github: [FelineJTD](https://github.com/FelineJTD))
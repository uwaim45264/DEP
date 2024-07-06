# Red-Blue Nim Game

## Introduction

The Red-Blue Nim Game is a two-player strategy game where players take turns removing marbles from two piles. The game has two versions: Standard and Misère. This implementation provides an interactive GUI using CustomTkinter.

## Game Rules

### 1. Standard Version
Players lose if either pile is empty on their turn.

### 2. Misère Version
Players win if either pile is empty on their turn.

### 3. Scoring
- Each red marble left: 2 points.
- Each blue marble left: 3 points.

## Command Line Usage

The game can be launched using the following command:

```sh
python game.py <num-red> <num-blue> <version> <first-player> <depth>

Parameters
<num-red>: Number of red marbles.
<num-blue>: Number of blue marbles.
<version>: 'standard' (default) or 'misere'.
<first-player>: 'computer' (default) or 'human'.
<depth>: Search depth for AI (optional).
Game Flow
1. Turn Order
The game alternates between the human and computer player until the game ends.

2. Human Move
The program prompts the human player for their move and validates the input.

3. Computer Move
The program determines the computer's move using the MinMax algorithm with Alpha Beta Pruning.

MinMax Algorithm
1. Overview
The MinMax algorithm is used to optimize decision-making in the game.

2. Alpha Beta Pruning
Alpha Beta Pruning improves the efficiency of the MinMax algorithm by eliminating branches that do not need to be explored.

3. Move Ordering (Standard)
Pick 2 red marbles.
Pick 2 blue marbles.
Pick 1 red marble.
Pick 1 blue marble.
4. Move Ordering (Misère)
Pick 1 blue marble.
Pick 1 red marble.
Pick 2 blue marbles.
Pick 2 red marbles.
Depth Limited Search (Extra Credit)
1. Purpose
Depth-limited search allows faster decision-making by limiting the search depth.

2. Evaluation Function
The heuristic evaluation function evaluates non-terminal game states.

End of Game
1. Game Over Conditions
The game ends when either pile is empty.

2. Scoring Calculation
The final score is calculated based on the remaining marbles.

Implementation Details
Modules
command-line parsing
game mechanics
human and computer moves
AI decision-making with MinMax and Alpha Beta Pruning
Demonstration
Walkthrough
A sample game walkthrough showcasing both human and computer interactions


Developer
Developed by: Muhammad Uwaim Qureshi

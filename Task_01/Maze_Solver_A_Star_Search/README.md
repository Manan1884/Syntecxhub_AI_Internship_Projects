# Maze Solver using A* Search Algorithm

## Project Description

This project implements a Maze Solver using the A* Search algorithm.

The maze is represented as a grid containing:

- Start node (S)
- Goal node (G)
- Walls (#)
- Empty paths (.)

Each grid cell is modeled as a node and searched using A*.

## Algorithm Used

### A* Search Algorithm

A* combines:

- Actual distance from start (g-cost)
- Estimated distance to goal (h-cost)

The total cost is:

f(n) = g(n) + h(n)

## Heuristic

Manhattan Distance is used:

h(n) = |x1-x2| + |y1-y2|

## Features

- Grid based maze representation
- Node based modeling
- A* shortest path search
- Manhattan heuristic
- Path reconstruction
- Unreachable path detection
- Console visualization

## Project Structure

Maze_Solver_A_Star_Search
│
├── main.py
├── README.md
└── requirements.txt

## How to Run

Clone repository: `git clone <repository-url>`
Run: python main.py

## Sample Output

```text
S . . # .

# . # .

. . . . .
. # # # .
. . . G .

Solved Maze:

S * * # .

# * # .

. . * * *
. # # # *
. . . G *

Path Length: 9
```

## Technologies Used

- Python
- A* Search Algorithm
- Heap Priority Queue

## Author

Manan

# 8-Puzzle Solver Using Search Methods

## Introduction

This project implements a solution for the 8-puzzle problem, where the goal is to arrange tiles on a 3x3 grid in ascending order (0-8), with 0 representing the blank space. Starting from an initial configuration, the task is to find the minimal sequence of moves to achieve the target state. The solution uses four search algorithms:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Iterative Deepening Search (IDS)
- A* Search

The project also includes a **GUI built with custom Tkinter** for visualization and easy interaction.

---

## Features

- **Algorithms Implemented**:
  - **BFS**: Explores all nodes level by level, ensuring the shortest path.
  - **DFS**: Explores as deep as possible before backtracking.
  - **IDS**: Combines DFS with a depth limit, increasing the limit iteratively.
  - **A***: Uses heuristics (Manhattan or Euclidean distance) for optimal and efficient pathfinding.

- **GUI**:
  - Input puzzle configurations interactively.
  - Visualize the solution path step by step.
  - Explore large solutions in manageable batches (30 states at a time).

---

## Assumptions

1. Each puzzle can be solved using any method, but to solve a new puzzle, the program must be restarted.
2. DFS results are displayed in chunks for large solutions.

---


## Algorithms Overview

### Breadth-First Search (BFS)
- **Properties**: Complete, Optimal.
- **Complexity**: Time and Space - O(b^d), where `b` is branching factor and `d` is solution depth.

### Depth-First Search (DFS)
- **Properties**: Complete, Not Optimal.
- **Complexity**: Time - O(b^m), Space - O(bm), where `m` is max depth.

### Iterative Deepening Search (IDS)
- **Properties**: Complete, Optimal.
- **Complexity**: Time and Space - O(b^d).

### A* Search
- **Properties**: Complete, Optimal (with admissible heuristic).
- **Heuristics**: Manhattan and Euclidean distances.
- **Complexity**: Time and Space - O(b^d).

---

### some Samples
![image](https://github.com/user-attachments/assets/2b6cbf38-f0cc-45eb-bba8-351e9edf217a)
![image](https://github.com/user-attachments/assets/4e5e3e4c-872f-4b64-8349-44a7c1c3e7e1)
![image](https://github.com/user-attachments/assets/1fa944f5-216a-4d82-aa14-8234ec47e372)
![image](https://github.com/user-attachments/assets/57ba388d-56ff-4fde-a346-eaa249c7c186)
![image](https://github.com/user-attachments/assets/0cda65d5-98b6-4877-99bc-5df676a6330a)

---

## How to Run

1. Clone the repository.
2. Install Python dependencies:
 ```bash
 pip install -r requirements.txt

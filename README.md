# Maze Solver

This is a GUI-based maze solver implemented using Python and Tkinter. The program can solve mazes using either the Breadth-First Search (BFS) or Depth-First Search (DFS) algorithms. You can choose which algorithm to use when running the program.

## Features

- **BFS Solver**: Finds the shortest path in the maze using the Breadth-First Search algorithm.
- **DFS Solver**: Finds a path in the maze using the Depth-First Search algorithm.
- **Graphical Interface**: Visualizes the maze and the pathfinding process using Tkinter.

## Requirements

- Python 3.x
- Tkinter (usually included with Python installations)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/AbsoluteZero000/maze-solver.git
   cd maze-solver
    ```
Make sure you have Python installed. You can check your Python version with:

```python3 --version```
Tkinter is usually included with Python. If it's not installed, you can install it using your package manager.

Usage
You can run the maze solver from the command line with the following options:

```bash
python3 src/main.py [-b] [-d] [-h]
-b: Run the BFS solver.
-d: Run the DFS solver.
-b -d: Run both the BFS and DFS solvers.
-h: Print the help message.
Examples
To run the BFS solver:
```
```bash
python3 src/main.py -b
```
or
```bash
./run.sh -b
```
To run the DFS solver:

```bash
python3 src/main.py -d
```
or
```bash
./run.sh -d
```
To run both the BFS and DFS solvers:
```bash
python3 src/main.py -b -d
```
or

```bash
./run.sh -b -d
```

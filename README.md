# Conway's Game of Life in Python

A very simple celluar automata written in `Python`, using `NumPy` and `Pygame`. The rules are that of [Conway's Game of Life](https://www.wikiwand.com/en/Conway%27s_Game_of_Life), where:
- Any live cell with fewer than two live neighbours dies
- Any live cell with two or three live neighbours lives on to the next
- Any live cell with more than three live neighbours dies
- Any dead cell with exactly three live neighbours becomes a live cell

<p align="center">
    <img src="https://github.com/Orbital-Web/GameOfLife/blob/c2b42106b3a4d0168fea0e7a31e3e78b693e78d1/demo.png" alt="demo of program" width=400/>
</p>

## Getting Started
1. Install the necessary modules, either to your system or to a virtualenv, using `py -m pip install -r requirements.txt`
2. Run `py main.py`

## Command Line Arguments
- `-s <int>` specify the simulation size, i.e., the number of cells in a row
- `-w <int>` specify the window size
- `-i <filename>` specify the starting state, defined by a txt file with `-` for empty (dead) cells and `*` for live cells
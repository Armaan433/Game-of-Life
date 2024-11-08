This project is an implementation of Conway's Game of Life, a cellular automaton created by British mathematician John Conway in 1970. It simulates the life and death of cells in a grid based on simple, predefined rules. The Game of Life is famous for showing how complex patterns can emerge from simple initial conditions.

The game operates on a grid of cells that can either be alive or dead, and it evolves over time based on the following four rules:

Any live cell with fewer than two live neighbors dies (underpopulation).


Any live cell with two or three live neighbors lives on to the next generation (survival).


Any live cell with more than three live neighbors dies (overpopulation).


Any dead cell with exactly three live neighbors becomes a live cell (reproduction).


The file main.py controls most of the code, but desighn.in is a set of cordinates that say where to create live cells, forking and then changing those create a different pattern.

# Game-of-Life-with-Pygame
This is Python implementation of John Conway's Game of Life.
# Conway's Game of Life
The Game of Life is a cellular automaton created by John Horton Conway in 1970. The game is a zero player game, meaning that its evolution is determined by its initial state. There are four rules of this game:
1. **Underpopulation**: Any live cell with has less than two neighbours dies and does not make it to the next generation.
2. **Equilibrium**: Any live cell with two or three live neighbours the cells stay alive and makes it to the next generation.
3. **Overpopulation**: Any live cell with more than three neighbours dies and does not make it to the next generation.
4. **Reproduction**: And dead cell with exactly three neighbours becomes a live cell.

## How to Run
This project uses Python 3.9.9 and only requires two libraries: **`NumPy`** and **`pygame`**. You can run this project by writing **`python gameoflife.py`** in the terminal in the directory.

### Available Keys:
- **`Space`** key will start or stop the run.
- **`Down`** key will slow the animation speed.
- **`Up`** key will speed up the animation.
- **`R`** key will reset the board while in pause.
- **`F`** key will fill whole make all the cells alive.
- **`T`** key will generate random blocks of live cells on the screen.
- **`Escape`** will terminate the window.
- You can use your mouse to select or unselect points. If you click with the **`Left`** or **`Middle`** mouse button, it will make the cell alive, and if you click with the **`Right`** mouse button it will make the cell die.

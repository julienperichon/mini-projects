from time import sleep

import numpy as np
import curses

from simulation import Simulation

N = 50
board = np.random.randint(0, 2, (N, 3 * N))
sim = Simulation(board)

console = curses.initscr()
console.nodelay(True)
i = 0


while True:
    console.clear()

    sim.step()

    console.addstr(f"{i}\n")

    str_row = "\n".join(
        [
            "".join(["#" if x == 1 else " " for x in row])
            for row in sim.get_board().tolist()
        ]
    )
    console.addstr(str_row)

    console.refresh()

    if console.getch() == ord("q"):
        break

    i += 1

    # sleep(0.05)

curses.endwin()

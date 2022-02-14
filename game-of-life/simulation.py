import numpy as np
from scipy.signal import convolve2d

NEIGHBORS_FILTER = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])


class Simulation:
    def __init__(self, init_board: np.array):
        self._board = init_board

    def step(self):
        conv_board = convolve2d(
            self._board, NEIGHBORS_FILTER, mode="same", boundary="wrap"
        )
        self._board = (conv_board == 3) + (conv_board == 2) * self._board

    def get_board(self):
        return self._board

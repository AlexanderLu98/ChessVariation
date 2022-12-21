from abc import ABC
import tkinter as tk

class piece(ABC):
    def __init__(self) -> None:
        self.isWhite=True

    def get_moves(self):
        pass

    def load_picture(self):
        pass


class king(piece):
    def load_picture(self):
        pass

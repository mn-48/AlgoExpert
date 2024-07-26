#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu
from DESIGNui import pYgubueXAMPLEUI


class pYgubueXAMPLE(pYgubueXAMPLEUI):
    def __init__(self, master=None):
        super().__init__(master)


if __name__ == "__main__":
    app = pYgubueXAMPLE()
    app.run()

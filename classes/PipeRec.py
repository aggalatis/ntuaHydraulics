import sys
from classes.Helpers import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class PipeRec:
    def __init__(self, pipe_width):
        print("I am creating rectangle pipe with width:", str(pipe_width))

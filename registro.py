import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QFileDialog


class Registrow():
    def __init__(self):
        self.v = uic.loadUi("registrotarea.ui")
        self.v.show()
  
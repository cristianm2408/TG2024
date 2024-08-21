import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QFileDialog


class Guiau():
    def __init__(self):
        self.guiau = uic.loadUi("guiau.ui")
        self.selfguiau.show()
  
from PyQt6.QtWidgets import QApplication

from gui.inicio import Login

class Redes():
    def __init__(self):
         self.app = QApplication([])
         self.login = Login()
         self.app.exec()
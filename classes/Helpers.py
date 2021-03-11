from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Helpers:

    @staticmethod
    def get_bold_font():
        bold_font = QFont()
        bold_font.setBold(True)
        return bold_font

    @staticmethod
    def validation_error(message):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Warning)
        message_box.setWindowTitle("Λάθος δεδομένα!")
        message_box.setText(message)
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec()

    @staticmethod
    def parse_float_from_string(s):
        try:
            return float(s.replace(',', '.'))
        except ValueError:
            return None

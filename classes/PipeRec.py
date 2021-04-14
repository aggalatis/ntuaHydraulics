import sys
from classes.Helpers import *
from PyQt5.QtWidgets import *


class PipeRec:
    def __init__(self, pipe_calculation_type, pipe_width, pipe_supply, pipe_depth, pipe_manning, pipe_slope):
        self.pipe_width = pipe_width
        self.pipe_depth = pipe_depth
        self.pipe_supply = pipe_supply
        self.pipe_manning = pipe_manning
        self.pipe_slope = pipe_slope
        self.pipe_calculation_type = pipe_calculation_type

    def save_to_file(self):
        file_name = QFileDialog.getSaveFileName(None, "Επιλογή σημείου αποθήκευσης", "", "Hyd Files (*.hyd)")
        try:
            file_str = "pipe_calculation_type: " + self.pipe_calculation_type + "\n"
            file_str += "pipe_type: " + "Ορθογωνική" + "\n"
            file_str += "pipe_width: " + str(self.pipe_width) + "\n"
            file_str += "pipe_depth: " + str(self.pipe_depth) + "\n"
            file_str += "pipe_supply: " + str(self.pipe_supply) + "\n"
            file_str += "pipe_manning: " + str(self.pipe_manning) + "\n"
            file_str += "pipe_slope: " + str(self.pipe_slope)
            f = open(str(file_name[0]), "w+")
            f.write(file_str)
            f.close()
            Helpers.success_message("Επιτυχής αποθήκευση αρχείου.")
        except:
            e = sys.exc_info()
            print(str(e))

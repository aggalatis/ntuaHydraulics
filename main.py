import sys
from classes.Helpers import *
from classes.PipeRec import PipeRec
from classes.PipeTrap import PipeTrap
from classes.PipeCir import PipeCir
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        print("Υπολογισμός παροχής και βάθους ροής ανοικτού αγωγού με GUI.")

        self.calculation_options = "Παροχή", "Βάθος ροής"
        self.pipe_schema_option = "Ορθογωνική", "Κυκλική", "Τραπεζοειδής"
        self.pipe_schema = None
        self.calculation_type = None
        self.calculation_label = None
        self.pipe_label = None
        self.supply = None
        self.supply_label = None
        self.depth = None
        self.depth_label = None
        self.width = None
        self.width_label = None
        self.diameter = None
        self.diameter_label = None
        self.diameter_label = None
        self.diameter_label = None
        self.angle_left = None
        self.angle_right = None
        self.angle_left_label = None
        self.angle_right_label = None
        self.manning = None
        self.manning_label = None
        self.slope = None
        self.slope_label = None
        self.onlyDouble = QDoubleValidator()
        self.setWindowTitle("NTUA - Hydraulics")
        self.setWindowIcon(QIcon("images/main-icon.png"))
        self.create_app()

    def create_app(self):
        """Create the whole grid layout"""
        grid = QGridLayout()
        grid.setSpacing(20)
        self.calculation_label = QLabel("Επιλέξτε τρόπο υπολογισμού:")
        self.calculation_label.setFont(Helpers.get_bold_font())
        self.calculation_type = QComboBox()
        self.calculation_type.addItems(self.calculation_options)
        self.calculation_type.currentIndexChanged.connect(self.show_potential_widgets)
        grid.addWidget(self.calculation_label, 0, 0, 1, 1)
        grid.addWidget(self.calculation_type, 0, 1, 1, 1)

        self.pipe_label = QLabel("Επιλέξτε σχήμα διατομής:")
        self.pipe_label.setFont(Helpers.get_bold_font())
        self.pipe_schema = QComboBox()
        self.pipe_schema.addItems(self.pipe_schema_option)
        self.pipe_schema.currentIndexChanged.connect(self.show_potential_widgets)
        grid.addWidget(self.pipe_label, 1, 0, 1, 1)
        grid.addWidget(self.pipe_schema, 1, 1, 1, 1)

        read_button = QPushButton("Εισαγωγή δεδομένων από αρχείο")
        save_button = QPushButton("Αποθήκευση δεδομένων σε αρχείο")
        execute_button = QPushButton("Εκτέλεση υπολογισμών")
        grid.addWidget(save_button, 4, 0, 1, 2)
        grid.addWidget(read_button, 4, 2, 1, 2)
        grid.addWidget(execute_button, 6, 0, 1, 4)

        self.supply = QLineEdit()
        self.supply.setValidator(self.onlyDouble)
        self.supply_label = QLabel("Παροχή (m3/s):")
        self.supply_label.setFont(Helpers.get_bold_font())
        grid.addWidget(self.supply_label, 0, 2, 1, 1)
        grid.addWidget(self.supply, 0, 3, 1, 1)

        self.depth = QLineEdit()
        self.depth.setValidator(self.onlyDouble)
        self.depth_label = QLabel("Βάθος ροής (m):")
        self.depth_label.setFont(Helpers.get_bold_font())
        grid.addWidget(self.depth_label, 0, 2, 1, 1)
        grid.addWidget(self.depth, 0, 3, 1, 1)

        self.width = QLineEdit()
        self.width.setValidator(self.onlyDouble)
        self.width_label = QLabel("Πλάτος διατομής (m):")
        self.width_label.setFont(Helpers.get_bold_font())
        grid.addWidget(self.width, 1, 3, 1, 1)
        grid.addWidget(self.width_label, 1, 2, 1, 1)

        self.diameter = QLineEdit()
        self.diameter.setValidator(self.onlyDouble)
        self.diameter_label = QLabel("Διάμετρος διατομής (m):")
        self.diameter_label.setFont(Helpers.get_bold_font())
        grid.addWidget(self.diameter, 1, 3, 1, 1)
        grid.addWidget(self.diameter_label, 1, 2, 1, 1)

        self.angle_left = QLineEdit()
        self.angle_left.setValidator(self.onlyDouble)
        self.angle_left_label = QLabel("Γωνία αριστερά (°):")
        self.angle_left_label.setFont(Helpers.get_bold_font())
        grid.addWidget(self.angle_left, 2, 3, 1, 1)
        grid.addWidget(self.angle_left_label, 2, 2, 1, 1)

        self.angle_right = QLineEdit()
        self.angle_right.setValidator(self.onlyDouble)
        self.angle_right_label = QLabel("Γωνία δεξιά (°):")
        self.angle_right_label.setFont(Helpers.get_bold_font())
        grid.addWidget(self.angle_right, 3, 3, 1, 1)
        grid.addWidget(self.angle_right_label, 3, 2, 1, 1)

        self.manning = QLineEdit()
        self.manning.setValidator(self.onlyDouble)
        self.manning_label = QLabel("Συντελεστής Manning:")
        self.manning_label.setFont(Helpers.get_bold_font())
        grid.addWidget(self.manning, 2, 1, 1, 1)
        grid.addWidget(self.manning_label, 2, 0, 1, 1)

        self.slope = QLineEdit()
        self.slope.setValidator(self.onlyDouble)
        self.slope_label = QLabel("Κλίση αγωγού (°):")
        self.slope_label.setFont(Helpers.get_bold_font())
        grid.addWidget(self.slope, 3, 1, 1, 1)
        grid.addWidget(self.slope_label, 3, 0, 1, 1)
        save_button.clicked.connect(self.save_data_to_file)
        read_button.clicked.connect(self.read_data_from_file)
        # execute_button.clicked.connect(self.create_pipeline)

        self.hide_widget(self.depth, self.depth_label)
        self.hide_widget(self.angle_left, self.angle_left_label)
        self.hide_widget(self.angle_right, self.angle_right_label)
        self.hide_widget(self.diameter, self.diameter_label)
        self.setLayout(grid)
        self.show()

    def hide_widget(self, widget, widget_label):
        widget.hide()
        widget_label.hide()

    def show_potential_widgets(self):
        if self.calculation_type.currentText() == "Παροχή":
            self.supply.show()
            self.supply_label.show()
            self.depth.hide()
            self.depth_label.hide()
        else:
            self.supply.hide()
            self.supply_label.hide()
            self.depth.show()
            self.depth_label.show()

        if self.pipe_schema.currentText() == "Ορθογωνική":
            self.angle_right.hide()
            self.angle_right_label.hide()
            self.angle_left.hide()
            self.angle_left_label.hide()
            self.diameter.hide()
            self.diameter_label.hide()
            self.width_label.show()
            self.width.show()
        elif self.pipe_schema.currentText() == "Τραπεζοειδής":
            self.angle_right.show()
            self.angle_right_label.show()
            self.angle_left.show()
            self.angle_left_label.show()
            self.diameter.hide()
            self.diameter_label.hide()
            self.width_label.show()
            self.width.show()
        else:
            self.angle_right.hide()
            self.angle_right_label.hide()
            self.angle_left.hide()
            self.angle_left_label.hide()
            self.diameter.show()
            self.diameter_label.show()
            self.width_label.hide()
            self.width.hide()

    def validate_and_proceed(self):
        type_validation = False
        if self.calculation_type.currentText() == "Παροχή":
            supply_num = Helpers.parse_float_from_string(self.supply.text())
            type_validation = True if supply_num is not None and supply_num > 0 else Helpers.validation_error(
                "Μη αποδεκτή τιμή παροχής.")
        else:
            depth_num = Helpers.parse_float_from_string(self.depth.text())

            type_validation = True if depth_num is not None and depth_num > 0 else Helpers.validation_error(
                "Μη αποδεκτή τιμή βάθους ροής.")

        return self.validate_geometry() if type_validation else False

    def validate_geometry(self):
        geometry_validation = False
        if self.pipe_schema.currentText() == "Ορθογωνική":
            width_num = Helpers.parse_float_from_string(self.width.text())
            geometry_validation = True if width_num is not None and width_num > 0 else Helpers.validation_error(
                "Μη αποδεκτή τιμή πλάτους ορθογωνικού αγωγού.")
        elif self.pipe_schema.currentText() == "Κυκλική":
            diameter_num = Helpers.parse_float_from_string(self.diameter.text())
            geometry_validation = True if diameter_num is not None and diameter_num > 0 else Helpers.validation_error(
                "Μη αποδεκτή τιμή διαμέτρου κυκλικού αγωγού.")
        else:
            width_num = Helpers.parse_float_from_string(self.width.text())
            angle_right_num = Helpers.parse_float_from_string(self.angle_right.text())
            angle_left_num = Helpers.parse_float_from_string(self.angle_left.text())
            if width_num is not None and angle_right_num is not None and angle_left_num is not None:
                if width_num > 0 and 0 < angle_left_num < 180 and angle_right_num > 0 and angle_right_num < 180:
                    geometry_validation = True
                else:
                    Helpers.validation_error("Μη αποδεκτή τιμή στη γεωμετρία τραπεζίου.")
            else:
                Helpers.validation_error("Μη αποδεκτή τιμή στη γεωμετρία τραπεζίου.")
        return self.static_fields_validation() if geometry_validation else False

    def static_fields_validation(self):
        manning_num = Helpers.parse_float_from_string(self.manning.text())
        if manning_num is not None and manning_num > 0:
            slope_num = Helpers.parse_float_from_string(self.slope.text())
            if slope_num is not None and slope_num >= 0:
                return True
            else:
                Helpers.validation_error("Μη αποδεκτή τιμή κλίσης αγωγού.")
        else:
            Helpers.validation_error("Μη αποδεκτή τιμή συντελεστή Manning.")
        return False

    def save_data_to_file(self):
        if self.validate_and_proceed():
            pipe_manning = Helpers.parse_float_from_string(self.manning.text())
            pipe_slope = Helpers.parse_float_from_string(self.slope.text())
            pipe_supply = Helpers.parse_float_from_string(self.supply.text())
            pipe_depth = Helpers.parse_float_from_string(self.depth.text())
            pipe_calculation_type = self.calculation_type.currentText()
            if self.pipe_schema.currentText() == "Ορθογωνική":
                pipe_width = Helpers.parse_float_from_string(self.width.text())
                rec_pipe = PipeRec(pipe_calculation_type, pipe_width, pipe_supply, pipe_depth, pipe_manning, pipe_slope)
                rec_pipe.save_to_file()
            elif self.pipe_schema.currentText() == "Τραπεζοειδής":
                pipe_width = Helpers.parse_float_from_string(self.width.text())
                pipe_angle_right = Helpers.parse_float_from_string(self.angle_right.text())
                pipe_angle_left = Helpers.parse_float_from_string(self.angle_left.text())
                trap_pipe = PipeTrap(pipe_calculation_type, pipe_width, pipe_supply, pipe_depth, pipe_manning, pipe_slope, pipe_angle_left, pipe_angle_right)
                trap_pipe.save_to_file()
            else:
                pipe_diameter = Helpers.parse_float_from_string(self.diameter.text())
                circle_pipe = PipeCir(pipe_calculation_type, pipe_diameter, pipe_supply, pipe_depth, pipe_manning, pipe_slope)
                circle_pipe.save_to_file()

    def read_data_from_file(self):
        file_read = QFileDialog.getOpenFileName(None, "Επιλογή αρχείου δεδομένων.", "", "Data Files (*.dat)")
        data_file = open(str(file_read[0]), "r")

        try:
            for line in data_file:
                line_attr = line.replace("\n", "").split(": ")
                if line_attr[0] == "pipe_calculation_type":
                    self.calculation_type.setCurrentText(line_attr[1])
                elif line_attr[0] == "pipe_type":
                    self.pipe_schema.setCurrentText(line_attr[1])
                elif line_attr[0] == "pipe_width":
                    self.width.setText(line_attr[1])
                elif line_attr[0] == "pipe_diameter":
                    self.diameter.setText(line_attr[1])
                elif line_attr[0] == "pipe_depth":
                    self.depth.setText(line_attr[1])
                elif line_attr[0] == "pipe_supply":
                    self.supply.setText(line_attr[1])
                elif line_attr[0] == "pipe_manning":
                    self.manning.setText(line_attr[1])
                elif line_attr[0] == "pipe_slope":
                    self.slope.setText(line_attr[1])
                elif line_attr[0] == "pipe_angle_left":
                    self.angle_left.setText(line_attr[1])
                else:
                    self.angle_right.setText(line_attr[1])
            Helpers.success_message("Επιτυχής ανάκτηση δεδομένων από αρχείο.")
        except:
            ex = sys.exc_info()
            print(str(ex))
        data_file.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        window = MainApp()
        window.resize(600, 300)
        sys.exit(app.exec())
    except:
        e = sys.exc_info()
        print(str(e))

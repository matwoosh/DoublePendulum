import sys

from PyQt4 import QtGui
from PyQt4.QtCore import Qt

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar

from data import Data
from plot import Plot


class Window(QtGui.QDialog):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.argument = 1
        self.animation_time = 50.0
        self.lbl1 = QtGui.QLabel("Animation time:")
        self.lbl5 = QtGui.QLabel("\nm1:")
        self.lbl6 = QtGui.QLabel("\nError:")
        self.radio_widget = QtGui.QWidget(self)
        self.error = QtGui.QLabel("-")
        self.value = QtGui.QLabel("-")
        self.derivative = QtGui.QLabel("-")
        self.edit = QtGui.QLineEdit()
        self.update_button = QtGui.QPushButton("Update")
        self.figure = Figure(figsize=(5,5), dpi=100)  # a figure instance to plot on
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.init_ui()

    def init_ui(self):
        self.init_radio()
        self.edit.textChanged[str].connect(self.change_argument)
        self.update_button.clicked.connect(self.update_animation)

        layout = QtGui.QVBoxLayout(self)

        splitter1 = QtGui.QSplitter(Qt.Vertical)
        splitter1.addWidget(self.lbl1)
        splitter1.addWidget(self.r0)
        splitter1.addWidget(self.r1)
        splitter1.addWidget(self.r2)
        splitter1.addWidget(self.r3)
        splitter1.addWidget(self.edit)
        splitter1.addWidget(self.value)
        splitter1.addWidget(self.lbl5)
        splitter1.addWidget(self.derivative)
        splitter1.addWidget(self.lbl6)
        splitter1.addWidget(self.error)
        splitter1.addWidget(self.update_button)
        # splitter1.addWidget(left)

        splitter0 = QtGui.QSplitter(Qt.Horizontal)
        splitter0.addWidget(splitter1)

        splitter2 = QtGui.QSplitter(Qt.Vertical)
        splitter2.addWidget(self.toolbar)
        splitter2.addWidget(self.canvas)

        splitter0.addWidget(splitter2)

        layout.addWidget(splitter0)

        self.setLayout(layout)
        self.plot()

    def plot(self):
        data = Data()
        p = Plot(self.figure, data)
        p.plot_animation(self.canvas)

    def init_radio(self):
        radio_group = QtGui.QButtonGroup(self.radio_widget)
        self.r0 = QtGui.QRadioButton("10s")
        self.r1 = QtGui.QRadioButton("25s")
        self.r2 = QtGui.QRadioButton("50s")
        self.r3 = QtGui.QRadioButton("100s")

        radio_group.addButton(self.r0)
        radio_group.addButton(self.r1)
        radio_group.addButton(self.r2)
        radio_group.addButton(self.r3)

        self.r0.toggled.connect(self.set_animation_time)
        self.r1.toggled.connect(self.set_animation_time)
        self.r2.toggled.connect(self.set_animation_time)
        self.r3.toggled.connect(self.set_animation_time)

    def set_animation_time(self):
        if self.r0.isChecked():
            self.animation_time = 10.0
        elif self.r1.isChecked():
            self.animation_time = 25.0
        elif self.r2.isChecked():
            self.animation_time = 50.0
        elif self.r3.isChecked():
            self.animation_time = 100.0
        else:
            print("Fatal error occured!")

    def change_argument(self, text):
        # try:
        #     self.argument = float(text)
        #     function_data = functions[self.combo.currentIndex()]
        #     value = function_data[1](self.argument, 0)
        #     derivative_result = deriv.central(function_data[1], self.argument, 1)
        #     self.value.setText(str(value))
        #     self.derivative.setText(str(derivative_result[0]))
        #     self.error.setText(str(derivative_result[1]))
        # except:
        #     print("Wrong input")
        pass

    def update_animation(self):
        pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    w = Window()
    w.show()
    w.resize(1000, 600)

    # Set window title
    w.setWindowTitle("DoublePendulum")

    sys.exit(app.exec_())

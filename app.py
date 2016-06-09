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
        self.G = 9.8  # acceleration due to gravity, in m/s^2
        self.L1 = 1.0  # length of pendulum 1 in m
        self.L2 = 1.0  # length of pendulum 2 in m
        self.M1 = 1.0  # mass of pendulum 1 in kg
        self.M2 = 1.0  # mass of pendulum 2 in kg
        self.alpha = 120.0
        self.beta = -10.0
        self.animation_time = 10.0
        self.data = Data(self.G, self.L1, self.L2, self.M1, self.M2, self.alpha, self.beta, self.animation_time)
        self.lbl1 = QtGui.QLabel("Acceleration:")
        self.lbl2 = QtGui.QLabel("\nL1:")
        self.lbl3 = QtGui.QLabel("\nL2:")
        self.lbl4 = QtGui.QLabel("\nM1:")
        self.lbl5 = QtGui.QLabel("\nM2:")
        self.lbl7 = QtGui.QLabel("\nAlpha:")
        self.lbl8 = QtGui.QLabel("\nBeta:")
        self.lbl6 = QtGui.QLabel("\nAnimation time:")
        self.radio_widget = QtGui.QWidget(self)
        self.acceleration_input = QtGui.QLineEdit()
        self.l1_input = QtGui.QLineEdit()
        self.l2_input = QtGui.QLineEdit()
        self.m1_input = QtGui.QLineEdit()
        self.m2_input = QtGui.QLineEdit()
        self.alpha_input = QtGui.QLineEdit()
        self.beta_input = QtGui.QLineEdit()
        self.update_button = QtGui.QPushButton("Animate")
        self.figure = Figure(figsize=(5,5), dpi=100)  # a figure instance to plot on
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.init_ui()

    def init_ui(self):
        self.init_radio()
        self.acceleration_input.setText("9.8")
        self.l1_input.setText("1.0")
        self.l2_input.setText("1.0")
        self.m1_input.setText("1.0")
        self.m2_input.setText("1.0")
        self.alpha_input.setText("120.0")
        self.beta_input.setText("-10.0")
        self.acceleration_input.textChanged[str].connect(self.change_argument)
        self.l1_input.textChanged[str].connect(self.change_argument)
        self.l2_input.textChanged[str].connect(self.change_argument)
        self.m1_input.textChanged[str].connect(self.change_argument)
        self.m2_input.textChanged[str].connect(self.change_argument)
        self.alpha_input.textChanged[str].connect(self.change_argument)
        self.beta_input.textChanged[str].connect(self.change_argument)
        self.update_button.clicked.connect(self.update_animation)

        layout = QtGui.QVBoxLayout(self)

        splitter1 = QtGui.QSplitter(Qt.Vertical)
        splitter1.addWidget(self.lbl1)
        splitter1.addWidget(self.acceleration_input)
        splitter1.addWidget(self.lbl2)
        splitter1.addWidget(self.l1_input)
        splitter1.addWidget(self.lbl3)
        splitter1.addWidget(self.l2_input)
        splitter1.addWidget(self.lbl4)
        splitter1.addWidget(self.m1_input)
        splitter1.addWidget(self.lbl5)
        splitter1.addWidget(self.m2_input)
        splitter1.addWidget(self.lbl7)
        splitter1.addWidget(self.alpha_input)
        splitter1.addWidget(self.lbl8)
        splitter1.addWidget(self.beta_input)
        splitter1.addWidget(self.lbl6)
        splitter1.addWidget(self.r0)
        splitter1.addWidget(self.r1)
        splitter1.addWidget(self.r2)
        splitter1.addWidget(self.r3)
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
        self.p = Plot(self.figure, self.data)

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

        self.r0.toggle()

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
        try:
            argument = float(text)
            if self.acceleration_input.senderSignalIndex() > 0:
                self.G = argument
            elif self.l1_input.senderSignalIndex() > 0:
                print(self.L1)
                self.L1 = argument
            elif self.l2_input.senderSignalIndex() > 0:
                self.L2 = argument
            elif self.m1_input.senderSignalIndex() > 0:
                self.M1 = argument
            elif self.m2_input.senderSignalIndex() > 0:
                self.M2 = argument
            elif self.alpha_input.senderSignalIndex() > 0:
                self.alpha = argument
            elif self.beta_input.senderSignalIndex() > 0:
                self.beta = argument
            else:
                print("Fatal error occured!")
        except:
            print("Wrong input")

    def update_animation(self):
        self.data.set_data(self.G, self.L1, self.L2, self.M1, self.M2, self.alpha, self.beta, self.animation_time)
        self.p.set_data(self.data.get_data())
        self.p.plot_animation(self.canvas)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    w = Window()
    w.show()
    w.resize(1000, 600)

    # Set window title
    w.setWindowTitle("DoublePendulum")

    sys.exit(app.exec_())

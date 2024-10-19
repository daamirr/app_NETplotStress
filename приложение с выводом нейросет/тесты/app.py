from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

# from plots2 import 

import plots2


class PlotsWindow(plots2.Ui_Form):

    def __init__(self, Form):
        super().__init__(self, Form)

        self.pushButton.setText('jjj')





    # self.pushButton.clicked.connect(self.plot)
    # def __init__(self, parent = None):
    #     # super(self).__init__()

    #     super(PlotsWindow, self).__init__(parent)
  
    #     # a figure instance to plot on
    #     self.figure = plt.figure()
  
    #     # this is the Canvas Widget that 
    #     # displays the 'figure'it takes the
    #     # 'figure' instance as a parameter to __init__
    #     self.canvas = FigureCanvas(self.figure)
  
    #     # this is the Navigation widget
    #     # it takes the Canvas widget and a parent
    #     self.toolbar = NavigationToolbar(self.canvas, self)
  
    #     # Just some button connected to 'plot' method
    #     self.button = QPushButton('Plot')
          
    #     # adding action to the button
    #     self.button.clicked.connect(self.plot)
  
    #     # creating a Vertical Box layout
    #     layout = QVBoxLayout()
          
    #     # adding tool bar to the layout
    #     layout.addWidget(self.toolbar)
          
    #     # adding canvas to the layout
    #     layout.addWidget(self.canvas)
          
    #     # adding push button to the layout
    #     layout.addWidget(self.button)
          
    #     # setting layout to the main window
    #     self.setLayout(layout)
  
    # action called by the push button
    def plot(self):
          
        print('privetrtt')
        # # random data
        # data = [random.random() for i in range(10)]

  
        # # clearing old figure
        # self.figure.clear()
  
        # # create an axis
        # ax = self.figure.add_subplot()
  
        # # plot data
        # ax.plot(data, '.-')
  
        # # refresh canvas
        # self.canvas.draw()

# PlotsWindow = plots.Ui_Form()
# PlotsWindow.pushButton.setText('HHH')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Main Window')
        

        self.button = QPushButton('Построить графики')
        self.button.clicked.connect(self.open_wn_plots)


        self.button2 = QPushButton('Подобрать параметры')
        self.button2.clicked.connect(self.open_wn_search)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.button2)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


    def open_wn_plots(self, checked):

        self.wn = QWidget()
        form = plots2.Ui_Form()
        form.setupUi(self.wn)
        self.wn.show()

    def open_wn_search(self):
            # def __init__(self):
            # super(Connector, self).__init__()
            # self.ui = Ui_MainWindow()
            # self.ui.setupUi(self)

        self.wn2 = QWidget()
        form = PlotsWindow(self.wn2)
        # form.setupUi(self.wn2)
        self.wn2.show()

        # self.wn2 = PlotsWindow()
        # self.wn2.show()


app = QApplication([])


window = MainWindow()
window.resize(600, 400)

window.show()


app.exec()
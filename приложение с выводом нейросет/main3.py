from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QDialog

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

from plots import Ui_Form
import data_ouput

import random

# replace запятую на точку

class PlotsWindow(QWidget):

    def __init__(self):
        super(PlotsWindow, self).__init__() #    дамир)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.plot)
        self.ui.pushButton.setText('Аня')

        self.ui.horizontalSliderTemp.valueChanged.connect(self.setValue_in_lineEditTEMP)
        self.ui.horizontalSliderSh.valueChanged.connect(self.setValue_in_lineEditSH)

        self.ui.spinBoxThickness.setButtonSymbols(4)# setText('4')
        self.ui.lineEdit_sh.setText('52')
        self.ui.lineEdit_temp.setText('0.001')
        # self.temp = 0.001

        self.figure = plt.figure()
        self.figure2 = plt.figure()
  
        self.canvas = FigureCanvas(self.figure)
        # self.canvas2 = FigureCanvas(self.figure)
        self.canvas2 = FigureCanvas(self.figure2)
    
   
        self.ui.LayoutDeform.addWidget(self.canvas)
        self.ui.LayoutStress.addWidget(self.canvas2)
        # self.ui.verticalLayout.addWidget(self.canvas2)
        # self.ui.horizontalLayout.addWidget(self.canvas)
 

    def setValue_in_lineEditTEMP(self):

        max = 0.0065
        min = 0.001

        # k = 0.055 / 100
        k = (max - min) / 100
        # b = 0.01
        b = min

        value = str(round(float(self.ui.horizontalSliderTemp.value()) * k + b, 4))
        self.ui.lineEdit_temp.setText(value)

    def setValue_in_lineEditSH(self):

        max = 1e4
        min = 52

        # k = 0.055 / 100
        k = (max - min) / 100
        # b = 0.01
        b = min

        value = str(round(float(self.ui.horizontalSliderSh.value()) * k + b, 4))
        self.ui.lineEdit_sh.setText(value)


    def plot(self):

        # self.thickness = float(self.ui.lineEdit_thickness.displayText()) * 1000
        self.thickness = float(self.ui.spinBoxThickness.value()) * 1000
        self.sh = float(self.ui.lineEdit_sh.displayText().replace(',', '.'))
        self.temp = float(self.ui.lineEdit_temp.displayText().replace(',', '.'))

 
        # data real
        datayr = data_ouput.Y_real_2mm
        dataxr = data_ouput.X_real_2mm

        # data deform
        datayd = data_ouput.draw_plots(self.thickness, self.sh, self.temp)[0]
        dataxd = data_ouput.edge_lenght

        # data stress
        datays = data_ouput.draw_plots(self.thickness, self.sh, self.temp)[1]
        dataxs = data_ouput.Z

 
        self.figure.clear()
        self.figure2.clear()
  
        # create an axis
        ax = self.figure.add_subplot()
        ax.grid()

        # ax.title("Деформации")
        ax.set_title('Деформации')
        ax.set_xlabel('Длина по кромке, мм')
        ax.set_ylabel('Прогиб, мм')
    
        ax.plot(dataxd, datayd, '.-')
        # ax.legend()
        
        # plt.xlabel('Длина по кромке, мм')
        # plt.ylabel('Прогиб, мм')

        ax2 = self.figure2.add_subplot()
        ax2.grid()
        ax2.set_title("Остаточные напряжения")
        ax2.set_xlabel('Глубина, мкм')
        ax2.set_ylabel('Остаточные деформации, МПа')

        ax2.plot(dataxs, datays, '.-')
        # ax2.legend()

        # ax.title(f'sh = {round(self.sh, 1)}, temp = {round(self.temp, 4)}')
           
        # ax.plot(dataxr, datayr, '.-')
  
        # refresh canvas
        self.canvas.draw()
        self.canvas2.draw()


app = QApplication([])

window = PlotsWindow()
# window.resize(600, 400)
window.show()

app.exec()
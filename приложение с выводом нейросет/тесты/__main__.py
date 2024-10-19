from PyQt5 import QtCore, QtGui, QtWidgets

import plots

import sys

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = plots.Ui_Form()
ui.setupUi(Form)
Form.show()
app.exec()
# sys.exit(app.exec_())

# Form, Window = uic.loadUiType("D:\НИРС\\Qt\приложение с выводом нейросет\\plots.ui")

# app = QApplication([])
# form = Form()
# window = Window()
# form.setupUi(window)
# window.show()
# app.exec()
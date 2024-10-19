from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

import plots

Form, Window = uic.loadUiType("D:\НИРС\\Qt\приложение с выводом нейросет\\plots.ui")

app = QApplication([])
form = Form()
window = Window()
form.setupUi(window)
window.show()
app.exec()
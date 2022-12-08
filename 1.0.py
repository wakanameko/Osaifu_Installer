vertion = "1.0"
developer = "@wakanameko2"

import sys
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow

def exit_tab():
  print('exit')

app = QApplication(sys.argv)
main = QMainWindow()

main.setWindowTitle('Osaifu_Installer')
main.resize(500, 200)

newAct = QAction("")

main.show ()

sys.exit(app.exec())

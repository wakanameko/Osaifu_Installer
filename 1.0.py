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

newAct = QAction("&New", main, triggerd = exit_tab)
menuBar = main.menuBar()
fileMenu = menuBar.addMenu("&Osaifu_Installer")
fileMenu.addAction(newAct)

main.setMenuBar(menuBar)
main.show ()

sys.exit(app.exec())

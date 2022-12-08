vertion = "1.0"
developer = "@wakanameko2"

import os
import platform
import sys
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow

if not os.name == 'nt':messagebox.showerror('Attention','Windows以外のOSでの実行は想定されていません。エラーが発生しても自己責任でお願いします。')

if ur.release == 'vista':messagebox.showerror('Attention','このバージョンのWindowsは対応していません。')
if ur.release == 'xp':messagebox.showerror('Attention','このバージョンのWindowsは対応していません。')
if ur.release == '2000':messagebox.showerror('Attention','このバージョンのWindowsは対応していません。')
if ur.release == 'me':messagebox.showerror('Attention','このバージョンのWindowsは対応していません。')
if ur.release == '98':messagebox.showerror('Attention','このバージョンのWindowsは対応していません。')
if ur.release == '95':messagebox.showerror('Attention','このバージョンのWindowsは対応していません。')

def exit_tab():
  print('exit')

label = QLabel()
label.setText('このソフトフェアを使用するにはADBが必要です。')

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

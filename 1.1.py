# coding: UTF-8
from distutils.cmd import Command
from email.mime import base
import tkinter as tk
from turtle import goto
import webbrowser
import platform
import os
import sys
from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image, ImageTk
import urllib.request as req

if not os.name == 'nt':messagebox.showerror('Attention','Windows以外のOSでの実行は想定されていません。エラーが発生しても自己責任でお願いします。')

ur = platform.uname()
print(ur.system)
print(ur.release)
print(ur.version)
print(ur.processor)

if ur.release == 'vista':messagebox.showerror('Attention','このバージョンのWindowsは対応していません。')
if ur.release == 'xp':messagebox.showerror('Attention','このバージョンのWindowsは対応していません。')
if ur.release == '2000':messagebox.showerror('Attention','このバージョンのWindowsは対応していません。')
if ur.release == 'me':messagebox.showerror('Attention','このバージョンのWindowsは対応していません。')
if ur.release == '98':messagebox.showerror('Attention','このバージョンのWindowsは対応していません。')
if ur.release == '95':messagebox.showerror('Attention','このバージョンのWindowsは対応していません。')

AppName = 'Osaifu_Installer_v1.1'
Developer = '@wakanameko2'
print(AppName)
print(Developer)

baseGround = tk.Tk()
baseGround.geometry('400x200')
baseGround.resizable(width = False, height = False)
baseGround.title(AppName)

windowicon = """R0lGODlhyADIAPcAAGM+FWhLJm5WTVpudmtra2NiYmZ3fVdUU3M9ULAULccAC8cA
CMkAE8sAHNMAFtY3Hsw7Hs0AI80EKs8KLsoNKNIBJdUGLM8WLM4EM88NMcoAOdEF
NNAOMdATNNIbPNEZNdEbLM4mJ9QpJtQtLatnGo1bJ6p3KspGGN1EGdFXD+RXDslq
B815AMxzAtR5ANt5ANRzANNvBuxlAOxsAOZkDO11AOR8AO58AO57DOx2CO58E+59
G+52FPJ5BO98J+59MoQ3Q9QnRtg7VtIzSrpdbdlFWttKZd1Vat9cc85fc9dnduFn
fOFxfI63L5O+E++CAO+EC+yIBvODAPuDAPGLAPCIDe+CHO+DFPCMFPCOGvCCHfGR
FO+DI++EK++KKfCJKfCSIvKWK/GYLu6HN/CMM/CLO/KaMvGXOvSmMPKgPvSlLtSC
AJjCHZ3IKZzENaHIM6LNN/CNQvCOS/GVRPGUS/KaSvGTVPKaVPKYXO+QUPOjQ/Ol
SvSoWPWwX/KeZfOkafW0Z/OoefW6cvW4e9ara/fAf8PbeqPEQ1x5i2N7huNtguN2
h+V+kNN4h26Fi2SEiGaYnW6otGOLmmy61Gm20XO5zHfD3HzCz3zK5JucnK2traWm
prW1tdOMl+eImOePl/OshPSvjPSyhvSzivW6ifW1lvW7lPW6m+ubqeylre6ptu+3
u/C3vvS5p9GsssnfiPfFivfEiPfHmPjQn8vijvbEpPfGrfjKrPfJqPnSo/nVrPrY
rPjNtPfLtvnStPnTvfrdu/nXt9TnrPvgufG6w+6+wYnF14XS7Izb9IbQ65Tj/Jrr
/5fo/5zz/577/5fw/47h/6rs68vLy8XGxdTU1dLNzfPFy/nVxPnbzPnXxfTM0/rd
0/bX2vvixPvmzPrj1fzp0/vl3Pzs3O711Pjd4tzt6ujq6fzs5Pvs6/rl5f3x5P3z
7Pb66fvu8fPz8/318v759f////n5+enx8NTe5bLBvgAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAACH5BAAAAAAAIf8LSW1hZ2VNYWdpY2sNZ2FtbWE9MC40NTQ1
NQAsAAAAAMgAyAAACP4AnwgcSLCgwYMIEypcqFAKw4cQI0qMSGWixYsYM2rcmNEh
x48gQ4ocSbKkSZMeT6pcyVJkxZYdYSJMKbOmzZs4KebcyVMgzYMvVf7sSXRm0aNC
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
"""
baseGround.tk.call('wm', 'iconphoto', baseGround._w, tk.PhotoImage(data = windowicon))

Menubaa = tk.Menu(baseGround) 
baseGround.config(menu=Menubaa)

def About_Osaifu():
    Pop_About = tk.Toplevel()
    Pop_About.geometry('300x225')
    Pop_About.resizable(width = False, height = False)
    Pop_About.title(AppName)
    Label_abt = tk.Label(Pop_About, text=AppName, font=("normal", 11, "bold"))
    Label_abt.pack(side = tk.TOP)
    canvas = tk.Canvas(Pop_About, bg="#deb887", height=200, width=200)
    canvas.pack(side = tk.RIGHT)

    def OpenGitHub():
        webbrowser.open('https://github.com/wakanameko/Osaifu_Installer')
    Pop_About.tk.call('wm', 'iconphoto', Pop_About._w, tk.PhotoImage(data = windowicon))
    img = tk.PhotoImage(data = windowicon, width=200, height=200)
    canvas.create_image(0, 0, image=img, anchor=tk.NW)

    Label_dev = tk.Label(Pop_About, text='Developer:        \n@wakanameko2')
    Label_dev.pack(expand = True)
    Label_sup = tk.Label(Pop_About, text='問題が発生した   \n場合は、            \n上記TwitterIDの \nDMもしくはリプ \nにお願いします。')
    Label_sup.pack(expand = True)
    button_Github = tk.Button(Pop_About, text = 'Githubに移動', command = OpenGitHub, width = 12)
    button_Github.pack(expand = True)

    Pop_About.mainloop()

    print(AppName)
    print(Developer)

def installOsaifu():
    Label_inst.forget()
    Label_ready = tk.Label(baseGround, text='処理を実行しています。')
    Label_ready.pack()
    print('selected install')
    import subprocess
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.store.appssha2')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.felicaremotelock')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.osaifu.tsmproxy')   
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.dpoint')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.android.tapandpay')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.dcard')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.nttdocomo.keitai.payment')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'jp.id_credit_sp.android')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'cmd', 'package', 'install-existing', 'com.felicanetworks.mfm.main')
    subprocess.call(cmd)
    print('AllDone!')
    Label_ready.forget()
    Label_Done = tk.Label(baseGround, text='処理が完了しました。')
    Label_Done.pack()

def uninstallOsaifu():
    Label_inst.forget()
    Label_ready = tk.Label(baseGround, text='処理を実行しています。')
    Label_ready.pack()
    print('selected uninstall')
    import subprocess
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.store.appssha2')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.felicaremotelock')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.osaifu.tsmproxy')   
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.dpoint')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.android.tapandpay')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.dcard')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.nttdocomo.keitai.payment')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'jp.id_credit_sp.android')
    subprocess.call(cmd)
    cmd = ('adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', 'com.felicanetworks.mfm.main')
    subprocess.call(cmd)
    print('AllDone!')
    Label_ready.forget()
    Label_Done = tk.Label(baseGround, text='処理が完了しました。')
    Label_Done.pack()
    
def exitOsaifu():
    exit()

menu_file = tk.Menu(baseGround)
Menubaa.add_cascade(label='Osaifu_Installer', menu=menu_file) 
menu_file.add_command(label='Install', command=installOsaifu) 
menu_file.add_command(label='Uninstall', command=uninstallOsaifu)
menu_file.add_command(label='exit', command=exitOsaifu)

menu_about = tk.Menu(baseGround)
Menubaa.add_cascade(label='about', menu=menu_about)
menu_about.add_command(label='about', command=About_Osaifu)

button_install = tk.Button(baseGround, text = "Install", command = installOsaifu, width = 8)
button_uninstall = tk.Button(baseGround, text = "Uninstall", command = uninstallOsaifu, width = 8)
Label_wlcm = tk.Label(baseGround, text='Welcome to Osaifu_Installer', font=("normal", 11, "bold"))
Label_inst = tk.Label(baseGround, text='オプションを選択してください。')
#Layout
Label_wlcm.pack()
button_install.pack(expand = True)
button_uninstall.pack(expand = True)
Label_inst.pack()

baseGround.mainloop()
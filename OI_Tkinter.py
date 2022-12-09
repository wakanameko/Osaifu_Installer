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

if ur.release == 'xp':messagebox.showerror('Attention','このバージョンのWindowsは対応していません。')
if ur.release == '2000':messagebox.showerror('Attention','このバージョンのWindowsは対応していません。')
if ur.release == 'me':messagebox.showerror('Attention','このバージョンのWindowsは対応していません。')
if ur.release == '98':messagebox.showerror('Attention','このバージョンのWindowsは対応していません。')
if ur.release == '95':messagebox.showerror('Attention','このバージョンのWindowsは対応していません。')

AppName = 'Osaifu_Installer_v1.0'
Developer = '@wakanameko2'
print(AppName)
print(Developer)

baseGround = tk.Tk()
baseGround.geometry('400x200')
baseGround.resizable(width = False, height = False)
baseGround.title(AppName)

Menubaa = tk.Menu(baseGround) 
baseGround.config(menu=Menubaa)

def About_Osaifu():
    Pop_About = tk.Toplevel()
    Pop_About.geometry('300x200')
    Pop_About.resizable(width = False, height = False)
    Pop_About.title(AppName)
    Label_abt = tk.Label(Pop_About, text=AppName, font=("normal", 11, "bold"))
    Label_abt.pack(side = tk.TOP)
    canvas = tk.Canvas(Pop_About, bg="#deb887", height=200, width=200)
    canvas.pack(side = tk.RIGHT)

    def OpenGitHub():
        webbrowser.open('https://github.com/wakanameko/Osaifu_Installer')

    url = "https://avatars.githubusercontent.com/u/63937252?v=4"
    req.urlretrieve(url, "test.png")
    img = Image.open('test.png')
    img = ImageTk.PhotoImage(img)
    img = tk.PhotoImage(file='test.png', width=420, height=420)
    img = img.subsample(2)
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
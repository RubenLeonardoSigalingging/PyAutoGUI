#!/usr/bin/env python3


# ---THIS TOOLS OR PROGRAM USING INDONESIA LANGUAGE---
# Dibuat Oleh: Ruben Leonardo Sigalingging.
# Dibuat Pada: Selasa, 14 Juni 2022, Pukul 22:22 PM.
# Menggunakan: Bahasa Pemrogramman Python Versi 3.8.10


# 1. IMPORT MODUL PYTHON3
import os
from os import system
system("chmod 777 PyAutoGUI.py")
system("chmod 777 Pesan.txt")
from pyfiglet import figlet_format
from time import time, sleep
from datetime import datetime
import pyautogui
# https://pypi.org/project/PyAutoGUI/


tema = figlet_format("PyAutoGUI",font="slant")
print(tema)
print("\033[91m[\033[94m!\033[91m] \033[94mDibuat Oleh: \033[91mRuben Leonardo Sigalingging.")
print("\033[91m[\033[94m!\033[91m] \033[94mDibuat Pada: \033[91mSelasa, 14 Juni 2022, Pukul 22:22 PM.")
print("\033[91m[\033[94m!\033[91m] \033[94mMenggunakan: \033[91mBahasa Pemrogramman Python Versi 3.8.10")
print("")
print("\033[91m---\033[94mPyAutoGUI\033[91m---")


# Dapatkan input dari user, untuk menginputkan file.
file = input("\033[91m[\033[94m!\033[91m] \033[94mFile: [Contoh: \033[91mPesan.txt] \033[94m~> \033[91m")
sleep(9)
# Buka dan baca file yang sudah diinputkan user.
buka_dan_baca_file = open(file,"r")
# Buat kode perulangan [For Loop]
for python_auto_grafik_user_interface in buka_dan_baca_file:
	pyautogui.typewrite(python_auto_grafik_user_interface,interval="0.50")
	pyautogui.typewrite("enter")
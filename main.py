#hub for deployment
#all rights reserved
import os
import sys

ver = 1.0
menu = 0
exec_type = 0

print("_" * 20 + "\n" * 2)

def ExecuteFile(exec_type, filename):
    if exec_type == "cmd":
        try:
            os.system(filename)
        except:
            print(filename + " not found...")
    else: 
        try:
            os.system("python3 " + filename)        
        except FileNotFoundError:
            print(filename + " not found...")

while True:

    if menu == 0:

        print("Make a selection below vvv" + "\n")
        print("1. Registry Edits")
        print("2. Building Blocks Edit")
        print("3. Full deployment")

        if menu == 1:

            print("Registry edits in progress..")
            ExecuteFile("python3", R'scripts\od_reg_edit.py')

        if menu == 2:

            print("Building Blocks edit in progress...")
            ExecuteFile("python3", R'scripts\building_blocks_edit.py')

        if menu == 3:
            ExecuteFile("cmd", R'scripts\run.bat')
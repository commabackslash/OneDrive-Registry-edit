# Script for adding corporate building blocks file for word. All rights reserved.

# imports
import sys
import shutil
import time
import os
from os import path

#config
email_format = ("")
global directory
global service
word_directory = (R"C:\Program Files\Microsoft Office\root\Office16\WINWORD.exe")
version = 1.0
success = 0

with open(r"includes\banner.txt") as f:
    banner = f.read()
    print(banner)

print("")
print("_" * 20 + "\n ")
print("[*] Building Blocks Deployment v" + str(version))

# [] Grabbing user information
device_username = str(os.getlogin())
user_directory = ("C:\\Users\\" + device_username)
email_format = ("")
print("[*] Logged in as user " + "'" + device_username + "'")
print("[*] Microsoft user " + "'" + device_username + email_format + "'")
print("_" * 20)
print("")

# [] creating a function that passes a path and verifies that a file is existent
def CheckFile(directory, service):

    existence = path.exists(directory)

    if existence == True:

        global success
        print("[*] " + str(service) + " exists...")
        success = success + 1

    else:

        print("[*] " + str(service) + " is unable to be verified... exiting..")
        time.sleep(5)
        exit()

# [] using our function to validate that word is installed, and that the building blocks file can be accessed
word_installation = CheckFile(word_directory, "Word Installation")
building_blocks_file = CheckFile(R"includes\building_blocks.docx", "Building Blocks File")

print("_" * 20 + "\n ")

# [] If the default files are found, move on with the installation process
if success == 2:

    print("[*] All requirements met, adding building blocks.." + "\n " + "_" * 20 + "\n")

    shutil.copy(R"includes\building_blocks.docx", user_directory + R"\AppData\Roaming\Microsoft\Document Building Blocks\1033\16")

    CheckFile(user_directory + R"\AppData\Roaming\Microsoft\Document Building Blocks\1033\16\building_blocks.docx", "Building blocks installed in the word directory")

    # [] Once we verify that the new building blocks file in installed in the word directory, tell user that it is ready.
    if success == 3:

        print("[*] Building blocks files succesfully installed and ready for user use. Exiting.")

    else:

        print("[*] Error occured. Exiting..")
        time.sleep(5)
        exit()

# [] if it dont work then idk
else:

    print("[*] Error verifying files or my code sucks. Please manually install the files. Exiting...")
    time.sleep(5)
    exit()


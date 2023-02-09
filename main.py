# Script for the one drive registry  edit
#packages
import os
import shutil
import winreg

version = 1.0
global registry_mod_path
reg_success = 0

with open(r"includes\banner.txt") as f:
    banner = f.read()
    print(banner)

print("")
print("_" * 20)
print("")

print("[*] Deployment v" + str(version))


# [] Grabbing user information
device_username = str(os.getlogin())
user_directory = ("C:\\Users\\" + device_username)
email_format = ("")
print("[*] Logged in as user " + "'" + device_username + "'")
print("[*] Microsoft user " + "'" + device_username + email_format + "'")
print("_" * 20)
print("")

# [] Registry modifications
OneDriveKey = ("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Desktop\\NameSpace\\{018D5C66-4533-4307-9B53-224DE2ED1FE6}") 
OneDriveCompanyKey = ("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Desktop\\NameSpace\\{04271989-C4D2-DADF-5567-307CA29F86E9}")
CLSID_Key = ("CLSID\\{018D5C66-4533-4307-9B53-224DE2ED1FE6}")

OneDriveRegistryKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, OneDriveKey, 0, winreg.KEY_READ)
OneDriveCompanyRegistryKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, OneDriveCompanyKey, 0, winreg.KEY_READ)

OneDriveKeyValue, regtype = winreg.QueryValueEx(OneDriveRegistryKey, "")
OneDriveCompanyRegistryKeyValue, regtype = winreg.QueryValueEx(OneDriveCompanyRegistryKey, "")

winreg.CloseKey(OneDriveRegistryKey)
winreg.CloseKey(OneDriveCompanyRegistryKey)

if OneDriveKeyValue == ("OneDrive"):

    reg_success = reg_success + 1
    print("[*] Detected default 'OneDrive' folder..")

else:

    print("Registry Error while detecting default OneDrive folder. Ensure the key value is {018D5C66-4533-4307-9B53-224DE2ED1FE6} manually")

if OneDriveCompanyRegistryKeyValue == ("REPLACE THIS WITH COMPANY ONEDRIVE REGISTRY NAME"):

    reg_success = reg_success + 1
    print("[*] Detected Company OneDrive folder....")

else:

    print("Registry Error")

if reg_success == 2:

    print("[*] Both OneDrive folders detected")

    winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, CLSID_Key)
    CLSID_RegistryKey = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, CLSID_Key, 0, winreg.KEY_READ)
    winreg.SetValueEx(CLSID_RegistryKey, "System.IsPinnedToNameSpaceTree", 0, winreg.REG_SZ, "0")
    winreg.CloseKey

    UpdatedCLSIDKey = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, CLSID_Key, 0, winreg.KEY_READ)
    UpdatedCLSIDKeyValue, regtype = winreg.QueryValueEx(UpdatedCLSIDKey, "System.IsPinnedToNameSpaceTree")

    if UpdatedCLSIDKeyValue == "0":

        print("[*] Succesfully disabled the personal OneDrive from file explorer")
        print("[*] Restart the PC to ensure changes, then confirm the changes were made.")
        exit()

os.wait()

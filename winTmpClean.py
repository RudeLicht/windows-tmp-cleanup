import os
import shutil
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def clear_temp_directory(directory_path, description):
    try:
        print(f"\n{description}...")
        if os.path.exists(directory_path):
            shutil.rmtree(directory_path, ignore_errors=True)
            print(f"Successfully cleaned: {description}")
        else:
            print(f"{description} not found")
    except Exception as e:
        print(f"Error cleaning {description}: {e}")

if is_admin():
    user_path = os.path.expanduser('~')

    print("\nCleaning Windows Temporary Files")

    # Clear User's Temp Directory
    clear_temp_directory(user_path + r'\AppData\Local\Temp', "User Temp Directory")

    # Clear Windows Update Download Cache
    clear_temp_directory(r'C:\Windows\SoftwareDistribution\Download', "Windows Update Download Cache")

    # Clear Windows System Temp Folder
    clear_temp_directory(r'C:\Windows\Temp', "Windows System Temp Folder")

    # Empty Recycle Bin
    print("\nNow emptying the Recycle Bin...")
    os.system("rd /s c:\$Recycle.Bin")
    print("Recycle Bin emptied")

    # Clear DNS Cache
    print("\nJunk files have been deleted, now clearing DNS cache...")
    os.system('ipconfig /flushdns')
    print("DNS cache cleared")
    
    print('\nCleaning is done. Press ENTER to close!')
    input()
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1)

# Made by licht :D

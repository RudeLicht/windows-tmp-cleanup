import os
import shutil
import ctypes
import sys
import platform

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def confirm_cleanup():
    confirmation = input("This script will delete temporary files. Are you sure you want to proceed? (y/n): ")
    return confirmation.lower() == 'y'

def delete_directory(path):
    try:
        if os.path.exists(path):
            shutil.rmtree(path)
            print(f"Deleted: {path}")
        else:
            print(f"Not found: {path}")
    except Exception as e:
        print(f"Error deleting {path}: {e}")

def clean_temporary_files():
    if not confirm_cleanup():
        print("Cleanup aborted.")
        return

    user_path = os.path.expanduser('~')

    print(f"\nYou are in: {os.getcwd()}")
    
    # Clean user's temp directory
    user_temp_path = os.path.join(user_path, 'AppData', 'Local', 'Temp')
    print(f"\nNow cleaning: {user_temp_path}")
    print('\nCleaning...')
    delete_directory(user_temp_path)
    print('\n--------------------------------------------------------')

    # Clean Windows update download cache
    if platform.system() == 'Windows':
        windows_download_path = os.path.join('C:', 'Windows', 'SoftwareDistribution', 'Download')
        print(f"\nNow cleaning: {windows_download_path}")
        print('\nCleaning...')
        delete_directory(windows_download_path)
        print('\n--------------------------------------------------------')

        # Clean Windows system temp folder
        windows_temp_path = os.path.join('C:', 'Windows', 'Temp')
        print(f"\nNow cleaning: {windows_temp_path}")
        print('\nCleaning...')
        delete_directory(windows_temp_path)
        print('\n--------------------------------------------------------')

        # Empty Recycle Bin
        print("\nNow cleaning: Recycle Bin")
        os.system("rd /s c:\$Recycle.Bin")
        print('\nCleaning...')
        print('\n--------------------------------------------------------')

    # Clear DNS cache
    print('\nJunk files have been deleted, now clearing DNS cache...')
    os.system('ipconfig /flushdns')
    print('\n--------------------------------------------------------')
    input('\nCleaning is done. Press ENTER to close!')

if is_admin():
    clean_temporary_files()
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1)

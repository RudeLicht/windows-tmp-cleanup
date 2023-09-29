import os
import shutil
import ctypes
import sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    user_path = os.path.expanduser('~')

    print("\nYou are in: "+os.getcwd())
    os.chdir(user_path+r'''\AppData\Local\Temp''')
    print('\n--------------------------------------------------------')
    print("\nNow cleaning: "+os.getcwd())

    print('\nCleaning...')
    shutil.rmtree(user_path+r'''\AppData\Local\Temp''', ignore_errors=True)
    print('\n--------------------------------------------------------')

    os.chdir(r'''C:\Windows\SoftwareDistribution\Download''')

    print("\nNow cleaning: "+os.getcwd())

    print('\nCleaning...')
    print('\n--------------------------------------------------------')
    shutil.rmtree(r'''C:\Windows\SoftwareDistribution\Download''',
                  ignore_errors=True)

    os.chdir(r'''C:\Windows\Temp''')

    print("\nNow cleaning: "+os.getcwd())

    print('\nCleaning...')
    print('\n--------------------------------------------------------')
    shutil.rmtree(r'''C:\Windows\Temp''',
                  ignore_errors=True)

    print("\nNow cleaning: c:\$Recycle.Bin, TYPE Y\n")
    os.system("rd /s c:\$Recycle.Bin")
    print('\nCleaning...')
    print('\n--------------------------------------------------------')

    print('\nJunk files have been deleted, now clearing cache...')
    os.system('ipconfig/flushdns')
    print('\n--------------------------------------------------------')
    print(input('\nCleaning is done Press ENTER to close!'))

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1)


# made by licht :D

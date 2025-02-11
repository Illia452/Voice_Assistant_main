from PIL import ImageGrab
from pathlib import Path
import webbrowser
import sys, os, subprocess, inspect

class VoiceCommands():
    def TakeScreenShot(self):
        path = Path("Screenshots") # шлях до папки
        path.mkdir(parents=True, exist_ok=True) # exist_ok=true - якщо папка screenshots існує то знехтувати помилкою

        screen = ImageGrab.grab()

        num = 1
        while True:
            file_screen = path / (f"screenshot_{num}.png") # збереження скріну в створену папку
            if file_screen.exists():
                num += 1
            else:
                break
            
        screen.save(file_screen)

    def OpenBrowser(self):
        webbrowser.open('https://www.google.com/')

    # def SelectFile(self):
    #     #subprocess.Popen(r'explorer /select,%s' % os.path.abspath(inspect.getfile(inspect.currentframe())))

    #     ## or...

    #     pFileName = os.path.abspath(inspect.getfile(inspect.currentframe()))
    #     pFileDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    #     print ( 'pFileName = %s\n' % pFileName)
    #     print ('pFileDir = %s' % pFileDir)
    #     subprocess.Popen(r'explorer /select,%s' % pFileName)
    #     if (pFileName.endswith(".png") or pFileName.endswith(".py") or pFileName.endswith(".txt")):
    #         # subprocess.call([r'C:\Program Files\Notepad++\notepad++.exe',  pFileName])
    #         subprocess.Popen([r'C:\Program Files\Notepad++\notepad++.exe',  pFileName])
            

    



commands = VoiceCommands()


    
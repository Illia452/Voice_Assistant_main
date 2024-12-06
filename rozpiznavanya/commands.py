from PIL import ImageGrab
from pathlib import Path

class Commands():
    def TakeScreenShot():
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




    
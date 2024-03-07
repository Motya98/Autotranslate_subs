import pyscreenshot
import pytesseract
import translate
import time
from tkinter import *
import threading


def target(tempory_text):
    garbage = []
    translator = translate.Translator(from_lang='en', to_lang='ru')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    while True:
        image = pyscreenshot.grab(bbox=(0, 50, 1000, 170))
        text = pytesseract.image_to_string(image, lang='eng')
        if text != tempory_text:
            try:
                tempory_text = text
                google = translator.translate(text)
                if len(garbage) != 0:
                    garbage[0].destroy()
                    garbage.pop()
                label = Label(text=google, font=("Arial", 10))
                label.pack(padx=20, pady=30)
                garbage.append(label)
            except:
                pass
        time.sleep(1)

tempory_text = []
root = Tk()
root.geometry("700x100+0+130")
root.attributes('-alpha', 0.4)
root.attributes("-topmost",True)
threading.Thread(target=target, args=(tempory_text,)).start()
root.mainloop()

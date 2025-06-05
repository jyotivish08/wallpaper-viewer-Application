from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title('Wallpeper Viewer')

root.geometry('250x400')
root.configure(background= '#111')

#added image on screen

files = os.listdir('wallpapers')
print(files)

img_array = []
for file in files:
    img = Image.open(os.path.join('wallpapers', file))
    resized_img = img.resize((200,300))
    img_array.append(ImageTk.PhotoImage(resized_img))

img_label = Label(root, image = img_array[0])
img_label.pack(pady=(15,10))
root.mainloop()



root.mainloop()
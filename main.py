from tkinter import *        # Tkinter GUI library import kar rahe hai
from PIL import ImageTk, Image  # PIL se images load aur resize karne ke liye modules import kiye
import os                      # OS module se folders ke andar ke files access kar paayenge

# Jab "Next" button dabaye to image change ho — uske liye function banaya
def rotate_image():
    global counter
    img_label.config(image=img_array[counter % len(img_array)])  # image_label me naye image lagao (modulo se circular rotation)
    counter = counter + 1  # counter badhate jao, taki agla image aaye

counter = 1  # Image rotation ke liye counter define kiya

root = Tk()  # Root window create kiya
root.title('Wallpaper Viewer')  # Title set kiya

root.geometry('250x400')  # Window ka size set kiya
root.configure(background='#111')  # Background color dark set kiya (dark grey/blackish)

# === Wallpaper folder se images load kar rahe hai ===
files = os.listdir('wallpapers')  # wallpapers folder ke andar jitne files hai unka list banaya
print(files)  # Debug ke liye print kar rahe hai ki kaunse files mile

img_array = []  # Sare resized PhotoImage objects store karne ke liye list banayi
for file in files:
    img = Image.open(os.path.join('wallpapers', file))  # File ko open kiya
    resized_img = img.resize((200, 300))  # Har image ko chhota resize kiya taaki window me fit aaye
    img_array.append(ImageTk.PhotoImage(resized_img))  # Resized image ko tkinter-compatible format me convert karke list me daal diya

# === Pehla image screen par dikhane ke liye label banaya ===
img_label = Label(root, image=img_array[0])
img_label.pack(pady=(15, 10))  # Thoda padding diya top aur bottom se

# === Next button banaya jo image rotate karega ===
next_btn = Button(root, text='Next', bg='white', fg='black', width=28, height=2, command=rotate_image)
next_btn.pack()  # Button ko screen par dikhaya

root.mainloop()  # GUI window ko chalu rakhta hai jab tak user band na kare

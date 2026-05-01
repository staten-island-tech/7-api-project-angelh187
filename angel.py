import requests
import tkinter as tk
from PIL import Image, ImageTk
import time

def cats():

    url = 'https://cataas.com/cat'
    print(url)
    response = requests.get(url)
    label.destroy()
    with open('cat.jpeg', 'wb') as f:
        f.write(response.content)

    images = Image.open("cat.jpeg")
    photo = ImageTk.PhotoImage(images)

    label = tk.Label(window, image=photo)
    label.pack(pady = 30)
    label.image = photo


    

    
    


window = tk.Tk()
window.title("message reverser")
window.geometry("1200x800")
window.resizable(False, False)
prompt = tk.Label(window,text="Click the button for a cat!",font =("Arial,16"))
prompt.pack(pady=10)
button = tk.Button(
    window,
    text="Cat here",
    command=cats,
    font = ("Arial",16),
    bg = "pink",
    fg = "blue",
    relief="raised",
    padx=10, pady=5
    )
button.pack(pady=20)



window.mainloop()

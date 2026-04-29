import requests
import tkinter as tk
from PIL import Image, ImageTk

def cats():
    url = 'https://cataas.com/cat'
    print(url)
    response = requests.get(url)
    with open('cat.jpeg', 'wb') as f:
        f.write(response.content)

    image = Image.open("cat.jpeg")
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(window, image=photo)
    label.pack(pady = 30)


window = tk.Tk()
window.title("message reverser")
window.geometry("1000x600")
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

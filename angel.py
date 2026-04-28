import requests
import tkinter as tk

window = tk.Tk()
window.title("message reverser")
window.geometry("400x250")
window.resizable(False, False)
prompt = tk.Label(window,text="Click the button for a cat!",font =("Arial,16"))
prompt.pack(pady=10)
button = tk.Button(
    window,
    text="Cat here",
    command=,
    font = ("Arial",16),
    bg = "pink",
    fg = "hot pink"
    relief="raised",
    padx=10, pady=5
    )

window.mainloop()



""" def cats(cats):
    select = input("What type of cat do u want?")
    response = requests.get(f"https://cataas.com/cat/{select}")
    if response.status_code != 200:
        print("Please hold!")
        return None
    data = response.json()
    print(data)
    return{
        "description": data["tag"]
    }
kitty = cats(input)
for key, value in kitty.items():
    print(f"{key.title()}: {value}") """

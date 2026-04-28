import requests
import tkinter as tk

window = tk.Tk()
window.title("What type of cat do you want?")
window.geometry("400x250")
window.resizable(False, False)



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

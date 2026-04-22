import requests

def cats(color, text):
    response = requests.get(f"https://cataas.com/cat/:tag/says/:text")
    if response.status_code != 200:
        print("Please hold!")
        return None
    data = response.json()
    return{
        "color": data["tag"],
        "text": data["text"]
    }
catss = cats("Orange","Hello")
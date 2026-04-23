import requests

def cats(cats):
    response = requests.get(f"https://cataas.com/cat/:tag")
    if response.status_code != 200:
        print("Please hold!")
        return None
    data = response.json()
    return{
        "color": data["tag"]
    }
catss = cats("Orange")
print(catss)
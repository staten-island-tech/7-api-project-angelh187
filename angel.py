import requests

def cats(cats):
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

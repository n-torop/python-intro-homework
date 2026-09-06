import requests

url="https://api.agify.io/"
params = {"name": "michael"
    }
try:
    response=requests.get(url, params=params)
    response.raise_for_status()
    data=response.json()
    name=data.get("name", 'N/A')
    age=data.get("age", 'N/A')
    birthday=data.get ("birthday", "Not available")
    print (f"Name: {name}\nPredicted age: {age}\nBirthday: {birthday}")


except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")


     


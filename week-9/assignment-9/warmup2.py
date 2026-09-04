import requests

url="https://api.agify.io/"
params = {"name": "michael"
    }
try:
    response=requests.get(url, params=params)
    response.raise_for_status()
    data=response.json()


except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")

try:
    name=data["name"]
    age=data["age"]
    birthday=data["birthday"]
    
except KeyError:
    birthday="Not available"

print (f"Name: {name}\nPredicted age: {age}\nBirthday: {birthday}")
     


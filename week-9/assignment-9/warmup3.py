
import requests
import os
from dotenv import load_dotenv


load_dotenv()

api_key=os.getenv("COUNTRY_API_KEY")

params ={
    "region": "Europe"
}

url= "https://api.restcountries.com/countries/v5"

headers={"Authorization": f"Bearer {api_key}"}

response = requests.get(url, headers=headers, params=params)
data=response.json()

countries=data["data"]["objects"]

for el in countries [:10]:
    print (el["names"]["common"])

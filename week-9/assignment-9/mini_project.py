
import requests
import os
from dotenv import load_dotenv
import json

# load_dotenv()
# api_key=os.getenv("COUNTRY_API_KEY")
# params ={
    
#     "response_fields": "names.common, capital.name, region, population"
# }
# base_url= "https://api.restcountries.com/countries/v5"
# headers={"Authorization": f"Bearer {api_key}"}
# try: 
#     response = requests.get(base_url, headers=headers, params=params)
#     if response.raise_for_status()==200:
#         data=response.json()
#     else:
#         print (f"{response.raise_for_status()}")
# except requests.exceptions.RequestException as e:
#         print ("Error: Could not reach the server. Check your connection and try again.")
    


# ####countries=data["data"]["objects"]
#############Create saved file with data
# with open ("api_data.json", "w") as f:
#     json.dump(data, f, indent=4)
# print ("Data saved!")




with open ("api_data.json", "r") as file:
    data_json=json.load(file)


countries=data_json["data"]["objects"]
parsed_data=[]

for el in countries:
    name=el.get("names", {}).get('common', "Unknown")
    capital=el.get("capital", "N/A")
    region=el.get('region',  "N/A")
    population=el.get('population')
    parsed_data.append({
        "name": name,
        "capital": capital, 
        "region": region, 
        "population": population
    })
    

def ():

while True:
    print ("\n=== Country Explorer ===")
    print ("1. Search by name")
    print ("2. Filter by region\n3. Quit")
    user_input=input ("Choose an option (1-3): ")
    

    


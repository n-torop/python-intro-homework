
import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()
api_key=os.getenv("COUNTRY_API_KEY")
# params ={
    
#     "response_fields": "names.common, capital.name, region, population"
# }
# base_url= "https://api.restcountries.com/countries/v5"

base_url= "https://api.restcountries.com/countries/v5?response_fields=names.official,capitals,region,population"

headers={"Authorization": f"Bearer {api_key}"}
try: 
    # response = requests.get(base_url, headers=headers, params=params)
    response = requests.get(base_url, headers=headers)

    status=response.raise_for_status()
    data=response.json()
except requests.exceptions.HTTPError:
    print (f'HTTP error occured')
except requests.exceptions.RequestException as e:
        print ("Error: Could not reach the server. Check your connection and try again.")
countries=data["data"]["objects"]

parsed_data=[]
for el in countries:
    name=el.get("names", {}).get('official', "Unknown")
    capital=el.get("capital", "N/A")
    region=el.get('region',  "N/A")
    population=el.get('population')
    parsed_data.append({
        "name": name,
        "capital": capital, 
        "region": region, 
        "population": population
    })
    

def search(list_info):
    user_country=input("Search: ").lower()
    matches_found=False
    
    for country in list_info:
        country_name=country.get("name", "")
        if user_country in country_name.lower():
            matches_found=True
            population_result=country.get("population", "N/A")
            capital_result=country.get("capital", "N/A")
            region_result=country.get("region", "N/A")
            print (f"{country_name} -  Capital:  {capital_result} | Region: {region_result} | Population: {population_result}")
    if not matches_found:
        print (f"No matching countries found: {user_country}")

def search_region(list_info):
    user_region=input("Enter region: ").lower()
    filtered_countries=[]
    for country in list_info:
        region_name=country.get("region", "").lower()
        if region_name==user_region:
            filtered_countries.append(country)
        
    population_list=sorted(filtered_countries, key=lambda x: x["population"])
    for el in population_list:
        selected_country=el.get("name", '')
        selected_population=el.get("population", '')
        print (f"Country: {selected_country} | Population: {selected_population}")
    
while True:
    print ("\n=== Country Explorer ===\n1. Search by name\n2. Filter by region\n3. Quit")
    user_input=int(input ("Choose an option (1-3): "))
    if user_input==1:
        search(parsed_data)
    elif user_input==2:
        search_region(parsed_data)
    elif user_input==3:
        break
    

    


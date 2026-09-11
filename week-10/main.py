
import requests
import os
from dotenv import load_dotenv
import json

def get_region_user():
    return input("Enter region: ").strip().lower()

def fetch_data(region): 
    load_dotenv()
    api_key=os.getenv("COUNTRY_API_KEY")
    params ={
        "region": region
    }
    base_url= "https://api.restcountries.com/countries/v5"
    headers={"Authorization": f"Bearer {api_key}"}
    
    try: 
        response = requests.get(base_url, headers=headers, params=params)
        status=response.raise_for_status()
        data=response.json()
        return data
    except requests.exceptions.HTTPError:
        print (f'HTTP error occured')
    except requests.exceptions.RequestException as e:
            print ("Error: Could not reach the server. Check your connection and try again.")

def process_data(data):
    countries=data["data"]["objects"]
    parsed_data=[]

    for el in countries:
        name_common=el.get ("names", {}).get("common", "Unknown")
        name_official=el.get ("names", {}).get("official", "Unknown")
        capitals=el.get("capitals", [])
        if capitals and isinstance (capitals, list) and len(capitals)>0:
            capital=capitals[0].get("name", "Unknown")
        else: 
            capital="Unknown"
        population=el.get('population', {})
        cars=el.get("cars", {}).get("driving_side", {})
        currencies=el.get("currency", [])
        if currencies and isinstance (currencies, list) and len(currencies)>0:
            currency=currencies[0].get("name", {})
        else:
            currency="N/A"
        date=el.get("date", {}).get("start_of_week", {})
        description=el.get ("descriptions", {}).get("short", {})
        government=el.get("government_type", {})
        languages=el.get("languages", {})
        if languages and isinstance (languages, list) and len(languages)>0:
            language=languages[0].get("name", {})
            lang_list=[]
            for lang in languages:
                name_lang=lang.get("name", "Unknown")
                lang_list.append(name_lang)
        timezone=el.get("timezones", {})
        all_memberships=el.get("memberships", {})
        selected_membership=[k for k, v in all_memberships.items() if v==True]
        if not selected_membership:
            selected_membership=["No memberships found"]

        parsed_data.append({
            "name_common": name_common, 
            "name_official": name_official, 
            "capital": capital, 
            "population": population, 
            "cars": cars, 
            "currency": currency, 
            "date": date, 
            "description": description, 
            "government": government, 
            "languages": lang_list, 
            "timezone": timezone, 
            "all_memberships": all_memberships, 
            "selected_membership": selected_membership
        })
    return parsed_data

    
def filter_by_membership(list_info):
    membership_menu="1. African Union\n2. Arab League\n3. Asean\n4. Brics\n5. Common Wealth\n6. EU\n7. Eurozone\n8. G20\n9. G7\n10. NATO\n11.OECD\n12. OPEC\n13. Schengen\n14. UN\n"
    print (membership_menu)
    user_input=input("Enter choice(s) separated by space(1-14): ").split()
    
    menu={
        "1": 'african_union', 
        "2": 'arab_league', 
        "3": 'asean',
        "4": 'brics', 
        "5": 'commonwealth', 
        "6": 'eu', 
        "7": "eurozone", 
        '8': 'g20', 
        '9': 'g7',
        '10': 'nato',
        '11': 'oecd', 
        '12': 'opec', 
        '13': 'schengen',
        '14': 'un'
    }
    
    user_choice_list=[] 
    for choice in user_input: #create a list of chosen groups
        if choice in menu:
            user_choice_list.append(menu[choice]) 
    if not user_choice_list:
        print ("No valid input was made")
        return []
    print (f'Searching for {user_choice_list}...')
    
    
    results=[]
    membership_list=[] #general list
    for country in list_info:
        country_res=country.get("name_common", {})
        membership_list=country.get("all_memberships", {})
        checks=[membership_list.get(key, False) for key in user_choice_list]
        
        for elem in checks:
            if elem==True:
                results.append(country_res)
    
    if len(results)>0:
        print (f"Found {len(results)} match(es).")
        print (f'The following countries are members: {", ".join(results)}')
        return results
    elif len(results)==0:
        print ("No match was found ")
        return []


def search_description(list_info):
    filtered_countries=[]
    for country in list_info:
        description=country.get("description", "")
        country_name=country.get("name_common", '')
        population=country.get("population", '')
        government=country.get("government", '')

        filtered_countries.append({
            'country_name': country_name,
            "description": description,
            "population": population, 
            "government": government
        })   
    for el in filtered_countries:
        selected_country=el.get("country_name", '')
        selected_description=el.get("description", '')
        selected_population=el.get("population", '')
        selected_governement=el.get("government", '')
        print (f"Country: {selected_country}\nDescription: {selected_description} | Population: {selected_population} | Government: {selected_governement}\n")
    return filtered_countries
   

def main():
    while True:
        print ("\n=== Country Explorer (by Region) ===\n1. Get general country information\n2. Filter by membership\n3. Quit\n")
        
        raw=input ("Choose an option (1-3): ")
        try:
            user_input=int(raw)
        except ValueError:
            print (f'"{raw}" is not a valid number.')
            continue

        if user_input==3:
            print ("Goodbye!")
            break
        if user_input not in (1, 2):
            print ("Invalid input. Please enter 1, 2, or 3.")
            continue

        user_region=get_region_user()
        data=fetch_data(user_region) 
        new_l=process_data(data)
        
        if user_input==1:
            description_res=search_description(new_l)
        elif user_input==2:
            membership_results=filter_by_membership(new_l)
        
if __name__=="__main__":
    main()


import requests

def fetch_api():
    url="https://thisurldoesnotexist.example.com"
    params={"fields": "some_field1, field_2"}
    try:
        response=requests.get(url, params=params)
        response.raise_for_status()
        
        data=response.json()
        return data
        
       
    except requests.exceptions.RequestException as e:
        print (f"Error: Could not reach the server. {e}")
        return []
    except requests.exceptions.JSONDecodeError:
        print("Error: Response is not valid JSON.")
        return []
    
fetch_api()
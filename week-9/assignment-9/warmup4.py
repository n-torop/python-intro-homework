import requests



def fetch_api():
    url="https://thisurldoesnotexist.example.com"
    params={"fields": "some_field1, field_2"}
    try:
        response=requests.get(url, params=params)
        if response.raise_for_status()==200:
            data=response.json()
            return data
        else:
            return f"{response.raise_for_status()}"
       
    except requests.exceptions.RequestException as e:
        print ("Error: Could not reach the server. Check your connection and try again.")
        return []
    except requests.exceptions.JSONDecodeError:
        print("Error: Response is not valid JSON.")
        return []
    
fetch_api()
import requests

url = "https://api.agify.io/?name=michael"

response=requests.get(url)
if response.status_code!=200:

    print ("Something went wrong. Status code:", response.status_code)
else:
    print (f"Status code: {response.status_code}")
    data=response.json()
    print (f'Response: {data}')
    # print (f'Response: {data["name"], data["age"], data["count"]}')
import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv('API_KEY')

def fetch_data(animal_name):
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return []


print(fetch_data("Fox"))

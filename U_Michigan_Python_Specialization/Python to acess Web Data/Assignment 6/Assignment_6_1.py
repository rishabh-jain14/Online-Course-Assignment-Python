import urllib.parse, urllib.request, urllib.error
import json
import sys

url = input("Enter URL : ")
if len(url) < 1:
    sys.exit(0)
data = urllib.request.urlopen(url).read().decode()
js = json.loads(data)
if len(js) < 1:
    sys.exit(0)
sum_c = 0
for c in js["comments"] :
    sum_c += int(c["count"])
print(sum_c)    
    

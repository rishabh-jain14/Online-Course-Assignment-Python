import urllib.parse, urllib.request, urllib.error
import json
import sys

locat = input("Enter Location : ")
if len(locat) < 1:
    sys.exit(0)
serviceurl = "http://py4e-data.dr-chuck.net/json?"
url = serviceurl + urllib.parse.urlencode({"key" : 42 , "address" : locat})
uh= urllib.request.urlopen(url)
data = uh.read().decode()
js = json.loads(data)
print(js["results"][0]["place_id"])
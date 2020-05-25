import urllib.request , urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import re
import sys

url = input("Enter : ")
if len(url) < 1:
    sys.exit(0)
data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)
sum_count = 0
counts = tree.findall('.//count')
for count in counts :
    sum_count += int(count.text)
print(sum_count)
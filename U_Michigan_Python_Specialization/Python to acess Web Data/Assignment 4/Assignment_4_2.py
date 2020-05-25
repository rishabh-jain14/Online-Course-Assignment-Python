import re
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

url = input("Enter URL - ")
count = int(input("Enter Count - "))
position = int(input("Enter Position - "))
n = 0
while n < count :
    data = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(data, 'html.parser')
    tags = soup('a')
    url = tags[position-1].get('href' , None)
    x = re.findall('.+by_(.+)\..+' , url)
    n += 1
print(x[0])
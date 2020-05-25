from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error


url = input()
data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data , 'html.parser')

tags = soup('span')
_sum = 0
for tag in tags:
    _sum += int((tag.contents[0]))
print(_sum)
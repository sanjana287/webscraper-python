from bs4 import BeautifulSoup
import urllib.request
import re
import pprint
url = "https://en.wikipedia.org/wiki/Coronavirus"
try:
    page = urllib.request.urlopen(url)
except:
    print("An error occured.")
soup = BeautifulSoup(page, 'html.parser')
regex = re.compile('^tocsection-')
content_lis = soup.find_all('li', {'class' : regex})
content = []
for li in content_lis:
    content.append(li.getText())
with open('content.txt', 'w',encoding="utf-8") as f:
    for i in content:
        output= pprint.pformat(i)
        f.write(output)

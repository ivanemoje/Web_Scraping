import urllib2
from bs4 import BeautifulSoup

page=urllib2.urlopen('http://www.4icu.org/Africa')
soup = BeautifulSoup(page, 'html.parser')
str="http://www.4icu.org"
data=[]
for link in soup.find_all('a'):
   data.append(str+link.get('href'))
data = [d.replace('/index.html', "/") for d in data]
africa=data[40:92] 

for i in range(len(africa)):
    link=africa[i]
    page=urllib2.urlopen("'"+link+"'")
    soup=BeautifulSoup(page, 'html.parser')
    for tr in soup.find_all('tr')[1:]:
        tds = tr.find_all('td')
        print tds[1].text
print "complete"
        #unis.append(tds[1].text)

#print unis

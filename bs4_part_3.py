import urllib2
from bs4 import BeautifulSoup

#open page and parse it for use to get links for all countries
page=urllib2.urlopen('http://www.4icu.org/Africa')
soup = BeautifulSoup(page, 'html.parser')

#string that will be appended to hyperlinks of countries
str="http://www.4icu.org"

#array list that will hold links
data=[]

#for loop to obtain links for all countries
for link in soup.find_all('a'):
   data.append(str+link.get('href'))
data = [d.replace('/index.html', "/") for d in data]

#new array that obtains links from africa -- rudimentary method
africa=data[40:92] 

#failed attempt to iterate over each link and add to array/insert into db
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

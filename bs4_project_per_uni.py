import urllib2
from bs4 import BeautifulSoup


#open page for algeria
page=urllib2.urlopen('http://www.4icu.org/dz/')

#parse page using bs4
soup = BeautifulSoup(page, 'html.parser')

#print uni_names
for tr in soup.find_all('tr')[1:]:
    tds = tr.find_all('td')
    print tds[1].text
   

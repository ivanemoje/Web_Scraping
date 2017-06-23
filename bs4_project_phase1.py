import urllib2
from bs4 import BeautifulSoup

quote_page='http://www.4icu.org/dz/'
page=urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find_all('a', {'class': 'lead'})
print name_box

import urllib2
from bs4 import BeautifulSoup

quote_page='http://www.4icu.org/dz/'
page=urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')
name_box_s = soup.find('a', {'class': 'lead'}).get_text()
print name_box_s
#this below works but produces
#name_box = soup.find_all('a', {'class': 'lead'})
#print name_box
datasets=[]
for row in soup.find_all("a")[1:]:
    dataset = soup.find('a', {'class': 'lead'}).get_text()
    datasets.append(dataset)
#print  datasets
for row2 in datasets:
    for field in row:
        format(field[0])

print datasets

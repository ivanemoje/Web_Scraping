
import urllib2
from bs4 import BeautifulSoup
import pymysql

#open connection and create cursor object
conn=pymysql.connect(host='localhost', port=3306, user='root', passwd='1234',db='4icu')
cur=conn.cursor()

#open url and parse to obtain all hyperlinks
page=urllib2.urlopen('http://www.4icu.org/Africa')
soup = BeautifulSoup(page, 'html.parser')

#string to be appended to each hyperlink
str="http://www.4icu.org"

#empty array list to hold hyperlinks
data=[]

#obtain all links, append to array list
for link in soup.find_all('a'):
   data.append(str+link.get('href'))
 
data = [d.replace('/index.html', "/") for d in data]

#select hyperlinks for Africa
africa=data[40:92] 

#loop data for each country and insert into table
for i in range(len(africa)):
    link=africa[i]
    page=urllib2.urlopen(link)
    print page
    soup=BeautifulSoup(page, 'html.parser')
    
    #to obtain country name
    name_box=soup.find('h1')
    country_full=name_box.text.strip()
    country=country_full[20:]
    country = ''.join(country)
    
    #to obtain universities per country and insert into database
    for tr in soup.find_all('tr')[1:]:
        tds = tr.find_all('td')
        params=[tds[1].text, country]
        cur.execute("""INSERT INTO university_africa VALUES (%s,%s);""",params)
      #write to csv file
        with open("/home/ivan/Documents/uni_csv.csv", "a") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([params, datetime.now()])
    conn.commit() 
print "complete"




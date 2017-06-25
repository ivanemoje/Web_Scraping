import urllib2
from bs4 import BeautifulSoup
import pymysql

#open connection
conn=pymysql.connect(host='localhost', port=3306, user='root', passwd='1234',db='mysql')

#cursor
cur=conn.cursor()
#open page
page=urllib2.urlopen('http://www.4icu.org/dz/')

#parse page using bs4
soup = BeautifulSoup(page, 'html.parser')

#print uni_names & insert into db
for tr in soup.find_all('tr')[1:]:
    tds = tr.find_all('td')
    print tds[1].text
    cur.execute("""INSERT INTO university_algeria2 VALUES (%s);""",tds[1].text)
conn.commit()

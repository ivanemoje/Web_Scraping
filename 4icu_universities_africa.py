#Extract names of all universities in Africa using bs4
#Generate CSV, PDF of stored data from mySQL


import urllib2
from bs4 import BeautifulSoup
import pymysql
import csv
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Spacer, Table, TableStyle

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
    conn.commit() 
print "complete"

#Query Data
cur.execute("""SELECT * FROM uni_test';""")
universities=cur.fetchall()
print data

#write into CSV
c = csv.writer(open("/uni_csv.csv","wb"))
for row in data:
    c.writerow(row)

#write into PDF

doc = SimpleDocTemplate("uni_pdf.pdf", pagesize=letter, showBoundary=1)
parts = []
#populate table in pdf with data from mysql
table = Table(data, [5 * inch, 0.5 * inch, inch])
parts.append(table)
parts.append(Spacer(1, 1.5 * inch))
#build doc
doc.build(parts)

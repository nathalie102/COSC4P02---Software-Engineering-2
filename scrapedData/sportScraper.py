# importing the libraries
from bs4 import BeautifulSoup
import requests

#Santiago Franco

def getGenInfo(html_content):
    soup = BeautifulSoup(html_content, "lxml")

    general = soup.find('div',{"class":"rich-text-block-4 w-richtext"})

    generalInfo = ''
    for i in general:
        if str(i.text) != "General Description":
            generalInfo += str(i.text).replace(u'Â', u' ')
    f1.write(str(generalInfo.encode('ascii', 'ignore').decode("utf-8"))+'\n')

def getTableData(html_content,tablenum):
    soup = BeautifulSoup(html_content, "lxml")
    general = soup.find('div',{"class":tablenum})
    count = 1
    table = ''
    for i in general:
        if count == 1:
            table += "%"+str(i.text)+"%"+"\n"
            count+=1
        elif count < 6:
            table += str(i.text)+";"
            count +=1
        elif count == 6:
            table += str(i.text)+"\n"
            count+=1
        elif count < 11:
            if str(i.text):
                table += str(i.text)+";"
            else:
                table += str("*;")  
            count+=1
        elif count == 11:
            if str(i.text):
                table += str(i.text)+"\n"
            else:
                table += str("*;")+"\n"  
            count = 7

    f1.write(str(table.encode('ascii', 'ignore').decode("utf-8")))

def getAlumni(html_content):
    soup = BeautifulSoup(html_content, "lxml")
    a1 = soup.find('div',{"class":"section-9"})

    for i in a1:
        if i.has_attr('href'):
            f1.write(str(i['href'].encode('ascii', 'ignore').decode("utf-8"))+"\n")
        if i.find('div',{"class":"text-block-33"}):
            f1.write(str(i.text.encode('ascii', 'ignore').decode("utf-8"))+"\n")
    f1.write("\r\n")



f = open('sportScraper.txt','r')
f1 = open('sportInfo.txt','a')


count = 1
for url in f:
    # Make a GET request to fetch the raw HTML content

    html= requests.get(str(url))
    html.encoding = html.apparent_encoding
    html_content = html.text

    sporturl = url.split("/")
    sportname = sporturl[len(sporturl)-1]
    f1.write(str(count))
    f1.write("\r\n")
    f1.write(sportname.encode('ascii', 'ignore').decode("utf-8")+"\n")
    getGenInfo(html_content)
    getTableData(html_content,"first-table")
    getTableData(html_content,"second-table")
    getTableData(html_content,"third-table")
    getAlumni(html_content)
    count += 1
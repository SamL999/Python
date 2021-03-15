from bs4 import BeautifulSoup as bs
import requests
import csv

url = "http://www.w3schools.com/html/html_media.asp"
csvfile = "videoformat.csv"
r = requests.get(url)
r.encoding = "utf8"
soup = bs(r.text, "lxml")
tag_table = soup.find(class_="w3-table-all")
rows = tag_table.findAll("tr")

with open (csvfile, "w", newline="", encoding="utf-8") as fp :
    writer = csv.writer(fp)    
    for row in rows :
        rowlist = []
        for cell in row.findAll(["td","th"]):
            rowlist.append(cell.get_text().replace("\n","").replace("\r",""))
        writer.writerow(rowlist)



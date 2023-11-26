import requests, json
from bs4 import BeautifulSoup
from lxml import etree
path = "/home/radu/Projects/workspace/proiect-compari"
dictionar = {
    "titlu" : [],
    "pret" : [],
    "site" : []
}
cautare = input("Ce cautati:")
url = f"https://www.compari.ro/CategorySearch.php?st={cautare}"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
dom = etree.HTML(str(soup))
URLcautare = (dom.xpath('//*[@id="normal-product-list"]/div/div/div[1]/div[2]/div[1]/h2/a/@href'))
url2 = URLcautare[0]

page1 = requests.get(url2)
soup1 = BeautifulSoup(page1.content, "html.parser")
nr = 0

titles = [list.find('h4') for list in soup1.find_all('div', class_="col-name offer-name")]
preturi = [list.find('span') for list in soup1.find_all('div', class_="row-price")]
sites = [list.find('meta')["content"] for list in soup1.find_all('div', class_="col-button button-box")]

for titlu in titles:
    title = titles[nr].get_text()
    dictionar['titlu'].append(title)
    nr += 1

nr = 0
for pret in preturi:
    pret = preturi[nr].get_text()
    dictionar['pret'].append(pret)
    nr += 1

nr = 0
for site in sites:
    site = sites[nr]
    dictionar['site'].append(site)
    nr += 1

with open(f"{path}/anunturi.json", "a") as f:
    json.dump(dictionar, f)
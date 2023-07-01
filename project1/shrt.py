import json
import time
from copy import deepcopy
from urllib import response
import requests
from post import blogpost
from bs4 import BeautifulSoup
import urlmaker
import re

start = time.time()
shortenurl = "https://radu.ovh/api/short" #link to sorten the URL

titles = 3              #specify how many titles you want!


#defining class for OOP
class getnews(object):
    def __init__(self, title, source, link):
        self.title = title
        self.source = source
        self.link = link

#defining a function to get links and shorten the URL
def rezulta(link):
    reqs = requests.get(link)
    soup = BeautifulSoup(reqs.content, 'html.parser')
    linkz = soup.find_all("a", attrs={'rel': 'nofollow'})
    clean = re.findall(urlmaker.URL_REGEX, f"{linkz}") # getting the real url not the newsnow.co.uk redirect.
    payload = {'URL': clean} # setting the payload for the API
    response = requests.get(shortenurl, payload)
    resp = response.text
    json_data = json.loads(resp)
    short = json_data['ShortURL'] # getting the shortened URL
    blogpost(short)
    return(short)


# def get_text(link):

#     page = requests.get(link)
#     soup = BeautifulSoup(page.text, "lxml")
#     text = [list.find('h2') for list in soup.find_all('div', class_='hl', limit=5)]
#     print(text)


def scraper():
    donelink = [] #dictionary for short url's
    titluri = [] #dictionary for objects.
    lista = [] # list to dump in json file.

    url = "https://www.newsnow.co.uk/h/Business+&+Finance/Cryptocurrencies?type=ln"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")

    title = [list.find('a', class_="hll") for list in soup.find_all('div', class_="hl", limit=titles)] # getting titles !
    source = [list.find('span', class_="src src-part") for list in soup.find_all('div', class_="hl", limit=titles)] # getting sources
    links = [list.find('a', href=True)['href'] for list in soup.find_all('div', class_="hl", limit=titles)] # getting links

    for link in links:
        links = rezulta(link) # using function to get shortened URL
        donelink.append(links)

    for index in range(titles):
        try:
            titlu = title[index].get_text() # getting title from object.
            sursa = source[index].get_text() # getting source from object
            news = getnews(titlu, sursa, donelink[index]) #getting the title + source + link
        except AttributeError as e:
            print("error")
        titluri.append(news)

    for news in titluri:
        stire = { #making a dictionary for json file dump.
            "titlu": news.title,
            "sursa": news.source,
            "link": news.link
                }
        lista.append(deepcopy(stire))
#    print(lista)
    return lista
lista = scraper()
with open('/config/workspace/project1/news.json', 'w') as f:
    json.dump(lista, f)
end = time.time()
print(f"it took {end - start} seconds")


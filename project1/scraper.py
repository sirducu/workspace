import requests
from bs4 import BeautifulSoup
from lxml import etree

FIREFOX_LINUX = {
    "Accept": "text/html, application/xhtml+xml, application/xml;q=0.9, "
              "*/*;q=0.8",
    "Accept-Language": "en-GB, en;q=0.5",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) "
                  "Gecko/20100101 Firefox/60.0",
}



paragrafe = 2
def beincrypto(link): #BeInCrypto
    page = requests.get(link, headers=FIREFOX_LINUX)
    soup = BeautifulSoup(page.text, "lxml")
    title = [list.find('p') for list in soup.find_all('div', class_="entry-content", limit=paragrafe)]
    for titluri in range(1):
        titlu = title[titluri].get_text()
        titlu = titlu.split('.', 1)[0]
    return titlu


def cointelegraph(link): #Cointelegraph
    page = requests.get(link, headers=FIREFOX_LINUX)
    soup = BeautifulSoup(page.text, "lxml")
    title = [list.find('p') for list in soup.find_all('div', class_="post__content-wrapper", limit=paragrafe)]
    for titluri in range(1):
        titlu = title[titluri].get_text()
        titlu = titlu.split('.', 1)[0]
    return titlu


def themotleyfool(link): #The Motley Fool
    page = requests.get(link, headers=FIREFOX_LINUX)
    soup = BeautifulSoup(page.text, "lxml")
    title = [list.find('h2') for list in soup.find_all('div', class_="foolcom-grid-content-sidebar mt-36px", limit=paragrafe)]
    for titluri in range(1):
        titlu = title[titluri].get_text()
        titlu = titlu.split('.', 1)[0]
    return titlu


def fxstreet(link): # FX Street
    page = requests.get(link, headers=FIREFOX_LINUX)
    soup = BeautifulSoup(page.text, "lxml")
    title = [list.find('p') for list in soup.find_all('div', class_="fxs_article_content", limit=paragrafe)]
    for titluri in range(1):
        titlu = title[titluri].get_text()
        titlu = titlu.split('.', 1)[0]
    return titlu


def cryptopotato(link): #CryptoPotato.com
    page = requests.get(link, headers=FIREFOX_LINUX)
    soup = BeautifulSoup(page.text, "lxml")
    title = [list.find('p') for list in soup.find_all('div', class_="entry-post", limit=paragrafe)]
    for titluri in range(1):
        titlu = title[titluri].get_text()
        titlu = titlu.split('.', 1)[0]
    return titlu

def decrypt(link): #Decrypt
    page = requests.get(link, headers=FIREFOX_LINUX)
    soup = BeautifulSoup(page.text, "lxml")
    title = [list.find('p') for list in soup.find_all('div', class_="grid grid-cols-1 md:grid-cols-8 unreset post-content md:pb-20", limit=paragrafe)]
    for titluri in range(1):
        titlu = title[titluri].get_text()
        titlu = titlu.split('.', 1)[0]
    return titlu

def zycrypto(link): #ZyCrypto
    page = requests.get(link, headers=FIREFOX_LINUX)
    soup = BeautifulSoup(page.text, "lxml")
    title = [list.find('p').find_next_sibling('p').find_next_sibling('p') for list in soup.find_all('div', class_="td-post-content tagdiv-type", limit=paragrafe)]
    for titluri in range(1):
        titlu = title[titluri].get_text()
        titlu = titlu.split('.', 1)[0]
    return titlu

def cryptopolitan(link): #Cryptopolitan
    page = requests.get(link, headers=FIREFOX_LINUX)
    soup = BeautifulSoup(page.text, "lxml")
    title = [list.find('p') for list in soup.find_all('div', class_="entry-content", limit=paragrafe)]
    for titluri in range(1):
        titlu = title[titluri].get_text()
        titlu = titlu.split('.', 1)[0]
    return titlu

def bitcoinworld(link): #BitcoinWorld
    page = requests.get(link, headers=FIREFOX_LINUX)
    soup = BeautifulSoup(page.text, "lxml")
    title = [list.find('p') for list in soup.find_all('div', class_="main-wrap container", limit=paragrafe)]
    for titluri in range(1):
        titlu = title[titluri].get_text()
        titlu = titlu.split('.', 1)[0]
    return titlu

def cryptoglobe(link): #CryptoGlobe
    page = requests.get(link, headers=FIREFOX_LINUX)
    soup = BeautifulSoup(page.text, "lxml")
    title = [list.find('p') for list in soup.find_all('div', class_="article-body", limit=paragrafe)]
    for titluri in range(1):
        titlu = title[titluri].get_text()
        titlu = titlu.split('.', 1)[0]
    return titlu

def cryptodaily(link): #CryptoDaily
    page = requests.get(link, headers=FIREFOX_LINUX)
    soup = BeautifulSoup(page.text, "lxml")
    title = [list.find('p') for list in soup.find_all('div', class_="news-content news-post-main-content", limit=paragrafe)]
    for titluri in range(1):
        titlu = title[titluri].get_text()
        titlu = titlu.split('.', 1)[0]
    return titlu

def coingape(link): #Coingape
    page = requests.get(link, headers=FIREFOX_LINUX)
    soup = BeautifulSoup(page.text, "lxml")
    title = [list.find('span') for list in soup.find_all('div', class_="Atcs", limit=paragrafe)]
    for titluri in range(1):
        titlu = title[titluri].get_text()
        titlu = titlu.split('.', 1)[0]
    return titlu

def theblock(link): #The Block
    page = requests.get(link, headers=FIREFOX_LINUX)
    soup = BeautifulSoup(page.text, "lxml")
    title = [list.find('h1') for list in soup.find_all('div', class_="articleContent", limit=paragrafe)]
    for titluri in range(1):
        titlu = title[titluri].get_text()
        titlu = titlu.split('.', 1)[0]
    return titlu

def bitcoincom(link): #Bitcoin.com
    page = requests.get(link, headers=FIREFOX_LINUX)
    soup = BeautifulSoup(page.text, "lxml")
    texte = soup.find_all('meta', limit=4)
    lista1 = []
    for titlu in texte:
        lista1.append(titlu.get("content"))
    titlu = lista1[3]
    titlu = titlu.split('.', 1)[0]
    return titlu

def utoday(link): #U.Today
    page = requests.get(link, headers=FIREFOX_LINUX)
    soup = BeautifulSoup(page.text, "lxml")
    title = [list.find('p') for list in soup.find_all('div', class_="article__content", limit=paragrafe)]
    for titluri in range(1):
        titlu = title[titluri].get_text()
        titlu = titlu.split('.', 1)[0]
    return titlu

def legitng(link): #Legit NG
    page = requests.get(link, headers=FIREFOX_LINUX)
    soup = BeautifulSoup(page.text, "lxml")
    title = [list.find('figcaption') for list in soup.find_all('div', class_="post__content", limit=paragrafe)]
    for titluri in range(1):
        titlu = title[titluri].get_text()
        titlu = titlu.split('.', 1)[0]
    return titlu
    
def thepunch(link): #The Punch
    page = requests.get(link, headers=FIREFOX_LINUX)
    soup = BeautifulSoup(page.text, "lxml")
    title = [list.find('p') for list in soup.find_all('div', class_="post-content", limit=paragrafe)]
    for titluri in range(1):
        titlu = title[titluri].get_text()
        titlu = titlu.split('.', 1)[0]
    return titlu

def dailycoin(link): #DailyCoin
    page = requests.get(link, headers=FIREFOX_LINUX)
    soup = BeautifulSoup(page.text, "lxml")
    title = [list.find('p') for list in soup.find_all('div', class_="mkd-post-text", limit=paragrafe)]
    for titluri in range(1):
        titlu = title[titluri].get_text()
        titlu = titlu.split('.', 1)[0]
    return titlu

def fxstreet2(link): #FXstreet
    page = requests.get(link, headers=FIREFOX_LINUX)
    soup = BeautifulSoup(page.text, "lxml")
    title = [list.find('p') for list in soup.find_all('div', class_="fxs_article_content", limit=paragrafe)]
    for titluri in range(1):
        titlu = title[titluri].get_text()
        titlu = titlu.split('.', 1)[0]
    return titlu

def rferl(link): #Radio Free Europe
    page = requests.get(link, headers=FIREFOX_LINUX)
    soup = BeautifulSoup(page.text, "lxml")
    title = [list.find('p') for list in soup.find_all('div', class_="intro m-t-md", limit=paragrafe)]
    for titluri in range(1):
        titlu = title[titluri].get_text()
        titlu = titlu.split('.', 1)[0]
    return titlu

def ethnews(link): #ETHNews.com
    page = requests.get(link, headers=FIREFOX_LINUX)
    soup = BeautifulSoup(page.text, "lxml")
    title = [list.find('strong') for list in soup.find_all('div', class_="td_block_wrap tdb_single_content tdi_74 td-pb-border-top td_block_template_1 td-post-content tagdiv-type", limit=paragrafe)]
    for titluri in range(1):
        titlu = title[titluri].get_text()
        titlu = titlu.split('.', 1)[0]
    return titlu

#insidebitcoins("https://www.ethnews.com/countdown-to-ripple-lawsuit-judgment-why-july-1-2023-holds-the-key-to-xrps-fate/")

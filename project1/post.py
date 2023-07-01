import requests
from bs4 import BeautifulSoup
titles = 15
def scraper():
    donelink = [] #dictionary for short url's
    titluri = [] #dictionary for objects.
    lista = [] # list to dump in json file.

    url = "https://www.newsnow.co.uk/h/Business+&+Finance/Cryptocurrencies?type=ln"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")

    title = [list.find('a', class_="hll") for list in soup.find_all('div', class_="hl", limit=titles)] # getting titles !
    source = [list.find('span', class_="src src-part") for list in soup.find_all('div', class_="hl", limit=titles)] # getting sources
    for index in range(titles):
        try:
            titlu = title[index].get_text() # getting title from object.
            sursa = source[index].get_text() # getting source from object
        except AttributeError as e:
            print("error")
        print(titlu, sursa)
scraper()


# def blogpost(link):

#     FIREFOX_LINUX = {
#     "Accept": "text/html, application/xhtml+xml, application/xml;q=0.9, "
#               "*/*;q=0.8",
#     "Accept-Language": "en-GB, en;q=0.5",
#     "Connection": "keep-alive",
#     "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) "
#                   "Gecko/20100101 Firefox/60.0",
# }

#     response_API = requests.get(link, headers=FIREFOX_LINUX)
#     data = response_API.text

# # using the BeautifulSoup module
#     soup = BeautifulSoup(response_API.text, 'html.parser')

# # displaying the title
#     for title in soup.find_all('title'):
#         title = title.get_text()
#         if "Cloudflare" in title:
#             title=""
#         else:
#             title=title
#     listpara = []
#     for tag in soup.find_all("p", limit=1):
#         paragraf = tag.get_text(separator=" ")
#         if "Cloudflare" in paragraf or "This website" in paragraf:
#             paragraf = ""
#         else:
#             paragraf = f"{paragraf}\n\n"
#             listpara.extend(paragraf)
#     news = ''.join(listpara)
#     print(title)
#     print(news)
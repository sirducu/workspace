import requests, json
from bs4 import BeautifulSoup



def get_links():
    r=requests.get('http://51.161.134.159:8080/crypto')
    all_news = r.json()
    links = []
    sources = []
    for part in all_news:
        link = part['link']
        source = part['sursa']
        sources.append(source)
        links.append(link)
    return links, sources

links, sources = get_links()
print(links, sources)
def get_news(link):

    FIREFOX_LINUX = {
    "Accept": "text/html, application/xhtml+xml, application/xml;q=0.9, "
              "*/*;q=0.8",
    "Accept-Language": "en-GB, en;q=0.5",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) "
                  "Gecko/20100101 Firefox/60.0",
}

    response_API = requests.get(link, headers=FIREFOX_LINUX)
    data = response_API.text

# using the BeautifulSoup module
    soup = BeautifulSoup(response_API.text, 'html.parser')

# displaying the title
    for title in soup.find_all('title'):
        title = title.get_text()
        if "Cloudflare" in title:
            title=""
        else:
            title=title
    listpara = []
    for tag in soup.find_all("p", limit=1):
        paragraf = tag.get_text(separator=" ")
        if "Cloudflare" in paragraf or "This website" in paragraf:
            paragraf = ""
        else:
            paragraf = f"{paragraf}\n\n"
            listpara.extend(paragraf)
    news = ''.join(listpara)
    print(news)

for link, source in zip(links,sources):
    get_news(link)
    print(source)
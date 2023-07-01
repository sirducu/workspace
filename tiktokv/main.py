import requests, json

def get_news():
    r=requests.get('http://51.161.134.159:8081/news')
    all_news = r.json()
    return all_news

allnews = get_news()
titlu = allnews['titlu']
sursa = allnews['sursa']
link = allnews['link']
news = allnews['stire']

print(sursa)
print(link)
print(titlu)
print(news)

# r = requests.get('http://radu.ovh:8080/crypto')
# all = r.json()
# print(all)


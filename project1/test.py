import requests, json
from scraper import *

def get_links():
    r=requests.get('http://51.161.134.159:8080/crypto')
    all_news = r.json()
    
    link = all_news[0]['link']
    sursa = all_news[0]['sursa']
    titlu = all_news[0]['titlu']
    return link, sursa, titlu

sursed = {'BeInCrypto': beincrypto, 'Cointelegraph': cointelegraph, 'The Motley Fool': themotleyfool, 'FX Street': fxstreet, 'CryptoPotato.com': cryptopotato, 'Decrypt': decrypt, 'ZyCrypto': zycrypto, 'Cryptopolitan': cryptopolitan,
'BitcoinWorld': bitcoinworld, 'Radio Free Europe': rferl, 'ETHNews.com': ethnews, 'FXstreet': fxstreet2, 'CryptoGlobe': cryptoglobe, 'CryptoDaily': cryptodaily, 'Coingape': coingape, 'The Block': theblock, 'Bitcoin.com': bitcoincom, 'U.Today': utoday, 'Legit NG': legitng, 'The Punch': thepunch, 'DailyCoin': dailycoin}


interzis = ["'", ",", ":", ";", "%", "$", "&"]


def get_news(link, sursa):
    for key,value in sursed.items():
        if f'{sursa}' in key:
            news = value(link)
            break
        else:
            news = f"nu avem scraper pentru {sursa}"
    return news

def split(word):
    lista = []
    for letter in word:
        if letter in interzis:
            letter = ""
        else: 
            lista.append(letter)
    word = ''.join(lista)
    return word


def splitter(n, s):
    pieces = s.split()
    return (" ".join(pieces[i:i+n]) for i in range(0, len(pieces), n))

link, sursa, titlu = get_links()
news = get_news(link, sursa)
link = link.replace("https://", "")

def apireturn():
    link, sursa, titlu = get_links()
    news = get_news(link, sursa)
    dict1 = {
        'titlu': titlu,
        'sursa': sursa,
        'link': link,
        'stire': news
    }
    print(dict1)
    return dict1

    


# inp = f"{titlu} ."
# length = 35
# new_input = split_txt_into_multi_lines(inp,length)
# speech = gTTS(text=inp, lang=language, tld='com.au', slow=False)
# speech.save(f"/config/python/audio/news{nr}.mp3")
# print(new_input, link)
#text(new_input, link, f"/config/python/audio/news{nr}.mp3", f"/config/python/result/news{nr}.mp4")

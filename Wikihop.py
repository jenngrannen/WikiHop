import requests
from bs4 import BeautifulSoup, SoupStrainer

def readLinks(url):
    result = requests.get(url)
    c = result.content
    bodySection = SoupStrainer(id="mw-content-text")
    soup = BeautifulSoup(c, "html.parser", parse_only=bodySection)
    #bodySection = soup.select("body > div:nth-of-type(3) > div:nth-of-type(3) > div:nth-of-type(4) > div")
    childrenList = []

    for a in soup.find_all('a', href=True):
        childrenList.append(a['href'])

    childrenListFinal = [l for l in childrenList if "/wiki/" in l]
    childrenListFinal = [l for l in childrenListFinal if "action=edit" not in l]
    return childrenListFinal

def convertLinkList(list):
    result = [l for l in list if (".png" and ".svg" and ".jpg" and ":") not in l ]
    return result

print(convertLinkList(readLinks("https://en.wikipedia.org/wiki/Manu_propria")))

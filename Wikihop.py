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
    return childrenList

def convertLinkList(list):
    result = [l for l in list if (".png" and ".svg" and ".jpg" and ":") not in l ]
    result = [l for l in result if "/wiki/" in l]
    result = [l for l in result if "action=edit" not in l]
    return result

def rewriteLinkList(list):
    result = []
    for l in list:
        result.append("https://en.wikipedia.org" + l)
    return result

filteredList = convertLinkList(readLinks("https://en.wikipedia.org/wiki/Manu_propria"))
print(rewriteLinkList(filteredList))

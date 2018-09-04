import requests
from bs4 import BeautifulSoup, SoupStrainer

def readLinks(url):
    result = requests.get(url)
    c = result.content
    bodySection = SoupStrainer(id="mw-content-text")
    soup = BeautifulSoup(c, "html.parser", parse_only=bodySection)
    #soup = BeautifulSoup(c, 'html.parser')
    #bodySection = soup.select("body > div:nth-of-type(3) > div:nth-of-type(3) > div:nth-of-type(4) > div")
    childrenList = []
    #link = soup.select("body > div:nth-of-type(3) > div:nth-of-type(3) > div:nth-of-type(4) > div a:nth-of-type(1)")
    #print(link)
    #p = 1

    for a in soup.find_all('a', href=True):
        childrenList.append(a['href'])

    childrenListFinal = [l for l in childrenList if "wikipedia.org" in l]
    childrenListFinal = [l for l in childrenListFinal if "action=edit" not in l]
    return childrenListFinal

    """while (link != -1):
        childrenList.append(link)
        p = p + 1
        link = soup.select("body > div:nth-of-type(3) > div:nth-of-type(3) > div:nth-of-type(4) > div a:nth-of-type({})".format(p)['href'])
        while "wikipedia.org" not in link:
            p = p + 1
            link = soup.select("body > div:nth-of-type(3) > div:nth-of-type(3) > div:nth-of-type(4) > div a:nth-of-type({})".format(p)['href'])
    return childrenList"""


print(readLinks("https://en.wikipedia.org/wiki/Manu_propria"))

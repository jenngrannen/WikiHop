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

def filterLinkList(list):
    result = [l for l in list if (".png" and ".svg" and ".jpg" and ":") not in l ]
    result = [l for l in result if "/wiki/" in l]
    result = [l for l in result if "action=edit" not in l]
    return result

def rewriteLinkList(list):
    result = []
    for l in list:
        result.append("https://en.wikipedia.org" + l)
    return result

class LinkClass:
    linkName = ""
    prevLink = None

    def __init__(self, linkName, prevLink):
        self.linkName = linkName
        self.prevLink = prevLink

def convertListObjects(list, parent):
    result = []
    for l in list:
        result.append(LinkClass(l, parent))
    return result

def printObjList(list):
    if list == None:
        return
    for l in list:
        print(l.linkName)
    #    print(l.prevLink.linkName)

def check(list, endURL):
    for l in list:
        if l.linkName == endURL:
            return True
    return False

def getFinalLinks(start):
    url = start.linkName
    list = readLinks(url)
    list = filterLinkList(list)
    list = rewriteLinkList(list)
    list = convertListObjects(list, start)
    return list

def runIt(startURL, endURL, depth):
    list = [LinkClass(startURL, None)]
    count = 0
    while not check(list, endURL) and count < depth:
        tempList = []
        for l in list:
            tempList.extend(getFinalLinks(l))
            #printObjList(tempList)
        list = tempList
        count = count + 1
    if check(list, endURL):
        goal = [l for l in list if l.linkName == endURL]
        path = [goal[0].linkName]
        p = goal[0]
        while p.prevLink != None:
            path.append(p.prevLink.linkName)
            p = p.prevLink
        return path[::-1]
    return None

"""starturl = "https://en.wikipedia.org/wiki/Manu_propria"
endurl = "https://en.wikipedia.org/wiki/Roman_Republic"
print(runIt(starturl, endurl))
"""

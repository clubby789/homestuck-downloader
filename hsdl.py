import urllib.request, requests #File retrieval
from bs4 import BeautifulSoup #Scraping
import os,glob #Filesystem work
import threading #Efficiency




def initialise():
    global directories
    directories=["downloaded","downloaded/images","downloaded/text"]
    global imagePath
    imagePath = "https://www.homestuck.com/images/storyfiles/hs2/"

    for i in directories:
        i = os.path.join(os.getcwd(), i)
        if not os.path.isdir(i):
            os.makedirs(i)

    #s = requests.Session()

def dlPage(pageNum,s): #Pass the pageNum and Requests session
    padNum = str(pageNum).rjust(5,'0')

    r = s.get("https://www.homestuck.com/story/"+str(pageNum))
    soup = BeautifulSoup(r.text, 'html.parser')

    title = soup.h2.get_text()

    try:
        body = soup.p.get_text().replace('\r','\n')
    except:
        body = None

    next = soup.find(href="/story/"+str(pageNum+1)).get_text()

    fileName = os.path.join(directories[2], str(pageNum)+".txt")
    with open(fileName, 'w') as f:
        f.write("title: "+title+"\n")
        if body is not None:
            f.write("body: "+body+"\n")
        f.write("next: "+next+"\n")

    imageUrl = imagePath+padNum+".gif"

    if s.get(imageUrl).status_code == 200:
        urllib.request.urlretrieve(imageUrl,'downloaded/images/'+padNum+'.gif')

    elif s.get(imagePath+padNum+"_1.gif").status_code == 200:
        imageUrl = imagePath+padNum+"_1.gif"
        urllib.request.urlretrieve(imageUrl,'downloaded/images/'+padNum+'_1.gif')
        imageUrl = imagePath+padNum+"_2.gif"
        urllib.request.urlretrieve(imageUrl,'downloaded/images/'+padNum+'_2.gif')

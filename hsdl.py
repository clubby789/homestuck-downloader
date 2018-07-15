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
    text = []
    noBody = 0
    padNum = str(pageNum).rjust(5,'0')       
    url = "https://www.homestuck.com/story/"+str(pageNum)

    r = s.get("https://www.homestuck.com/story/"+str(pageNum))
    soup = BeautifulSoup(r.text, 'html.parser')
    text = []
    text.append(soup.h2.get_text())
    try:
        text.append(soup.p.get_text().replace('\r','\n'))
    except:
        noBody = 1
    text.append(soup.find(href="/story/"+str(pageNum+1)).get_text())
    fileName = os.path.join(directories[2], str(pageNum)+".txt")
    with open(fileName, 'w') as f:
        f.write("title:"+text[0]+"\n")
        if noBody == 1:
            f.write("next:"+text[1]+"\n")
        else:
            f.write("body:"+text[1]+"\n")
            f.write("next:"+text[2]+"\n")
    
    imageUrl = imagePath+padNum+".gif"
    
    if s.get(imageUrl).status_code == 200:
        urllib.request.urlretrieve(imageUrl,'downloaded/images/'+padNum+'.gif')
        
    elif s.get(imagePath+padNum+"_1.gif").status_code == 200:
        imageUrl = imagePath+padNum+"_1.gif"
        urllib.request.urlretrieve(imageUrl,'downloaded/images/'+padNum+'_1.gif')
        imageUrl = imagePath+padNum+"_2.gif"
        urllib.request.urlretrieve(imageUrl,'downloaded/images/'+padNum+'_2.gif')
    
'''
begin = input("What page to start download on? ")
end = input("What page to end download on? ")
current = int(begin)
total = int(end) - int(begin)


while not current == int(end)+1:
    fileName = "./downloaded/images/"+str(current).rjust(5,'0')+"*.gif"

    
    if not glob.glob(fileName, recursive=True):
        t = threading.Thread(target=dlPage, args=(current,))
        t.start()
    current+=1
for i in glob.glob("./downloaded/images/*.gif"):
    while os.path.getsize(i) == 0:
        urllib.request.urlretrieve(imagePath+i[20:],i)
        
'''

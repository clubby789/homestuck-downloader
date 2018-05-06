import urllib.request,requests,os,threading,time,glob
directories=["/downloaded","/downloaded/images"]
imagePath = "https://www.homestuck.com/images/storyfiles/hs2/"

for i in directories:
    i = os.getcwd() + i
    if not os.path.isdir(i):
        os.makedirs(i)

def dlPage(pageNum):
    
    padNum = str(pageNum).rjust(5,'0')       
    url = "https://www.homestuck.com/story/"+str(pageNum)
    imageUrl = imagePath+padNum+".gif"

    if requests.get(imageUrl).status_code == 200:
        urllib.request.urlretrieve(imageUrl,'downloaded/images/'+padNum+'.gif')
        
    elif requests.get(imagePath+padNum+"_1.gif").status_code == 200:
        imageUrl = imagePath+padNum+"_1.gif"
        urllib.request.urlretrieve(imageUrl,'downloaded/images/'+padNum+'_1.gif')
        imageUrl = imagePath+padNum+"_2.gif"
        urllib.request.urlretrieve(imageUrl,'downloaded/images/'+padNum+'_2.gif')
        
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
        

import requests, threading, urllib.request, glob, os
import hsdl

brokenPages = [2399]

hsdl.initialise()
s = requests.Session() #Open session
begin = input("What page to start download on? ")
end = input("What page to end download on? ")
current = int(begin)
total = int(end) - int(begin)


while not current == int(end)+1:
    if current in brokenPages:
    	current+=1
    	continue
    fileName = "./downloaded/images/"+str(current).rjust(5,'0')+"*.gif"

    
    if not glob.glob(fileName, recursive=True):
        t = threading.Thread(target=hsdl.dlPage, args=(current,s)) #Pass session to downloader
        t.start()
    current+=1
for i in glob.glob("./downloaded/images/*.gif"):
    while os.path.getsize(i) == 0:
        urllib.request.urlretrieve(imagePath+i[20:],i)

import requests, threading, urllib.request, glob, os
import hsdl

hsdl.initialise()
s = requests.Session() #Open session
begin = input("What page to start download on? ")
end = input("What page to end download on? ")
total = int(end) - int(begin)


for pageNum in range(int(begin),int(end)+1):
    if pageNum in hsdl.brokenPages:
    	continue

    fileName = "./downloaded/images/{:05}*.gif".format(pageNum)

    if not glob.glob(fileName, recursive=True):
        t = threading.Thread(target=hsdl.dlPage, args=(pageNum,s)) #Pass session to downloader
        t.start()

for i in glob.glob("./downloaded/images/*.gif"):
    while os.path.getsize(i) == 0:
        urllib.request.urlretrieve(imagePath+i[20:],i)

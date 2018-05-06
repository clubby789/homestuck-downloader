import urllib,requests,os,threading,time,glob
directories=["/downloaded","/downloaded/images"]
imagePath = "https://www.homestuck.com/images/storyfiles/hs2/"

for i in directories:
    i = os.getcwd() + i
    if not os.path.isdir(i):
        os.makedirs(i)

def dlPage(pageNum):
    
    padNum = str(pageNum).rjust(5,'0')
    if glob.glob(padNum+'*.gif'):
        return("Already got page "+pageNum)
        
    url = "https://www.homestuck.com/story/"+str(pageNum)
    imageUrl = imagePath+padNum+".gif"
    #print(imagepath+pageNum+".gif","downloaded/images/"+padNum+".gif")
    try:
        urllib.request.urlretrieve(imageUrl,'downloaded/images/'+padNum+'.gif')
    except:
        try:
            urllib.request.urlretrieve(imageUrl,'downloaded/images/'+padNum+'_1.gif')
            urllib.request.urlretrieve(imageUrl,'downloaded/images/'+padNum+'_2.gif')
        except:
            print("Error on "+padNum)
            return False
    return True

begin = input("What page to start download on? ")
end = input("What page to end download on? ")
current = int(begin)
while not current == int(end)+1:
    t = threading.Thread(target=dlPage, args=(current,))
    t.start()
    current+=1

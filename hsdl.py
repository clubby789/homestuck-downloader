import urllib.request, requests #File retrieval
from bs4 import BeautifulSoup #Scraping
import os #Filesystem work

# List of broken pages. It is currently believed that there
# should be 6 pages in this list. Add them as they are found!
brokenPages = [2399]

directories=["downloaded","downloaded/images","downloaded/text"]
imagePath = "https://www.homestuck.com/images/storyfiles/hs2/"

def initialise():
    for i in directories:
        i = os.path.join(os.getcwd(), i)
        if not os.path.isdir(i):
            os.makedirs(i)

    #s = requests.Session()

def compensate_image_name(name, pageNum):
	# Separate page number from the other stuff
	other = name[5:]

	# Then rebuild string and return it
	return "{:05}{}".format(pageNum,other)

def dlPage(pageNum,s): #Pass the pageNum and Requests session
    padNum = str(pageNum).rjust(5,'0')

    r = s.get("https://www.homestuck.com/story/"+str(pageNum))
    soup = BeautifulSoup(r.text, 'html.parser')

    if r.status_code == 404:
        print("Got 404 on retrieving page {}".format(pageNum))
        return

    title = soup.h2.get_text()

    try:
        body = soup.p.get_text().replace('\r','\n')
    except:
        body = None

    nextPage=pageNum+1
    while nextPage in brokenPages:
        nextPage += 1

    try:
        next = soup.find(href="/story/"+str(nextPage)).get_text()
    except AttributeError:
        next = "Next page title could not be found"

    fileName = os.path.join(directories[2], str(pageNum)+".txt")
    with open(fileName, 'w') as f:
        f.write("title: "+title+"\n")
        if body is not None:
            f.write("body: "+body+"\n")
        f.write("next: "+next+"\n")

    #imageUrl = imagePath+padNum+".gif"
    imageUrl = soup.findAll("img", {"class": "mar-x-auto disp-bl"})
    for i in imageUrl:
        i = i.attrs['src']

        name = i.split('/')[-1]
        name = compensate_image_name(name, pageNum)

        urllib.request.urlretrieve(i,'downloaded/images/'+name)

'''
    if s.get(imageUrl).status_code == 200:
        urllib.request.urlretrieve(imageUrl,'downloaded/images/'+padNum+'.gif')

    elif s.get(imagePath+padNum+"_1.gif").status_code == 200:
        imageUrl = imagePath+padNum+"_1.gif"
        urllib.request.urlretrieve(imageUrl,'downloaded/images/'+padNum+'_1.gif')
        imageUrl = imagePath+padNum+"_2.gif"
        urllib.request.urlretrieve(imageUrl,'downloaded/images/'+padNum+'_2.gif')
'''

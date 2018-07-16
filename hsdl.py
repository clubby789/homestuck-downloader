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

def compensate_image_name(name):
	# Separate page number from the other stuff
	page = int(name[:5])
	other = name[5:]

	# Increment page depending on number of known lower broken pages
	print("Compensating page {} with {} steps".format(page , sum(p < page for p in brokenPages)))
	page += sum(p <= page for p in brokenPages)

	# Then rebuild string and return it
	return "{:05}{}".format(page,other)

def dlPage(pageNum,s): #Pass the pageNum and Requests session
    if pageNum in brokenPages:
        print("Skipping known broken page: {}".format(pageNum))
        return

    padNum = str(pageNum).rjust(5,'0')

    r = s.get("https://www.homestuck.com/story/"+str(pageNum))
    soup = BeautifulSoup(r.text, 'html.parser')

    if r.status_code == 404:
        print("Got 404 on retrieving page {}".format(pageNum))
	brokenPages.append(pageNum) #Output to file later?
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
        name = compensate_image_name(name)

        urllib.request.urlretrieve(i,'downloaded/images/'+name)

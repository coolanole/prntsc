import random, requests, urllib2, urlparse, os
from bs4 import BeautifulSoup


class Lightshot(object):
    def __init__(self):
        super(Lightshot, self).__init__()

    def getHeader(self):
        return {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:64.0) Gecko/20100101 Firefox/64.0",
        }

    def generateLink(self, length=6):
        link = ""
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

        for c in range(length):
            link += random.choice(chars)

        return link

    def getScreenshot(self):
        url = "https://prnt.sc/%s" % self.generateLink()
        r = requests.get(url, headers=self.getHeader())
        # print("Link:%s - %s" % (url, r.status_code))
        screenshot = self.parseResponse(r.text)

        if screenshot:
            self.downloadScreenshot(screenshot)

    def parseResponse(self, response):
        soup = BeautifulSoup(response, 'html.parser')
        screenshot = soup.find("img", {"id": "screenshot-image"})

        if screenshot is None:
            return False

        if screenshot["src"] == "//st.prntscr.com/2018/10/13/2048/img/0_173a7b_211be8ff.png":
            return False

        return screenshot["src"]

    def getFilename(self, url):
        a = urlparse.urlparse(url)
        return os.path.basename(a.path)

    def downloadScreenshot(self, url):
        try:
            filedata = urllib2.urlopen(url)
            datatowrite = filedata.read()

            with open("screenshots/%s" % self.getFilename(url), "wb") as f:
                f.write(datatowrite)
        except Exception as e:
            pass
        else:
            print(" [~] Downloaded: %s" % url)


prntsc = Lightshot()

while True:
    prntsc.getScreenshot()

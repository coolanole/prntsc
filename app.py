import random, requests, urllib2, urlparse, os, sys
from bs4 import BeautifulSoup
from threading import Thread

# Number of threads in which screenshots will be searched
threads = 2 if len(sys.argv) < 2 else int(sys.argv[1])


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
        bcolors.info("Trying to find a screenshot: %s" % url)
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
            bcolors.success("The screenshot was downloaded successfully: %s" % url)

    def run(self):
        while True:
            self.getScreenshot()


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def success(message):
        print bcolors.OKGREEN + "[>] " + message + bcolors.ENDC

    @staticmethod
    def fail(message):
        print bcolors.FAIL + "[!] " + message + bcolors.ENDC

    @staticmethod
    def warning(message):
        print bcolors.WARNING + "[~] " + message + bcolors.ENDC

    @staticmethod
    def info(message):
        print bcolors.OKBLUE + "[~] " + message + bcolors.ENDC


bcolors.warning("Getting download screenshots...")
prntsc = Lightshot()

bcolors.warning("Search started in %s threads..." % threads)

for x in range(threads):
    thread = Thread(target=prntsc.run)
    thread.start()

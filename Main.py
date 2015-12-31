# V 1.0
# Imports
from config import Configuration
from show import *
from datetime import datetime
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# Load/Create config
config = Configuration()

# Load shows


myShowsList = ShowManager().retrieveShowList()

# Check web - Recover list of available shows
recShowList = []

req = Request(config.BaseUrl, None, config.Headers)
data = urlopen(req).read().decode("utf-8")
soup = BeautifulSoup(data, "html.parser")

trs = soup.find_all("tr", {'class': 'forum_header_border'})
for row in trs:
    recoveredShow = Show()
    # Getting show name
    showText = row.find_all("td")[1].get_text().lower()
    # print(showText)

    if showText.find("720") > -1:
        recoveredShow.Is720p = True
    else:
        if showText.find("1080") > -1:
            # 1080p ??
            pass
        else:
            recoveredShow.Is720p = False  # HDTV



    magnetItem = row.find("a", {'class': 'magnet'})
    magnetLink = None
    # Searching magnet link
    if magnetItem is not None:
        magnetLink = magnetItem["href"]
        recoveredShow.Magnet = magnetLink

    # print(magnetLink)
    # Searching torrent links
    torrentSource = 1
    torrentItem = None
    torrentLink = None
    while torrentItem == None and torrentSource <= config.TorrentSourcesCount:
        torrentItem = row.find("a", {'class': 'download_{0}'.format(torrentSource)})
        torrentSource += 1
    if torrentItem is not None:
        torrentLink = torrentItem["href"]
        recoveredShow.Torrent = torrentLink

        # print(torrentLink)

    #Comprar con mis shows
    for s in myShowsList:
        if showText.find(s.Name.lower()) > -1 and recoveredShow.Is720p == s.Is720p:
            print("Show encontrado {0}".format(s.Name))
            recoveredShow.Name = s.Name
            recoveredShow.CompleteText = showText
            s.downloadTorrent(recoveredShow)


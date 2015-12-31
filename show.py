class Show(object):
    def __init__(self, Name=None, Is720p=False, Magnet=None, Torrent=None):
        self.Name = Name
        self.CompleteText = None
        self.Is720p = Is720p
        self.Magnet = Magnet
        self.Torrent = Torrent
        self.History = []

    def toString(self):
        if (self.Is720p):
            return "{0} (720p)".format(self.CompleteText)
        else:
            return "{0}".format(self.CompleteText)

    # Evaluate last download and download
    def downloadTorrent(self, recovered):
        from urllib.request import Request, urlopen
        from config import Configuration
        import os.path
        # TODO Check History



        if recovered.Torrent is not None:
            config = Configuration()
            torrentName = recovered.Torrent[recovered.Torrent.rfind("/") + 1:]
            if not os.path.isfile(config.TorrentWatchPath + torrentName):#TODO Revisar validacion
                torrentReq = Request(recovered.Torrent.replace(" ","%20"), None, config.Headers)
                torrentData = urlopen(torrentReq).read()
                torrentFile = open(config.TorrentWatchPath + torrentName, "wb")
                torrentFile.write(torrentData)
                torrentFile.close()
                #print("Torrent saved")
            else:
                #File already exists
                #print("Torrent already exists")
                pass


class ShowDownload(object):
    def __init__(self, Magnet=None, Torrent=None, DownloadDate=None):
        self.Torrent = Torrent
        self.Magnet = Magnet
        self.DownloadDate = DownloadDate

class ShowManager(object):
    def retrieveShowList(self):
        import jsonpickle

        showListFile = open("showList.json", "r")
        showListData = showListFile.read()
        showListFile.close()
        parsedShowList = jsonpickle.decode(showListData)
        return parsedShowList

    def updateShowList(self, showList):
        import jsonpickle

        encodedShowList = jsonpickle.encode(showList)
        showListFile = open("showList.json", "w")
        showListFile.write(encodedShowList)
        showListFile.close()

    def createDefaultShowList(self):
        showList = []
        showList.append(Show("Default1"))
        showList.append(Show("Default2"))

        self.updateShowList(showList)
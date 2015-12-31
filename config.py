class Configuration(object):
    def __init__(self,baseUrl="https://eztv.ag/sort/100/"):
        self.BaseUrl = baseUrl
        self.Headers = {'User-Agent': 'Mozilla/5.0'}
        self.TorrentSourcesCount=3
        self.TorrentWatchPath = '/home/lean/Downloads/'
# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
from threading import Thread, Lock
class Solution:
    def __init__(self):
        self.q = deque()
        self.visited = set()
        self.lock = Lock()
        
    def getHostname(self, url):
        return "".join(url.split("/")[2])
    
    def downloadUrls(self, htmlParser, url):
        urls = htmlParser.getUrls(url)
        with self.lock:
            for v in urls:
                if v not in self.visited and self.getHostname(v) == self.hostname:
                    self.q.append(v)
                    self.visited.add(v)
        
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]: 
        self.hostname = self.getHostname(startUrl)
        self.q.append(startUrl)
        self.visited.add(startUrl)
        maxthreads = 10
        while self.q:
            t = 0
            threads = []
            while self.q and t < maxthreads:
                u = self.q.popleft()
                threads.append(Thread(target=self.downloadUrls, args=(htmlParser, u)))
                t += 1
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()
        return list(self.visited)
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

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        i, slashes = 0, 0
        while i < len(startUrl) and slashes < 3:
            if startUrl[i] == "/": slashes += 1
            i += 1
        hostname = startUrl if i == len(startUrl) else startUrl[:i-1]
        res = set()
        stack = [iter([startUrl])]
        while stack:
            nxt = next(stack[-1], None)
            if nxt is None:
                stack.pop()
                continue
            if nxt in res:
                continue
            if nxt.startswith(hostname):
                res.add(nxt)
                stack.append(iter(htmlParser.getUrls(nxt)))
        return list(res)  
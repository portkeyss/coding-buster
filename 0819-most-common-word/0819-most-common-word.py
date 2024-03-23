class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """ 
        count = collections.Counter()
            
        p = paragraph.lower()
        sb = []
        for c in p:
            if c in "!?',;.":
                sb.append(' ')
            else:
                sb.append(c)
        
        q = ''.join(sb).split()
        print(q)
        
        banned_words = set(banned) # make future check of banned words in O(1)
        for x in q:
            if x in banned_words:
                continue
            else:
                count[x] += 1
                
        maxCount = 0
        ans = ''
        for word in count.keys():
            if count[word] > maxCount:
                ans = word
                maxCount = count[word]
        return ans
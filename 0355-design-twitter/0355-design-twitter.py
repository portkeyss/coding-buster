class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followee = defaultdict(set)
        self.tweets = defaultdict(list) #map user id to its tweets
        self.order = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].append((self.order, tweetId))
        self.order += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        self.follow(userId, userId) #follow userself themself
        hq = []
        for followeeId in self.followee[userId]:
            A = self.tweets[followeeId]
            if A != []:
                heapq.heappush(hq,(-A[-1][0], A[-1][1], A, len(A)-1))
        
        ans = []
        n = 0
        while n < 10 and hq:
            _, tweetId, A, j = heapq.heappop(hq)
            ans.append(tweetId)
            j -= 1
            if j > -1:
                heapq.heappush(hq,(-A[j][0], A[j][1], A, j))
            n += 1
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followee[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
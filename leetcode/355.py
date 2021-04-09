# 355. Design Twitter
# https://leetcode.com/problems/design-twitter/

class Twitter:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.tweets = collections.defaultdict(list)
        self.followee = collections.defaultdict(set)
        
​
    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].append((-self.time, tweetId))
        self.time += 1
        
​
    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        res = []
        heap, tweets = [], self.tweets
        people = self.followee[userId] | set([userId])
​
        for p in people:
            if tweets[p]:
                time, tweet = tweets[p][-1]
                heap.append((time, tweet, p, len(tweets[p]) - 1))
                
        heapq.heapify(heap)
        read = 0
        
        while heap and read < 10:
            _, tweet, p, idx = heapq.heappop(heap)
            res.append(tweet)
            if idx > 0:
                time, tweet2 = tweets[p][idx - 1]
                heapq.heappush(heap, (time, tweet2, p, idx - 1))
            
            read += 1
        
        return res
        
​
    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        
        self.followee[followerId].add(followeeId)
​
    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        mp = self.followee[followerId]
        if followeeId in mp:
            mp.remove(followeeId)
        
​
​
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

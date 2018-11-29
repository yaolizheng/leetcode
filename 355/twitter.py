import heapq


class Twitter:

    def __init__(self):
        self._follow = dict()
        self.tweet = dict()
        self.user = list()
        self.count = 0

    def postTweet(self, userId, tweetId):
        if userId not in self.tweet:
            self.tweet[userId] = []
        self.count += 1
        if userId not in self._follow:
            self._follow[userId] = []
        if userId not in self._follow[userId]:
            self._follow[userId].append(userId)
        self.tweet[userId].append([self.count, tweetId])

    def follow(self, followerId, followeeId):
        if followerId not in self._follow:
            self._follow[followerId] = []
        self._follow[followerId].append(followeeId)

    def unfollow(self, followerId, followeeId):
        self._follow[followerId].remove(followeeId)

    def getNewsFeed(self, userId):
        top10 = []
        for user in self._follow[userId]:
            for tweet in self.tweet[user]:
                heapq.heappush(top10, tweet)
                if len(top10) > 10:
                    heapq.heappop(top10)
        rv = []
        while len(top10) > 0:
            rv.append(heapq.heappop(top10)[1])
        return rv


if __name__ == '__main__':
    twitter = Twitter()
    twitter.postTweet(1, 5)
    print twitter.getNewsFeed(1)
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    print twitter.getNewsFeed(1)
    twitter.unfollow(1, 2)
    print twitter.getNewsFeed(1)

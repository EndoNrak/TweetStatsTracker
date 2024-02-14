class TweetStats:
    def __init__(self, tweet_id, bookmarks, likes, views, retweets, quotes, replies):
        self.tweet_id = tweet_id
        self.bookmarks = bookmarks
        self.likes = likes
        self.views = views
        self.retweets = retweets
        self.quotes = quotes
        self.replies = replies
    
    @classmethod
    def fromJson(cls, data):
        tweet_id = data["data"]["tweetResult"]["result"]["rest_id"]
        bookmarks = data["data"]["tweetResult"]["result"]["legacy"]["bookmark_count"]
        likes = data["data"]["tweetResult"]["result"]["legacy"]["favorite_count"]
        views = data["data"]["tweetResult"]["result"]["views"]["count"]
        retweets = data["data"]["tweetResult"]["result"]["legacy"]["retweet_count"]
        quotes = data["data"]["tweetResult"]["result"]["legacy"]["quote_count"]
        replies = data["data"]["tweetResult"]["result"]["legacy"]["reply_count"]
        
        return cls(tweet_id, bookmarks, likes, views, retweets, quotes, replies)

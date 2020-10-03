import tweepy

from config import create_api, logger

class HutsbotStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api

    def on_status(self, tweet):
        if tweet.is_quote_status == False and tweet.user != self.api.me():
            logger.info(f"@{tweet.user.screen_name}: {tweet.text} ({tweet.id})")
            quote_url = f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
            self.api.update_status("😖", attachment_url=quote_url)

    def on_error(self, status):
        if status == 420:
            logger.error(f"{status}: Rate limit exceeded")
        else:
            logger.error(f"{status}: API error")


def main():
    api = create_api()
    tweet_listener = HutsbotStreamListener(api)
    stream = tweepy.Stream(api.auth, tweet_listener)
    stream.filter(track=["hutspot"])

if __name__ == "__main__":
    main()

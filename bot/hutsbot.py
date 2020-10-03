import tweepy

from config import create_api, logger


class HutsbotStreamListener(tweepy.StreamListener):
    """
    Listens to incoming tweets containing the word 'hutspot' and
    quotes them
    """

    def __init__(self, api):
        self.api = api

    def on_status(self, tweet: tweepy.models.Status):
        """
        Take action when a new tweet comes in
        """
        if tweet.is_quote_status is False and tweet.user != self.api.me():
            logger.info(
                f"@{tweet.user.screen_name}: {tweet.text} ({tweet.id})"
            )
            quote_url = (
                f"https://twitter.com/{tweet.user.screen_name}"
                f"/status/{tweet.id}"
            )
            self.api.update_status("😖", attachment_url=quote_url)

    def on_error(self, status: int):
        """
        This only is called when something goes wrong (duh)
        """
        if status == 420:
            logger.error(f"{status}: Rate limit exceeded")
        else:
            logger.error(f"{status}: API error")


def main():
    """
    Driver method
    """
    api = create_api()
    tweet_listener = HutsbotStreamListener(api)
    stream = tweepy.Stream(api.auth, tweet_listener)
    stream.filter(track=["hutspot"])


if __name__ == "__main__":
    main()

import tweepy
import random

from config import create_api, logger

RESPONSES = ["Iewl", "Huuuuu", "Brrrrr", "Vies hè", "Gedverderrie", "Blèh"]
RANDOM_INTERVAL = 5


class HutsbotStreamListener(tweepy.StreamListener):
    """
    Listens to incoming tweets containing the word 'hutspot' and
    quotes them
    """

    def __init__(self, api):
        self.api = api
        self.random_counter = 0

    def on_status(self, tweet: tweepy.models.Status):
        """
        Take action when a new tweet comes in
        """
        if not hasattr(tweet, "retweeted_status") and tweet.user != self.api.me():
            logger.info(f"@{tweet.user.screen_name}: {tweet.text} ({tweet.id})")
            quote_url = (
                f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
            )

            # Tweet something else than an emoji after 5 times
            if self.random_counter < RANDOM_INTERVAL:
                self.api.update_status("😖", attachment_url=quote_url)
                self.random_counter += 1
            else:
                tweet = random.choice(RESPONSES)
                self.api.update_status(tweet, attachment_url=quote_url)
                self.random_counter = 0

    def on_error(self, status: int):
        """
        This only is called when something goes wrong
        """
        if status == 420:
            logger.error(f"{status}: Rate limit exceeded")
        else:
            logger.error(f"{status}: Other API error")


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

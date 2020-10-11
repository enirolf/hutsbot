import tweepy
import random, time

from config import create_api, logger


RANDOM_TWEETS = ['Iewl',
                 'Huuuuu',
                 'Brrrrr'
                 'Vies hè'
                ]


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
            logger.info(f"@{tweet.user.screen_name}: {tweet.text} ({tweet.id})")
            quote_url = (
                f"https://twitter.com/{tweet.user.screen_name}" f"/status/{tweet.id}"
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


def tweet_random(api: tweepy.api):
    """
    Tweet anti-hutspot exclamations at random intervals between 30 minutes
    and 2 hours
    """
    while True:
        tweet = random.choice(RANDOM_TWEETS)
        api.update_status(tweet)
        # Pick a random interval to wait between 30 and 120 minutes
        sleep_interval = random.randrange(1800, 7200)
        time.sleep(sleep_interval)


def main():
    """
    Driver method
    """
    api = create_api()
    tweet_listener = HutsbotStreamListener(api)
    stream = tweepy.Stream(api.auth, tweet_listener)

    # Run stream in a separate thread so we can still tweet random
    # anti-hutspot related stuff at an interval
    stream.filter(track=["hutspot"], is_async=True)
    tweet_random(api)


if __name__ == "__main__":
    main()

import os
import logging
import tweepy
from dotenv import load_dotenv

load_dotenv()

FORMAT = "%(asctime)s %(message)s"

if os.getenv("ENV") == "develop":
    logging.basicConfig(level=logging.DEBUG, format=FORMAT)
else:
    logging.basicConfig(level=logging.INFO, format=FORMAT)

logger = logging.getLogger()


def create_api() -> tweepy.models.User:
    """
    Create a new twitter API instance for sending and receiving tweets
    """
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        user = api.verify_credentials()

        if user:
            logger.info(f"API for @{user.screen_name} successfully created")
        else:
            logger.error("Failed verifying credentials")

        return api
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e

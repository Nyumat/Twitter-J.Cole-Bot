import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    # Keys have been changed, for anyone trying to breach my bot. - Sorry not sorry :)
    consumer_key = os.getenv("***************")
    consumer_secret = os.getenv("************************")
    access_token = os.getenv("******************")
    access_token_secret = os.getenv("*****************")

    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

    try: 
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating an API", exc_info=True)
        raise e
    logger.info("API has been created.")
    return api

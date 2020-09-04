import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("jRKLllEQoGrAqey9zzN30ROS5")
    consumer_secret = os.getenv("3LtXS1IsGFWX8w9YS7my8BSISCkdEDVwv0Uy9Pf3WyhHKcunHu")
    access_token = os.getenv("1301298497715609600-D0AEH9UipG6impn5cFiQUNYVohtr64")
    access_token_secret = os.getenv("A1MsupoLBRz9IKnqAE062n6v0sIYqomBYNUd1WCKTvk94")

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
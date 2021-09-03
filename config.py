import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    """"
    Apply for developer credentials for the ability to create your own Bot instance!
    (https://developer.twitter.com/en/apply-for-access) 
    Then, replace the placeholders with your token below.
    
    """
    
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

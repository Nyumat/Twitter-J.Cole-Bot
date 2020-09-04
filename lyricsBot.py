import time
import tweepy
import logging
import bs4
from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import sys


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
# Keys have been changed, @ anyone trying to breach my bot :)
consumer_key = '******************'
consumer_secret = '****************'
access_token = '************'
access_token_secret = '***********'



def getLyrics(): 
            print("Enter a J. Cole song you'd like to append lyrics to .txt")
            print("Keep in mind, if the song has spaces, it must be one entirely lowercase string.")
            print("For example, Goin' Off would be : goingoff")


            song = input(">> ")
            url = "https://www.azlyrics.com/lyrics/jcole/" + song + ".html"

            rawHTML = requests.get(url).text
            soup = BeautifulSoup(rawHTML, "lxml")

            for br in soup.findAll('br'):
                lyrics = br.nextSibling
                if not (lyrics and isinstance(lyrics,NavigableString)):
                    break
                next_lyric = lyrics.nextSibling
                if next_lyric and isinstance(next_lyric,Tag) and next_lyric.name == 'br':
                    text = str(lyrics).strip()
                    if text:
                        with open("stored_lyrics.txt", "a") as storage:
                            print(text,file=storage)
            
def getTweet():
            line_num = 1
            with open("stored_lyrics.txt") as stored_lyrics:
                lyrics = stored_lyrics.readlines()
                currentTweet = lyrics[line_num].strip()
                return currentTweet
                
def create_api():

            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
            return api


def main():
    api = create_api()
    while True:
        getLyrics()
        tweet = getTweet()
        api.update_status(tweet)


if __name__ == "__main__":
    main()


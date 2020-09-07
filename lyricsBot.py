import time
import tweepy
import logging
import bs4
from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import sys
import re


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Keys have been changed, @ anyone trying to breach my bot :)
consumer_key = '******************'
consumer_secret = '****************'
access_token = '************'
access_token_secret = '***********'

def addLyrics():
    print("How many songs would you like to add?")
    add_amount = int(input(">> "))

    for _ in range(0,add_amount):
        getLyrics()
        print(f'{add_amount} Added')

def prompt():
    print("~ Welcome, Thomas.")

    print("~ Would you like to [Tweet] or [Add lyrics] ???")

    prompt  = input(">> ")

    if (prompt == "Add lyrics"):
        addLyrics()

    if (prompt == "Tweet"):
        main()


def getLyrics(): 
            print("Enter the J. Cole song you'd like to add to the stored data.")
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
                    text = re.sub(r'[()]'," ", lyrics)
                    if text:
                        with open("stored_lyrics.txt", "a") as storage:
                            print(text.replace('\n', '')
                            print(text.strip(),file=storage)

def getTweet():
            num = getLineNum()
            with open("stored_lyrics.txt") as stored_lyrics:
                lyrics = stored_lyrics.readlines()
                currentTweet = lyrics[int(num)].strip()
                return currentTweet
                
def getLineNum():
    with open("currentTweet.txt", 'r') as line:
        line_num = line.read()
        int_line = int(line_num)
        new_line = int(int_line) + 1
    with open("currentTweet.txt", 'w') as line:
        line.write(str(new_line))
    return line_num


def create_api():

            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
            return api


def main():
    api = create_api()
    time.sleep(0.1)
    tweet = getTweet()
    api.update_status(tweet)
        


if __name__ == "__main__":
    prompt()


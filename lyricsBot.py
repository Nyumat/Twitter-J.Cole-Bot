# Imports Required Files

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
    # Iteratively adds lyrics to .txt for the range in add_amount.
    print("How many songs would you like to add?")
    add_amount = int(input(">> "))
    # Calls getLyrics() so that the program actually does the "song adding"
    for _ in range(0,add_amount):
        getLyrics()
        print(f'{add_amount} Added')

def prompt():
    # Prompt the user {me} to choose an endpoint, wheter it be Add Lyrics to the .txt file or "tweet"
    print("~ Welcome, Thomas.")

    print("~ Would you like to [Tweet] or [Add lyrics] ???")

    prompt  = input(">> ")

    if (prompt == "Add lyrics"):
        addLyrics()

    if (prompt == "Tweet"):
        main()

# Get Lyrics from AZlyrics and parse the HTML into text.
def getLyrics():
            print("Enter the J. Cole song you'd like to add to the stored data.")
            print("Keep in mind, if the song has spaces, it must be one entirely lowercase string.")
            print("For example, Goin' Off would be : goingoff")


            song = input(">> ")
            url = "https://www.azlyrics.com/lyrics/jcole/" + song + ".html"

            rawHTML = requests.get(url).text
            soup = BeautifulSoup(rawHTML, "lxml")
    
            # Find all occurances of breaks in text or <br> 
            for br in soup.findAll('br'):
                lyrics = br.nextSibling
                if not (lyrics and isinstance(lyrics,NavigableString)):
                    break
                next_lyric = lyrics.nextSibling
                # We know that the text is inbetween tags <br></br> so we use .nextSibling to get each line of text.
                if next_lyric and isinstance(next_lyric,Tag) and next_lyric.name == 'br':
                    text = str(lyrics).strip()
                    # Remove parentheses and the words in between them with regex's .sub method.
                    parsed_text = re.sub(r'\([^()]*\)','', lyrics)
                    if text:
                        with open("stored_lyrics.txt", "a") as storage:
                            # Write the parsed text to the storage file that is open.
                            print(parsed_text.strip(),file=storage)

def getTweet():
    # Creates a object num to be used as the line_num from the return of function "getLineNum".
    num = getLineNum()
    with open("stored_lyrics.txt") as stored_lyrics:
        # Reads the entire lyrics file and takes the current line_num to be used as the tweet.
        lyrics = stored_lyrics.readlines()
        currentTweet = lyrics[int(num)].strip()
        return currentTweet

def getLineNum():
    # Refrences the currentTweet.txt file to find out which line/lyric the program is currently on.
    with open("currentTweet.txt", 'r') as line:
        line_num = line.read()
        int_line = int(line_num)
        # Increments the line_num for each call to the function.
        new_line = int(int_line) + 1
    with open("currentTweet.txt", 'w') as line:
        line.write(str(new_line))
    return line_num


def create_api():
            # Tweepy uses OAuth2, so we have to set up an API instance to be used inside our main() call.
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

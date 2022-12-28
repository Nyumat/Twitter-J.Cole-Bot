import time
import tweepy
import logging
from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import re
import random
import os
from dotenv import load_dotenv
# import keep_alive

class JcoleBot:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger()
        # print env variables
        print(os.getenv("consumer_key"))

    def create_api(self):
        print("\n\n\t\t Creating API... \n\n")
        try:
            consumer_key = os.getenv("consumer_key")
            consumer_secret = os.getenv("consumer_secret")
            access_token = os.getenv("access_token")
            access_token_secret = os.getenv("access_token_secret")

            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            api = tweepy.API(auth, wait_on_rate_limit=True)
            api.verify_credentials()

            print("\n\n\t\t API Created! \n\n")
            return api

        except Exception as e:
            print("Error Creating API")
            print(e)
            return None

    def get_options(self):
        valid = False
        prompt = ""

        while not valid:

            print(
                """
                Would you like to: \t \t \n
                Tweet [1]  \t\t\n
                Add lyrics [2] (Case-Sensitive) \t\t\n
                Exit [3] \t\t\n
                """
            )

            prompt = input(">> ")

            if prompt == "3":
                print("Exiting...")
                exit()

            if prompt == "2":
                self.add_lyrics()
                break

            if prompt == "1":
                print(" \t\t \n\n Loop [1] \n\nSingle Tweet [2]? \n\n")
                choice = input(">> ")
                if choice == "1":
                    self.tweet_loop()
                if choice == "2":
                    self.tweet()
                else:
                    print("Please enter a valid number.")
                    continue
            else:
                print("Please enter a valid number.")
                continue

    def add_lyrics(self):
        # Iteratively adds lyrics to .txt for the range in add_amount.
        print("How many songs would you like to add?")
        try:
            add_amount = int(input(">> "))
        except ValueError:
            print("Please enter a valid number.")
            self.add_lyrics()
        added_songs = self.scrape_lyrics(add_amount)
        formatted_song = ", ".join(added_songs)
        print(f"{add_amount} Songs Added. {formatted_song}")

    # Get Lyrics from AZlyrics.com
    def scrape_lyrics(self, add_amount):
        songs_added = []

        for i in range(add_amount):
            print(
                """
                Enter the J. Cole song you'd like to add to the stored data.\n\n
                
                Keep in mind, if the song has spaces, 
                it must be one entirely lowercase string. \n\n
                
                For example, Goin' Off would be : goingoff 
                """
            )

            song = input(">> ")

            url = "https://www.azlyrics.com/lyrics/jcole/" + song + ".html"
            songs_added.append(song)

            rawHTML = requests.get(url).text
            soup = BeautifulSoup(rawHTML, "lxml")

            # Find all occurances of breaks in text or <br>
            for br in soup.findAll("br"):
                lyrics = br.nextSibling
                if not (lyrics and isinstance(lyrics, NavigableString)):
                    break
                next_lyric = lyrics.nextSibling
                # We know that the text is inbetween tags <br></br> so we use .nextSibling to get each line of text.
                if (
                    next_lyric
                    and isinstance(next_lyric, Tag)
                    and next_lyric.name == "br"
                ):
                    text = str(lyrics).strip()
                    # Remove parentheses and the words in between them with regex's .sub method.
                    parsed_text = re.sub(r"\([^()]*\)", "", lyrics)
                    if text:
                        with open("stored_lyrics.txt", "a") as storage:
                            # Write the parsed text to the storage file that is open.
                            print(parsed_text.strip(), file=storage)

        return songs_added

    def get_line_count(self):
        with open("stored_lyrics.txt") as file:
            for count, line in enumerate(file):
                pass
        return count + 1

    def get_tweet(self):
        # Should we bring this back?
        # num = getLineNum()
        count = self.get_line_count()
        with open("stored_lyrics.txt") as stored_lyrics:
            # Reads the entire lyrics file and takes the current line_num to be used as the tweet.
            lyrics = stored_lyrics.readlines()
            currentTweet = lyrics[random.randint(0, count)].strip()
            return currentTweet

    def get_line_num(self):
        # Refrences the currentTweet.txt file to find out which line/lyric the program is currently on.
        with open("currentTweet.txt", "r") as line:
            line_num = line.read()
            print(line_num)
            int_line = int(line_num)
            # Increments the line_num for each call to the function.
            new_line = int(int_line) + 1
        with open("currentTweet.txt", "w") as line:
            line.write(str(new_line))
        return line_num

    def tweet(self, tweet_text=None):
        api = self.create_api()
        if tweet_text is None:
            tweet_text = input("Enter your tweet: ")
            api.update_status(tweet_text)
            print(f"Tweeted: \n {tweet_text}")
        else:
            tweet = self.get_tweet()
            line_num = self.get_line_num()
            api.update_status(tweet)
            print(
                f"""
                Tweeting: \n
                {tweet}
                
                Line Number: \n
                {line_num}    
                """
            )

    def tweet_loop(self):
        while True:
            self.tweet(self.get_tweet())
            time.sleep(1800)


if __name__ == "__main__":
    load_dotenv()
    bot = JcoleBot()
    bot.get_options()

import bs4
from bs4 import BeautifulSoup, NavigableString, Tag
import time 
import requests
import sys
from config import create_api

def getLyrics(): 
  
    print("Enter a J. Cole song you'd like to return the lyrics for.")
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
                            



<h1 align="center" style="font-size: 3rem;">The J. Cole Lyric Bot</h1>

<p align="center">J. Cole bot is for entertainment purposes only!</p>

## The Project

J.Cole Bot is an opt-in automated twitter bot. The bot incooperates the [Twitter API](https://developer.twitter.com/en/docs/twitter-api), [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#), and [Tweepy](https://www.tweepy.org/) to post J.Cole song lyrics derived from [AZLyrics](azlyrics.com) every 10-30 minutes. The codebase is formatted using black. [What's Black?](https://github.com/psf/black#installation)

## Building Your Own Bot Instance.

**To create your own bot instance, the first thing you will need to do is setup your very own virtual enviornment.**

First, make sure you have the latest version of pip installed:
```
pip install --upgrade pip
```
Next, clone the repo.
<br><img src="img/venv.png" width="264" height="204"></br>

Now, install the packages in the requirements.txt.
```
pip install -r requirements.txt
```
> You'll now have virtualenv, but if you don't--'pip install virtualenv' should get you set up.


Create your new enviornment '$some_name':
```
python -m venv ($some_name)
```
Activate your virtual enviornment: 
```
source $some_name/bin/activate
```
To deactivate the enviornment use:
```
decativate
```

Finally, you'll need some enviornment variables.
```
touch .env && vim .env
```

Format it like so. Grab the keys [here.](https://developer.twitter.com/en/portal/petition/essential/basic-info)
```
consumer_key=
consumer_secret=
access_token=
access_token_secret=
```

Once do this step, you're now ready to run the bot.
```
python3 lyricsBot.py
```

# To-Do's:

- [x] Finish Documentation
- [x] Add Lyrics to stored_lyrics.txt
- [ ] Finish compatibility for different artists 

# License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](LICENSE)

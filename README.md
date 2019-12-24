### mastobot
a very simple mastodon bot thing to make making bots easier and get rid of all
of the boilerplate
not life-changing, but it helps me get a bot out fast

## usage
```
import mastobot

# create bot instance
bot = mastobot()

# login using config file, assuming you're making a bot on botsin.space,
# otherwise specify url as a string
bot.login()

# post some sort of text
bot.text_post("mastobot makes making mastodon bots in python so great")

# post some media
bot.media_toot("file/path/to/media")

```

## requirements
uses the [mastodon](https://mastodonpy.readthedocs.io/en/stable/) library
```
pip install requirements.txt
```

### mastobot
a very simple mastodon bot thing to make making bots easier and get rid of a lot
of the boilerplate, without giving up a certain degree of customizability!
not life-changing, but useful! helps to get a bot out fast

## usage
```
import mastobot

# create bot instance!
bot = mastobot()

# login using config file, assuming you're making a bot on botsin.space,
# otherwise specify url as a string
bot.login()

# post some sort of text
bot.text_post("mastobot makes making mastodon bots in python so great")

# post some media!
bot.media_toot("file/path/to/media")

```

## requirements
uses the [mastodon](https://mastodonpy.readthedocs.io/en/stable/) library
```
pip install requirements.txt
```

### suggestions
if you have any features you wanna see, or have some code you wanna implement here or
if you have used this, please let me know!
you can email me at:
reeseporter [at] ufl [dot] edu

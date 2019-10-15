import config
from mastodon import Mastodon

class mastobot(object):
    """
    making simple bots on mastodon even easier!!

    example use:

    # create bot instance!
    bot = mastobot()

    # login using config file
    bot.login()

    # create text output!
    output = new_output()

    # post that output
    bot.text_post(output)

    # post some media!
    bot.media_toot("file/path/to/media")

    """

    def __init__(self, api):
        super(mastobot, self).__init__()
        self.api = api
        self.datetimeimported = False

    def login(self, url="https://botsin.space", key=config.key,
              secret=config.secret, access=config.access):
        """
        logs in to Mastodon, assuming it's a bot on botsin.space,
        otherwise, have to specify in the url argument
        """
        self.api = Mastodon(
            client_id=key, client_secret=secret, access_token=access,
            api_base_url=url
        )


    def media_toot(self, media, text, logs=None):
        """
        media = path to media
        text = accompanying text for media
        logs = path to plain text log file for error handling, optional
        """
        try:
            post = self.api.media_post(media)
            self.api.status_post(text, media_ids=post)
        except Exception as e:
            if logs is not None:
                self.error_handling(e, logs)
            else:
                print("error!!! : ", str(e))

    def text_post(self, text, logs=None):
        """
        text = post text
        logs = path to plain text log file for error handling, optional
        """
        try:
            self.api.toot(text)
        except Exception as e:
            if logs is not None:
                self.error_handling(e, logs)
            else:
                print("error!!! : ", str(e))

    def error_handling(self, errors, logs):
        """
        imports datetime if datetime not imported, writes error to log file
        """
        if not self.datetimeimported:
            from datetime import datetime
            self.datetimeimported = True
        with open(logs, "w+") as f:
            f.write(datetime.datetime.now())
            f.write("\n")
            f.write(str(errors))
            f.write("\n")
        f.close()

import os
from flask import Flask, request

from api.config import config
import botArchiver


def create_app(test_config=None):
    app = Flask(__name__)

    # check environment variables to see which config to load
    env = os.environ.get("FLASK_ENV", "dev")
    # for configuration options, look at api/config.py
    if test_config:
        # purposely done so we can inject test configurations
        # this may be used as well if you'd like to pass
        # in a separate configuration although I would recommend
        # adding/changing it in api/config.py instead
        # ignore environment variable config if config was given
        app.config.from_mapping(**test_config)
    else:
        app.config.from_object(config[env])  # config dict is from api/config.py

    @app.route('/')
    def receive_update():
        def webhook():
            botArchiver.bot.remove_webhook()
            botArchiver.bot.set_webhook(url='https://your_heroku_project.com/' + TOKEN)
            return "!", 200

    return app

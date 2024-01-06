from os import environ
from dotenv import load_dotenv

load_dotenv()


class Config:
    TUMBLR_CONSUMER_KEY = environ.get("TUMBLR_CONSUMER_KEY")
    TUMBLR_SECRET_KEY = environ.get("TUMBLR_SECRET_KEY")

    TUMBLR_BLOG_NAME = environ.get("TUMBLR_BLOG_NAME")


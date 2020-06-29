# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import praw
import os


def get_reddit_meme():
    client_id = os.environ['redditID']
    client_secret = os.environ['redditSecret']
    username = os.environ['redditUsername']
    password = os.environ['redditPassword']
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         password=password,
                         user_agent="testscript",
                         username=username)
    subreddit = reddit.subreddit("trippinthroughtime")
    for submission in subreddit.top(limit=1):
        url = submission.url
        return url


# Download the helper library from https://www.twilio.com/docs/python/install
def send_message(phone_numbers, joke):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = os.environ['accountSID']
    auth_token = os.environ['authToken']
    client = Client(account_sid, auth_token)

    for phoneNumber in phone_numbers:
        message = client.messages.create(
            media_url=joke,
            body='Welcome to the random meme generator',
            from_=os.environ['fromNumber'],
            to=phoneNumber
        )

        print(message.sid)


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
def lambda_handler(event, context):
    phone_numbers = [os.environ['phoneNumber1'], os.environ['phoneNumber2'], os.environ['phoneNumber3'],
                     os.environ['phoneNumber4'], os.environ['phoneNumber5'], os.environ['phoneNumber6'],
                     os.environ['phoneNumber7'], os.environ['phoneNumber8'], os.environ['phoneNumber9']]
    url = get_reddit_meme()
    send_message(phone_numbers, url)
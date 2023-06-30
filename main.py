
#import gspread

import  tweepy
import calendar
import datetime
#gc = gspread.service_account('credetials.json')

consumer_key = ''
consumer_secret = 'HQx4y034zCOVERquExLhWby2GQqroRvwbDKzx3pOhxfyq5wcYt'

token = '1663863564623331328-nWBRHeBx4oXZb4uUBsnQCCw0mNdr1G'
token_secret = 'UhHjsYYRutKaPFnUzNPwoUFlo1AilWBChybCoBtGpphsp'
#bearer_token = "AAAAAAAAAAAAAAAAAAAAAI2InwEAAAAAEKJRx23YKFH%2BETWKzk8wnFmhv5g%3DFg4l478h5sUD1hY9EPedx93vvcRLztb4QdpCnDY9nv6zL6pBh0"
#client_id = "UWk3bU9WRHVkM3BsM2JGdzQ1QlI6MTpjaQ"
#client_secret = "g_ALAkQV2QjCQrC7drhkHei5FmN_gY6IjsffFo1DaYra-AFz-X"

#t = Twitter(
#    auth=OAuth(token, token_secret, consumer_key, consumer_secret))
#t.home_timeline()
# Open a sheet from a spreadsheet in one go
#wks = gc.open("python-code").sheet1
#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(token, token_secret)
# Authenticate with bearer token
#auth = tweepy.AppAuthHandler(bearer_token = bearer_token)
#api = tweepy.API(auth)

# Verify the authentication
# Authenticate with OAuth 2.0 Client ID and Client Secret

#auth = tweepy.AppAuthHandler(client_id, client_secret)
#auth.apply_auth()

# Create the API object
#api = tweepy.API(auth)

# Verify the authentication

#api.verify_credentials()
#print("Authentication successful")


# Get the current month and year
#now = datetime.datetime.now()
#current_month = now.month
#current_year = now.year
# Calculate the number of tweets posted in the current month
#tweets_month = api.user_timeline(count=10)
#tweets_count = sum(1 for tweet in tweets_month if tweet.created_at.month == current_month and tweet.created_at.year == current_year)


# Check if the tweet limit has been reached
#if tweets_count >= 10:
    #print("Tweet limit reached for this month. Unable to post.")
#else:
    # Compose and post the tweet
    #tweet = "Hello, Twitter! This is my tweet using Tweepy and the Twitter API. #Tweepy #API"
    #api.update_status(tweet)
    #print("Tweet posted successfully!")

# Update a range of cells using the top left corner address
#wks.update('A1', [[1, 2], [3, 4]])

# Or update a single cell
#wks.update('B42', "it's down there somewhere, let me take another look.")

# Format the header
#wks.format('A1:B1', {'textFormat': {'bold': True}})
#  read tweets update a   range of cells using the top left corner   address
#next_tweets =wks.acell('A2').value
# post tweet through   twitter Api

#delete tweet row

import requests
import datetime
from requests_oauthlib import OAuth1

# Define your Twitter API credentials
API_KEY = "kLRKz8dhGTPv2XfXoeZj2fs9T"
API_SECRET = "4Bkmcqd1MKg6Qld7rrInbtdVmfQqnJpNG0FNTcOOdwSPECfoHf"
ACCESS_TOKEN = "1663863564623331328-5LKy5EumFS43254JrzbM0obbuOm5Rb"
ACCESS_TOKEN_SECRET = "2bX4BhSn28m9jw6Huz3ccDbgIPPqmBBlW2eaG1JsfrQP3"

# Create the tweet message with the current date
current_date = datetime.date.today().strftime("%Y-%m-%d")
tweet_message = f"Today's date is: {current_date}"

# Construct the API endpoint URL
url = "https://api.twitter.com/1.1/statuses/update.json"

# Set the OAuth1 authentication credentials
auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Set the request parameters
params = {
    "status": tweet_message
}

# Send the API request to post the tweet
response = requests.post(url, auth=auth, params=params)

# Check the API response
if response.status_code == 200:
    tweet_data = response.json()
    created_at = tweet_data["created_at"]
    print(f"Tweet posted successfully at {created_at}.")
else:
    print(f"Error occurred while posting the tweet. Status code: {response.status_code}.")
    print(response.text)



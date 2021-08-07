import tweepy # Use "pip install tweepy" in the command line

# To gain access to the Twitter API keys, create a developer account
# https://developer.twitter.com/en/apply-for-access

# Once your account is set up, create a new project. You will then recieve unique authentication keys
# Configuring authentication data:
auth = tweepy.OAuthHandler("<Consumer_Access_Key>", "<Consumer_Access_Secret_Key>")
auth.set_access_token("<Access_Token>", "<Access_Token_Secret>")

# Authenticating and creating api for extracting data
api = tweepy.API(auth)

# Returns data structure consisting of all tweet objects under a certain account
# Index 0 is the most recent tweet
tweets = api.user_timeline(screen_name = '<Account Tag>', count = 100, include_rts = True)

pfp = tweets[0].user.profile_image_url # Profile Picture Image URL
tweet = tweets[0].text # Tweet Text
date = tweets[0].created_at # Tweet Time Stamp
verified = tweets[0].user.verified # Boolean for verification (True if verified)
link = "https://twitter.com/twitter/statuses/" + str(tweets[0].id) # Tweet URL

import json
import twitter

ConsumerKey = 'ConsumerKey'
ConsumerSecret = 'ConsumerSecret'
OwnerId = 'OwnerId'
AccessToken = 'AccessToken'
AccessSecret = 'AccessSecret'

def main():
	config = {}
with open('config.json') as config_file:
	config = json.load(config_file)

	api = twitter.Api(consumer_key=config[ConsumerKey],
		consumer_secret=config[ConsumerSecret],
		access_token_key=config[AccessToken],
		access_token_secret=config[AccessSecret])

	print api.statuses.home_timeline(count=5)



if __name__ == '__main__':
	main()
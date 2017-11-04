import json
import time
import argparse
import twitter

DEFAULT_TWEET_COUNT = 10
DEFAULT_USER_NAME = '_glocks'

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', required=False, help='Number of tweets since latest to check if favorited')
    parser.add_argument('-u', '--user', required=False, help='Twitter Username')
    return parser.parse_args()

def dispense_candy(count):
    print "Dispensing {} Candy".format(count)

def main():
    args = parse_args()
    tweet_count = args.count
    if tweet_count == None or tweet_count == 0:
        tweet_count = DEFAULT_TWEET_COUNT

    config = {}
    with open('config.json') as config_file:
        config = json.load(config_file)


    print "----- Starting Up Tweet Sweets ------"

    api = twitter.Api(consumer_key=config['ConsumerKey'],
        consumer_secret=config['ConsumerSecret'],
        access_token_key=config['AccessToken'],
        access_token_secret=config['AccessSecret'])

    all_statuses = api.GetUserTimeline(screen_name=config['UserName'], count=tweet_count)
    status_favorites = {}

    # Get initial status favorite counts
    for status in all_statuses:
        status_favorites[status.id] = status.favorite_count

    try:
        while (True):
            print "SCANNING TWEET FAVS..."
            for id,favs in status_favorites.iteritems():
                current_status = api.GetStatus(id)
                if current_status.favorite_count > favs:
                    print "New Favorite(s) Detected for {}".format(id)
                    new_count = current_status.favorite_count - favs
                    dispense_candy(new_count)
                    status_favorites[id] = current_status.favorite_count
            print "SLEEPING FOR 10 SECONDS..."
            time.sleep(10)
    finally:
        print "----- Shutting down Tweet Sweets ------"

if __name__ == '__main__':
    main()

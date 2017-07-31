import twitter
import time
import configparser
import os
import gybc

keysconfig = os.path.join(gybc.GYBC_PATH, 'gybc', 'twitterkeys.cfg')
config = configparser.ConfigParser()
config.read(keysconfig)

api = twitter.Api(consumer_key=config['twitterkeys']['consumer_keys'],
                      consumer_secret=config['twitterkeys']['consumer_secret'],
                      access_token_key=config['twitterkeys']['access_token_key'],
                      access_token_secret=config['twitterkeys']['access_token_secret'])

statuses = api.GetUserTimeline(195082066, count=200)


f = open(os.path.join(gybc.GYBC_PATH, '..', '..', 'bin' 'archive.txt'), 'w')
last_id = statuses[-1].id
count=len(statuses)

while statuses:
    print("Last id: %s, count: %s" % (last_id, count))
    for status in statuses:
        f.write("%s\n" % status.text.replace("\n", " "))
    time.sleep(10)
    statuses = api.GetUserTimeline(195082066, count=200, max_id = last_id-1)
    last_id = statuses[-1].id
    count += len(statuses)
f.close()
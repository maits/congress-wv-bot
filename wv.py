from twython import Twython
import time

API_KEY = 'zX9kWz5W33iF0JGWHDCCKEhko'
API_SECRET = 'XXXXX'
ACCESS_TOKEN = 'XXXXX'
ACCESS_TOKEN_SECRET = 'XXXXX'

twitter = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#twitter.update_status(status= "")

filename=open('intro.txt', 'r')
f=filename.readlines()
filename.close()

for line in f:
    twitter.update_status(status=line)
    time.sleep(1)

print "DONE!"

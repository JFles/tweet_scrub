"""
    Script: scrub_tweets.py
    Author: Jeremy Fleshman
    Intent: Pull list of tweets for an associated user using Twitter's
             public API and store them locally for parsing/filtering.
            Filter tweets with specified keyword filters.
            Use Twitter API to delete list of filtered tweets.
            Confirm that tweets are no longer available for user.
    Notes: - Should this have an option to archive instead of delete?
           - Should there be an option to echo the tweet body and ask
              for action via CLI/GUI?
"""
# modules
import requests 

########
# Steps
########
# retrieve tweets for specified user
# save response in a file (only {"Id": "Body"} needed? TBD)
# process tweet bodies against a filter
# save some ID of each filtered tweet (separate file?)
# read in IDs from filtered list and delete/archive each (API call?)

# (testing) open file and write to it
# with open('scrap.txt', 'w') as f: # add 'w' to enable file write mode
#     for i in range(5):
#         f.write("test\n")
#     print("text added to {}", f) # autocloses file at end of block

# with open('scrap.txt') as f:
#     READ_DATA = f.read()
#     print("Reading data from {}:", f)
#     print(READ_DATA)

# call api
# test code for 'requests'
response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))
# print(response)

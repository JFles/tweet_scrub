"""
    Script: scrub_tweets.py
    Author: Jeremy Fleshman
    Date: 03/22/2018
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
import requests # for making the API call
import json # for parsing the JSON response

########
# Steps
########
# retrieve tweets for specified user
# save response in a file (only {"Id": "Body"} needed? TBD)
# process tweet bodies against a filter
# save some ID of each filtered tweet (separate file?)
# read in IDs from filtered list and delete/archive each

# call api
# test code for 'requests'
# response = requests.get('https://httpbin.org/ip')

# print('Your IP is {0}'.format(response.json()['origin']))
# print(response)

# http://docs.python-requests.org/en/master/user/quickstart/
response = requests.get('https://api.github.com/events')
if response.ok:
    print("successful reply from server")
    # print(response.json())
    with open('ghApiResp.json', 'w') as file:
        try:
            # file.write(response.json()) # fails - write() accepts str only
            file.write(json.dumps(response.json())) # succeeds - parses and saves properly
        except Exception as e:
            print("~Error: ", e)
        else:
            print("Response saved successfully!")


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
# import oauth2 # for authentication of API calls
from requests_oauthlib import OAuth1

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

"""
    Twitter API:
        # oauth authentication
        https://developer.twitter.com/en/docs/basics/authentication/overview/oauth
        https://developer.twitter.com/en/docs/basics/authentication/guides/authorizing-a-request
        https://developer.twitter.com/en/docs/basics/authentication/guides/single-user

        # twitter app management
        https://apps.twitter.com/
        # implement 3-leg OAuth
        https://developer.twitter.com/en/docs/basics/authentication/overview/3-legged-oauth
        # 

        # timeline endpoint to retrieve user tweets
        https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline
        # timeline best practices
        https://developer.twitter.com/en/docs/tweets/timelines/guides/working-with-timelines

        # destroy using 'id'
        https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-destroy-id
"""

# authenticate user
# get tweets for user
payload = {"screen_name": "jefles", "count": 2}
auth = OAuth1(APP_KEY, APP_SECRET, USER_OAUTH_TOKEN, USER_OAUTH_TOKEN_SECRET)
response = requests.get("https://api.twitter.com/1.1/statuses/user_timeline.json", params=payload, auth=auth)
if response.ok:
    print("successful reply from server")
    # print(response.json())
    with open('timelineApiResp.json', 'w') as file:
        try:
            # file.write(response.json()) # fails - write() accepts str only
            file.write(json.dumps(response.json(), sort_keys=True, indent=4)) # succeeds - parses and saves properly
            resp_obj = response.json()
        except Exception as e: #TODO replace with proper exception (or add specific handler and keep this as a generic case?)
            print("~Error: ", e)
        else:
            print("Response saved successfully!")
else:
    #TODO - Add proper error handling for non 200 response
    print("wut in tarnation")

# stitched together test API call for testing
# TODO - Replace with Twitter API call to get list of tweets (Have to be authenticated)
# TODO - Refactor call into a function
"""
# test code using sample public API
response = requests.get('https://api.github.com/events')
if response.ok:
    print("successful reply from server")
    # print(response.json())
    with open('ghApiResp.json', 'w') as file:
        try:
            # file.write(response.json()) # fails - write() accepts str only
            file.write(json.dumps(response.json(), sort_keys=True, indent=4)) # succeeds - parses and saves properly
            resp_obj = response.json()
        except Exception as e: #TODO replace with proper exception (or add specific handler and keep this as a generic case?)
            print("~Error: ", e)
        else:
            print("Response saved successfully!")
"""

# loop through a nested dictionary, compare against a list of keywords, add id for each offending tweet

"""
# debug
print("Response = {0} || Val = {0}".format(type(respObj), respObj))
print("First Index of JSON obj = {0} || Val = {1}".format(type(respObj[0]), respObj[0]))
print("Nested Key = {0} || Val = {1}".format(type(respObj[0]["id"]), respObj[0]["id"]))

# response is a list(python array)
# In each index is a dictionary
# Can probably use multiple nested loops to traverse and filter after json obj struct known
"""

# print(type(respObj))
# print(len(respObj))
# print(respObj[0])

"""
filtered_id = []
filtered_url = [] #TODO zip these together so they loop at the same time
# count = 0
for resp_obj_dict in resp_obj:
    # print("{}\n".format(index))
#     print(type(resp_obj_dict))
#     count += 1
# print(count)
    for key, value in resp_obj_dict.items():
        # print(key)
        # print(value)
        if key == "id":
            filtered_id.append(value)
        elif key == "org":
            filtered_url.append(value["url"])
    # print("\n")

print(len(filtered_id))
print(len(filtered_url))
"""

# dictionary = {"a": 1, "b": 2, "c": "test"} # can be mixed types
# print(dictionary["a"])

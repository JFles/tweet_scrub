"""
    Script: scrub_tweets.py
    Author: Jeremy Fleshman
    Intent: Pull list of tweets for an associated user using Twitter's public API and store
              them locally for parsing/filtering.
            Filter tweets with specified keyword filters.
            Use Twitter API to delete list of filtered tweets.
            Confirm that tweets are no longer available for user.
    Notes: - Should this have an option to archive instead of delete?
           - Should there be an option to echo the tweet body and ask for action via CLI/GUI?
"""

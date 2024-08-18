#!/usr/bin/python3
""" Recurse it """

import requests

def recurse(subreddit, hot_list=[], after=None):
    """ returns a list containing the titles of all hot
    articles for a given subreddit """
    if (after):
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
            subreddit, after)
    else:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url, headers={'User-agent': '1-top_ten.'})
    if (res.status_code != 200):
        return None
    res = res.json()
    for post in res['data']['children']:
        hot_list.append(post['data']['title'])
    after = res['data']['after']
    if (not after):
        return hot_list
    return recurse(subreddit, hot_list, after)


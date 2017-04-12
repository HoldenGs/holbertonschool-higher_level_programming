#!/usr/bin/python3

if __name__ == '__main__':
    """
    This program searches twitter for a parameter given as an argument

    Usage: ./103-search_twitter.py <consumer_key> <consumer_secret> <param>
    """
    import base64
    from sys import argv
    import requests

    hashtag = argv[3]
    hashtag = hashtag.replace("#", "23")
    search_url = "https://api.twitter.com/1.1/search/tweets.json?q=%" + hashtag
#    search_url = 'https://api.twitter.com/1.1/search/tweets.json'
    auth_url = 'https://api.twitter.com/oauth2/token'
    consumer_key = argv[1]
    consumer_secret = argv[2]
    bearer_token = '{}:{}'.format(consumer_key, consumer_secret)
    bearer_token_encoded = base64.b64encode(bearer_token.encode('ascii'))
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Authorization': 'Basic {}'
        .format(bearer_token_encoded.decode('ascii'))
    }
    data = 'grant_type=client_credentials'
    r = requests.post(auth_url, headers=headers, data=data)

    access_token = r.json()['access_token']
    search_header = {'Authorization': 'Bearer {}'.format(access_token)}
#    params = {'q': argv[3]}
    response = requests.get(search_url, headers=search_header)

    tweets = []
    count = 0
    for tweet in response.json()['statuses']:
        count += 1
        if count > 5:
            break
        tweets.append('[{}] {} by {}'.format(tweet['id'], tweet['text'],
                                             tweet['user']['name']))
    print('\n'.join(tweets))

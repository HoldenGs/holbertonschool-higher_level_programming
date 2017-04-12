#!/usr/bin/python3

if __name__ == '__main__':
    import base64
    from sys import argv
    import requests

    search_url = 'https://api.twitter.com/1.1/search/tweets.json'
    auth_url = 'https://api.twitter.com/oauth2/token'
    consumer_key = argv[1]
    consumer_secret = argv[2]
    bearer_token = '{:s}:{:s}'.format(consumer_key, consumer_secret)
    bearer_token_encoded = base64.b64encode(bearer_token.encode('ascii'))
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Authorization': 'Basic {}'
        .format(bearer_token_encoded.decode('ascii'))
    }
    data = 'grant_type=client_credentials'
    r = requests.post(auth_url, headers=headers, data=data)

    params = {'q': argv[3]}
    access_token = r.json()['access_token']
    search_header = {'Authorization': 'Bearer {}'.format(access_token)}
    response = requests.get(search_url, params=params, headers=search_header)

    tweets = []
    for tweet in response.json()['statuses']:
        tweets.append('[{}] {} by {}'.format(tweet['id'], tweet['text'],
                                             tweet['user']['name']))
    print('\n'.join(tweets))

import requests
import json
import os

from urls import get_url
from TweetStats import TweetStats

auth_bearer_code = "Bearer " + os.environ.get("AUTH_BEARER_CODE")
x_guest_token = os.environ.get("X_GUEST_TOKEN")


def lambda_handler(event, context):
    tweet_Id = event["body"]
    _url = get_url(tweet_Id)
    _headers = {
        'Authorization': auth_bearer_code,
        'X-Guest-Token': x_guest_token
    }

    try:        
        response = requests.get(_url, headers = _headers)
        data = json.loads(response.content)
        stats = TweetStats.fromJson(data)
        print(stats.__dict__)
        return {
            'statusCode': 200,
            'body': json.dumps('Suceeded.')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error : {str(e)}')
        }
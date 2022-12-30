# Before connecting to the stream, you'll need Twitter Developer account and to set up your rules you'll filter the stream for:
# https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule

import requests
import os
import json

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your bearer token here>'
bearer_token = os.environ.get("BEARER_TOKEN")

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FilteredStreamPython"
    return r

# You can edit the URL in the function with whatever query parameters you want:
# https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/get-tweets-search-stream
  
def get_stream(set):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream", auth=bearer_oauth, stream=True,
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            print(json.dumps(json_response, indent=4, sort_keys=True))

get_stream(set)

# You can close the stream with CTRL+C in terminal

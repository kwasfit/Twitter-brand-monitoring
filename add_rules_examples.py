# Super basic rules to get you started with the Twitter filtered stream API if you're
# interested in brand monitoring. Find more customization here: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule

curl -X POST 'https://api.twitter.com/2/tweets/search/stream/rules' \
-H "Content-type: application/json" \
-H "Authorization: Bearer <bearer token here>" -d \
'{
  "add": [
    {"value": "#<your brand name here>", "tag": "hashtag <your brand name here>"},
    {"value": "<your brand name here>", "tag": "<your brand name here> name in plaintext"},
    {"value": "@<your brand name here>", "tag": "<your brand name here> account mention"},
    {"value": "<your brand name here> url_contains:<your brand name here>", "tag": "<your brand name here> in URL"}
  ]
}'

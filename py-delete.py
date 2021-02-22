# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 09:41:08 2021

@author: ebart
"""

#!/usr/bin/env python3

import json
import requests
import os



## Now we'll use the Github token to authenticate you to and create a
## simple gist.

token = os.getenv('GITHUB_TOKEN')

url = "https://api.github.com/gists"
data = {
    "public": True,
    "files": {
        "ds3002.py": {
            "content": "'Hello':'World'"
        },
    }
}
headers = {'Authorization': f'token {token}'}
r = requests.post(url, headers=headers, data=json.dumps(data))
# print(r.json())

## Visit this URL and you can see your new gist:
print("Your new gist has been created: ")

# Put the response into json to parse
d = r.json()
# Grab the html_url value:
link = d['html_url']
print(link)
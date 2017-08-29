#!/usr/bin/env python3
#

import argparse
import hashlib
import hmac
import json
import requests
import os


github_events = ['push', 'pull_request', 'issue_comment',
                 'pull_request_review', 'status']
parser = argparse.ArgumentParser()
parser.add_argument('event', help='The type of GitHub event',
                    choices=github_events)
parser.add_argument('filename', help='The json file to send')
parser.add_argument('--url', help='The URL to send.',
                    default='http://localhost:8001/connection/github/payload')
parser.add_argument('--token', help='Webhook secret for signing',
                    default='00000000000000000000000000000000000000000')

options = parser.parse_args()

with open(os.path.expanduser(options.filename)) as json_file:
    data = json.load(json_file)


request = requests.Request('POST', options.url, json=data).prepare()

signature = 'sha1=' + hmac.new(options.token.encode('utf-8'), request.body,
                               hashlib.sha1).hexdigest()

request.headers.update({'Content-Type': 'application/json',
                  'X-Github-Event': options.event,
                  'X-Hub-Signature': signature,
                  'X-GitHub-Delivery': 'derp'})

with requests.Session() as s:
    resp = s.send(request)

print(resp)

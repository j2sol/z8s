#!/usr/bin/env python3
#

import argparse
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

options = parser.parse_args()

with open(os.path.expanduser(options.filename)) as json_file:
    data = json.load(json_file)

s = requests.session()
s.headers.update({'Content-Type': 'application/json',
                  'X-Github-Event': options.event})

s.post(options.url, json=data)

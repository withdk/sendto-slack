#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Quick lib to send messages to Slack.

@DK 2021
"""

import json
import requests
from config import config

class SendToSlack():

    def __init__(self, channel, token):
        self.channel = channel
        self.token = token

    def post_message_to_slack(self, text, blocks = None):
        return requests.post('https://slack.com/api/chat.postMessage', {
        'token': self.token,
        'channel': self.channel,
        'text': text,
        'icon_url': None,
        'username': None,
        'blocks': json.dumps(blocks) if blocks else None
        }).json()

if __name__ == "__main__":
    s = SendToSlack(config.channel,config.token)
    s.post_message_to_slack("message")

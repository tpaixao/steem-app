#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 13:55:25 2017

@author: pnbrown
"""

import signal
import logging

class DelayedKeyboardInterrupt(object):
    def __enter__(self):
        self.signal_received = False
        self.old_handler = signal.getsignal(signal.SIGINT)
        signal.signal(signal.SIGINT, self.handler)

    def handler(self, sig, frame):
        self.signal_received = (sig, frame)
        logging.debug('SIGINT received. Delaying KeyboardInterrupt.')

    def __exit__(self, type, value, traceback):
        signal.signal(signal.SIGINT, self.old_handler)
        if self.signal_received:
            self.old_handler(*self.signal_received)

START_BLOCK = 1
GENESIS_INTERVAL = (14*24*60)*20 # 14 days, 20 blocks/minute
GENESIS_ACCOUNT = 'biophil'
GENESIS_POSTS_TH = 5
GENESIS_CREDIT = 1000001
TOKEN_NAME = 'pocket'
SAVE_INTERVAL = 10*20 # 10 minutes, 20 blocks/minute
GRAPHENE_DATE_FORMAT_STRING = '%Y-%m-%dT%H:%M:%S'
FEE = 1
GENESIS_PERMLINK = 'genesis-' + TOKEN_NAME
GENESIS_IDENTIFIER = '@' + GENESIS_ACCOUNT + '/' + GENESIS_PERMLINK

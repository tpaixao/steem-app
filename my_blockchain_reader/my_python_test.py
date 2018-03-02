#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import steembase
from steembase.account import PasswordKey
import steem

steembase.chains.known_chains['STEEM'] = {
    'chain_id': '79276aea5d4877d9a25892eaa01b0adf019d3e5cb12a97478df3298ccdd01673',
    'prefix': 'STX', 'steem_symbol': 'STEEM', 'sbd_symbol': 'SBD', 'vests_symbol': 'VESTS'
}

client = steem.Steem(['https://testnet.steem.vc'])

balance = client.get_account('tiago')['balance']

# print(balance)

# key_dict = client.get_account('tiago').keys()

# account = 'tiago'
# password = 'paixao'
account = 'tiagotest'
password = 'tiagotest'
key_types = ['posting','active','owner','memo','foobar']

print(account,'\n',password)

# for key_type in key_types:
    # private_key = PasswordKey(account, password, key_type).get_private_key()
    # public_key = private_key.pubkey

    # print('Private ' + key_type + ' key: ' + str(private_key))
    # print('Public ' + key_type + ' key: ' + str(public_key) + '\n')

# try to post something wth these keys that do NOT seem to be working with steem-js

s = steem.Steem(['https://testnet.steem.vc'],keys=['5J8UmwoWoySnkjfdrR9BDLjPVAmsDfof6ovqXVZXCfM3ZYZxVSA'])



title='this is a post that i just made'
body = 'a body is a body is a body'
author='tiagotest'
permlink = 'this-is-a-post-that-i-just-made'
reply_indentifier = ''
json_metadata = None
comment_options = None
community = None
tags = ['tag1','tag2'] #tags NEED to be set
beneficiaries = []
self_vote = False

s.commit.post(title,body,author,permlink,reply_indentifier,json_metadata,comment_options,community,tags)


# s.commit.post(title,body,permlink,reply_indentifier,json_metadata,comment_options,community,tags,beneficiaries,self_vote)



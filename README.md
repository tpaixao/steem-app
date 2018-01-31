# STEEM environment

## Setting up

### setting up python

we require python3.6. For Linux Mint this could be a problem (install Anaconda)

```bash 
apt install virtualenv
pip3 install -U git+git://github.com/Netherdrake/steem-python
```
to activate the environment:
```bash
source ./steem/bin/activate
```


activating the testnet:
```
```

### setting up steem-js

```bash
sudo npm install --save steem
sudo npm install http-server -g
```
switching to the testnet
```javascript
steem.config.set('websocket','wss://testnet.steem.vc')
steem.config.set('address_prefix', 'STX')
steem.config.set('chain_id', '79276aea5d4877d9a25892eaa01b0adf019d3e5cb12a97478df3298ccdd01673')
```

# STEEM environment

## setting up python

we require python3.6. For Linux Mint this could be a problem (install Anaconda)

```bash
sudo apt install virtualenv
pip3 install -U git+git://github.com/Netherdrake/steem-python
```
to activate the environment:
```bash
source ./steem/bin/activate
```


### steem-js



```bash
sudo npm install --save steem
sudo npm install http-server -g
```
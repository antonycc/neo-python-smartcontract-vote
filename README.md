Overview
========

A demonstration of a voting system using NEO Smart Conracts on a private blockchain consensus network

Useful addresses:
* NEO: c56f33fc6ecfcd0c225c4ab356fee59390af8560be0e930faebe74a6daff7c9b
* GAS: 602c79718b16e442de58778e148d0b1084e3b2dffd5de6b7b16cee7969282de7

Resources
=========

Links:
* [NEO Python](https://github.com/CityOfZion/neo-python)
* [Prompt](https://neo-python.readthedocs.io/en/latest/prompt.html)
* [CLI](http://docs.neo.org/en-us/node/cli/cli.html)
* [API](https://github.com/neo-project/docs/tree/master/en-us/node/cli/2.7.6/api)
* [API reference](https://github.com/neo-project/neo/wiki/API-Reference)
* [NEO Python docker](https://hub.docker.com/r/cityofzion/neo-python/)
* [NEO private net](hhttps://hub.docker.com/r/cityofzion/neo-privatenet/)
* [NEO Python compiler](https://github.com/CityOfZion/neo-boa)
* [Smart Contracts](http://neo-python.readthedocs.io/en/latest/neo/SmartContract/smartcontracts.html)
* [Smart Contracts Workshop](https://github.com/CityOfZion/python-smart-contract-workshop)
* [Smart Contract Examples](https://github.com/CityOfZion/neo-smart-contract-examples/blob/master/README.md)
* [Screen](https://kb.iu.edu/d/acuy)

Demo steps
==========

Start network
-------------

Download and start private net and two neo nodes:
```bash
$ docker pull cityofzion/neo-privatenet
$ docker pull cityofzion/neo-python
$ # To kill all instances on this host: docker kill $(docker ps -q)
$
```

Start private net and two neo nodes on different terminals and connent.

4 Node NEO consensus network:
```bash
tty1 $ docker run --rm -d --name neo-privatenet -p 20333-20336:20333-20336/tcp -p 30333-30336:30333-30336/tcp cityofzion/neo-privatenet
tty1 $ docker exec -it neo-privatenet /bin/bash
tty1 root@neo-python:/neo-python# screen -ls
tty1 root@neo-python:/neo-python# screen -r node1
<ctrl-a> d
tty1 root@neo-python:/neo-python#
# To stop:
# $ docker ps | grep private
# $ docket kill <the.leftmost.number>
```

NEO monitor node with root wallet:
```bash
tty2 $ docker run --rm -it --net=host -v $(pwd):/neo-python/sc -h neo-python --name neo-python cityofzion/neo-python /bin/bash
tty2 root@neo-python:/neo-python# np-prompt -p -v
tty2 neo># open wallet neo-privnet.wallet
<"coz">
tty2 neo># wallet
... truncated ...
    "height": 9366,
    "percent_synced": 100,
    "synced_balances": [
        "[NEO]: 100000000.0 ",
        "[NEOGas]: 74679.9999 "
    ],
    "public_keys": [
        {
            "Address": "AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y",
            "Public Key": "031a6c6fbbdf02ca351745fa86b9ba5a9452d785ac4f7fc2b7548ca2a46c4fcf4a"
        }
    ],
... truncated ...
```

NEO client with new wallet
```bash
tty3 $ docker run --rm -it --net=host -v $(pwd):/neo-python/sc -h neo-python-client --name neo-python-client cityofzion/neo-python /bin/bash
tty3 root@neo-python:/neo-python# np-prompt -p -v
tty3 neo># create wallet neo-client.wallet
[password]> ********** <"ababababab">                                                                    
[password again]> ********** <"ababababab">
... truncated ...
    "height": 0,
    "percent_synced": 0,
    "synced_balances": [],
    "public_keys": [
        {
            "Address": "AaP232YEsqkptMrjsNfLCateZquXwFADLQ",
            "Public Key": "02e22be69743d53e0650ddad7384c31354c04e75dbf9b614da08e4ea042225de0b"
        }
    ],
... truncated ...
```

Test network
-------------

Fund the client wallet from the root wallet with NEO and GAS:
```bash
tty2 neo># open wallet neo-privnet.wallet
<"coz">
tty2 neo># wallet
... truncated ...
    "synced_balances": [
        "[NEO]: 100000000.0 ",
        "[NEOGas]: 74679.9999 "
    ],
... truncated ...
tty2 neo># send NEO <neo-client.wallet address> 10000
<"coz">
tty2 neo># send GAS <neo-client.wallet address> 5000 
<"coz">
tty2 neo># wallet
... truncated ...
    "synced_balances": [
        "[NEO]: 99990000.0 ",
        "[NEOGas]: 69679.9999 "
    ],
... truncated ...
```

Observe the updated client wallet:
```bash
tty3 neo># open wallet neo-client.wallet
<"ababababab">                                                                    
... truncated ...
    "synced_balances": [
        "[NEO]: 10000.0 ",
        "[NEOGas]: 5000.0 "
    ],
    "public_keys": [
        {
            "Address": "AaP232YEsqkptMrjsNfLCateZquXwFADLQ",
            "Public Key": "02e22be69743d53e0650ddad7384c31354c04e75dbf9b614da08e4ea042225de0b"
        }
    ],
... truncated ...
```


Deploy and test contract
------------------------

Compile a smart contract distribution in a local workspace
```bash
$ mkdir -p './avm'
$ cd neo-boa-compiler/
$ docker build --tag neo-boa-compiler .
$ docker run -it --rm -v $(pwd)/../sc:/python-contracts -v $(pwd)/../awm:/compiled-contracts neo-boa
$ cd ..
$ 
```

Deploy a notifying contract and execite it, viewing the output on the monitor nodes:
```bash
$ TODO
```


Deploy a contract with storage and execite it, viewing the output on the monitor nodes:
```bash
 $ TODO
```


Deploy a contract with storage for voting and execite it, viewing the output on the monitor nodes:
```bash
 $ TODO
```


Voting using the API
--------------------

Invoke API to cast a VOTE
```bash
 $ TODO
```

Invoke API to query the result
```bash
 $ TODO
```


Multiple voters
---------------

Create new wallet and Invoke API to cast a VOTE
```bash
 $ TODO
```

TODO: The first voter fails to vote twice
```bash
 $ TODO
```


View the result in a web page
-----------------------------

Link and screen shot.
[TODO]
[TODO]


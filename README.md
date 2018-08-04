Overview
========

A demonstration of a voting system using NEO Smart Conracts on a private blockchain consensus network

For NEO: c56f33fc6ecfcd0c225c4ab356fee59390af8560be0e930faebe74a6daff7c9b
For GAS: 602c79718b16e442de58778e148d0b1084e3b2dffd5de6b7b16cee7969282de7

Resources
=========

[NEO Python](https://github.com/CityOfZion/neo-python)
[Prompt](https://neo-python.readthedocs.io/en/latest/prompt.html)
[CLI](http://docs.neo.org/en-us/node/cli/cli.html)
[API](https://github.com/neo-project/docs/tree/master/en-us/node/cli/2.7.6/api)
[API reference](https://github.com/neo-project/neo/wiki/API-Reference)
[NEO Python docker](https://hub.docker.com/r/cityofzion/neo-python/)
[NEO private net](hhttps://hub.docker.com/r/cityofzion/neo-privatenet/)
[NEO Python compiler](https://github.com/CityOfZion/neo-boa)
[Smart Contracts](http://neo-python.readthedocs.io/en/latest/neo/SmartContract/smartcontracts.html)
[Smart Contracts Workshop](https://github.com/CityOfZion/python-smart-contract-workshop)
[Smart Contract Examples](https://github.com/CityOfZion/neo-smart-contract-examples/blob/master/README.md)

Demo steps
==========

Start network
-------------

Download and start private net and two neo nodes:
```bash
$ docker pull cityofzion/neo-privatenet
$ docker pull cityofzion/neo-python
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
tty2 /# np-prompt -p -v
tty3 $root@neo-python:/neo-python#
```

NEO client with new wallet
```bash
tty3 $ docker run --rm -it --net=host -v $(pwd):/neo-python/sc -h neo-python-client --name neo-python-client cityofzion/neo-python /bin/bash
tty2 /# np-prompt -p -v
tty3 $
```


Test network
-------------

Create a new private wallet and fund it from the shipped wallet:
```bash
 $ TODO
```


Deploy and test contract
------------------------

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


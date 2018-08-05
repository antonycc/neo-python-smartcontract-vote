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
tty2 neo> open wallet neo-privnet.wallet
<"coz">
tty2 neo> wallet
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
tty3 neo> create wallet neo-client.wallet
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
tty2 neo> open wallet neo-privnet.wallet
<"coz">
tty2 neo> wallet
... truncated ...
    "synced_balances": [
        "[NEO]: 100000000.0 ",
        "[NEOGas]: 74679.9999 "
    ],
... truncated ...
tty2 neo> send NEO <neo-client.wallet address> 10000
<"coz">
tty2 neo> send GAS <neo-client.wallet address> 5000 
<"coz">
tty2 neo> wallet
... truncated ...
    "synced_balances": [
        "[NEO]: 99990000.0 ",
        "[NEOGas]: 69679.9999 "
    ],
... truncated ...
```

Observe the updated client wallet:
```bash
tty3 neo> open wallet neo-client.wallet
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

Build and test a contract using the NEO prompt
```bash
tty3 neo># config sc-events on
tty3 neo># build sc/sc/hello-world.py test '' 01 False False
```

Build then import a contract and supply meta-data
```bash
tty3 neo> build sc/sc/hello-world.py
tty3 neo> import contract sc/sc/hello-world.avm '' 01 False False 
[Contract Name] > hello-world01                                                          
[Contract Version] > 0.0.1                                                           
[Contract Author] > client                                                                     
[Contract Email] > client@local                                                                        
[Contract Description] > Hello World Contract
[password]> ********** <"ababababab">
```

Note the script hash:
```bash
[I 180805 19:59:20 EventHub:58] [test_mode][SmartContract.Contract.Create] [09a129673c61917593cb4b57dce066688f539d15] {'type': 'InteropInterface', 'value': {'version': 0, 'code': {'hash': '0x09a129673c61917593cb4b57dce066688f539d15', 'script': '54c56b0b48656c6c6f20576f726c64680f4e656f2e52756e74696d652e4c6f67516c7566', ...   ... }}}
tty3 neo> contract 0x09a129673c61917593cb4b57dce066688f539d15
{
    "version": 0,
    "code": {
        "hash": "0x09a129673c61917593cb4b57dce066688f539d15",
        "script": "54c56b0b48656c6c6f20576f726c64680f4e656f2e52756e74696d652e4c6f67516c7566",
        "parameters": "10",
        "returntype": 1
    },
    "name": "hello-world01",
    "code_version": "0.0.1",
    "author": "client",
    "email": "client@local",
    "description": "Hello World Contract",
    "properties": {
        "storage": true,
        "dynamic_invoke": true
    }
}
```

Invoke the function and see logging on tty2 and tty3:
```bash
tty3 neo> testinvoke 0x09a129673c61917593cb4b57dce066688f539d15
...
tty2 neo> [I 180805 20:09:23 EventHub:62] [SmartContract.Runtime.Log][13894] [09a129673c61917593cb4b57dce066688f539d15] [tx 45eef678f288c854684c3d81bbac2131f1e6b07118ed3753a2d0d3776934fe73] {'type': 'String', 'value': 'Hello World'}
[I 180805 20:09:23 EventHub:62] [SmartContract.Execution.Success][13894] [09a129673c61917593cb4b57dce066688f539d15] [tx 45eef678f288c854684c3d81bbac2131f1e6b07118ed3753a2d0d3776934fe73] {'type': 'Array', 'value': [{'type': 'Integer', 'value': '1'}]}
...
tty3 neo> [I 180805 20:09:23 EventHub:62] [SmartContract.Runtime.Log][13894] [09a129673c61917593cb4b57dce066688f539d15] [tx 45eef678f288c854684c3d81bbac2131f1e6b07118ed3753a2d0d3776934fe73] {'type': 'String', 'value': 'Hello World'}
[I 180805 20:09:23 EventHub:62] [SmartContract.Execution.Success][13894] [09a129673c61917593cb4b57dce066688f539d15] [tx 45eef678f288c854684c3d81bbac2131f1e6b07118ed3753a2d0d3776934fe73] {'type': 'Array', 'value': [{'type': 'Integer', 'value': '1'}]}
```


Deploy a contract with storage and execite it, viewing the output on the monitor nodes:
```bash
tty2 neo> build sc/sc/balance_tracker.py test 070502 02 True False add AG4GfwjnvydAZodm4xEDivguCtjCFzLcJy 3   
tty2 neo> import contract sc/sc/balance_tracker.avm 070502 02 True False
tty2 neo> testinvoke 0x65bc18944450249f6658acc0a7ab81f5769ae6fe add AG4GfwjnvydAZodm4xEDivguCtjCFzLcJy 3 
...
[I 180805 20:32:25 EventHub:62] [SmartContract.Execution.Success][13971] [65bc18944450249f6658acc0a7ab81f5769ae6fe] [tx 75e8799e43dc1d046263913178faab5ccee00d799c1ae3eb503eb1b5c3e646d5] {'type': 'Array', 'value': [{'type': 'Integer', 'value': '3'}]}
```

Invoking the same contract from another wallet increases the balance:
```bash
tty3 neo> testinvoke 0x65bc18944450249f6658acc0a7ab81f5769ae6fe add AG4GfwjnvydAZodm4xEDivguCtjCFzLcJy 5
...
[I 180805 20:33:56 EventHub:62] [SmartContract.Execution.Success][13976] [65bc18944450249f6658acc0a7ab81f5769ae6fe] [tx cf4cfe8f5b74a82ac4fc4ec247f2eae744d68989fa30fb6964b62768ea4bd4d4] {'type': 'Array', 'value': [{'type': 'Integer', 'value': '8'}]}
```
(the output appears in both tty2 and tty3)


Deploy a contract with storage for voting and execite it, viewing the output on the monitor nodes:
```bash
 $ TODO
```

Deploy a smart contracts to cast a VOTE:
```bash
tty2 neo> build sc/sc/poll.py test 070710 02 True False 'create' 'test-poll' ['selection-1', 'selection-2']
tty2 neo> import contract sc/sc/poll.avm 070710 02 True False
tty2 neo> testinvoke 0x65bc18944450249f6658acc0a7ab81f5769ae6fe 'create' 'test-poll' ['selection-1', 'selection-2']
tty2 neo> testinvoke 0x65bc18944450249f6658acc0a7ab81f5769ae6fe 'select' 'test-poll' ['selection-1']
tty2 neo> testinvoke 0x65bc18944450249f6658acc0a7ab81f5769ae6fe 'result' 'test-poll' ['selection-1']
tty2 neo> testinvoke 0x65bc18944450249f6658acc0a7ab81f5769ae6fe 'freeze' 'test-poll' []
tty2 neo> testinvoke 0x65bc18944450249f6658acc0a7ab81f5769ae6fe 'delete' 'test-poll' []

```

Compile a smart contract distribution in a local workspace:
```bash
$ rm -rf './avm' && mkdir -p './avm'
$ cd neo-boa-compiler/
$ docker build --tag neo-boa .
$ docker run -it --rm -v $(pwd)/../sc:/python-contracts -v $(pwd)/../avm:/compiled-contracts neo-boa
$ cd ..
$ 
```
(Useful to build outside the NEO node prompt)


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




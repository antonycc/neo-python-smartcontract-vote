Overview
========

A demonstration of a voting system using NEO Smart Contracts on a private block-chain consensus network


Technologies used
-----------------

* Python
* Docker
* NEO Block-chain Smart Contracts
* neo-python


Current features
----------------

* Run a NEO private network and attach a wallet from the command line
* Deploy a simple NEO SmartContract on the private block-chain and invoke it
* Deploy a poll NEO SmartContract enforcing one for vote per poll per address


Backlog
-------

In a chronological order (suggested only) and broken into work packages.

Demo:
* [ ] Images in README
* [ ] Consistent return type
* [ ] Review links for duplicates and redundant sources
* [ ] Expose REST API on monitor node
* [ ] Consume REST API with Browser page
* [ ] Deploy to test net
* [ ] Consensus container configured for Wifi distributed private net
* [ ] Create Vagrant VM hosting everything with smart contract samples deployed
* [ ] Re-brand as "Neapolitan"

Code hygiene:
* [ ] Unit tests
* [ ] PEP-8 checker

Closed polls:
* [ ] Retain poll creator and allow creator to set fixed selection list
* [ ] Poll creator, creates wallet addresses for the selections

App:
* [ ] Change the notification wallet to a lite wallet suitable for embedding in an native app
* [ ] Deploy to test net with apps connected via a lite wallet

ICO:
* [ ] Overlay the voting rules with a NEP5 standard ICO (https://github.com/CityOfZion/neo-boa/blob/master/boa_test/example/demo/NEP5.py)
* [ ] Poll creation privilege requires contract currency
* [ ] Poll creator and voters need to be KYC registered
* [ ] Link to KYC service
* [ ] Deploy to Test net
* [ ] Deploy to Main net
* [ ] Contract currency exchanged for NEO


Resources
=========

Links:
* [NEO Python](https://github.com/CityOfZion/neo-python)
* [Docker](https://www.docker.com)
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
* [URL](https://en.wikipedia.org/wiki/Uniform_Resource_Name)
* [DotNet docs](http://docs.neo.org/en-us/sc/reference/fw/dotnet/neo.html)
* [NEO Smart Contract: Caller Validation]https://medium.com/coinmonks/neo-smart-contract-caller-validation-58d99f21232a)
* [https://github.com/CityOfZion/neo-smart-contract-examples](https://github.com/CityOfZion/neo-smart-contract-examples)

Useful addresses:
* NEO: c56f33fc6ecfcd0c225c4ab356fee59390af8560be0e930faebe74a6daff7c9b
* GAS: 602c79718b16e442de58778e148d0b1084e3b2dffd5de6b7b16cee7969282de7


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

Start private net and two NEO nodes on different terminals and connect.

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


Private network
---------------

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

Build and test a contract using the NEO prompt:
```bash
tty3 neo># config sc-events on
tty3 neo># build sc/sc/hello-world.py test '' 01 False False False
tty3 neo> 
```

Build then import a contract and supply meta-data:
```bash
tty3 neo> build sc/sc/hello-world.py
tty3 neo> import contract sc/sc/hello-world.avm '' 01 False False False
[Contract Name] > hello-world01                                                          
[Contract Version] > 0.0.1                                                           
[Contract Author] > client                                                                     
[Contract Email] > client@local                                                                        
[Contract Description] > Hello World Contract
[password]> ********** <"ababababab">
...
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
tty3 neo> 
```

Invoke the function and see logging on tty2 and tty3:
```bash
tty3 neo> testinvoke 0x09a129673c61917593cb4b57dce066688f539d15
...
[I 180805 20:09:23 EventHub:62] [SmartContract.Runtime.Log][13894] [09a129673c61917593cb4b57dce066688f539d15] [tx 45eef678f288c854684c3d81bbac2131f1e6b07118ed3753a2d0d3776934fe73] {'type': 'String', 'value': 'Hello World'}
[I 180805 20:09:23 EventHub:62] [SmartContract.Execution.Success][13894] [09a129673c61917593cb4b57dce066688f539d15] [tx 45eef678f288c854684c3d81bbac2131f1e6b07118ed3753a2d0d3776934fe73] {'type': 'Array', 'value': [{'type': 'Integer', 'value': '1'}]}
tty3 neo> 

tty2 neo> testinvoke 0x09a129673c61917593cb4b57dce066688f539d15
...
[I 180805 20:09:23 EventHub:62] [SmartContract.Runtime.Log][13894] [09a129673c61917593cb4b57dce066688f539d15] [tx 45eef678f288c854684c3d81bbac2131f1e6b07118ed3753a2d0d3776934fe73] {'type': 'String', 'value': 'Hello World'}
[I 180805 20:09:23 EventHub:62] [SmartContract.Execution.Success][13894] [09a129673c61917593cb4b57dce066688f539d15] [tx 45eef678f288c854684c3d81bbac2131f1e6b07118ed3753a2d0d3776934fe73] {'type': 'Array', 'value': [{'type': 'Integer', 'value': '1'}]}
tty2 neo> 
```

The NEO Smart Contract source used for the above Hello World example is:
```python
def Main():
  print("Hello World")
  return True

```


Deploy Poll NEO Smart Contract
------------------------------

Build and import contract with meta-data:
```bash
tty3 neo> open wallet neo-client.wallet                                                                            
[password]> **********                                                                                        
Opened wallet at neo-client.wallet
tty3 neo> wallet
...
            "Address": "AXpm7MnucoDDW78X4c1NHggy6TYorMfrxT",
...
tty3 neo> build sc/sc/poll.py
[I 180812 14:43:12 BuildNRun:50] Saved output to sc/sc/poll.avm 
tty3 neo>
tty3 neo> import contract sc/sc/poll.avm 07070707 02 True False False
Please fill out the following contract details:
[Contract Name] > poll
[Contract Version] > 0.0.1
[Contract Author] > a
[Contract Email] > a@local
[Contract Description] > A poll contract enforcing one for vote per poll per address
Creating smart contract....
                 Name: poll 
              Version: 0.0.1
               Author: a 
                Email: a@local 
          Description: A poll contract enforcing one for vote per poll per address 
        Needs Storage: True 
 Needs Dynamic Invoke: False 
{
    "hash": "0x3a10794833ed2f280215bb28b1adea3f88fd5882",
...
}
[I 180812 14:44:22 EventHub:58] [test_mode][SmartContract.Contract.Create] [3a10794833ed2f280215bb28b1adea3f88fd5882] {...}}
[I 180812 14:44:22 EventHub:58] [test_mode][SmartContract.Execution.Success] [451a66e87292250538cb0a7a19d1a489c28dd2f5] {...}
Used 500.0 Gas 
-------------------------------------------------------------------------------------------------------------------------------------
Test deploy invoke successful
Total operations executed: 11 
Results:
[<neo.Core.State.ContractState.ContractState object at 0x7f7927541048>]
Deploy Invoke TX GAS cost: 490.0 
Deploy Invoke TX Fee: 0.0 
-------------------------------------------------------------------------------------------------------------------------------------
Enter your password to continue and deploy this contract
[password]> **********
[I 180812 14:44:31 Transaction:615] Verifying transaction: b'cf9b5511789cdf78c42dec949f036d754d767ab4645f05d878ffefe8e613b604' 
[I 180812 14:44:31 EventHub:62] [SmartContract.Verification.Success][27890] [cf6f6e49739373791a51a9431d817200bc4458e1] [...] {...}
Relayed Tx: cf9b5511789cdf78c42dec949f036d754d767ab4645f05d878ffefe8e613b604 
tty3 neo>                                                                    
```

Initially the contract will not be available
```bash
tty3 neo> contract 0x3a10794833ed2f280215bb28b1adea3f88fd5882                                   
tty3 neo> 
```

When the contract has been imported the script hash matched a script resource:
```bash
tty3 neo> contract 0x3a10794833ed2f280215bb28b1adea3f88fd5882                                   
...
{
    "version": 0,
    "code": {
        "hash": "0x3a10794833ed2f280215bb28b1adea3f88fd5882",
...
    "name": "poll",
    "code_version": "0.0.1",
    "author": "a",
    "email": "a@local",
    "description": "A poll contract enforcing one for vote per poll per address",
    "properties": {
        "storage": true,
        "dynamic_invoke": false
    }
}
tty3 neo>                                                                                       
```

Make one selection, then check the result from a single wallet:
```bash
tty3 neo> testinvoke 0x3a10794833ed2f280215bb28b1adea3f88fd5882 AXpm7MnucoDDW78X4c1NHggy6TYorMfrxT select poll-1 selection-1                                                                                     
...
Used 2.531 Gas 
-------------------------------------------------------------------------------------------------------------------------------------
Test invoke successful
Total operations: 205
Results [{'type': 'Integer', 'value': '1'}]
Invoke TX GAS cost: 0.0
Invoke TX fee: 0.0001
-------------------------------------------------------------------------------------------------------------------------------------
Enter your password to continue and invoke on the network
[password]> **********
[I 180812 15:11:56 Transaction:615] Verifying transaction: b'fc01ae50184de0caf7e6087233a6dcf8b395c7a35830c3f70c47e6e124fd50f9' 
[I 180812 15:11:56 EventHub:62] [SmartContract.Verification.Success][27982] [0577893f6a2e57cc67576e860fb8328d2a20a1ec] [..] {...}
Relayed Tx: fc01ae50184de0caf7e6087233a6dcf8b395c7a35830c3f70c47e6e124fd50f9 
tty3 neo> 
tty3 neo> testinvoke 0x3a10794833ed2f280215bb28b1adea3f88fd5882 AXpm7MnucoDDW78X4c1NHggy6TYorMfrxT result poll-1 
...
Used 0.386 Gas 
-------------------------------------------------------------------------------------------------------------------------------------
Test invoke successful
Total operations: 127
Results [{'type': 'ByteArray', 'value': ''}]
Invoke TX GAS cost: 0.0
Invoke TX fee: 0.0001
-------------------------------------------------------------------------------------------------------------------------------------
Enter your password to continue and invoke on the network
[password]> **********
[E 180812 15:12:25 Wallet:1080] insufficient funds for asset id: 602c79718b16e442de58778e148d0b1084e3b2dffd5de6b7b16cee7969282de7 
Insufficient funds
tty3 neo>
...
Logging events as transaction clears
...
tty3 neo>
tty3 neo> testinvoke 0x3a10794833ed2f280215bb28b1adea3f88fd5882 AXpm7MnucoDDW78X4c1NHggy6TYorMfrxT result poll-1 selection-1                                                                                     
...
Used 0.386 Gas 
-------------------------------------------------------------------------------------------------------------------------------------
Test invoke successful
Total operations: 127
Results [{'type': 'ByteArray', 'value': '01'}]
Invoke TX GAS cost: 0.0
Invoke TX fee: 0.0001
-------------------------------------------------------------------------------------------------------------------------------------
Enter your password to continue and invoke on the network
[password]> **********
[I 180812 15:12:43 Transaction:615] Verifying transaction: b'2405224ddff4a28524ff27b84dd386dabcf040b9444d0a6b3a5f27308b033d60' 
[I 180812 15:12:43 EventHub:62] [SmartContract.Verification.Success][27984] [f40ad105932fdae37cea3aaf8e18ee1c299bb04a] [...] {...}
Relayed Tx: 2405224ddff4a28524ff27b84dd386dabcf040b9444d0a6b3a5f27308b033d60 
tty3 neo>  
```
Note: the first request for the result came before the previous transaction has cleared and the invoke fails with "insufficient funds")


Using a different wallet in another terminal, add a subsequent selection, attempt a second (which fails) and check the result:
```bash
tty2 neo> open wallet neo-privnet.wallet 
[password]> **********                                                                                        
Opened wallet at neo-privnet.wallet
tty2 neo> wallet
...
            "Address": "AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y",
...
tty2 neo> testinvoke 0x3a10794833ed2f280215bb28b1adea3f88fd5882 AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y select poll-1 selection-1                                                                                     
-------------------------------------------------------------------------------------------------------------------------------------
Test invoke successful
Total operations: 205
Results [{'type': 'Integer', 'value': '2'}]
Invoke TX GAS cost: 0.0
Invoke TX fee: 0.0001
-------------------------------------------------------------------------------------------------------------------------------------
tty2 neo>                                                                                                                                                                                                        
...
Logging events as transaction clears
...
tty2 neo>
tty2 neo> testinvoke 0x3a10794833ed2f280215bb28b1adea3f88fd5882 AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y select poll-1 selection-1                                                                                     
-------------------------------------------------------------------------------------------------------------------------------------
Test invoke successful
Total operations: 144
Results [{'type': 'ByteArray', 'value': ''}]
Invoke TX GAS cost: 0.0
Invoke TX fee: 0.0001
-------------------------------------------------------------------------------------------------------------------------------------
tty2 neo>                                                                                                                                                                                                        
...
Logging events as transaction clears
...
tty2 neo>                                                                                                                                                                                                        
tty2 neo> testinvoke 0x3a10794833ed2f280215bb28b1adea3f88fd5882 AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y result poll-1 selection-1                                                                                     
-------------------------------------------------------------------------------------------------------------------------------------
Test invoke successful
Total operations: 127
Results [{'type': 'ByteArray', 'value': '02'}]
Invoke TX GAS cost: 0.0
Invoke TX fee: 0.0001
-------------------------------------------------------------------------------------------------------------------------------------
...
```

View the same result on the original terminal:
```bash
tty3 neo> testinvoke 0x3a10794833ed2f280215bb28b1adea3f88fd5882 AXpm7MnucoDDW78X4c1NHggy6TYorMfrxT result poll-1 selection-1                                                                                     
-------------------------------------------------------------------------------------------------------------------------------------
Test invoke successful
Total operations: 127
Results [{'type': 'ByteArray', 'value': '02'}]
Invoke TX GAS cost: 0.0
Invoke TX fee: 0.0001
-------------------------------------------------------------------------------------------------------------------------------------
...
```

Source
------

The NEO Smart Contract source used for the above Poll example is:
```python
from boa.interop.Neo.Runtime import CheckWitness
from boa.interop.Neo.Storage import Get,Put,GetContext
from boa.builtins import concat

def Main(voter, operation, poll, selection):

    if not CheckWitness(voter):
        print(concat("CheckWitness failed for: ", voter))
        return False

    ctx = GetContext()
    
    if operation == "select":
        return vote_for_selection(ctx, voter, poll, selection)

    elif operation == "result":
        return get_selection_result(ctx, poll, selection)

    return False


def vote_for_selection(ctx, voter, poll, selection):
    poll_voter_key = concat(poll, voter)
    voter_status = Get(ctx, poll_voter_key)
    if voter_status == "voted":
        return False

    else:
        poll_selection_key = concat(poll, selection)
        votes = Get(ctx, poll_selection_key) + 1
        Put(ctx, poll_voter_key, "voted")
        Put(ctx, poll_selection_key, votes)
        print(concat("Selected: ", selection))
        return votes


def get_selection_result(ctx, poll, selection):
    poll_selection_key = concat(poll, selection)
    votes = Get(ctx, poll_selection_key)
    print(concat("Result: ", votes))
    return votes

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



Miscellaneous 
=============

Script fragments, commands and alternate examples.


Compile from command line
-------------------------

Useful to build outside the NEO node prompt.

Compile a smart contract distribution in a local workspace:
```bash
$ rm -rf './avm' && mkdir -p './avm'
$ cd neo-boa-compiler/
$ docker build --tag neo-boa .
$ docker run -it --rm -v $(pwd)/../sc:/python-contracts -v $(pwd)/../avm:/compiled-contracts neo-boa
$ cd ..
$ 
```


Balance Contract
----------------

[Source](http://neo-python.readthedocs.io/en/latest/neo/SmartContract/smartcontracts.html)

Deploy a contract with storage and execite it, viewing the output on the monitor nodes:
```bash
tty2 neo> build sc/sc/balance_tracker.py test 070502 02 True False False add AG4GfwjnvydAZodm4xEDivguCtjCFzLcJy 3   
tty2 neo> import contract sc/sc/balance_tracker.avm 070502 02 True False False
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



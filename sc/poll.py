"""
Date Created:               2018-08-25
Date Modified:              <TODO>
Version:                    1
Contract Hash:              <TODO>
Available on NEO TestNet:   False
Available on CoZ TestNet:   False
Available on MainNet:       False
Example: (return as integer)
    Test Invoke:            build /path/to/poll.py test 07070707 02 True False \
                                'test-1' select 'poll-1' 'selection-1' 
    Expected Result:        1
    Operation Count:        382
    GAS Consumption:        2.447
Example: (return as integer)
    Test Invoke:            build /path/to/poll.py test 07070707 02 True False \
                                'test-1' result 'poll-1' 'selection-1' 
    Expected Result:        1
    Operation Count:        234
    GAS Consumption:        0.255
"""

# from boa.blockchain.vm.Neo.Runtime import CheckWitness
from boa.interop.Neo.Runtime import CheckWitness
from boa.interop.Neo.Storage import Get,Put,Delete,GetContext
from boa.interop.Neo.Contract import Script
from boa.builtins import concat

allow_test_users = True
urn_base = "urn:example:poll:"

def Main(caller, operation, poll, selection):

    ctx = GetContext()

    # Is the declared caller the invoker?
    try:
        witness = True
        if allow_test_users == True and caller != "test-1" and caller != "test-2" and caller != "test-3":
            print(concat("WARNING: Skipping CheckWitness for: ", caller))
        else:
            print(concat("Calling CheckWitness for: ", caller))
            if not CheckWitness(caller):
                print(concat("CheckWitness failed for: ", caller))
                return False
    except:
        print(concat("CheckWitness error for: ", caller))
        return False
    voter = caller

    print(concat("Choosing operation: ", operation))
    
    if operation == "select":
        poll_selection_key = build_poll_selection_key(poll, selection)
        poll_voter_key = build_poll_voter_key(poll, voter)
        votes = Get(ctx, poll_selection_key) + 1
        voter_status = Get(ctx, poll_voter_key)
        if voter_status == 'voted':
            print(concat("Voter status: ", voter_status))
            return False
        else:
            Put(ctx, poll_voter_key, "voted")
        votes = votes + 1
        Put(ctx, poll_selection_key, votes)
        print(concat("Selected: ", selection))
        return votes

    elif operation == "result":
        poll_selection_key = build_poll_selection_key(poll, selection)
        votes = Get(ctx, poll_selection_key)
        print(concat("Result: ", votes))
        return votes

    return False


def build_poll_selection_key(poll, selection):
    base_and_poll = build_base_and_poll("pollselection:", poll)
    return concat(base_and_poll, selection)


def build_poll_voter_key(poll, voter):
    base_and_poll = build_base_and_poll("pollvoter:", poll)
    return concat(base_and_poll, voter)


def build_base_and_poll(resource, poll):
    base = concat(urn_base, resource) 
    base_and_poll = concat(base, poll)
    return concat(base_and_poll, ";")

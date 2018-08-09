"""
Date Created:               2018-08-25
Date Modified:              <TODO>
Version:                    1
Contract Hash:              <TODO>
Available on NEO TestNet:   False
Available on CoZ TestNet:   False
Available on MainNet:       False
Example: (1 vote)
    Test Invoke:            build /path/to/poll.py test 07070707 02 True False \
                                AXpm7MnucoDDW78X4c1NHggy6TYorMfrxT selection poll-1 selection-1
    Expected Result:        1
    Operation Count:        372
    GAS Consumption:        2.441
Example: (1 vote, this selection not taken)
    Test Invoke:            build /path/to/poll.py test 07070707 02 True False \
                                AXpm7MnucoDDW78X4c1NHggy6TYorMfrxT selection poll-1 selection-1
    Expected Result:        0
    Operation Count:        345
    GAS Consumption:        0.427
Example: (return as integer)
    Test Invoke:            build /path/to/poll.py test 07070707 02 True False \
                                AXpm7MnucoDDW78X4c1NHggy6TYorMfrxT result 'poll-1' 'selection-1' 
    Expected Result:        1
    Operation Count:        234
    GAS Consumption:        0.255
"""

from boa.interop.Neo.Runtime import CheckWitness
from boa.interop.Neo.Storage import Get,Put,Delete,GetContext
from boa.interop.Neo.Contract import Script
from boa.builtins import concat

allow_test_users = True
urn_base = "urn:example:poll:"

def Main(voter, operation, poll, selection):

    if not voter_is_caller(voter):
        return False

    print(concat("Choosing operation: ", operation))

    ctx = GetContext()
    
    if operation == "select":
        poll_voter_key = build_poll_voter_key(poll, voter)
        voter_status = Get(ctx, poll_voter_key)
        if voter_status != 'voted':
            vote = vote_for_selection(ctx, poll_voter_key, poll, selection)
            return votes

    elif operation == "result":
        votes = get_selection_result(ctx, poll, selection)
        return votes

    return False


def voter_is_caller(caller):
    try:
        if allow_test_users == True and (caller == "test-1" or caller == "test-2"):
            print(concat("WARNING: Skipping CheckWitness for: ", caller))
        else:
            #print(concat("Calling CheckWitness for: ", caller))
            if not CheckWitness(caller):
                print(concat("CheckWitness failed for: ", caller))
                return False
    except:
        print(concat("ERROR: CheckWitness error for: ", caller))
        return False
    return True


def vote_for_selection(ctx, poll_voter_key, poll, selection):
    poll_selection_key = build_poll_selection_key(poll, selection)
    votes = Get(ctx, poll_selection_key) + 1
    Put(ctx, poll_voter_key, "voted")
    Put(ctx, poll_selection_key, votes)
    print(concat("Selected: ", selection))
    return votes


def get_selection_result(ctx, poll, selection):
    poll_selection_key = build_poll_selection_key(poll, selection)
    votes = Get(ctx, poll_selection_key)
    print(concat("Result: ", votes))
    return votes


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

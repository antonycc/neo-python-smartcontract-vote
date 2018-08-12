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
Example: (1 vote, this selection not accepted)
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
Source: https://github.com/antonycc/neo-python-smartcontract-vote
"""

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

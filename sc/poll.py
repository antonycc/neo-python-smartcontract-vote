# Usage:
#    poll create poll_id [selection_addr, selection_addr., ...] > 0
#    poll vote   poll_id [selection_addr](max 1) > votes_for_selection_addr
#    poll result poll_id [selection_addr](max 1) > votes_for_selection_addr
#    poll freeze poll_id [] > 0
#    poll delete poll_id [] > 0

from boa.interop.Neo.Storage import Get,Put,Delete,GetContext


def Main(operation, poll_id, selection_addr):

    print("operation: %s" % operation)
    print("poll_id: %s" % poll_id)
    print("selection_addr: %s" % selection_addr)

    #if not is_valid_addr(poll_id):
    #    return False

    ctx = GetContext()

    if operation == 'create':
        new_balance = 0
        Put(ctx, poll_id, new_balance)
        print("Created: %s" % poll_id)
        return new_balance

    elif operation == 'select':
        balance = Get(ctx, poll_id)
        new_balance = balance + 1
        Put(ctx, poll_id, new_balance)
        print("Selected: %s" % poll_id)
        return new_balance

    elif operation == 'result':
        balance = Get(ctx, poll_id)
        print("Result: %s" % poll_id)
        return balance

    elif operation == 'delete':
        Delete(ctx, poll_id)
        print("Deleted: %s" % poll_id)
        return 0

    return False

#def is_valid_addr(addr):
#
#    if len(addr) == 20:
#        return True
#    return False

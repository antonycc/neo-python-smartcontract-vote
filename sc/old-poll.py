# Usage:
#    poll create poll_id [selection_addr, selection_addr., ...] > 0
#    poll vote   poll_id [selection_addr](max 1) > votes_for_selection_addr
#    poll result poll_id [selection_addr](max 1) > votes_for_selection_addr
#    poll freeze poll_id [] > 0
#    poll delete poll_id [] > 0

from boa.interop.Neo.Storage import Get,Put,Delete,GetContext


def Main(operation, poll_id, selection_addr):

    #print("operation: " +       operation)
    #print("poll_id: " +         poll_id)
    #print("selection_addr: " + selection_addr)

    ctx = GetContext()

    if operation == 'create':
        #poll_selection_list_key = build_poll_selection_list_key(poll_id)
        #Put(ctx, poll_selection_list_key, selection_addrs)
        #poll_status_key = build_poll_status_key(poll_id)
        #Put(ctx, poll_status_key, 'created')
        print("Created: " + poll_id)
        return 0

    if operation == 'select':
        #poll_status_key = build_poll_status_key(poll_id)
        #poll_status = Get(ctx, poll_status_key)
        #if poll_status == 'frozen':
        #    print("Can not vote, poll frozen: " + poll_id)
        #    return -1
        #else:
        #    poll_selection_list_key = build_poll_selection_list_key(poll_id)
        #    current_selection_addrs = Get(ctx, poll_selection_list_key)
            #for selection_addr in current_selection_addrs:
                #if selection_addrs[0] == selection_addr:
                    # TODO: Ensure sender can only vote once
                    #    build_poll_voter_status_key(poll_id, voter_addr)
                    #    poll_voter_status = Get(ctx, poll_voter_status_key)
                    #poll_voter_status = 'not voted'
                    #if poll_voter_status == 'voted':
                    #    # print("Can not vote, voter voted: " + voter_addr)
                    #    return -1
                    #else:
        poll_selection_key = build_poll_selection_key(poll_id, selection_addr)
        votes_for_selection_addr = Get(ctx, poll_selection_key)
        votes_for_selection_addr = votes_for_selection_addr + 1
        Put(ctx, poll_selection_key, votes_for_selection_addr)
        print("Selected: : " + selection_addrs[0])
        return votes_for_selection_addr
            #print("Can not vote, unknown selection: " + selection_addrs[0])
            #return -1

    if operation == 'result':
        poll_selection_key = build_poll_selection_key(poll_id, selection_addr)
        votes_for_selection_addr = Get(ctx, poll_selection_key)
        print("Result: " + votes_for_selection_addr)
        return votes_for_selection_addr

    #if operation == 'freeze':
    #    poll_status_key = build_poll_status_key(poll_id)
    #    Put(ctx, poll_status_key, 'frozen')
    #    print("Frozen: " + poll_id)
    #    return 0

    #if operation == 'delete':
    #    poll_selection_list_key = build_poll_selection_list_key(poll_id)
    #    current_selection_addrs = Get(ctx, poll_selection_list_key)
    #    for selection_addr in current_selection_addrs:
    #        poll_selection_key = build_poll_selection_key(poll_id, selection_addr)
    #        Delete(ctx, poll_selection_key)
    #    poll_status_key = build_poll_status_key(poll_id)
    #    Delete(ctx, poll_status_key)
    #    Delete(ctx, poll_id)
    #    print("Deleted: " + poll_id)
    #    return 0

    return -1

#def build_poll_selection_list_key(poll_id):
#    return 'urn:example:poll:selections:' + poll_id

#def build_poll_status_key(poll_id):
#    return 'urn:example:poll:status:' + poll_id

def build_poll_selection_key(poll_id, selection_addr):
    return selection_addr
    # return 'urn:example:pollselection:' + poll_id + ';' + selection_addr

#def build_poll_voter_status_key(poll_id, voter_addr):
#    return 'urn:example:pollvoter:' + poll_id + ';' + voter_addr

#def is_valid_addr(addr):
#
#    if len(addr) == 20:
#        return True
#    return False

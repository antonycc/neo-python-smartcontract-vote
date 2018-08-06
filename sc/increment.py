from boa.interop.Neo.Storage import Get,Put,Delete,GetContext

def Main(operation, addr, value):

    if not is_valid_addr(addr):
        return False

    ctx = GetContext()

    if operation == 'create':
        new_balance = 0
        Put(ctx, addr, new_balance)
        return new_balance

    elif operation == 'select':
        balance = Get(ctx, addr)
        new_balance = balance + value
        Put(ctx, addr, new_balance)
        return new_balance

    elif operation == 'result':
        balance = Get(ctx, addr)
        return balance

    elif operation == 'delete':
        Delete(ctx, addr)
        return 0

    return False

def is_valid_addr(addr):

    if len(addr) == 20:
        return True
    return False

from neo.contrib.smartcontract import SmartContract

smart_contract = SmartContract("6537b4bd100e514119e3a7ab49d520d20ef2c2a4")

@smart_contract.on_notify
def sc_notify(event):
    print("SmartContract Runtime.Notify event:", event)

    # Make sure that the event payload list has at least one element.
    if not isinstance(event.event_payload, ContractParameter) or event.event_payload.Type != ContractParameterType.Array or not len(event.event_payload.Value):
        return

    # The event payload list has at least one element. As developer of the smart contract
    # you should know what data-type is in the bytes, and how to decode it. In this example,
    # it's just a string, so we decode it with utf-8:
    print("- payload part 1:", event.event_payload.Value[0].Value.decode("utf-8"))
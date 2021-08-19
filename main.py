import logging
import sys

import smpplib
from smpplib import consts, gsm


def handle_deliver_sm(pdu):
    sys.stdout.write('delivered {}\n'.format(pdu.receipted_message_id))
    return 0


if __name__ == '__main__':
    logging.basicConfig(level='DEBUG')

    client = smpplib.client.Client(host='192.168.1.100', port=9550)

    client.set_message_sent_handler(lambda pdu: sys.stdout.write('sent {} {}\n'.format(pdu.sequence, pdu.message_id)))

    client.set_message_received_handler(lambda pdu: handle_deliver_sm(pdu))

    client.connect()

    client.bind_transceiver(system_id='fb', password='fb')
    for i in range(100):
        parts, encoding_flag, msg_type_flag = smpplib.gsm.make_parts('test message send smpp by python3 - ' + str(i))

        for part in parts:
            pdu = client.send_message(
                source_addr_ton=smpplib.consts.SMPP_TON_ALNUM,
                source_addr_npi=smpplib.consts.SMPP_NPI_UNK,
                # Make sure it is a byte string, not unicode:
                source_addr='3332222332266666655',

                dest_addr_ton=smpplib.consts.SMPP_TON_INTL,
                dest_addr_npi=smpplib.consts.SMPP_NPI_ISDN,
                # Make sure these two params are byte strings, not unicode:
                destination_addr='66699993355444',
                short_message=part,

                data_coding=encoding_flag,
                esm_class=msg_type_flag,
                registered_delivery=True,
            )
            print(pdu.sequence)

    client.listen()

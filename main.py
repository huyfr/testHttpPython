import smpplib
from smpplib import consts
import tqdm

if __name__ == '__main__':
    for i in tqdm.tqdm(range(10000000)):
        client = None
        try:
            client = smpplib.client.Client(host='192.168.1.100', port=9550)
            client.connect()
            try:
                client.bind_transmitter(system_id='fb', password='fb')
                message_bytes = bytes('test message send smpp by python3 - ' + str(i), 'utf-8')
                client.send_message(source_addr_ton=smpplib.consts.SMPP_TON_INTL,
                                    source_addr='3332222332266666655',
                                    dest_addr_ton=smpplib.consts.SMPP_TON_INTL,
                                    destination_addr='66699993355444',
                                    registered_delivery=True,
                                    short_message=message_bytes)
            except Exception as ex:
                print(ex)
            finally:
                if client.state in [smpplib.consts.SMPP_CLIENT_STATE_BOUND_TX]:
                    try:
                        client.unbind()
                    except smpplib.exceptions.UnknownCommandError as ex:
                        try:
                            client.unbind()
                        except smpplib.exceptions.PDUError as ex:
                            pass
        finally:
            if client:
                client.disconnect()

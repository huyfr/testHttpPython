import smpplib
from smpplib import consts
import tqdm

if __name__ == '__main__':
    for i in tqdm.tqdm(range(10)):
        client = None
        try:
            client = smpplib.client.Client(host='192.168.1.100', port=9550)
            client.connect()
            try:
                client.bind_transmitter(system_id='testSmpp', password='testSmpp')
                message_bytes = bytes('test message send smpp by python3 - ' + str(i), 'utf-8')
                client.send_message(source_addr_ton=smpplib.consts.SMPP_TON_INTL,
                                    source_addr='0858358088',
                                    dest_addr_ton=smpplib.consts.SMPP_TON_INTL,
                                    destination_addr='9535134654',
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

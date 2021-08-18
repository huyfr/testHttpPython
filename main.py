import requests as requests

HOST = 'http://192.168.37.129:8080'
API = '/secure/send'
USER_NAME = 'huy'
PASSWORD = 'huy'
RECIPIENT = '0858358088'
MESSAGE_BODY = 'Hello world from python 3 to jasmin - '
MESSAGE_SUCCESS = 'Success'


def compose_request(recipient, message_body, count):
    body = {}
    try:
        body['to'] = recipient
        body['from'] = 'huy'
        body['content'] = message_body + str(count)
        body['dlr'] = 'no'
    except Exception as ex:
        print(f'Error at function compose_request with message: ', ex)
    return body


def send_request(body):
    result = False
    try:
        if len(body) > 0:
            resp = requests.post(url=HOST + API, json=body, auth=(USER_NAME, PASSWORD))
            str_content = resp.content.decode('utf-8')
            if resp.status_code == 200 and MESSAGE_SUCCESS in str_content:
                result = True
                # print('Send SMS successful!')
            else:
                print('Fail while send SMS')
    except Exception as ex:
        print(f'Error at function send_request with message: ', ex)
    return result


if __name__ == '__main__':
    for i in range(1000000):
        request = compose_request(RECIPIENT, MESSAGE_BODY, i)
        response = send_request(request)

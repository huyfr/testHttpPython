import requests as requests

HOST = 'http://127.0.0.1:9501'
API = '/api?action=sendMessage'
USER_NAME = 'admin'
PASSWORD = 'admin'
RECIPIENT = '0858358088'
MESSAGE_BODY = 'Hello world from python 3 - '
MESSAGE_SUCCESS = 'Message accepted for delivery'


def compose_request(host, api, user_name, password, recipient, message_body, count):
    req = ''
    try:
        req = host + api +\
              '&username=' + requests.utils.quote(user_name) + \
              '&password=' + requests.utils.quote(password) +\
              '&recipient=' + requests.utils.quote(recipient) + \
              '&messagedata=' + requests.utils.quote(message_body + str(count))
    except Exception as ex:
        print(f'Error at function compose_request with message: ', ex)
    return req


def send_request(req):
    result = False
    try:
        if req != '':
            resp = requests.post(req)
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
        request = compose_request(HOST, API, USER_NAME, PASSWORD, RECIPIENT, MESSAGE_BODY, i)
        response = send_request(request)

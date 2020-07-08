from pprint import pprint
import requests
from urllib.parse import urlencode

OAUTH_URL = 'https://oauth.vk.com/authorize'
APP_ID = 7533990  #получен СОИ по ссылке https://vk.com/editapp?act=create
TOKEN = 'd6c5a3a20cb669b4b16ec66b94a9fa6c0f7a7f181da7c6099d97496b90918395d3c12385531a035e98d69' #получен СОИ 08.07.20
#TOKEN = '959ee46eb78b742b5ee80b b968704aef92da579b4035475e70df4a7a5df432b0a6cbfb6eaa04dcd431f4b' #получен в Нетологии

####Запрос ссылки для получения токена на 1 сут!
# OAUTH_DATA = {
#      'client_id': APP_ID,
#      'display': 'mobile',
#      'scope': 'status, friends, offline',
#      'response_type': 'token',
#      'v': 5.120
#  }
# #print('****', urlencode(OAUTH_DATA))
# print('?'.join((OAUTH_URL, urlencode(OAUTH_DATA))))


# def get_status(token):
#     response = requests.get(
#         'https://api.vk.com/method/status.get',
#         params={
#             'access_token': token,
#             'v': 5.21
#         }
#     )
#     return response.json()
#
#
# def set_status(token, text):
#     response = requests.get(
#         'https://api.vk.com/method/status.set',
#         params={
#             'access_token': token,
#             'v': 5.21,
#             'text': text
#         }
#     )
#     return response.json()
#
#
# status = get_status(TOKEN)
# set_status(TOKEN, 'some status')


class VK_User:
    def __init__(self, token) -> None:
        self.token = token

    def get_user_ids(self):
        response = requests.get(
            'https://api.vk.com/method/users.get',
            params={
                'access_token': self.token,
                'user_ids': 210700286,
                'v': 5.21
            }
        )
        print(response, response.text)
        #pprint(response.json())
        return response.json()

    def get_status(self):
        response = requests.get(
            'https://api.vk.com/method/status.get',
            params={
                'access_token': self.token,
                'v': 5.21
            }
        )
        return response.json()

    def set_status(self, text):
        response = requests.get(
            'https://api.vk.com/method/status.set',
            params={
                'access_token': self.token,
                'v': 5.21,
                'text': text
            }
        )
        return response.json()


user1 = VK_User(TOKEN)
user2 = VK_User(TOKEN)
user1.get_user_ids()
# artyom.get_status()
# artyom.set_status('Another hello!')
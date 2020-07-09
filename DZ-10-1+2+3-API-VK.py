import json
from pprint import pprint
import requests
from urllib.parse import urlencode

OAUTH_URL = 'https://oauth.vk.com/authorize'
APP_ID = 7533990  #получен СОИ по ссылке https://vk.com/editapp?act=create
TOKEN = '123' #получен СОИ 08.07.20
TOKEN = '959ee46eb78b742b5ee80b b968704aef92da579b4035475e70df4a7a5df432b0a6cbfb6eaa04dcd431f4b' #получен в Нетологии

class VK_user:
    def __init__(self, token) -> None:
        self.token = token

    def get_user_ids(self, id): #вывести информацию о пользователе
        response = requests.get(
            'https://api.vk.com/method/users.get',
            params={
                'access_token': self.token,
                'user_ids': id,
                'v': 5.21
            }
        )
        name = json.loads(response.text)['response'][0]['first_name']
        last_name = json.loads(response.text)['response'][0]['last_name']
        print(f'Данные по пользователю id{id} ({last_name} {name}): {response.text}')
        #pprint(response.json())
        return response.json()

    def print(self, id=5346546): #вывести ссылку пользователя
        url = 'www.vk.com/id'+str(id)
        print(f'URL страницы пользователя {id} в Вконтакте: {url}')
        return url

    def get_status(self): #считать свой статус ВК
        response = requests.get(
            'https://api.vk.com/method/status.get',
            params={
                'access_token': self.token,
                'v': 5.21
            }
        )
        return response.json()

    def set_status(self, text): #задать себе статус ВК
        response = requests.get(
            'https://api.vk.com/method/status.set',
            params={
                'access_token': self.token,
                'v': 5.21,
                'text': text
            }
        )
        return response.json()

    def get_friends(self, id=210700286): #считать друзей у пользователя
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params={
                'access_token': self.token,
                'user_id': id,
                'order': 'name',
                'v': 5.21
            }
        )
        data = json.loads(response.text)['response']['items']
        print(f'Пользователь с id{id} имеет следующих друзей: {data}')
        return response.json()

    def common_friends(self, user1=5346546, user2=2925854): #отобрать общих друзей 2 пользователей
        friends1 = self.get_friends(user1)
        friends2 = self.get_friends(user2)
        common_friends = []
        for friend in friends1['response']['items']:
            if friend in friends2['response']['items']:
                #print('***', friend, type(friend))
                common_friends.append(friend)
        print(f'Пользователи {user1} и {user2} имеют {len(common_friends)} общих друзей: {common_friends}')
        return common_friends


user0 = VK_user(TOKEN)
user1 = VK_user(TOKEN)
user2 = VK_user(TOKEN)

user0.get_user_ids(4326594)

user1.get_user_ids(5346546)
user2.get_user_ids(2925854)
user1.common_friends()

user2.print()



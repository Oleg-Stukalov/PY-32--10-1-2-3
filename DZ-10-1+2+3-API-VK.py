import json
from pprint import pprint
import requests
from urllib.parse import urlencode

OAUTH_URL = 'https://oauth.vk.com/authorize'
APP_ID = 7533990  #получен СОИ по ссылке https://vk.com/editapp?act=create
TOKEN = '10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c' #получен в Нетологии

class VKUser:
    def __init__(self, id=4326594, id2=2925854) -> None:
        self.token = TOKEN
        self.id = id
        self.id2 = id2

    # def __and__(self, other):
    #     common_friends = user1 & user2
    #     for friend in common_friends:
    #         print(friend)
    #     return [VKUser(51676659), VKUser(58597357), VKUser(3968335)]

    def __str__(self): #вывести ссылку пользователя
        url = 'www.vk.com/id'+str(self.id)
        return url

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
        print(f'Данные по пользователю id{self.id} ({last_name} {name}): {response.text}')
        #pprint(response.json())
        return response.json()

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

    def get_friends(self, id): #считать друзей у пользователя
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

    def common_friends(self, id, id2): #отобрать общих друзей 2 пользователей
        friends1 = set(self.get_friends(id)['response']['items'])
        friends2 = set(self.get_friends(id2)['response']['items'])
        common_friends = friends1 & friends2
        print(f'Пользователи {id} и {id2} имеют {len(common_friends)} общих друзей: {common_friends}')
        return common_friends

        ###############backup-copy
        # friends1 = self.get_friends(id)
        # friends2 = self.get_friends(id2)
        # common_friends = []
        # for friend in friends1['response']['items']:
        #     if friend in friends2['response']['items']:
        #         #print('***', friend, type(friend))
        #         common_friends.append(friend)
        # print(f'Пользователи {id} и {id2} имеют {len(common_friends)} общих друзей: {common_friends}')
        # return common_friends

user0 = VKUser(4326594)
user1 = VKUser(5346546)
user2 = VKUser(2925854)

user0.get_user_ids(4326594) ##########Почему не выводится???????????
user1.get_user_ids(5346546)
user2.get_user_ids(2925854)
user1.common_friends(5346546, 2925854)
print(user2)

#user2.common_friends(user0, user1)


import json
from typing import List

import scrapy

from scrapgitubapi.data.datauser import DataUser
from scrapgitubapi.table.TableUsers import TableUsers


class UsersSpider(scrapy.Spider):
    name = 'users'
    allowed_domains = ['api.github.com']

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.user_index = -1
        data_user = DataUser()
        self.users_list: List[str] = data_user.user_login_list
        self.table_users = TableUsers()

    @property
    def next_user(self) -> int:
        self.user_index = self.user_index + 1
        if self.user_index >= len(self.users_list):
            return None
        return self.users_list[self.user_index]

    @property
    def next_url(self) -> str:
        nu = self.next_user
        if nu is None:
            return None
        return f"https://api.github.com/users/{nu}"

    def start_requests(self):
        yield scrapy.Request(url=self.next_url, callback=self.parse)

    def parse(self, response):
        text = response.text
        try:

            x = json.loads(text)
            id = x['id']
            login = x['login']
            site_admin = x['site_admin']
            type = x['type']
            name = x['name']
            email = x['email']
            hireable = x['hireable']
            self.table_users.write(id, login, site_admin, type, name, email, hireable)

            nu = self.next_url
            # while Cache.is_cached(nu):
            #    nu = self.next_url
            if not nu is None:
                yield scrapy.Request(url=nu, callback=self.parse)
            return None
        except:
            print(text)

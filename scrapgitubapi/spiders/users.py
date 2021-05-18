import json
from typing import List

import scrapy

from scrapgitubapi.data.datanotfoundurl import DataNotFoundUrl
from scrapgitubapi.data.datauser import DataUser
from scrapgitubapi.table.TableUsers import TableUsers
from scrapgitubapi.util.cache import Cache


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
        url = f"https://api.github.com/users/{nu}"
        not_found_urls = DataNotFoundUrl().not_found_url
        # print(f"not_found_urls: {not_found_urls}, url: {url}")
        if url in not_found_urls:
            # print("Skip: " + url)
            return self.next_url
        return url

    def start_requests(self):
        nu = self.next_url
        print(nu)
        yield scrapy.Request(url=nu, callback=self.parse)

    def parse(self, response):
        text = response.text
        status = response.status
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
            print(nu)
            while Cache.is_cached(nu):
                nu = self.next_url
            if not nu is None:
                yield scrapy.Request(url=nu, callback=self.parse)
            return None
        except:
            print(text)

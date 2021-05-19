import json

import scrapy

from scrapgitubapi.data.datagithubapi import DataGithubApi
from scrapgitubapi.data.datauser import DataUser
from scrapgitubapi.table.TableSubscribers import TableSubscribers


class ContributorsSpider(scrapy.Spider):
    name = 'subscribers'
    allowed_domains = ['api.github.com']

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.page = 0
        self.data_github_api = DataGithubApi()
        self.data_user = DataUser()
        self.table_subscribers = TableSubscribers()

    @property
    def next_page(self) -> int:
        self.page = self.page + 1;
        return self.page

    @property
    def next_url(self) -> str:
        base_url = f"https://api.github.com/repos/nginx/nginx/subscribers"
        return f"{base_url}?page={self.next_page}"

    def start_requests(self):
        yield scrapy.Request(url=self.next_url, callback=self.parse)

    def parse(self, response):
        text = response.text
        obj = json.loads(text)
        for x in obj:
            id = x['id']
            login = x['login']
            site_admin = x['site_admin']
            type = x['type']
            self.table_subscribers.write(id, login, site_admin, type)
            # self.data_user.add_user_login(login)
        if len(text) > 2 and text != '[]':
            yield scrapy.Request(url=self.next_url, callback=self.parse)
        return None

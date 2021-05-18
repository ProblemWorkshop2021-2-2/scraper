import json

import scrapy

from scrapgitubapi.util.datagithubapi import DataGithubApi
from scrapgitubapi.util.datauser import DataUser


class ContributorsSpider(scrapy.Spider):
    name = 'contributors'
    allowed_domains = ['api.github.com']

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.page = 0
        self.data_github_api = DataGithubApi()
        self.data_user = DataUser()

    @property
    def next_page(self) -> int:
        self.page = self.page + 1;
        return self.page

    @property
    def next_url(self) -> str:
        return f"{self.data_github_api.contributors_url}?page={self.next_page}"

    def start_requests(self):
        yield scrapy.Request(url=self.next_url, callback=self.parse)

    def parse(self, response):
        text = response.text
        obj = json.loads(text)
        for x in obj:
            login = x['login']
            self.data_user.add_user_login(login)
        if len(text) > 2 and text != '[]':
            yield scrapy.Request(url=self.next_url, callback=self.parse)
        return None

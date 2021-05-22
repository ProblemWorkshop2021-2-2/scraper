import json

import scrapy

from scrapgitubapi.data.datagithubapi import DataGithubApi
from scrapgitubapi.data.datauser import DataUser
from scrapgitubapi.table.TableContributors import TableContributors


class ContributorsSpider(scrapy.Spider):
    name = 'contributors'
    allowed_domains = ['api.github.com']

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.page = 0
        self.data_github_api = DataGithubApi()
        self.data_user = DataUser()
        self.table_contributors = TableContributors()

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
            id = x['id']
            login = x['login']
            contributions = x['contributions']
            site_admin = x['site_admin']
            type = x['type']
            self.table_contributors.write(id, login, contributions, site_admin, type)
            self.data_user.add_user_login(login)
        if len(text) > 2 and text != '[]':
            yield scrapy.Request(url=self.next_url, callback=self.parse)
        return None

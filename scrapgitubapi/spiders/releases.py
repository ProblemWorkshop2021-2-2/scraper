import json

import scrapy

from scrapgitubapi.data.datagithubapi import DataGithubApi
from scrapgitubapi.data.datauser import DataUser
from scrapgitubapi.table.TableReleases import TableReleases
from scrapgitubapi.util import Config


class ReleasesSpider(scrapy.Spider):
    name = 'releases'
    allowed_domains = ['api.github.com']

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.page = 0
        self.data_github_api = DataGithubApi()
        # self.data_user = DataUser()
        self.table_releases = TableReleases()

    @property
    def next_page(self) -> int:
        self.page = self.page + 1
        return self.page

    @property
    def next_url(self) -> str:
        url = f"https://api.github.com/repos/{Config.repository_owner()}/{Config.repository_name()}/releases?page={self.next_page}"
        # url = f"https://api.github.com/repos/{Config.repository_owner()}/{Config.repository_name()}/milestones/{self.next_page}"
        # url = f"{self.data_github_api.milestones_url}/{self.next_page}"
        print('url:', url)
        return url

    def start_requests(self):
        yield scrapy.Request(url=self.next_url, callback=self.parse)

    def parse(self, response):
        text = response.text
        obj = json.loads(text)
        for x in obj:
            tag_name = x['tag_name']
            self.table_releases.write(tag_name)
            # self.data_user.add_user_login(login)
        if len(text) > 2 and text != '[]':
            yield scrapy.Request(url=self.next_url, callback=self.parse)
        return None


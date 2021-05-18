import json
from typing import List

import scrapy

from scrapgitubapi.util import Config
from scrapgitubapi.util.datagithubapi import DataGithubApi


class GithubapiSpider(scrapy.Spider):
    name = 'githubapi'
    allowed_domains = ['api.github.com']

    urls_to_crawl: List[str] = [
        'https://api.github.com/repos/tensorflow/tensorflow'
    ]

    def start_requests(self):
        Config.github_token()
        for url in self.urls_to_crawl:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        url = response.url
        text = response.text
        obj = json.loads(text)
        data = DataGithubApi()
        data.contributors_url = obj['contributors_url']
        return {}

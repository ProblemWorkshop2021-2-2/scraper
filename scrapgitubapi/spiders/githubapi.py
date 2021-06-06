import json
from typing import List

import scrapy

from scrapgitubapi.data.datagithubapi import DataGithubApi
from scrapgitubapi.util import Config


class GithubapiSpider(scrapy.Spider):
    name = 'githubapi'
    allowed_domains = ['api.github.com']

    urls_to_crawl: List[str] = [
        f"https://api.github.com/repos/{Config.repository_owner()}/{Config.repository_name()}"
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
        data.subscribers_url = obj['subscribers_url']
        # data.milestones_url = obj['milestones_url']
        return {}

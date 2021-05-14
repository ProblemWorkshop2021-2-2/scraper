import json
from typing import List

import scrapy

from scrapgitubapi.util import Util


class GithubapiSpider(scrapy.Spider):
    name = 'githubapi'
    allowed_domains = ['api.github.com']
    urls_to_crawl: List[str] = [
        'http://api.github.com/repos/tensorflow/tensorflow'
    ]

    def start_requests(self):
        for url in self.urls_to_crawl:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        url = response.url
        text = response.text
        print("-----------------------------------------")
        print(f"text: {type(text)}")
        print("-----------------------------------------")
        print(text)
        print("-----------------------------------------")
        obj = json.loads(text)
        urls = Util.extract_url(obj)
        return {"url":url, "text":text}

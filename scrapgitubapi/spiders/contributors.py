import scrapy

from scrapgitubapi.util.datagithubapi import DataGithubApi


class ContributorsSpider(scrapy.Spider):
    name = 'contributors'
    allowed_domains = ['api.github.com']

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.page = 0
        self.data_github_api = DataGithubApi()

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
        if len(text) > 2 and text != '[]':
            yield scrapy.Request(url=self.next_url, callback=self.parse)
        else:
            print(text)
        return None

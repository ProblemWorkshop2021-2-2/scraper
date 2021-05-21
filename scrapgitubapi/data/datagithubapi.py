from scrapgitubapi.data.data import Data


class DataGithubApi(Data):

    def __init__(self):
        super().__init__('githubapi')

    @property
    def contributors_url(self) -> str:
        return self.get_key('contributors_url')

    @contributors_url.setter
    def contributors_url(self, value: str):
        self.set_key('contributors_url', value)

    @property
    def subscribers_url(self) -> str:
        return self.get_key('subscribers_url')

    @subscribers_url.setter
    def subscribers_url(self, value: str):
        self.set_key('subscribers_url', value)

from typing import List

from scrapgitubapi.data.data import Data


class DataNotFoundUrl(Data):

    def __init__(self):
        super().__init__('NotFoundUrl')

    @property
    def not_found_url(self) -> List[str]:
        return self.get_key_default('not_found_url', [])

    def clear_not_found_url(self):
        self.set_key('not_found_url', [])

    def add_not_found_url(self, url: str):
        list: List[str] = self.not_found_url
        if not url in list:
            list.append(url)
            self.set_key('not_found_url', list)

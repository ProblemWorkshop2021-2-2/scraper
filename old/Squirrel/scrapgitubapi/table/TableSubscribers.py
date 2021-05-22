from typing import List

from scrapgitubapi.table.table import Table


class TableSubscribers(Table):

    def __init__(self):
        super().__init__("subscribers")

    def get_columns(self) -> List[str]:
        return ['id', 'login', 'site_admin', 'type']

    def write(self, id, login, site_admin, type):
        values = [id, login, site_admin, type]
        self._write_list_as_line(values)

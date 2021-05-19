from typing import List

from scrapgitubapi.table.table import Table


class TableContributors(Table):

    def __init__(self):
        super().__init__("contributors")

    def get_columns(self) -> List[str]:
        return ['id', 'login', 'contributions', 'site_admin', 'type']

    def write(self, id, login, contributions, site_admin, type):
        values = [id, login, contributions, site_admin, type]
        self._write_list_as_line(values)

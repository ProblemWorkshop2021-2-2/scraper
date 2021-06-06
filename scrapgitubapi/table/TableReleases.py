from typing import List

from scrapgitubapi.table.table import Table


class TableReleases(Table):

    def __init__(self):
        super().__init__("releases")

    def get_columns(self) -> List[str]:
        return ['tag_name']

    def write(self, tag_name):
        values = [tag_name]
        self._write_list_as_line(values)

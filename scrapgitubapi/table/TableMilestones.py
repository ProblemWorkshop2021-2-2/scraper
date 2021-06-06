from typing import List

from scrapgitubapi.table.table import Table


class TableMilestone(Table):

    def __init__(self):
        super().__init__("milestones")

    def get_columns(self) -> List[str]:
        return ['number', 'id', 'created_at', 'closed_at', 'title', 'description']

    def write(self, number, id, created_at, closed_at, title, description):
        values = [number, id, created_at, closed_at, title, description]
        self._write_list_as_line(values)

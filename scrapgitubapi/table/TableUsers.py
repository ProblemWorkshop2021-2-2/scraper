from typing import List

from scrapgitubapi.table.table import Table


class TableUsers(Table):

    def __init__(self):
        super().__init__("users")

    def get_columns(self) -> List[str]:
        return ['id', 'login', 'site_admin', 'type', 'name', 'email', 'hireable']

    def write(self, id, login, site_admin, type, name, email, hireable):
        values = [id, login, site_admin, type, name, email, hireable]
        self._write_list_as_line(values)

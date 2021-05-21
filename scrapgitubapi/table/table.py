from typing import List

from scrapgitubapi.util import Config, Util


class Table:

    def __init__(self, file, _delimiter=','):
        self.filePath = f"{Config.working_directory()}/{Config.data_dir()}/{Config.repository_owner()}_{Config.repository_name()}/{file}.csv"
        Util.mkdir(self.filePath)
        self.file = open(self.filePath, 'w')
        self.delimiter = _delimiter
        self._write_list_as_line(self.get_columns())

    def setDelimiter(self, _delimiter: str):
        self.delimiter = _delimiter

    def getDelimiter(self) -> str:
        return self.delimiter

    def _joint_list(self, list: List[str]) -> str:
        joined = ""
        for x in list:
            joined += f"{self.getDelimiter()}{x}"
        joined = joined[1:len(joined)]
        return joined

    def _write_line(self, line: str):
        self.file.write(line + "\n")

    def _write_list_as_line(self, list: List[str]):
        joined = self._joint_list(list)
        self._write_line(joined)

    def get_columns(self) -> List[str]:
        raise NotImplementedError()

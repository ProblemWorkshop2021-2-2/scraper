import json
import os

from scrapgitubapi.util import Config


class Data:

    def __init__(self, file):
        self.filePath = f"{Config.working_directory()}/{file}.json"
        self._data = {}

    def data_load(self) -> None:
        if os.path.exists(self.filePath) and os.path.isfile(self.filePath):
            with open(self.filePath, 'r') as json_file:
                json_lines = json_file.readlines()
                json_file.close()
                json_string = ""
                for json_line in json_lines:
                    json_string += f"{json_line}\n"

                if not json_string == "":
                    json_object = json.loads(json_string)
                    for key in json_object.keys():
                        value = json_object[key]
                        self._data[key] = value
                    self._data_loaded = True

        with open(self.filePath, 'w') as json_file:
            json_config = json.dumps(self._data, ensure_ascii=False, sort_keys=True)
            json_file.write(json_config)
            json_file.writelines("")
            json_file.close()

    def data_save(self):
        with open(self.filePath, 'w') as json_file:
            json_config = json.dumps(self._data, ensure_ascii=False, sort_keys=True)
            json_file.write(json_config)
            json_file.writelines("")
            json_file.close()

    def get_key(self, key: str) -> str:
        self.data_load()
        try:
            return self._data[key]
        except:
            print(f"Key not defined: {key}")
            raise RuntimeError(f"Key not defined: {key}")

    def set_key(self, key: str, value: str):
        self.data_load()
        self._data[key] = value
        self.data_save()

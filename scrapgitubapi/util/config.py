import json
import os

def _load_config_decorator(function):
    def wrapper(*args,**kwargs):
        Config.config_load()
        return function(*args)
    return wrapper

class Config:
    _config_loaded: bool = False
    _config = {
        "github_token":""
    }

    @staticmethod
    def _config_file_path() -> str:
        return Config.working_directory()+"/scraperconfig.json"

    @staticmethod
    def config_load() -> None:
        if Config._config_loaded:
            return
        if os.path.exists(Config._config_file_path()) and os.path.isfile(Config._config_file_path()):
            with open(Config._config_file_path(),'r') as json_file:
                json_lines = json_file.readlines()
                json_file.close()
                json_string = ""
                if not json_string == "":
                    for json_line in json_lines:
                        json_string += f"{json_line}\n"
                    json_object = json.loads(json_string)

                    for key in json_object.keys():
                        value = json_object[key]
                        Config._config[key] = value
                    Config._config_loaded = True

        with open(Config._config_file_path(),'w') as json_file:
            json_config = json.dumps(Config._config,ensure_ascii=False,sort_keys=True)
            json_file.write(json_config)
            json_file.writelines("")
            json_file.close()

    @staticmethod
    def working_directory() -> str:
        return os.getcwd()

    @staticmethod
    @_load_config_decorator
    def github_token() -> str:
        return Config._config['github_token']


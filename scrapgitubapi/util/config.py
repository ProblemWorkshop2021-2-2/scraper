import os

from dotenv import load_dotenv


class Config:
    GITHUB_TOKEN = "GITHUB_TOKEN"
    REPOSITORY_OWNER = "REPOSITORY_OWNER"
    REPOSITORY_NAME = "REPOSITORY_NAME"
    TEMP_DIR = "TEMP_DIR"
    CACHE_DIR = "CACHE_DIR"
    DATA_DIR = "DATA_DIR"

    _config_loaded = False

    @staticmethod
    def _config_file_path() -> str:
        return Config.working_directory() + "/.env"

    @staticmethod
    def config_load() -> None:
        load_dotenv(Config._config_file_path())

    @staticmethod
    def working_directory() -> str:
        return os.getcwd()

    def _get_key(key: str, default):
        if not Config._config_loaded:
            Config.config_load()
            Config._config_loaded = True
        return os.environ.get(key, default)

    @staticmethod
    def github_token() -> str:
        x = Config._get_key(Config.GITHUB_TOKEN, None)
        if x is None:
            raise RuntimeError("You need to setup GITHUB_TOKEN in .env file or enviroment variables")
        return x

    @staticmethod
    def repository_owner() -> str:
        x = Config._get_key(Config.REPOSITORY_OWNER, None)
        if x is None:
            raise RuntimeError("You need to setup REPOSITORY_OWNER in .env file or enviroment variables")
        return x

    @staticmethod
    def repository_name() -> str:
        x = Config._get_key(Config.REPOSITORY_NAME, None)
        if x is None:
            raise RuntimeError("You need to setup REPOSITORY_NAME in .env file or enviroment variables")
        return x

    @staticmethod
    def temp_dir() -> str:
        return Config._get_key(Config.TEMP_DIR, 'temp')

    @staticmethod
    def cache_dir() -> str:
        return Config._get_key(Config.CACHE_DIR, 'cache')

    @staticmethod
    def data_dir() -> str:
        return Config._get_key(Config.DATA_DIR, 'data')

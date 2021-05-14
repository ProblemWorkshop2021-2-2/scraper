import hashlib
import os
from scrapgitubapi.util.config import Config

class Cache(object):

    @staticmethod
    def _cache_directory():
        path = Config.working_directory() + "/cache"
        if not os.path.exists(path):
            os.mkdir(path)
        return path

    @staticmethod
    def _hash(url: str) -> str:
        return hashlib.md5(url.encode('utf-8')).hexdigest()

    @staticmethod
    def save_to_cache(url, text) -> None:
        path = Cache._cache_directory()
        path = f"{path}/{Cache._hash(url)}.json"
        with open(path,'w') as file:
            file.write(text)
            file.close()

    @staticmethod
    def is_cached(url) -> bool:
        path = Cache._cache_directory()
        path = f"{path}/{Cache._hash(url)}.json"
        return os.path.exists(path)

    @staticmethod
    def load_cache(url) -> str:
        path = Cache._cache_directory()
        path = f"{path}/{Cache._hash(url)}.json"
        content = ""
        with open(path,"r") as file:
            for l in file.readlines():
                content += f"{l}\n"
            file.close()
        return content

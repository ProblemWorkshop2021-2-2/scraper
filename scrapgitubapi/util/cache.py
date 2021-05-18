import hashlib
import os

from scrapgitubapi.util.config import Config


class Cache(object):

    @staticmethod
    def mkdir(path: str):
        pathParts = path.split('/')
        pathDirParts = pathParts[0:len(pathParts) - 1]
        pathDir = ""
        for x in pathDirParts:
            pathDir += f"/{x}"
        pathDir = pathDir[1:len(pathDir)]
        if pathDir == '':
            return
        Cache.mkdir(pathDir)
        if not os.path.exists(pathDir):
            os.mkdir(pathDir)

    @staticmethod
    def _url_to_file_path(url):
        path: str = url
        path = path.lower()
        path = path.replace('//', '/')
        path = path.replace('//', '/')
        path = path.replace('//', '/')
        path = path.replace(':', '_')
        path = path.replace('.', '_')
        path = path.replace('___', '_')
        path = path.replace('__', '_')
        path = path.replace('___', '_')
        path = path.replace('__', '_')
        path = path.replace('___', '_')
        path = path.replace('__', '_')
        path = path.replace('___', '_')
        path = path.replace('__', '_')
        path = path.replace('_/', '/')
        path = path.replace('?', '_')
        path = path.replace('=', '_')
        path = path.replace('&', '_')
        path = f"{Cache._cache_directory()}/{path}.json"
        Cache.mkdir(path)
        return path

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
        path = f"{Cache._url_to_file_path(url)}"
        with open(path, 'w') as file:
            file.write(text)
            file.close()

    @staticmethod
    def is_cached(url) -> bool:
        path = f"{Cache._url_to_file_path(url)}"
        return os.path.exists(path)

    @staticmethod
    def load_cache(url) -> str:
        path = f"{Cache._url_to_file_path(url)}"
        content = ""
        with open(path, "r") as file:
            for l in file.readlines():
                content += f"{l}\n"
            file.close()
        return content

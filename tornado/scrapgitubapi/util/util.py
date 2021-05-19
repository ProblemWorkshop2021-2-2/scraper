import os
from typing import List


class Util(object):

    @staticmethod
    def extract_url(obj) -> List[str]:
        print(obj)
        return []

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
        Util.mkdir(pathDir)
        if not os.path.exists(pathDir):
            os.mkdir(pathDir)

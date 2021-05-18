from typing import List

from scrapgitubapi.data.data import Data
from scrapgitubapi.util import Config


class DataUser(Data):

    def __init__(self):
        super().__init__('user')

    def _load_git_log_users(self) -> List[str]:
        list = []
        with open(f"{Config.working_directory()}/commandline_scraped_data_from_git_log/user_names.txt", "r") as file:
            for line in file.readlines():
                login = line.strip()
                list.append(login)
        return list

    # @property
    # def user_not_found_list(self) -> List[str]:
    #    return self.get_key_default('user_not_found_list', [])

    # def clear_user_not_found_list(self):
    #    self.set_key('user_not_found_list', [])

    # def add_user_not_found_list(self, login: str):
    #    list: List[str] = self.user_not_found_list
    #    if not login in list:
    #        list.append(login)
    #        self.set_key('user_not_found_list', list)

    @property
    def user_login_list(self) -> List[str]:
        list = self.get_key_default('user_login_list', [])
        list_from_git_log = self._load_git_log_users()
        for login in list_from_git_log:
            if not login in list:
                list.append(login)
        return list

    def clear_user_login_list(self):
        self.set_key('user_login_list', [])

    def add_user_login(self, login: str):
        list: List[str] = self.user_login_list
        if not login in list:
            list.append(login)
            self.set_key('user_login_list', list)

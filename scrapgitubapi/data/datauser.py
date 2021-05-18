from typing import List

from scrapgitubapi.data.data import Data


class DataUser(Data):

    def __init__(self):
        super().__init__('user')

    @property
    def user_login_list(self) -> List[str]:
        return self.get_key_default('user_login_list', [])

    def clear_user_login_list(self):
        self.set_key('user_login_list', [])

    def add_user_login(self, login: str):
        list: List[str] = self.user_login_list
        if not login in list:
            list.append(login)
            self.set_key('user_login_list', list)

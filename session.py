from typing import Dict


class Session:
    list_session: Dict = {}

    def add_session(self, chat_id, data=""):
        self.list_session[chat_id] = data

    def delete_session(self, chat_id):
        self.list_session.pop(chat_id)

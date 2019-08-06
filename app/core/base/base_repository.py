from abc import ABC, abstractmethod


class BaseRepository(ABC):
    @abstractmethod
    def get_post_list(self):
        pass

    @abstractmethod
    def get_post_item(self, id):
        pass

    @abstractmethod
    def create_post(self, adict):
        pass

    @abstractmethod
    def create_comment(self, adict):
        pass

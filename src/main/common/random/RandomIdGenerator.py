from uuid import uuid4

from injector import singleton

@singleton
class RandomIdGenerator(object):
    def get(self) -> str:
        return uuid4().__str__()
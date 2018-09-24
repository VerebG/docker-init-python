class Resource(object):
    __name: str
    __state: str
    __checksum: str

    def __init__(self,
        name: str,
        state: str,
        checksum: str
    ) -> None:
        self.__name = name
        self.__state = state
        self.__checksum = checksum

    @staticmethod
    def from_exist_resource(self):
        pass

    def get_name(self) -> str:
        return self.__name

    def get_state(self) -> str:
        return self.__state

    def get_checksum(self) -> str:
        return self.__checksum

    def __eq__(self, other):
        pass

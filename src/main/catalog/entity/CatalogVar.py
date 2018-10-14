class CatalogVar(object):
    __name: str
    __value: str

    def __init__(self,
        name: str,
        value: str
    ) -> None:
        self.__name = name
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @property
    def value(self) -> str:
        return self.__value


from src.main.common.exception.DockerContainerInitializationApplicationException import \
    DockerContainerInitializationApplicationException


class CatalogVarNotFoundException(DockerContainerInitializationApplicationException):
    __var_name: str

    def __init__(self,
        var_name: str
    ) -> None:
        self.__var_name = var_name

    def get_message(self) -> str:
        return '{0} variable not found'.format(self.__var_name)





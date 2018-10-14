from src.main.common.exception.DockerContainerInitializationApplicationException import \
    DockerContainerInitializationApplicationException


class ResourceNotFoundException(DockerContainerInitializationApplicationException):
    __id: str

    def __init__(self, id: str) -> None:
        self.__id = id

    def get_message(self) -> str:
        return 'resource not found with #{0}'.format(self.__id)
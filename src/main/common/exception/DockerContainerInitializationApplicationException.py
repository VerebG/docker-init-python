from abc import abstractmethod, ABC


class DockerContainerInitializationApplicationException(Exception, ABC):
    @abstractmethod
    def get_message(self) -> str:
        pass

    def __repr__(self):
        self.get_message()
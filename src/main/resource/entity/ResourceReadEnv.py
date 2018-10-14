from typing import Optional

from src.main.resource.entity.Resource import Resource


class ResourceReadEnv(Resource):
    __name: str
    __value: str
    __default_value: str

    def __init__(self,
        id: str,
        catalog_task_id: str,
        state: str,
        name: str,
        value: Optional[str],
        default_value: Optional[str]
    ) -> None:
        super().__init__(id, catalog_task_id, state)
        self.__name = name
        self.__value = value
        self.__default_value = default_value

    def __eq__(self, other):
        if isinstance(other, ResourceReadEnv):
            return (
                (self.name == other.name) and
                (self.value == other.value)
            )
        else:
            return False

    @property
    def name(self) -> str:
        return self.__name

    @property
    def value(self) -> Optional[str]:
        return self.__value

    @property
    def default_value(self) -> Optional[str]:
        return self.__default_value

    @property
    def can_register(self) -> Optional[str]:
        return self.value

    @property
    def create_from_exist(self) -> str:
        return self.name




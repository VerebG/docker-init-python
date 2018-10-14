from abc import abstractmethod
from typing import Dict

from src.main.common.default.DefaultInterface import DefaultInterface


class CatalogVarListAllBusinessLogic(DefaultInterface):
    @abstractmethod
    def list_all(self) -> Dict:
        pass
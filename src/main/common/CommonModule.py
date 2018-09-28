from injector import Module, singleton, Key

from src.main.common.CommonKey import CommonKey
from src.main.common.logging.AppLogger import AppLogger
from src.main.common.random.RandomIdGenerator import RandomIdGenerator

class CommonModule(Module):
    __colorized_console: bool
    __log_level: str

    def __init__(self,
        colorized_console: bool,
        log_level: str
    ) -> None:
        self.__colorized_console = colorized_console
        self.__log_level = log_level

    def configure(self, binder):

        binder.bind(CommonKey.ColorizedConsole, to=self.__colorized_console, scope=singleton)
        binder.bind(CommonKey.LogLevel, to=self.__log_level, scope=singleton)

        binder.bind(AppLogger, scope=singleton)
        binder.bind(RandomIdGenerator, scope=singleton)
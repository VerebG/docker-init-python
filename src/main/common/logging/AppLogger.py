from logging import Logger, StreamHandler, Formatter
import coloredlogs

from injector import singleton


@singleton
class AppLogger(Logger):

    def __init__(self) -> None:
        super().__init__('app')

        coloredlogs.install(logger=super(), milliseconds=True, fmt='%(levelname)s %(message)s')
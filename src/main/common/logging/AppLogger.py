from logging import Logger, NOTSET, DEBUG, INFO, WARN, ERROR, CRITICAL, StreamHandler, Formatter, LoggerAdapter, getLogger
from injector import singleton, inject

from src.main.common.CommonKey import CommonKey

@singleton
class AppLogger(object):
    __logger: Logger
    __system_logger: Logger
    __stream_handler: StreamHandler
    __colorized_console: bool
    __extra_fields = {}

    @inject
    def __init__(self,
        colorized_console: CommonKey.ColorizedConsole,
        log_level: CommonKey.LogLevel
    ) -> None:
        self.__system_logger = getLogger('app')
        self.__logger = self.__system_logger
        self.__stream_handler = StreamHandler()
        self.__colorized_console = colorized_console
        self.__stream_handler.setFormatter(Formatter('%(level)s: %(message)s'))

        if log_level is None:
            self.__system_logger.setLevel(NOTSET)
        elif log_level.__eq__('debug'):
            self.__system_logger.setLevel(DEBUG)
        elif log_level.__eq__('info'):
            self.__system_logger.setLevel(INFO)
        elif log_level.__eq__('warn'):
            self.__system_logger.setLevel(WARN)
        elif log_level.__eq__('error'):
            self.__system_logger.setLevel(ERROR)
        elif log_level.__eq__('critical'):
            self.__system_logger.setLevel(CRITICAL)
        else:
            raise TypeError('Log level value is not valid!')

    def format(self, format_string: str) -> None:
        self.__stream_handler.setFormatter(Formatter(format_string))
        self.__system_logger.handlers.clear()
        self.__system_logger.addHandler(self.__stream_handler)
        self.__logger = LoggerAdapter(self.__system_logger, self.__extra_fields)

    @property
    def catalog(self) -> str:
        return self.__extra_fields['catalog_name']

    @catalog.setter
    def catalog(self, catalog: str):
        self.__extra_fields['catalog_name'] = catalog

    @property
    def catalog_task_name(self) -> str:
        return self.__extra_fields['catalog_task_name']

    @catalog_task_name.setter
    def catalog_task_name(self, catalog_task_name: str):
        self.__extra_fields['catalog_task_name'] = catalog_task_name

    @property
    def catalog_task_resource_name(self) -> str:
        return self.__extra_fields['catalog_task_resource_name']

    @catalog_task_resource_name.setter
    def catalog_task_resource_name(self, catalog_task_resource_name: str):
        self.__extra_fields['catalog_task_resource_name'] = catalog_task_resource_name

    def debug(self, msg, *args, **kwargs):
        self.__logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.__logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.__logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.__logger.error(msg, *args, **kwargs)
        exit(1)

    def critical(self, msg, *args, **kwargs):
        self.__logger.critical(msg, *args, **kwargs)
        exit(1)

from logging import Logger, NOTSET, DEBUG, INFO, WARN, ERROR, CRITICAL, StreamHandler, Formatter
from coloredlogs import install
from injector import singleton, inject

from src.main.common.CommonKey import CommonKey

@singleton
class AppLogger(Logger):
    extra_field_storage = {}
    stream_handler: StreamHandler

    @inject
    def __init__(self,
        colorized_console: CommonKey.ColorizedConsole,
        log_level: CommonKey.LogLevel
    ) -> None:
        super().__init__('app')

        self.stream_handler = StreamHandler()

        if log_level is None:
            super().setLevel(NOTSET)
        elif log_level.__eq__('debug'):
            super().setLevel(DEBUG)
        elif log_level.__eq__('info'):
            super().setLevel(INFO)
        elif log_level.__eq__('warn'):
            super().setLevel(WARN)
        elif log_level.__eq__('error'):
            super().setLevel(ERROR)
        elif log_level.__eq__('critical'):
            super().setLevel(CRITICAL)
        else:
            TypeError('Log level value is not valid!')

        if colorized_console is True:
            install(logger=super(), milliseconds=True, fmt='%(levelname)s %(message)s')
        else:
            super().addHandler(self.stream_handler)


    def change_format(self, format_string: str) -> None:
        self.stream_handler.setFormatter(Formatter(format_string))
        self.addHandler(self.stream_handler)


from logging import Logger

from injector import Module, singleton

from src.main.common.logging.AppLogger import AppLogger
from src.main.common.random.RandomIdGenerator import RandomIdGenerator


class CommonModule(Module):
    def configure(self, binder):

        binder.bind(AppLogger, scope=singleton)
        binder.bind(RandomIdGenerator, scope=singleton)
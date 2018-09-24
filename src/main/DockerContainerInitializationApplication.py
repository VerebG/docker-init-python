from injector import Module, Injector

from src.main.catalog.CatalogModule import CatalogModule
from src.main.catalog.business.CatalogPrepareToApplyBusinessLogicImpl import CatalogPrepareToApplyBusinessLogicImpl
from src.main.common.CommonModule import CommonModule


class DockerContainerInitializationApplication(object):
    def __get_modules(self) -> [Module]:
        return [
            CommonModule(),
            CatalogModule()
        ]

    def main(self) -> None:
        injector = Injector()

        for module in self.__get_modules():
            injector.binder.install(module)

        run = injector.get(CatalogPrepareToApplyBusinessLogicImpl)
        run.prepare_to_apply('/root/docker-init-python/test.yml')


DockerContainerInitializationApplication().main()
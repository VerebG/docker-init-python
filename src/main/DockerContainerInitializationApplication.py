import pprint

from injector import Module, Injector, singleton

from src.main.catalog.CatalogModule import CatalogModule
from src.main.catalog.business.CatalogPrepareToApplyBusinessLogicImpl import CatalogPrepareToApplyBusinessLogicImpl
from src.main.catalog.business.CatalogTaskListBusinessLogicImpl import CatalogTaskListBusinessLogicImpl
from src.main.catalog.storage.DataMapperCatalog import DataMapperCatalog
from src.main.common.CommonModule import CommonModule


class DockerContainerInitializationApplication(object):
    def __get_modules(self) -> [Module]:
        return [
            CommonModule(True, 'debug'),
            CatalogModule()
        ]

    #def __get_dic_configuration(self, colorized_console: bool) -> None:

    def main(self) -> None:
        injector = Injector()

        for module in self.__get_modules():
            injector.binder.install(module)

        run = injector.get(CatalogPrepareToApplyBusinessLogicImpl)
        run.prepare_to_apply('/root/docker-init-python/test.yml')

        #x = injector.get(DataMapperCatalog).list()

        #print(True)


DockerContainerInitializationApplication().main()
from time import time
from injector import Module, Injector

from src.main.catalog.CatalogModule import CatalogModule
from src.main.catalog.business.CatalogCreateBusinessLogic import CatalogCreateBusinessLogic
from src.main.catalog.business.CatalogExecuteBusinessLogic import CatalogExecuteBusinessLogic
from src.main.common.CommonModule import CommonModule
from src.main.resource.ResourceModule import ResourceModule

start_time = time()

class DockerContainerInitializationApplication(object):
    def __get_modules(self) -> [Module]:
        return [
            CommonModule(True, 'debug'),
            CatalogModule(),
            ResourceModule()
        ]

    def main(self) -> None:
        injector = Injector()

        for module in self.__get_modules():
            injector.binder.install(module)

        run = injector.get(CatalogCreateBusinessLogic)
        run.create('/root/docker-init-python/test.yml')

        execute = injector.get(CatalogExecuteBusinessLogic)
        execute.execute()

        print(True)


DockerContainerInitializationApplication().main()

print("--- %s seconds ---" % (time() - start_time))
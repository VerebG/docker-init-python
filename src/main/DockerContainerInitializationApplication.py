from argparse import ArgumentParser
from time import time
from injector import Module, Injector
from sys import exit

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
        parser = ArgumentParser(description='Configuration manager')
        parser.add_argument('--catalog', help='Specify catalog location')
        parser.add_argument('--log_level', help='Specify log level')
        args = parser.parse_args()

        injector = Injector()

        for module in self.__get_modules():
            injector.binder.install(module)

        run = injector.get(CatalogCreateBusinessLogic)

        if not args.catalog is None:
            run.create(args.catalog)
        else:
            print('Catalog parameter must be filled!')
            exit(1)


        execute = injector.get(CatalogExecuteBusinessLogic)
        execute.execute()


DockerContainerInitializationApplication().main()

print("--- %s seconds ---" % (time() - start_time))
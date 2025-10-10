

from tienda.infrastructure.product_repository import ProductRepository


class DependenciesManager:
    _instance = None
    def __init__(self):
        self.product_repository = ProductRepository()

    @staticmethod
    def get_instance():
        if DependenciesManager._instance is None:
            DependenciesManager._instance = DependenciesManager()
        return DependenciesManager._instance

from tienda.domain.product import Product

class ProductRepository:

    _products = [
        Product(id=1, name="Product 1", price=10.0, stock=100),
        Product(id=2, name="Product 2", price=20.0, stock=200),
        Product(id=3, name="Product 3", price=30.0, stock=300),
    ]

    def __init__(self):
        pass
    def add_product(self, product):
        self._products.append(product)

    def get_all_products(self):
        return self._products

    def find_product_by_name(self, name):
        for product in self._products:
            if product.name == name:
                return product
        return None
    
    def get_product_by_id(self, id):
        for product in self._products:
            if product.id == id:
                return product
        return None
    
    def search_products_by_name(self, name):
        results = []
        for product in self._products:
            if name.lower() in product.nombre.lower():
                results.append(product)
        return results
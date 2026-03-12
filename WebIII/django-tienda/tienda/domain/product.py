
from datetime import datetime

class Product:
    def __init__(self, id: int, name: str, price: float, stock: int):
        self.id = id
        self.nombre = name
        self.precio = price
        self.stock = stock
        self.descripcion = ""
        self.enOferta = False
        self.fechaAlta = datetime.now()

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.nombre}', price={self.precio}, stock={self.stock})"
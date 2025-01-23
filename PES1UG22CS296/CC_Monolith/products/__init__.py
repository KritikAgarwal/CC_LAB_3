from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @classmethod  
    def load(cls, data: dict) -> 'Product':
        return cls(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> list[Product]:
    return [Product.load(product) for product in dao.list_products()]  # Replaced loop with list comprehension


def get_product(product_id: int) -> Product:
    product_data = dao.get_product(product_id)
    if product_data is None:  
        raise ValueError(f'Product with ID {product_id} not found.')
    return Product.load(product_data)


def add_product(product: dict):
    if not all(key in product for key in ['name', 'description', 'cost', 'qty']): 
        raise ValueError('Missing required product fields.')
    if product['cost'] <= 0:  # Added cost validation
        raise ValueError('Cost must be positive.')
    if product['qty'] < 0:  # Added quantity validation
        raise ValueError('Quantity cannot be negative.')
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    if qty < 0: 
        raise ValueError('Quantity cannot be negative.')
    dao.update_qty(product_id, qty)


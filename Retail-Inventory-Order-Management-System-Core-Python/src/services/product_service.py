from typing import List, Dict
from src.dao.product_dao import product_dao, ProductDAO


class ProductError(Exception):
    """Custom exception for product-related errors"""
    pass
    def __init__(self, message: str):
        super().__init__(message)


class ProductService:
    def __init__(self):
        self.dao = ProductDAO()  # Use singleton instance

    def create_product(self, name: str, sku: str, price: float, stock: int = 0, category: str | None = None) -> Dict:
        if price <= 0:
            raise ProductError("Price must be greater than 0")
        if self.dao.get_product_by_sku(sku):
            raise ProductError(f"SKU already exists: {sku}")
        return self.dao.create_product(name, sku, price, stock, category)

    def restock_product(self, prod_id: int, delta: int) -> Dict:
        if delta <= 0:
            raise ProductError("Delta must be positive")
        p = self.dao.get_product_by_id(prod_id)
        if not p:
            raise ProductError("Product not found")
        new_stock = (p.get("stock") or 0) + delta
        return self.dao.update_product(prod_id, {"stock": new_stock})

    def get_low_stock(self, threshold: int = 5) -> List[Dict]:
        all_products = self.dao.list_products(limit=1000)
        return [p for p in all_products if (p.get("stock") or 0) <= threshold]

    def list_products(self, limit: int = 100, category: str | None = None) -> List[Dict]:
        return self.dao.list_products(limit=limit, category=category)

    def get_product(self, prod_id: int) -> Dict:
        p = self.dao.get_product_by_id(prod_id)
        if not p:
            raise ProductError("Product not found")
        return p
    def delete_product(self, prod_id: int) -> Dict:
        p = self.dao.get_product_by_id(prod_id)
        if not p:
            raise ProductError("Product not found")
        return self.dao.delete_product(prod_id)
from typing import List, Dict

from src.dao.order_dao import OrderDAO
from src.dao.product_dao import ProductDAO, product_dao
from src.dao.customer_dao import CustomerDAO   

class OrderError(Exception):
    pass

class OrderService:
    def __init__(self):
        self.dao = OrderDAO()
        self.customer_dao = CustomerDAO()
        self.product_dao = ProductDAO()

    def create_order(self, customer_id: int, items: List[Dict]) -> Dict:
        # Check customer exists
        customer = self.customer_dao.get_customer_by_id(customer_id)
        if not customer:
            raise OrderError("Customer not found")

        total_amount = 0
        stock_updates = []

        # Check product stock
        for item in items:
            product = self.product_dao.get_product_by_id(item["prod_id"])
            if not product:
                raise OrderError(f"Product ID {item['prod_id']} not found")
            if product.get("stock", 0) < item["quantity"]:
                raise OrderError(f"Not enough stock for product {product['name']}")
            total_amount += product["price"] * item["quantity"]
            stock_updates.append((product["prod_id"], product["stock"] - item["quantity"]))
            item["price"] = product["price"]  # store price at order time

        # Deduct stock
        for pid, new_stock in stock_updates:
            self.dao.update_product(pid, {"stock": new_stock})

        # Create order and order items
        return self.dao.create_order(customer_id, total_amount, items)

    def get_order(self, order_id: int) -> Dict:
        order = self.dao.get_order_details(order_id)
        if not order:
            raise OrderError("Order not found")
        customer = self.customer_dao.get_customer_by_id(order["customer_id"])
        order["customer"] = customer
        return order

    def list_orders_for_customer(self, customer_id: int) -> List[Dict]:
        return self.dao.list_orders_by_customer(customer_id)

    def cancel_order(self, order_id: int) -> Dict:
        order = self.dao.get_order_details(order_id)
        if not order:
            raise OrderError("Order not found")
        if order["status"] != "PLACED":
            raise OrderError("Only PLACED orders can be cancelled")

        # Restore product stock
        for item in order["items"]:
            product = product_dao.get_product_by_id(item["prod_id"])
            product_dao.update_product(item["prod_id"], {"stock": product.get("stock", 0) + item["quantity"]})

        # Update order status
        return self.dao.update_order_status(order_id, "CANCELLED")

    def complete_order(self, order_id: int) -> Dict:
        order = self.dao.get_order_details(order_id)
        if not order:
            raise OrderError("Order not found")
        return self.dao.update_order_status(order_id, "COMPLETED")

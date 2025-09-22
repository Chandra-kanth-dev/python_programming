from typing import List, Dict

from src.dao.customer_dao import  CustomerDAO


class CustomerError(Exception):

    pass
    def __init__(self, message: str):
        super().__init__(message)


class CustomerService:
    def __init__(self):
        self.dao = CustomerDAO()  # Use singleton instance

    def add_customer(self, name: str, email: str, phone: str, city: str | None = None) -> Dict:
        if self.dao.get_email_by(email):
            raise CustomerError(f"Email already exists: {email}")
        return self.dao.add_customer(name, email, phone, city)

    def get_customer(self, customer_id: int) -> Dict:
        c = self.dao.get_customer_by_id(customer_id)
        if not c:
            raise CustomerError("Customer not found")
        return c

    def update_customer(self, customer_id: int, fields: Dict) -> Dict:
        c = self.dao.get_customer_by_id(customer_id)
        if not c:
            raise CustomerError("Customer not found")
        return self.dao.update_customer(customer_id, fields)

    def delete_customer(self, customer_id: int) -> Dict:
        c = self.dao.get_customer_by_id(customer_id)
        if not c:
            raise CustomerError("Customer not found")
        return self.dao.delete_customer(customer_id)

    def list_customers(self, limit: int = 100, city: str | None = None) -> List[Dict]:
        return self.dao.list_customers(limit=limit, city=city)




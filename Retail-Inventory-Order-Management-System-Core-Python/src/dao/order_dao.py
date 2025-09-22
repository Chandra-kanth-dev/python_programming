from typing import List, Dict, Optional
from src.config import get_supabase

class OrderDAO:
    def _sb(self):
        return get_supabase()

    # Insert new order and return the row
    def create_order(self, customer_id: int, total_amount: float, items: List[Dict]) -> Dict:
        resp = self._sb().table("orders").insert({"customer_id": customer_id, "total_amount": total_amount}).execute()
        order = resp.data[0]

        # Insert items
        for item in items:
            self._sb().table("order_items").insert({
                "order_id": order["order_id"],
                "prod_id": item["prod_id"],
                "quantity": item["quantity"],
                "price": item["price"]
            }).execute()
        return self.get_order_details(order["order_id"])

    def get_order_details(self, order_id: int) -> Optional[Dict]:
        order_resp = self._sb().table("orders").select("*").eq("order_id", order_id).limit(1).execute()
        order = order_resp.data[0] if order_resp.data else None
        if not order:
            return None

        items_resp = self._sb().table("order_items").select("*").eq("order_id", order_id).execute()
        order["items"] = items_resp.data or []
        return order

    def list_orders_by_customer(self, customer_id: int) -> List[Dict]:
        resp = self._sb().table("orders").select("*").eq("customer_id", customer_id).execute()
        return resp.data or []

    def update_order_status(self, order_id: int, status: str) -> Optional[Dict]:
        self._sb().table("orders").update({"status": status}).eq("order_id", order_id).execute()
        return self.get_order_details(order_id)

order_dao = OrderDAO()

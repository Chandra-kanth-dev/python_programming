from src.dao.order_dao import order_dao
from src.config import get_supabase

class PaymentError(Exception):
    pass

class PaymentService:
    def __init__(self):
        self.sb = get_supabase()

    def create_payment(self, order_id: int, amount: float) -> dict:
        # Insert pending payment
        resp = self.sb.table("payments").insert({
            "order_id": order_id,
            "amount": amount,
            "status": "PENDING"
        }).execute()
        return resp.data[0]

    def process_payment(self, order_id: int, method: str) -> dict:
        # Update payment to PAID
        resp = self.sb.table("payments").update({
            "status": "PAID",
            "method": method,
            "paid_at": "NOW()"
        }).eq("order_id", order_id).execute()

        # Update order status to COMPLETED
        order_dao.update_order_status(order_id, "COMPLETED")
        return resp.data[0] if resp.data else {}

    def refund_payment(self, order_id: int) -> dict:
        # Mark payment as REFUNDED
        resp = self.sb.table("payments").update({
            "status": "REFUNDED",
            "refunded_at": "NOW()"
        }).eq("order_id", order_id).execute()
        return resp.data[0] if resp.data else {}

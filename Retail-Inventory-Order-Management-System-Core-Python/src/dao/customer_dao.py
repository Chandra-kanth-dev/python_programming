from typing import Optional, List, Dict
from src.config import get_supabase

class CustomerDAO:
    def _sb(self):
        return get_supabase()

    def add_customer(self, name: str, email: str, phone: int, city: str | None = None) -> Optional[Dict]:
        if self.get_email_by(email):
            return None  # Email already exists

        payload = {"name": name, "email": email, "phone": phone, "city": city}

    # Insert the record
        self._sb().table("customers_new").insert(payload).execute()

    # Fetch the inserted record
        resp = self._sb().table("customers_new").select("*").eq("email", email).limit(1).execute()
        return resp.data[0] if resp.data else None

    def get_email_by(self, email: str) -> Optional[Dict]:
        resp = self._sb().table("customers_new").select("*").eq("email", email).limit(1).execute()
        return resp.data[0] if resp.data else None

    def get_customer_by_id(self, customer_id: int) -> Optional[Dict]:
        resp = self._sb().table("customers_new").select("*").eq("customer_id", customer_id).limit(1).execute()
        return resp.data[0] if resp.data else None

    def get_customer_by_email(self, email: str) -> Optional[Dict]:
        resp = self._sb().table("customers_new").select("*").eq("email", email).limit(1).execute()
        return resp.data[0] if resp.data else None

    def update_customer(self, customer_id: int, fields: Dict) -> Optional[Dict]:
        self._sb().table("customers_new").update(fields).eq("customer_id", customer_id).execute()
        resp = self._sb().table("customers_new").select("*").eq("customer_id", customer_id).limit(1).execute()
        return resp.data[0] if resp.data else None

    def delete_customer(self, customer_id: int) -> Optional[Dict]:
        resp_before = self._sb().table("customers_new").select("*").eq("customer_id", customer_id).limit(1).execute()
        row = resp_before.data[0] if resp_before.data else None
        self._sb().table("customers_new").delete().eq("customer_id", customer_id).execute()
        return row

    def list_customers(self, limit: int = 100, city: str | None = None) -> List[Dict]:
        q = self._sb().table("customers_new").select("*").order("customer_id", desc=False).limit(limit)
        if city:
            q = q.eq("city", city)
        resp = q.execute()
        return resp.data or []


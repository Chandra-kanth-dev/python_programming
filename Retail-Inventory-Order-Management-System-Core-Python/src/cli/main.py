import argparse
import json
import traceback
from src.services.product_service import ProductService
#from src.services import order_service
from src.dao.product_dao import ProductDAO
from src.dao.customer_dao import  CustomerDAO
from src.dao.order_dao import OrderDAO

from src.services.customer_service import CustomerService
from src.services.order_service import OrderService



class RetailCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(prog="retail-cli")
        self.sub = self.parser.add_subparsers(dest="cmd")
        self._build_product_commands()
        self._build_customer_commands()
        self._build_order_commands()
        self.product_service = ProductService()
        self.customer_service = CustomerService()
        self.order_service = OrderService()

    # ---------- PRODUCT ----------
    def _build_product_commands(self):
        p_prod = self.sub.add_parser("product", help="product commands")
        pprod_sub = p_prod.add_subparsers(dest="action")

        addp = pprod_sub.add_parser("add")
        addp.add_argument("--name", required=True)
        addp.add_argument("--sku", required=True)
        addp.add_argument("--price", type=float, required=True)
        addp.add_argument("--stock", type=int, default=0)
        addp.add_argument("--category", default=None)
        addp.set_defaults(func=self.cmd_product_add)

        listp = pprod_sub.add_parser("list")
        listp.set_defaults(func=self.cmd_product_list)

    def cmd_product_add(self, args):
        try:
            po = ProductDAO()
            p = po.add_product(args.name, args.sku, args.price, args.stock, args.category)
            print("Created product:")
            print(json.dumps(p, indent=2, default=str))
        except Exception as e:
            print("Error:", e)

    def cmd_product_list(self, args):
        try:
            ps = self.product_service.list_products(limit=50)
            print(json.dumps(ps, indent=2, default=str))
        except Exception as e:
            print("Error:", e)
            import traceback
            traceback.print_exc()


    # ---------- CUSTOMER ----------
    def _build_customer_commands(self):
        pcust = self.sub.add_parser("customer", help="customer commands")
        pcust_sub = pcust.add_subparsers(dest="action")

        addc = pcust_sub.add_parser("add")
        addc.add_argument("--name", required=True)
        addc.add_argument("--email", required=True)
        addc.add_argument("--phone", required=True)
        addc.add_argument("--city", default=None)
        addc.set_defaults(func=self.cmd_customer_add)

    def cmd_customer_add(self, args):
        try:
        
            service = CustomerService()
            c = service.add_customer(args.name, args.email, args.phone, args.city)
            print("Created customer:")
            print(json.dumps(c, indent=2, default=str))
        except Exception as e:
            print("Error:", e)
    
    def cmd_customer_list(self, args):
        try:
            customers = CustomerService().list_customers(limit=args.limit, city=args.city)
            if customers:
                print(json.dumps(customers, indent=2, default=str))
            else:
                print("No customers found.")
        except Exception as e:
            print("Error:", e)

            traceback.print_exc()

    # ---------- ORDER ----------
    def _build_order_commands(self):
        porder = self.sub.add_parser("order")
        porder_sub = porder.add_subparsers(dest="action")

        createo = porder_sub.add_parser("create")
        createo.add_argument("--customer", type=int, required=True)
        createo.add_argument("--item", required=True, nargs="+", help="prod_id:qty (repeatable)")
        createo.set_defaults(func=self.cmd_order_create)

        showo = porder_sub.add_parser("show")
        showo.add_argument("--order", type=int, required=True)
        showo.set_defaults(func=self.cmd_order_show)

        cano = porder_sub.add_parser("cancel")
        cano.add_argument("--order", type=int, required=True)
        cano.set_defaults(func=self.cmd_order_cancel)

    def cmd_order_create(self, args):
        items = []
        for item in args.item:
            try:
                pid, qty = item.split(":")
                items.append({"prod_id": int(pid), "quantity": int(qty)})
            except Exception:
                print("Invalid item format:", item)
                return
        try:
            ord_data = self.order_service.create_order(args.customer, items)
            print("Order created:")
            print(json.dumps(ord_data, indent=2, default=str))
        except Exception as e:
            print("Error:", e)

    def cmd_order_show(self, args):
        try:
            o = self.order_service.get_order_details(args.order)
            print(json.dumps(o, indent=2, default=str))
        except Exception as e:
            print("Error:", e)

    def cmd_order_cancel(self, args):
        try:
            o = self.order_service.cancel_order(args.order)
            print("Order cancelled (updated):")
            print(json.dumps(o, indent=2, default=str))
        except Exception as e:
            print("Error:", e)

    def run(self):
        args = self.parser.parse_args()
        if not hasattr(args, "func"):
            self.parser.print_help()
            return
        args.func(args)


def main():
    cli = RetailCLI()
    cli.run()


if __name__ == "__main__":
    main()

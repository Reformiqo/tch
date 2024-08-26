#create sales order from shopify
import frappe
from frappe.utils import getdate
@frappe.whitelist(allow_guest=True)
def create_order(data):
    data = frappe.parse_json(data)
    create_sales_order(data)
    return "Order Created"


def create_customer(customer_name):
    customer = frappe.get_doc({
        "doctype": "Customer",
        "customer_name": customer_name,
        "customer_type": "Individual",
        "customer_group": "Shopify",
        "territory": "All Territories",

    })
    customer.insert(ignore_permissions=True)
    frappe.db.commit()
    return customer

def get_item(data):
    items = []
    for item in data.get("line_items"):
        item = {
            "item_code": item.get("sku"),
            "qty": item.get("quantity"),
            "rate": item.get("price"),
            "warehouse": "Finished Goods - DPL",
            "delivery_date": getdate(data.get("created_at")),
            "uom": "Meter",
            "gst_treatment": "Taxable",
            'igs_amount': get_igst(item)[0] if get_igst(item) else 0,
            'igs_rate': get_igst(item)[1] if get_igst(item) else 0,
            'sgst_amount': get_sgst(item)[0] if get_sgst(item) else 0,
            'sgst_rate': get_sgst(item)[1] if get_sgst(item) else 0,
            'cgst_amount': get_cgst(item)[0] if get_cgst(item) else 0,
            'cgst_rate': get_cgst(item)[1] if get_cgst(item) else 0,
            


        }
        items.append(item)
    return items

def create_sales_order(data):
    customer_name = data.get("customer").get("first_name") + " " + data.get("customer").get("last_name")
    if frappe.db.exists("Customer", {"customer_name": customer_name}):
        customer = frappe.get_doc("Customer", {"customer_name": customer_name})
    else:
        customer = create_customer(customer_name)

    items = get_item(data)
    sales_order = frappe.get_doc({
        "doctype": "Sales Order",
        "shopify_order_id": data.get("id"),
        "shopify_order_number": data.get("name"),
        "customer": customer.name,
        "items": items,
        "delivery_date": getdate(data.get("created_at")),
        "order_type": "Sales",
        "company": "Doeraa Private Limited",
        "currency": "INR",
    })
    sales_order.insert(ignore_permissions=True)
    frappe.db.commit()
    return sales_order.name

def get_igst(item):
    tax_lines = item.get("tax_lines")
    for tax_line in tax_lines:
        if tax_line.get("title") == "IGST":
            return float(tax_line.get("price")), float(tax_line.get("rate"))

def get_cgst(item):
    tax_lines = item.get("tax_lines")
    for tax_line in tax_lines:
        if tax_line.get("title") == "CGST":
            return float(tax_line.get("price")), float(tax_line.get("rate"))

def get_sgst(item):
    tax_lines = item.get("tax_lines")
    for tax_line in tax_lines:
        if tax_line.get("title") == "SGST":
            return float(tax_line.get("price")), float(tax_line.get("rate"))

def get_taxes(data):
    
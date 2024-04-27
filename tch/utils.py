import frappe
@frappe.whitelist()
def get_contact(phone):
    contact = frappe.db.get_value("Customer", {"mobile_no": phone}, fieldname=["name", "mobile_no"], as_dict=1)
    return contact
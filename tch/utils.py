import frappe
@frappe.whitelist(allow_guest=True)
def get_contact(phone):
    #ignore permission
    if not frappe.db.exists("Customer", {"mobile_no": phone}):
        return
    return frappe.get_list("Customer", {'mobile_no':phone})

@frappe.whitelist()
def attendance():
    #reset the check button of attended to 0 of all customers
    cust = frappe.get_all("Customer", filters={"custom_attend": 1}, fields=["name"])
    for c in cust:
        frappe.db.set_value("Customer", c.name, "custom_attend", 0)
        frappe.db.commit()

@frappe.whitelist()
def order():
    items = frappe.qb.DocType("Customers")
    q = (frappe.qb.from_(items))
    return str(items)
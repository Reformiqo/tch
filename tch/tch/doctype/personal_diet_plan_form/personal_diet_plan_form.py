# Copyright (c) 2024, erpera and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PersonalDietPlanForm(Document):
	def validate(self):
		contact = frappe.db.get_value("Customer", {"mobile_no": self.mobile_number}, "mobile_no")
		if not contact:
			frappe.throw("User not found please register first")

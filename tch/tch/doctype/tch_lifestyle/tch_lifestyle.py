# Copyright (c) 2024, erpera and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class TCHLifestyle(Document):
	def after_insert(self):
		if frappe.db.exists("Customer", {"mobile_no": self.mobile_number}):
			customer = frappe.get_doc("Customer", {"mobile_no": self.mobile_number})
			customer.append("custom_tch_lifestyle_forms", {
				"form": self.name,
				'in_the_last_week_what_percentage__did_you_follow_your_diet': self.in_the_last_week_what_percentage__did_you_follow_your_diet,
				'last_week_for_how_many_days_did_you_follow_your_exercise': self.last_week_for_how_many_days_did_you_follow_your_exercise,
				'last_week_how_many_hours_was_your_average_sleep': self.last_week_how_many_hours_was_your_average_sleep,
				'weight': self.weight,
				'current_weight': self.current_weight,
				
			})
			customer.save(ignore_permissions=True)
			frappe.db.commit()
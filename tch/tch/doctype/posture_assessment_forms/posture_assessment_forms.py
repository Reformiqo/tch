# Copyright (c) 2024, erpera and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PostureAssessmentForms(Document):
	def validate(self):
		pass
	def after_insert(self):
		#append the form to the customer's list of forms
		if frappe.db.exists("Customer", {"mobile_no": self.mobile_number}):
			customer = frappe.get_doc("Customer", {"mobile_no": self.mobile_number})
			customer.append("custom_posture_assessment_forms", {
				"form": self.name,
				"image_1": self.image_1,
				"image_2": self.image_2,
				"image_3": self.image_3,
			})
			customer.save(ignore_permissions=True)
			frappe.db.commit()
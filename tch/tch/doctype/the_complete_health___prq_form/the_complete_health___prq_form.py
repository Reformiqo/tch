# Copyright (c) 2024, erpera and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class TheCompleteHealthPRQForm(Document):
	def after_insert(self):
		if frappe.db.exists("Customer", {"mobile_no": self.mobile_number}):
			customer = frappe.get_doc("Customer", {"mobile_no": self.mobile_number})
			customer.append("custom_health_prq_form", {
				"form": self.name,
				'do_you_have_heart_problem': self.do_you_have_heart_problem,
				'do_you_have_high_blood_pressurehypertension': self.do_you_have_high_blood_pressurehypertension,
				'do_you_have_diabetes': self.do_you_have_diabetes,
				'do_you_have_any_joint_pain': self.do_you_have_any_joint_pain,
				'if_yes_then_explain': self.if_yes_then_explain,
				'describe': self.describe,
				'pain_experience_score': self.pain_experience_score,
				'do_you_have_any_injury_in_past': self.do_you_have_any_injury_in_past,
				'do_you_have_asthma_or_any_lungs_diseases': self.do_you_have_asthma_or_any_lungs_diseases,
				'any_other_physical_problem': self.any_other_physical_problem,
				'excercise_experience_score': self.excercise_experience_score,
				
			})
			customer.save(ignore_permissions=True)
			frappe.db.commit()
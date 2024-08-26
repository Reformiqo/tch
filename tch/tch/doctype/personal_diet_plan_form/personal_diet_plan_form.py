# Copyright (c) 2024, erpera and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PersonalDietPlanForm(Document):
	def validate(self):
		# contact = frappe.db.get_value("Customer", {"mobile_no": self.mobile_number}, "mobile_no")
		# if not contact:
		# 	frappe.throw("User not found please register first")
		pass
	def after_insert(self):
		#append the form to the customer's list of forms
		if frappe.db.exists("Customer", {"mobile_no": self.mobile_number}):
			customer = frappe.get_doc("Customer", {"mobile_no": self.mobile_number})
			customer.append("custom_personal_diet_forms", {
				"form": self.name,
				'mobile_number': self.mobile_number,
				'gender':self.gender,
				'age':self.age,
				'height_ft_inch_or_cm':self.height_ft_inch_or_cm,
				'current_weight	':self.current_weight,
				'goal_weight':self.goal_weight,
				'past_3_years_highest_weight':self.past_3_years_highest_weight,
				'past_3_years_lowest_weight':self.past_3_years_lowest_weight,
				'current_waist_inch':self.current_waist_inch,
				'goal_waist_inch':self.goal_waist_inch,
				'current_hip_inch':self.current_hip_inch,
				'goal_hip_inch':self.goal_hip_inch,
				'fat_loss_zone':self.fat_loss_zone,
				'fat_maintain_zone':self.fat_maintain_zone,
				'fat_gain_zone':self.fat_gain_zone,
				'fasting_hours':self.fasting_hours,
				'any_food_allergy':self.any_food_allergy,
				'food_intake':self.food_intake,
				'breakfast':self.breakfast,
				's1':self.s1,
				'lunch':self.lunch,
				's2':self.s2,
				'dinner':self.dinner,	
				'medication_intake':self.medication_intake,			
				'whats_your_b12_level_':self.whats_your_b12_level_,
				'whats_your_d3_level_':self.whats_your_d3_level_,
				'lifestyle_diseases':self.lifestyle_diseases,
				'if_other_diseases_please_write_down_below':self.if_other_diseases_please_write_down_below,
				'what_is_your_goal':self.what_is_your_goal,
				'which_person_are_you_':self.which_person_are_you_,
			})
			customer.save(ignore_permissions=True)
			frappe.db.commit()


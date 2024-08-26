# Copyright (c) 2024, erpera and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class MemberAttendance(Document):
	def after_insert(self):
		#remove any space from the mobile number
		mobile_no = self.phone_number.replace(" ", "")
		if frappe.db.exists("Customer", {"mobile_no": mobile_no}):
			attended = frappe.db.get_value("Customer", {"mobile_no": mobile_no}, "custom_attend")
			if attended == 0:
				att_value = frappe.db.get_value("Customer", {"mobile_no": mobile_no}, "custom_attendance")
				value = att_value + 1
				frappe.db.set_value("Customer", {"mobile_no": mobile_no}, "custom_attendance", value)
				frappe.db.set_value("Customer", {"mobile_no": mobile_no}, "custom_attend", 1)

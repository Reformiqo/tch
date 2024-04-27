// frappe.ready(function() {
// 	// get phone number from server side
// 	value = '8733828562';
// 		frappe.call({
// 			method: "tch.utils.get_contact",
// 			args: {
// 				phone: value,
// 			},
// 			callback: function(r) {
// 				console.log(r.message);
// 						}
// 			}
// 		);
// });

		
// frappe.web_form.validate = () => {
// 		value = frappe.web_form.get_value('mobile_number');
// 		frappe.call({
// 			method: "tch.utils.get_contact",
// 			args: {
// 				phone: value,
// 			},
// 			callback: function(r) {
// 				console.log(r.message);
// 						}
// 			}
// 		);
// 	}

frappe.web_form.on('mobile_number', (field, value) => {
    console.log(value);
});

	

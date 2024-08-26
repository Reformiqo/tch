frappe.ready(function() {
    //set itemShow
    
    frappe.web_form.on('mobile_number', function(fieldname, value) {
        // #while the value is less than 10 dont call the function from the backend
        // if (value.length < 10) {
        //     return;
        // }
        // #call the function from the backend
        
        frappe.call({
            method: 'tch.utils.get_contact',
            args: {
                phone: value
            },
            callback: function(r) {
                

                if (r.message) {
                    var itemShow = [];
                    //iterate over the response and add it to the itemShow
                    for (var i = 0; i < r.message.length; i++) {
                        itemShow.push(r.message[i].name);
                        frappe.web_form.set_df_property('customer', 'options', [""].concat(itemShow))
                        frappe.web_form.set_value('customer', itemShow[0])

                    }
                }
                //clear the customer field if r.message is empty
                else {
                    frappe.web_form.set_df_property('customer', 'options', [""])
                    frappe.web_form.set_value('customer', "")
                }
                
            }
        });
    });
})
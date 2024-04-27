frappe.listview_settings[Lead] = {
button: {
    show: function(doc) {
    return true;
    },
    get_label: function() {
    return __('Send Whatsapp');
    },
    get_description: function(doc) {
    return ('Print {0}', [doc.name])
    },
    action: function(doc) {
        // get the whatsapp number and open the whatsapp web
        var link = 'https://wa.me/' + frm.doc.whatsapp_no;
        window.open(link, "_blank");
    
    }
    }
    }

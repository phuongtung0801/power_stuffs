

import datetime
from dateutil.relativedelta import relativedelta
import frappe


@frappe.whitelist()
def get_list_site_OM_PLINK():
    user_full_name = frappe.request.args.get("user_full_name")
    query = frappe.db.sql(f"""
        select
            `tabSite`.* from `tabSite`;
    """, as_dict=True);
    
    # query = frappe.db.sql(f"""
    #     select * from `tabCustomer Site Owner` where  `tabCustomer Site Owner`.customer_site_owner_name = "{user_full_name}"
    # """, as_dict=True);

    return query

@frappe.whitelist()
def get_list_site_Customer_PLINK():
    user_full_name = frappe.request.args.get("user_full_name")
    query = frappe.db.sql(f"""
        select
            `tabSite`.* from `tabSite`
            inner join `tabCustomer Site Owner` on tabSite.site_label = `tabCustomer Site Owner`.site_label where  `tabCustomer Site Owner`.customer_site_owner_name = "{user_full_name}"
    """, as_dict=True);
    
    # query = frappe.db.sql(f"""
    #     select * from `tabCustomer Site Owner` where  `tabCustomer Site Owner`.customer_site_owner_name = "{user_full_name}"
    # """, as_dict=True);

    return query

    #where  `tabCustomer Site Owner`.customer_site_owner_name = "{user_full_name}"


@frappe.whitelist()
def get_user_type_PLINK():
    user_id = frappe.request.args.get("user_id")
    query = frappe.db.sql(f"""
        select name, full_name, user_type from `tabUser` where name = "{user_id}"
    """, as_dict=True);
    return query
    
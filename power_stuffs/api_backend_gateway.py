

import datetime
from dateutil.relativedelta import relativedelta
import frappe

#GET Site list
@frappe.whitelist()
def get_list_site_OM_PLINK():
    site_label = frappe.request.args.get("site_label")
    if site_label is None:
        query = frappe.db.sql(f"""
            select
                `tabSite`.* from `tabSite`;
        """, as_dict=True);
    else:
        query = frappe.db.sql(f"""
            select
                `tabSite`.* from `tabSite` where site_label = "{site_label}";
        """, as_dict=True);
    
    # query = frappe.db.sql(f"""
    #     select * from `tabCustomer Site Owner` where  `tabCustomer Site Owner`.customer_site_owner_name = "{user_full_name}"
    # """, as_dict=True);

    return query

#GET Site list with filter user
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


#GET Inverter list
@frappe.whitelist()
def get_list_inverter_OM_PLINK():
    query = 0
    site_label = frappe.request.args.get("site_label")
    inverter_name = frappe.request.args.get("inverter_name")
    if site_label is None:
        query = frappe.db.sql(f"""
            select
                `tabSolar Inverter`.* from `tabSolar Inverter`;
        """, as_dict=True);
    else:
        if inverter_name is None:
            query = frappe.db.sql(f"""
                select
                    `tabSolar Inverter`.* from `tabSolar Inverter` where site_label = "{site_label}";
            """, as_dict=True);
        else:
            query = frappe.db.sql(f"""
                select
                    `tabSolar Inverter`.* from `tabSolar Inverter` where site_label = "{site_label}" and name = "{inverter_name}";
            """, as_dict=True);
    
    # query = frappe.db.sql(f"""
    #     select * from `tabCustomer Site Owner` where  `tabCustomer Site Owner`.customer_site_owner_name = "{user_full_name}"
    # """, as_dict=True);

    return query

#GET Inverter list with filter user
@frappe.whitelist()
def get_list_inverter_Customer_PLINK():
    user_full_name = frappe.request.args.get("user_full_name")
    query = frappe.db.sql(f"""
        select
            `tabSolar Inverter`.* from `tabSolar Inverter`
            inner join `tabCustomer Site Owner` on `tabSolar Inverter`.site_label = `tabCustomer Site Owner`.site_label where  `tabCustomer Site Owner`.customer_site_owner_name = "{user_full_name}"
    """, as_dict=True);
    
    # query = frappe.db.sql(f"""
    #     select * from `tabCustomer Site Owner` where  `tabCustomer Site Owner`.customer_site_owner_name = "{user_full_name}"
    # """, as_dict=True);

    return query


#GET user type of account
@frappe.whitelist()
def get_user_type_PLINK():
    user_id = frappe.request.args.get("user_id")
    query = frappe.db.sql(f"""
        select name, full_name, user_type from `tabUser` where name = "{user_id}"
    """, as_dict=True);
    return query
    
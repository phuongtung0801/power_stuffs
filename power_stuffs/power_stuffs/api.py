import frappe

#handle site power daily GET request
#param: 
# {
#     "param": {
#         "dateFrom": "2023-01-16",
#         "site_name": "Gia Lai 4"
#     }
# }
@frappe.whitelist()
def site_power_daily(param):
    dateFrom = param["dateFrom"]
    site_name = param["site_name"]
    dateStart = dateFrom + " 00:00:00"
    dateEnd = dateFrom + " 23:59:59"
    values = {'site_name': site_name, "from": dateStart, "to": dateEnd}
    docArr = frappe.db.sql("""
    select name, docstatus, site_name, power_per_hour, `from`, `to` from `tabSite Power Per Hour` where site_name = %(site_name)s and `from` > %(from)s and `from` < %(to)s order by `from` asc
    """, values= values, as_dict=0)
    sumPowerDaily = 0
    for element in docArr:
        sumPowerDaily = sumPowerDaily + element[3]
    return sumPowerDaily


#handle site power total GET request
#param: 
# {
#     "param": {
#         "dateFrom": "2023-01-09",
#         "dateTo": "2023-01-16",
#         "site_name": "Gia Lai 4"
#     }
# }
@frappe.whitelist()
def site_power_total(param):
    dateFrom = param["dateFrom"]
    dateTo = param["dateTo"]
    site_name = param["site_name"]
    dateStart = dateFrom + " 00:00:00"
    dateEnd = dateTo + " 23:59:59"

    values = {'site_name': site_name, "from": dateStart, "to": dateEnd}
    docArr = frappe.db.sql("""
    select name, docstatus, site_name, power_per_hour, `from`, `to` from `tabSite Power Per Hour` where site_name = %(site_name)s and `from` > %(from)s and `from` < %(to)s order by `from` asc
    """, values= values, as_dict=0)
    sumPowerWeekly = 0
    for element in docArr:
        sumPowerWeekly = sumPowerWeekly + element[3]
    
    return sumPowerWeekly


# #handle site power monthly GET request
# #param: 
# # {
# #     "param": {
# #         "dateFrom": "2023-01-09",
# #         "dateTo": "2023-01-16",
# #         "site_name": "Gia Lai 4"
# #     }
# # }
# @frappe.whitelist()
# def site_power_monthly(param):
#     dateFrom = param["dateFrom"]
#     dateTo = param["dateTo"]
#     site_name = param["site_name"]
#     dateStart = dateFrom + " 00:00:00"
#     dateEnd = dateTo + " 23:59:59"

#     values = {'site_name': site_name, "from": dateStart, "to": dateEnd}
#     docArr = frappe.db.sql("""
#     select name, docstatus, site_name, power_per_hour, `from`, `to` from `tabSite Power Per Hour` where site_name = %(site_name)s and `from` > %(from)s and `from` < %(to)s order by `from` asc
#     """, values= values, as_dict=0)
#     sumPowerMonthly = 0
#     for element in docArr:
#         sumPowerMonthly = sumPowerMonthly + element[3]
    
#     return sumPowerMonthly

# #handle site power quarterly GET request
# #param: 
# # {
# #     "param": {
# #         "dateFrom": "2023-01-09",
# #         "dateTo": "2023-01-16",
# #         "site_name": "Gia Lai 4"
# #     }
# # }
# @frappe.whitelist()
# def site_power_quarterly(param):
#     dateFrom = param["dateFrom"]
#     dateTo = param["dateTo"]
#     site_name = param["site_name"]
#     dateStart = dateFrom + " 00:00:00"
#     dateEnd = dateTo + " 23:59:59"

#     values = {'site_name': site_name, "from": dateStart, "to": dateEnd}
#     docArr = frappe.db.sql("""
#     select name, docstatus, site_name, power_per_hour, `from`, `to` from `tabSite Power Per Hour` where site_name = %(site_name)s and `from` > %(from)s and `from` < %(to)s order by `from` asc
#     """, values= values, as_dict=0)
#     sumPowerQuaterly = 0
#     for element in docArr:
#         sumPowerQuaterly = sumPowerQuaterly + element[3]
    
#     return sumPowerQuaterly



########################################################################################################
#handle site power per hour POST request
#param: an array of Site Power Per Hour doctype object
# Excample: [{
#      "owner": "Administrator",
#      "modified_by": "Administrator",
#      "site_name": "Tan Hoi 3",
#      "power_per_hour": 123,
#      "from": "2023-01-16 12:00:00",
#      "to": "2023-01-16 13:00:00",
#      "doctype": "Site Power Per Hour"
#  }]
#return: number of new or old site power per hour record update
@frappe.whitelist()
def site_power_hourly(param):
    requestBody = param
    # return len(requestBody)
    doc = 0
    newCounter = 0
    oldCounter = 0
    title = 0
    for element in requestBody:
        try:
            doc = frappe.get_last_doc("Site Power Per Hour", filters={"from": element["from"],"to": element["to"], "site_name": element['site_name']})
            doc.delete()
            doc = frappe.get_doc(element)
            doc.insert()
            oldCounter = oldCounter + 1
        except:
            doc = frappe.get_doc(element)
            doc.insert()
            newCounter = newCounter + 1
    return "new site power per hour record:" + str(newCounter) + "\n" + "old record updated: " + str(oldCounter)


#handle inverter power per hour POST request
#param: an array of Inverter Power Per Hour doctype object
# Excample: [{
#      "owner": "Administrator",
#      "modified_by": "Administrator",
#      "inverter_name": "TH3-INV 06",
#      "power_per_hour": 123,
#      "from": "2023-01-16 12:00:00",
#      "to": "2023-01-16 13:00:00",
#      "doctype": "Inverter Power Per Hour"
#  }]dasss
#return: number of new or old site power per hour record update
@frappe.whitelist()
def inverter_power_hourly(param):
    requestBody = param
    # return len(requestBody)
    doc = 0
    newCounter = 0
    oldCounter = 0
    title = 0
    for element in requestBody:
        try:
            doc = frappe.get_last_doc("Inverter Power Per Hour", filters={"from": element["from"],"to": element["to"], "inverter_name": element['inverter_name']})
            doc.delete()
            doc = frappe.get_doc(element)
            doc.insert()
            oldCounter = oldCounter + 1
        except:
            doc = frappe.get_doc(element)
            doc.insert()
            newCounter = newCounter + 1
    return "new inverter power per hour record:" + str(newCounter) + "\n" + "old record updated: " + str(oldCounter)
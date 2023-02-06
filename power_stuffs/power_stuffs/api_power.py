
import datetime
from dateutil.relativedelta import relativedelta
import frappe

@frappe.whitelist()
def site_power_daily(param):
    dateFrom = param["date"]
    site_name = param["site_name"]
    
    # strptime(input_string, input_format)
    date_time_obj = datetime.datetime.strptime(dateFrom, '%Y-%m-%d')
    year = date_time_obj.year
    month = date_time_obj.month
    day = date_time_obj.day
    #######
    powerMonthlyArr  = []
    dateStringStart = datetime.datetime(year, month, day, 00, 00, 00)
    dateStringEnd = datetime.datetime(year, month, day, 23, 59, 59)
    queryString = f"""select site_name, power_per_hour, `from`, `to` from `tabSite Power Per Hour`  where site_name = "{site_name}" and `from` > "{dateStringStart}" and `to` < "{dateStringEnd}" order by `from` asc"""
    docArr = frappe.db.sql(queryString)
    for element in docArr:
        jsonObjDay = {
            "site_name": element[0],
            "power": element[1],
            "from": element[2],
            "to": element[3]
        }
        powerMonthlyArr.append(jsonObjDay)
    response = {
        "length": len(powerMonthlyArr),
        "body": powerMonthlyArr
    }
    return response 


@frappe.whitelist()
def site_power_weekly(param):
    dateFrom = param["date"]
    site_name = param["site_name"]
    
    # strptime(input_string, input_format)
    date_time_obj = datetime.datetime.strptime(dateFrom, '%Y-%m-%d')
    year = date_time_obj.year
    month = date_time_obj.month
    day = date_time_obj.day
    #######
    powerMonthlyArr  = []
    dateStringStart = datetime.datetime(year, month, day, 00, 00, 00)
    dateStringEnd = datetime.datetime(year, month, day + 7, 23, 59, 59)
    queryString = f"""select site_name, power_per_hour, `from`, `to` from `tabSite Power Per Hour`  where site_name = "{site_name}" and `from` > "{dateStringStart}" and `to` < "{dateStringEnd}" order by `from` asc"""
    docArr = frappe.db.sql(queryString)
    for element in docArr:
        jsonObjDay = {
            "site_name": element[0],
            "power": element[1],
            "from": element[2],
            "to": element[3]
        }
        powerMonthlyArr.append(jsonObjDay)
    response = {
        "length": len(powerMonthlyArr),
        "body": powerMonthlyArr
    }
    return response 



@frappe.whitelist()
def site_power_monthly(param):
    dateFrom = param["date"]
    site_name = param["site_name"]
    
    # strptime(input_string, input_format)
    date_time_obj = datetime.datetime.strptime(dateFrom, '%Y-%m-%d')
    year = date_time_obj.year
    month = date_time_obj.month
    day = date_time_obj.day
    #######
    powerMonthlyArr  = []
    dateStringStart = datetime.datetime(year, month, day, 00, 00, 00)
    dateStringEnd = dateStringStart + relativedelta(months=1, days= -1, hours= 23, minutes=59)
    queryString = f"""select site_name, power_per_hour, `from`, `to` from `tabSite Power Per Hour`  where site_name = "{site_name}" and `from` > "{dateStringStart}" and `to` < "{dateStringEnd}" order by `from` asc"""
    docArr = frappe.db.sql(queryString)
    for element in docArr:
        jsonObjDay = {
            "site_name": element[0],
            "power": element[1],
            "from": element[2],
            "to": element[3]
        }
        powerMonthlyArr.append(jsonObjDay)
    response = {
        "length": len(powerMonthlyArr),
        "body": powerMonthlyArr
    }
    return response 


@frappe.whitelist()
def site_power_quarter(param):
    dateFrom = param["date"]
    site_name = param["site_name"]
    
    # strptime(input_string, input_format)
    date_time_obj = datetime.datetime.strptime(dateFrom, '%Y-%m-%d')
    year = date_time_obj.year
    month = date_time_obj.month
    day = date_time_obj.day
    #######
    powerMonthlyArr  = []
    dateStringStart = datetime.datetime(year, month, day, 00, 00, 00)
    dateStringEnd = dateStringStart + relativedelta(months=4, days= -1, hours= 23, minutes=59)
    queryString = f"""select site_name, power_per_hour, `from`, `to` from `tabSite Power Per Hour`  where site_name = "{site_name}" and `from` > "{dateStringStart}" and `to` < "{dateStringEnd}" order by `from` asc"""
    docArr = frappe.db.sql(queryString)
    for element in docArr:
        jsonObjDay = {
            "site_name": element[0],
            "power": element[1],
            "from": element[2],
            "to": element[3]
        }
        powerMonthlyArr.append(jsonObjDay)
    response = {
        "length": len(powerMonthlyArr),
        "body": powerMonthlyArr
    }
    return response 















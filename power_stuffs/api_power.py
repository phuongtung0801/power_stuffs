
import datetime
from dateutil.relativedelta import relativedelta
from collections import defaultdict
import pandas as pd
import frappe


#GET Inverter of Site Power by time range
@frappe.whitelist()
def inverter_of_site_power_by_time_range():
    dateFrom = frappe.request.args.get("dateFrom")
    dateTo = frappe.request.args.get("dateTo")
    site_name = frappe.request.args.get("site_name")

    # #######
    powerMonthlyArr  = []
    sum = 0
    queryString = f"""select site_name, power_per_hour, `from`, `to`, is_accumulated from `tabSite Power Per Hour`  where `from` > "{dateFrom}" and `to` < "{dateTo}" order by `from` asc"""
    # return queryString
    docArr = frappe.db.sql(queryString)
    for element in docArr:
        sum = sum + element[1]
        jsonObjDay = {
            "site_name": element[0],
            "power": element[1],
            "from": element[2],
            "to": element[3],
            "is_accumulated": element[4]
        }
        powerMonthlyArr.append(jsonObjDay)
    response = {
        "length": len(powerMonthlyArr),
        "powerSum": sum,
        "body": powerMonthlyArr
    }
    return response 

#GET all Site Power by time range
@frappe.whitelist()
def all_site_power_by_time_range():
    dateFrom = frappe.request.args.get("dateFrom")
    dateTo = frappe.request.args.get("dateTo")
    # site_name = frappe.request.args.get("site_name")

    # #######
    powerMonthlyArr  = []
    sum = 0
    queryString = f"""select site_name, power_per_hour, `from`, `to` from `tabSite Power Per Hour`  where `from` > "{dateFrom}" and `to` < "{dateTo}" order by `from` asc"""
    # return queryString
    docArr = frappe.db.sql(queryString)
    for element in docArr:
        sum = sum + element[1]
        jsonObjDay = {
            "site_name": element[0],
            "power": element[1],
            "from": element[2],
            "to": element[3],
        }
        powerMonthlyArr.append(jsonObjDay)
    response = {
        "length": len(powerMonthlyArr),
        "powerSum": sum,
        "body": powerMonthlyArr
    }
    return response 
#GET Site Power by time range day view
@frappe.whitelist()
def site_power_by_time_range_day_view():
    dateFrom = frappe.request.args.get("dateFrom")
    dateTo = frappe.request.args.get("dateTo")
    site_name = frappe.request.args.get("site_name")
    # # strptime(input_string, input_format)
    # date_time_obj_from = datetime.datetime.strptime(dateFrom, '%Y-%m-%d')
    # date_time_obj_to = datetime.datetime.strptime(dateTo, '%Y-%m-%d')

    # year = date_time_obj.year
    # month = date_time_obj.month
    # day = date_time_obj.day

    # #######
    powerMonthlyArr  = []
    sum = 0
    # dateStringStart = datetime.datetime(year, month, day, 00, 00, 00)
    # dateStringEnd = datetime.datetime(year, month, day, 23, 59, 59)
    queryString = f"""select site_name, power_per_hour, `from`, `to` from `tabSite Power Per Hour`  where site_name = "{site_name}" and `from` > "{dateFrom}" and `to` < "{dateTo}" order by `from` asc"""
    # return queryString
    docArr = frappe.db.sql(queryString)
    for element in docArr:
        sum = sum + element[1]
        jsonObjDay = {
            "site_name": element[0],
            "power": element[1],
            "from": element[2],
            "to": element[3],
        }
        powerMonthlyArr.append(jsonObjDay)
    response = {
        "length": len(powerMonthlyArr),
        "powerSum": sum,
        "body": powerMonthlyArr
    }
    return response 

#GET Site Power by time range month view
@frappe.whitelist()
def site_power_by_time_range_month_view():
    dateFrom = frappe.request.args.get("dateFrom")
    dateTo = frappe.request.args.get("dateTo")
    site_name = frappe.request.args.get("site_name")
    
    # # strptime(input_string, input_format)
    # date_time_obj_from = datetime.datetime.strptime(dateFrom, '%Y-%m-%d')
    # date_time_obj_to = datetime.datetime.strptime(dateTo, '%Y-%m-%d')

    # year = date_time_obj.year
    # month = date_time_obj.month
    # day = date_time_obj.day

    # #######
    powerMonthlyArr  = []
    powerMonthly  = {
        "power_day_view": 0
    }
    sum = 0
    # dateStringStart = datetime.datetime(year, month, day, 00, 00, 00)
    # dateStringEnd = datetime.datetime(year, month, day, 23, 59, 59)
    queryString = f"""select site_name, power_per_hour, `from`, `to` from `tabSite Power Per Hour`  where site_name = "{site_name}" and `from` > "{dateFrom}" and `to` < "{dateTo}" order by `from` asc"""
    # return queryString
    docArr = frappe.db.sql(queryString)
    # Process day powe
    power_by_date = defaultdict(int)
    for site_name, power, date_from, date_to in docArr:
        date_range = pd.date_range(date_from, date_to, freq="D")
        for date in date_range:
            power_by_date[date.strftime("%Y-%m-%d")] += power
            
        return powerMonthly
        powerMonthlyArr.append(powerMonthly)
    return powerMonthlyArr
    for element in docArr:
        sum = sum + element[1]
        jsonObjDay = {
            "site_name": element[0],
            "power": element[1],
            "from": element[2],
            "to": element[3],
        }
        powerMonthlyArr.append(jsonObjDay)
    response = {
        "length": len(powerMonthlyArr),
        "powerSum": sum,
        "body": powerMonthlyArr
    }
    return response 





#########SITE API###############
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
    queryString = f"""select site_name, power_per_hour, `from`, `to`, is_accumulated from `tabSite Power Per Hour`  where site_name = "{site_name}" and `from` > "{dateStringStart}" and `to` < "{dateStringEnd}" order by `from` asc"""
    docArr = frappe.db.sql(queryString)
    for element in docArr:
        jsonObjDay = {
            "site_name": element[0],
            "power": element[1],
            "from": element[2],
            "to": element[3],
            "is_accumulated": element[4]
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
    queryString = f"""select site_name, power_per_hour, `from`, `to`, is_accumulated from `tabSite Power Per Hour`  where site_name = "{site_name}" and `from` > "{dateStringStart}" and `to` < "{dateStringEnd}" order by `from` asc"""
    docArr = frappe.db.sql(queryString)
    for element in docArr:
        jsonObjDay = {
            "site_name": element[0],
            "power": element[1],
            "from": element[2],
            "to": element[3],
            "is_accumulated": element[4]
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
    queryString = f"""select site_name, power_per_hour, `from`, `to`, is_accumulated from `tabSite Power Per Hour`  where site_name = "{site_name}" and `from` > "{dateStringStart}" and `to` < "{dateStringEnd}" order by `from` asc"""
    docArr = frappe.db.sql(queryString)
    for element in docArr:
        jsonObjDay = {
            "site_name": element[0],
            "power": element[1],
            "from": element[2],
            "to": element[3],
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
    queryString = f"""select site_name, power_per_hour, `from`, `to`, is_accumulated from `tabSite Power Per Hour`  where site_name = "{site_name}" and `from` > "{dateStringStart}" and `to` < "{dateStringEnd}" order by `from` asc"""
    docArr = frappe.db.sql(queryString)
    for element in docArr:
        jsonObjDay = {
            "site_name": element[0],
            "power": element[1],
            "from": element[2],
            "to": element[3],
            "is_accumulated": element[4]
        }
        powerMonthlyArr.append(jsonObjDay)
    response = {
        "length": len(powerMonthlyArr),
        "body": powerMonthlyArr
    }
    return response 







#########INVERTER API###############
@frappe.whitelist()
def inverter_power_daily(param):
    dateFrom = param["date"]
    inverter_name = param["inverter_name"]
    
    # strptime(input_string, input_format)
    date_time_obj = datetime.datetime.strptime(dateFrom, '%Y-%m-%d')
    year = date_time_obj.year
    month = date_time_obj.month
    day = date_time_obj.day
    #######
    powerMonthlyArr  = []
    dateStringStart = datetime.datetime(year, month, day, 00, 00, 00)
    dateStringEnd = datetime.datetime(year, month, day, 23, 59, 59)
    queryString = f"""select inverter_name, power_per_hour, `from`, `to` from `tabInverter Power Per Hour`  where inverter_name = "{inverter_name}" and `from` > "{dateStringStart}" and `to` < "{dateStringEnd}" order by `from` asc"""
    docArr = frappe.db.sql(queryString)
    for element in docArr:
        jsonObjDay = {
            "inverter_name": element[0],
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
def inverter_power_weekly(param):
    dateFrom = param["date"]
    inverter_name = param["inverter_name"]
    
    # strptime(input_string, input_format)
    date_time_obj = datetime.datetime.strptime(dateFrom, '%Y-%m-%d')
    year = date_time_obj.year
    month = date_time_obj.month
    day = date_time_obj.day
    #######
    powerMonthlyArr  = []
    dateStringStart = datetime.datetime(year, month, day, 00, 00, 00)
    dateStringEnd = datetime.datetime(year, month, day + 7, 23, 59, 59)
    queryString = f"""select inverter_name, power_per_hour, `from`, `to` from `tabInverter Power Per Hour`  where inverter_name = "{inverter_name}" and `from` > "{dateStringStart}" and `to` < "{dateStringEnd}" order by `from` asc"""
    docArr = frappe.db.sql(queryString)
    for element in docArr:
        jsonObjDay = {
            "inverter_name": element[0],
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
def inverter_power_monthly(param):
    dateFrom = param["date"]
    inverter_name = param["inverter_name"]
    
    # strptime(input_string, input_format)
    date_time_obj = datetime.datetime.strptime(dateFrom, '%Y-%m-%d')
    year = date_time_obj.year
    month = date_time_obj.month
    day = date_time_obj.day
    #######
    powerMonthlyArr  = []
    dateStringStart = datetime.datetime(year, month, day, 00, 00, 00)
    dateStringEnd = dateStringStart + relativedelta(months=1, days= -1, hours= 23, minutes=59)
    queryString = f"""select inverter_name, power_per_hour, `from`, `to` from `tabInverter Power Per Hour`  where inverter_name = "{inverter_name}" and `from` > "{dateStringStart}" and `to` < "{dateStringEnd}" order by `from` asc"""
    docArr = frappe.db.sql(queryString)
    for element in docArr:
        jsonObjDay = {
            "inverter_name": element[0],
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
def inverter_power_quarter(param):
    dateFrom = param["date"]
    inverter_name = param["inverter_name"]
    
    # strptime(input_string, input_format)
    date_time_obj = datetime.datetime.strptime(dateFrom, '%Y-%m-%d')
    year = date_time_obj.year
    month = date_time_obj.month
    day = date_time_obj.day
    #######
    powerMonthlyArr  = []
    dateStringStart = datetime.datetime(year, month, day, 00, 00, 00)
    dateStringEnd = dateStringStart + relativedelta(months=4, days= -1, hours= 23, minutes=59)
    queryString = f"""select inverter_name, power_per_hour, `from`, `to` from `tabInverter Power Per Hour`  where inverter_name = "{inverter_name}" and `from` > "{dateStringStart}" and `to` < "{dateStringEnd}" order by `from` asc"""
    docArr = frappe.db.sql(queryString)
    for element in docArr:
        jsonObjDay = {
            "inverter_name": element[0],
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













import datetime
from dateutil.relativedelta import relativedelta
from collections import defaultdict
import pandas as pd
import frappe


@frappe.whitelist()
def get_latest_date_from():
    queryString = f"""select site_name, `from`, `to`, `power_per_hour` from `tabSite Power Per Hour` as a where `from`=(select max(`from`)
from `tabSite Power Per Hour`) limit 1;
"""
    docArr = frappe.db.sql(queryString)
    return docArr


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

#GET all Site Power by time range
@frappe.whitelist()
def all_site_power_by_time_range_for_customer():
    dateFrom = frappe.request.args.get("dateFrom")
    dateTo = frappe.request.args.get("dateTo")
    user_email = frappe.request.args.get("user_email")
    # site_name = frappe.request.args.get("site_name")

    # #######
    powerMonthlyArr  = []
    sum = 0
    docArr = frappe.db.sql(f"""
        select
            power.site_name, power.power_per_hour, power.`from`, power.`to`
            from `tabCustomer Site Owner` as site_owner
            inner join `tabSite` as site on site.name = site_owner.site
            inner join `tabCustomer OM` as customer_om on customer_om.name = site_owner.customer_om
            inner join `tabCustomer User` as user on user.customer_name = customer_om.name 
            inner join `tabSite Power Per Hour` as power on power.site_name = site.name
            where user.email = "{user_email}" and 
            power.`from` > "{dateFrom}" and power.`to` < "{dateTo}"
            order by power.`from` asc
    """, as_dict=True);
    for element in docArr:
        sum = sum + element["power_per_hour"]
        jsonObjDay = {
            "site_name": element["site_name"],
            "power": element["power_per_hour"],
            "from": element["from"],
            "to": element["to"],
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
    # #######
    powerMonthlyArr  = []
    sum = 0
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

@frappe.whitelist()
def site_power_by_time_range_day_view_for_customer():
    dateFrom = frappe.request.args.get("dateFrom")
    dateTo = frappe.request.args.get("dateTo")
    user_email = frappe.request.args.get("user_email")
    site_name = frappe.request.args.get("site_name")
    # #######
    powerMonthlyArr  = []
    sum = 0
    # return queryString
    docArr = frappe.db.sql(f"""
        select
            power.site_name, power.power_per_hour, power.`from`, power.`to`
            from `tabCustomer Site Owner` as site_owner
            inner join `tabSite` as site on site.name = site_owner.site
            inner join `tabCustomer OM` as customer_om on customer_om.name = site_owner.customer_om
            inner join `tabCustomer User` as user on user.customer_name = customer_om.name 
            inner join `tabSite Power Per Hour` as power on power.site_name = site.name
            where user.email = "{user_email}" and where power.site_name = {site_name}
            power.`from` > "{dateFrom}" and power.`to` < "{dateTo}"
            order by power.`from` asc
    """, as_dict=True);
    for element in docArr:
        sum = sum + element["power_per_hour"]
        jsonObjDay = {
            "site_name": element["site_name"],
            "power": element["power_per_hour"],
            "from": element["from"],
            "to": element["to"],
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
    # queryString = f"""select site_name, power_per_hour, `from`, `to` from `tabSite Power Per Hour`  where site_name = "{site_name}" and `from` > "{dateFrom}" and `to` < "{dateTo}" order by `from` asc"""
    queryString = f"""SELECT site_name, DATE(`from`) AS day, SUM(power_per_hour) AS sum_power 
        FROM `tabSite Power Per Hour` 
        WHERE site_name = "{site_name}" AND `from` > "{dateFrom}" AND `to` < "{dateTo}"
        GROUP BY site_name, DATE(`from`);"""
    docArr = frappe.db.sql(queryString)
    # # Process day power

    obj = []
    for element in docArr:
        obj.append({
            "site_name": element[0],
            "date": element[1],
            "sum_power": element[2]
        })
    res = {
        "length": len(obj),
        "body": obj
    }
    return res

@frappe.whitelist()
def site_power_by_time_range_month_view_for_customer():
    dateFrom = frappe.request.args.get("dateFrom")
    dateTo = frappe.request.args.get("dateTo")
    site_name = frappe.request.args.get("site_name")
    user_email = frappe.request.args.get("user_email")
    queryString = f"""
         SELECT power.site_name, DATE(power.`from`) AS date, SUM(power.power_per_hour) AS sum_power 
        FROM `tabCustomer Site Owner` AS site_owner
        INNER JOIN `tabSite` AS site ON site.name = site_owner.site
        INNER JOIN `tabCustomer OM` AS customer_om ON customer_om.name = site_owner.customer_om
        INNER JOIN `tabCustomer User` AS user ON user.customer_name = customer_om.name 
        INNER JOIN `tabSite Power Per Hour` AS power ON power.site_name = site.name
        WHERE user.email = "{user_email}" AND power.site_name = "{site_name}" AND 
            power.`from` > "{dateFrom}" AND power.`to` < "{dateTo}" 
        GROUP BY power.site_name, DATE(power.`from`)
        ORDER BY power.`from` ASC
    """
 
    docArr = frappe.db.sql(queryString, as_dict=True);
    # Process day power
    # obj = []
    # for element in docArr:
    #     obj.append({
    #         "site_name": element[0],
    #         "date": element[1],
    #         "sum_power": element[2]
    #     })
    res = {
        "length": len(docArr),
        "body": docArr
    }
    return res


#GET Site Power by time range year view
@frappe.whitelist()
def site_power_by_time_range_year_view():
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
   
    # dateStringStart = datetime.datetime(year, month, day, 00, 00, 00)
    # dateStringEnd = datetime.datetime(year, month, day, 23, 59, 59)
    queryString = f"""select site_name, power_per_hour, `from`, `to` from `tabSite Power Per Hour`  where site_name = "{site_name}" and `from` > "{dateFrom}" and `to` < "{dateTo}" order by `from` asc"""
    # return queryString
    docArr = frappe.db.sql(queryString)
  
    # Process day power
    totals = defaultdict(int)
    for element in docArr:
        date = element[2].strftime("%Y-%m")
        totals[date] += element[1]
    obj = []
    
    for date, total in totals.items():
        obj.append({
            "site_name": site_name,
            "date": date,
            "power": total
        })
    res = {
        "length": len(obj),
        "body": obj
    }
    return res
    





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












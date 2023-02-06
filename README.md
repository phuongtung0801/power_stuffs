## Power Stuffs

calculate power total of site, inverter, add record site, inveter power pwer hour

#### License

MIT# power_stuffs

### APIs
similar

EX: `GET https://erp.plink-cloud.com/api/method/power_stuffs.api_power.inverter_power_daily`
**body**: 
```json
{
     "param": {
         "date": "2023-01-01",
         "inverter_name": "GL4-INV 01"
     }
}
```
**response**:
```json
{
    "message": {
        "length": 1,
        "body": [
            {
                "inverter_name": "GL4-INV 01",
                "power": 0.0,
                "from": "2023-01-01 22:00:00",
                "to": "2023-01-01 23:00:00"
            }
        ]
    }
}
```


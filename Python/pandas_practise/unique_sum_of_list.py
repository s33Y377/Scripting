import pandas as pd
import json

date_data = [
    {"date": "24-Aug", "count": 1},
    {"date": "24-Aug", "count": 1},
    {"date": "25-Aug", "count": 0},
    {"date": "26-Aug", "count": 0},
    {"date": "27-Aug", "count": 0},
    {"date": "28-Aug", "count": 0},
    {"date": "29-Aug", "count": 2},
    {"date": "30-Aug", "count": 0},
    {"date": "31-Aug", "count": 1},
    {"date": "01-Sep", "count": 0},
    {"date": "02-Sep", "count": 0},
    {"date": "03-Sep", "count": 1},
    {"date": "04-Sep", "count": 0},
    {"date": "05-Sep", "count": 1},
    {"date": "06-Sep", "count": 0},
    {"date": "07-Sep", "count": 1},
    {"date": "08-Sep", "count": 0},
    {"date": "09-Sep", "count": 2},
    {"date": "10-Sep", "count": 0},
    {"date": "11-Sep", "count": 1},
    {"date": "12-Sep", "count": 0},
    {"date": "13-Sep", "count": 0},
    {"date": "14-Sep", "count": 0},
    {"date": "15-Sep", "count": 0},
    {"date": "16-Sep", "count": 0},
    {"date": "17-Sep", "count": 0},
    {"date": "18-Sep", "count": 1},
    {"date": "19-Sep", "count": 1},
    {"date": "20-Sep", "count": 0},
    {"date": "21-Sep", "count": 0},
]
date_new_data = [
    {"date": "24-Aug", "count": 1, "avg_count": 5},
    {"date": "24-Aug", "count": 1, "avg_count": 5},
    {"date": "25-Aug", "count": 1, "avg_count": 5},
]
dfObj = pd.DataFrame(date_data)
df2 = dfObj.groupby("date")["count"].sum().to_json()
print(json.loads(df2))

dfObj = pd.DataFrame(date_new_data)
df2 = dfObj.groupby("date")["count"].sum().to_json()
print(json.loads(df2))

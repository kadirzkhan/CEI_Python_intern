import pandas as pd
import requests
import os

def veg_data_scrapper(day:str):
    url = f"https://vegetablemarketprice.com/api/dataapi/market/uttarpradesh/daywisedata?date={day}"
    response = requests.get(url)
    if response.status_code == 200:
        info = response.json()
        date = info['date']
        data = info['data']
        rows = []
        for item in data:
            row = {
            "Date": day,
            "State Name": "Maharashtra",
            "Vegetable Name": item["vegetablename"],
            "Wholesale Price": item["price"],
            "Retail Price": item["retailprice"],
            "Shopping Mall Price": item["shopingmallprice"],
            "Units": item["units"],
            "Vegetable Image": item["table"]["table_image_url"]
            }
            rows.append(row)
        # print(f"Srapping done for {day}")
        df = pd.DataFrame(rows)
        return df
        
if __name__ == "__main__":
    START_DATE = "2024-05-01"
    END_DATE = "2024-06-30"
    days = pd.date_range(START_DATE, END_DATE)
    dfs = []
    for day in days:
        df = veg_data_scrapper(day)
        dfs.append(df)
    
    final_df = pd.concat(dfs, axis='rows')
    final_df.to_csv("Day3_assignment\\Vegetable_data.csv")
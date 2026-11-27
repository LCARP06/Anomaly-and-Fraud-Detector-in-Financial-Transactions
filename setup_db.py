import pandas as pd
import sqlite3 
import numpy as np

#WE CREATE THE DATABASE 
con = sqlite3.connect("transactions.db")


"""
NOW, WE GENERATE THE DATAFRAME OF 500 USERS 
WITH HIS ID, CITY WHERE THEY LIVE AND THEY DAILY LIMIT 
"""
rng = np.random.default_rng(seed=42)

cities = rng.choice(["CDMX","Monterrey","Guadalajara","Tijuana"],
                    size=500)

user_id = np.arange(1,501)

daily_limit = rng.choice([25000,10000,500,2500,5650,1250,1500,2800,7800,1000000,400,6500,1000],
                         size=500)

users = {"cities" : cities, 
         "user_id": user_id,
         "daily_limit": daily_limit}

df_users = pd.DataFrame(users)

df_users.to_sql(name = "users",
                con= con,
                if_exists= "replace",
                index=False)


"""
AFTER THIS, WE GENERATE THE DATAFRAME OF THE TRANSACTIONS FROM THE USERS
WITH HIS 
"""

id_transaction = np.arange(1,20001)

user_id_tran = rng.integers(1,501, size= 20000)

charge = np.round(rng.lognormal(mean=6.0, sigma= 0.8, size= 20000),2)

timestamp = rng.choice(pd.date_range("2026-10-01", "2026-10-31", freq="2min"),size=20000)

is_fraud = 0

category = rng.choice(["Supermarket","Electronics","Restaurant","Streaming"],
                      size=20000)

purchase_city = rng.choice(cities, size= 20000)

transactions = {"id_transaction" : id_transaction,
                "user_id": user_id_tran,
                "charge" : charge,
                "date" : timestamp,
                "category" : category,
                "city": purchase_city,
                "is_fraud": is_fraud}

df_transactions = pd.DataFrame(transactions)

#HERE, WE'RE GOING TO CREATE THE FRAUD TRANSACTIONS

frauds = []
tx_counter = 20001

for i in range(1,101):
    uid = rng.choice(user_id)
    base_time = pd.Timestamp("2026-10-17 13:00:00")     
    fecha_fraude = base_time + pd.Timedelta(minutes=rng.integers(0, 10000))
    
    frauds.append([tx_counter,uid,rng.choice(charge),
                  fecha_fraude,rng.choice(category),"CDMX", 
                    1])
    tx_counter += 1
    frauds.append([tx_counter,uid, 12000,
                  fecha_fraude + pd.Timedelta(minutes=8),rng.choice(category),"Tijuana",1])
    tx_counter += 1
    
df_frauds = pd.DataFrame(frauds, columns=df_transactions.columns)
df_total = pd.concat([df_transactions, df_frauds])

df_total = df_total.sort_values("date")

df_total.to_sql(name = "transactions",
                con = con,
                if_exists = "replace",
                index = False)

con.close()
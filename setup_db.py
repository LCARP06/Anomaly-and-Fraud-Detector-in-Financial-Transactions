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




con.close()
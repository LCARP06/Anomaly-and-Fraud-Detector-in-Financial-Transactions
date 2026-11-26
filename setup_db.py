import pandas as pd
import sqlite3 
import numpy as np

"""
WE CREATE THE DATABASE (BOTH TABLES)
"""

con = sqlite3.connect("transactions.db")
con.close()


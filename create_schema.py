import sqlite3 
conn = sqlite3.connect('ecommerce.db') 
cursor = conn.cursor()

#now we need to create table - 1 
cursor.execute("""
            CREATE TABLE IF NOT EXISTS dim_products(
            product_id INTEGER PRIMARY KEY,
            product TEXT ,
            catagory TEXT )""")

cursor.execute(""" 
                CREATE TABLE IF NOT EXISTS dim_locations(
               location_id INTEGER PRIMARY KEY,
               region TEXT, 
               city TEXT)""")

cursor.execute("""
                  CREATE TABLE IF NOT EXISTS fact_orders(
               order_id INTEGER PRIMARY KEY,
               product_id INTEGER, 
               location_id INTEGER,
               amount FLOAT, 
               order_date TEXT )""")

conn.commit()
conn.close()
print("schema created successfullly")
import sqlite3
import pandas as pd 

conn = sqlite3.connect('ecommerce.db')

df = pd.read_sql('SELECT * FROM ORDERS ', conn )

print(df.head())
print(df.columns)

products = df[['product','category']].drop_duplicates()
print (products)
products = products.reset_index(drop=True)
products['product_id'] = products.index+1
print(products) 

products.to_sql('dim_products',conn , if_exists='replace', index=False)
print("dim_products populated")  

locations = df[['region','city']].drop_duplicates()
print(locations)
locations = locations.reset_index(drop=True)
locations['location_id'] = locations.index + 1
print(locations) 
locations.to_sql('dim_locations', conn ,if_exists='replace',index=False)
print("dim_locations populated")  

fact = df.merge(products, on=['product','category'])
fact = fact.merge(locations, on=['region','city'])
print(fact.columns) 
fact_orders = fact[['order_id', 'product_id', "location_id",'amount', 'order_date']]
print(fact_orders.head()) 
fact_orders.to_sql('fact_orders', conn, if_exists='replace', index=False)
print("fact_orders populated") 
cursor = conn.cursor()
cursor.execute(""" 
                SELECT f.order_id, p.product, l.city, f.amount
                FROM fact_orders f
                JOIN dim_products p ON f.product_id = p.product_id
                JOIN dim_locations l ON f.location_id = l.location_id
                LIMIT 5
                """)
rows = cursor.fetchall()
for row in rows:
    print(row)
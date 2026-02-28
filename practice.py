import sqlite3
import pandas as pd 

conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()
df =  pd.read_sql('SELECT * FROM orders')

products = df[['product','category']].drop_duplicates() 
locations = df[['city','region']].drop_duplicates()

products = products.reset_index(drop=True)
products['product_id']=products.index+1 
products.to_sql('dim_products', conn , if_exists = 'replace', index=False) 

locations = locations.reset_index(drop=True)
locations['location_id'] = locations.index + 1
locations.to_sql('dim_locations',conn , if_exists = 'replace', index=False)

fact = df.merge(products, on=['product', 'category'])
fact = fact.merge(locations , on=['region' , 'city']) 
fact_orders = fact[['order_id', 'product_id' , 'location_id', 'amount', 'order_date']]
fact_orders.to_sql('fact_orders' , conn , if_exists = 'replace' , index = False)
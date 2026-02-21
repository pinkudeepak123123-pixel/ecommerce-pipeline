from generate_orders import generate_orders
import pandas as pd 
import sqlite3



#step 1 - generate orders 
df = generate_orders(1000)


#step- 2 lad to database  
conn = sqlite3.connect('ecommerce.db') 
df.to_sql('orders', conn , if_exists='replace' , index=False )
conn.close()

print("pipeline complete ! 1000 orders generated and loaaded.")
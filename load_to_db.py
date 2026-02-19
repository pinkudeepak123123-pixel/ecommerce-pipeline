import pandas as pd 
import sqlite3
conn = sqlite3.connect('ecommerce.db')
df = pd.read_csv('raw_orders.csv')
df.to_sql('orders', conn , if_exists= 'replace', index=False)
print("Data loaded successfully!")
print(f"Total rows loaded: {len(df)}")
conn.close() 
import sqlite3
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM orders LIMIT 5")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.execute("SELECT product , amount FROM orders WHERE city = 'Tokyo'")    
rows = cursor.fetchall()
for row in rows :
    print (row)

cursor.execute("SELECT product , amount FROM orders WHERE city ='Tokyo' AND amount >=1000" )    
rows = cursor.fetchall()
for row in rows : 
           print(row)  
              
import sqlite3
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

cursor.execute("SELECT product, amount FROM orders WHERE city = 'Tokyo' AND amount >= 1000")
rows = cursor.fetchall()
print(len(rows))

cursor.execute("""
               SELECT product, COUNT(*) as total_orders, SUM(amount) as total_revenue 
               FROM orders
               WHERE city = 'Tokyo'
               GROUP BY product 
                 """)
rows = cursor.fetchall()
for row in rows:
      print(row)
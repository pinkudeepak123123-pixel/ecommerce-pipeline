import sqlite3
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

cursor.execute("""
    SELECT p.category, l.city, SUM(f.amount) as total_revenue
    FROM fact_orders f
    JOIN dim_products p ON f.product_id = p.product_id
    JOIN dim_locations l ON f.location_id = l.location_id
    WHERE p.category = 'Electronics'
    GROUP BY p.category, l.city
    ORDER BY total_revenue DESC
""")


    ### which city has highest average order amount for audio products ? ###
    
cursor.execute(""" 
        SELECT p.product ,l.city , AVG(f.amount) as total_average 
        FROM fact_orders f
        JOIN dim_products p ON f.product_id = p.product_id
        JOIN dim_locations l ON f.location_id = l.location_id
        WHERE p.category = 'Audio'
        GROUP BY p.product , l.city
        ORDER BY total_average DESC 
        """)    





cursor.execute( """ 
    SELECT l.city, MAX(f.amount) as highest_order
FROM fact_orders f
JOIN dim_locations l ON f.location_id = l.location_id
GROUP BY l.city
ORDER BY highest_order DESC """)

rows = cursor.fetchall()
for row in rows:
    print(row) 

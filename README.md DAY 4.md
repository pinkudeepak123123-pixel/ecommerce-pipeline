README.md day-4

create_schema.py 
in this file we divided the whole database into three tables 


1. detailes of products i.e dim_products table 
it contains 1.product_id (primary key)
            2.product 
            3.category
             

2.details of location i.e dim_locations table 
it contains 1.location_id (primary key)
            2.region
            3.city


3.details of orders against product_id from dim_products, location_id from dim_locations 
it contains 1.order_id(primary key)
            2.product_id 
            3.location_id
            4.amount
            5.date 
                                    
so we created three relational tables which are indepent of eachother . 
but these tables are empty right so to fill these tables we need to write another set of codes 
which we did in populate_tables.py 

here we filled the tables and then created a star schema and performed 
a join query to get product_id , city , amount , product as rows  

#JOIN - so we have multiple different unique tables ,which have unique columns which identifies the tables . so using those unique column i.e the primary keys , we can join and get a row of data using multiple different coulmns
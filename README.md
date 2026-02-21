# E-Commerce Analytics Pipeline

## Problem
E-commerce businesses generate thousands of orders daily. 
Without proper data pipelines, it's impossible to track 
which products are selling, where, and when.

## What This Project Does
This pipeline simulates a Rakuten-style e-commerce platform 
generating 1000 orders across Japanese cities. It automatically 
analyzes sales trends by product and region.

## Current Progress
- Stage 1: Data generation (Python + Faker) ✅
- Stage 2: Sales analysis (Pandas) ✅
- Stage 3: Database loading (coming soon)
- Stage 4: Cloud deployment on AWS (coming soon)

## Key Insight From Data
- Top selling product: Monitor (¥795,137 total revenue)
- Top city: Sapporo (¥800,227 total revenue)

#DAY - 2 

# difference between .csv file and data base
 a .csv file is big excel file with texts where we cannot search data using querries , we'll have to search manually and find all the data 
 but a data base is structured file place where there exists relationships and can be querried using sql and can be manipualted 
 SELECT -- selects the column where we will do operations 
 WHERE -- forces conditions and filters out the data 
GROUP BY -- it groups and piles columns in to one group , which is easier to search and perform operatiobs 
COUNT(*) -- counts the ROWS number 



# today i solved one business problems using group by

#DAY-4

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

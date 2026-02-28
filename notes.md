notes.m
  
## merge()
Combines two DataFrames side by side by matching column values.
Adds columns, not rows.

df has orders but no product_id.
products has product_id.
merge connects them by matching 'product' and 'category'.
Result: df now has product_id column.

fact = df.merge(products, on=['product', 'category'])
from faker import Faker
import pandas as pd
import random

fake = Faker()

def generate_orders(num_orders=1000):
    orders = []
    products = ['Laptop', 'Phone', 'Headphones', 'Keyboard', 'Monitor']
    categories = ['Electronics', 'Electronics', 'Audio', 'Accessories', 'Electronics']
    cities = ['Tokyo', 'Osaka', 'Nagoya', 'Fukuoka', 'Sapporo']
    regions = ['Kanto', 'Kansai', 'Chubu', 'Kyushu', 'Hokkaido']

    for i in range(num_orders):
        product_index = random.randint(0, 4)
        city_index = random.randint(0, 4)
        order = {
            'order_id': i + 1,
            'customer_name': fake.name(),
            'product': products[product_index],
            'category': categories[product_index],
            'amount': round(random.uniform(10, 1500), 2),
            'city': cities[city_index],
            'region': regions[city_index],
            'order_date': fake.date_time_between(
                start_date='-30d', end_date='now'
            ).strftime('%Y-%m-%d %H:%M:%S')
        }
        orders.append(order)

    df = pd.DataFrame(orders)
    df.to_csv('raw_orders.csv', index=False)
    print(f"Generated {num_orders} orders and saved to raw_orders.csv")
    print(df.head(10))
    return df

if __name__ == "__main__":
    generate_orders(1000)  
    import pandas as pd
df = pd.read_csv('raw_orders.csv')
print(len(df))
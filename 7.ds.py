import pandas as pd
data = {
    'customer_id': [101, 102, 101, 103, 104, 102, 101],
    'order_date': ['2023-07-01', '2023-07-02', '2023-07-03', '2023-07-03', '2023-07-04', '2023-07-05', '2023-07-06'],
    'product_name': ['A', 'B', 'A', 'C', 'B', 'A', 'C'],
    'order_quantity': [3, 5, 2, 1, 2, 4, 3]
}
order_data = pd.DataFrame(data)
print(order_data)
orders_per_cus = order_data.groupby('customer_id')['order_date'].count()
print('The total number of orders made by each customer:',orders_per_cus)
avg = order_data.groupby('product_name')['order_quantity'].mean()
print('Average order quantity for each product:',avg)
early= order_data['order_date'].min()
print('The earliest order dates in the dataset:',early)
latest = order_data['order_date'].max()
print('The latest order dates in the dataset:',latest)

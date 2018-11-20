'''
    This third file goes over common operations when
working with multiple tables.
'''

import pandas as pd

# Start by creating DataFrames using the .csv files
# Contains information about available products
products = pd.read_csv('products.csv')
print(products.head())
print()
# Contains information about each transaction
orders = pd.read_csv('orders.csv')
print(orders.head())
print()
# Contains information about customers
customers = pd.read_csv('customers.csv')
print(customers.head())
print()
print()
print()


# pandas.merge()
# DataFrame.merge()
'''
pandas.merge()
    Merge two DataFrames. At its simplest, just call
pandas.merge(dataframe1, dataframe2) to merge dataframe2
to dataframe1 (the first dataframe to be passed as an
argument will be leftmost, that is, with this call we
are appending dataframe2's columns to dataframe1).

DataFrame.merge()
    Merge a DataFrame to another existing DataFrame. At
its simplest, call dataframe1.merge(dataframe2) to append
dataframe2's columns to dataframe1.

    The arguments that can be passed are pretty much the same
for both methods.
'''
'''
pandas.merge(left, right, how='inner', left_on=None, 
right_on=None, sort=False, suffixes=('_x', '_y'))

    left: The first DataFrame to be merged.

    right: The second DataFrame to be merged.

    how: {‘left’, ‘right’, ‘outer’, ‘inner’}, defaults to ‘inner’.
        left: includes all rows from the left frame and matched
rows from the right table;
        right: includes all rows from the right frame and matched
rows from the left table;
        outer: use union of keys from both frames, allowing for
mismatched merges. If a mismatch occurs, the missing data will be
substituted by NaN;
        inner: use intersection of keys from both frames. Doesn't
allow mismatched merges.

    left_on: column name or list of names. Match the names passed to
the right_on kwarg to the ones passed to left_one.

    right_on: column name or list of names. Match the names passed to
the right_on kwarg to the ones passed to left_one.

    sort: boolean, defaults to False. If True, sorts the columns in
the resulting DataFrame.

    suffixes: 2-length sequence (tuple, list, etc.). Suffix to apply 
to overlapping column names in the left and right side, respectively.
Suffixes will always be used if left_on and right_on are passed.
'''
# Merge the 'products' and 'orders' DataFrames into a\
# single DataFrame, then merge 'customers' to that
complete_orders = pd.merge(products, orders).merge(customers)
print('Complete Orders DataFrame merge (products+orders+customers):')
print(complete_orders.head())
print()
# Select only the rows where the order price is bigger\
# than 17
orders_over_17 = complete_orders[
    (complete_orders['price'] * complete_orders['quantity']) > 17
    ].reset_index()
# Then, to this DataFrame that holds just the orders that\
# cost more than 17, append a new column with the order cost
orders_over_17['total_cost'] = orders_over_17['price'] * orders_over_17['quantity']
print('Orders that cost more than 17, with its total cost:')
print(orders_over_17)
print()
print()



# pandas.concat()
'''
    Concatenate different DataFrames that hold the same columns
but with different values.
'''
'''
pandas.concat(objs, axis=0, join='outer', ignore_index=False)

    objs: DataFrames to concatenate (must be passed in a list,
array, etc.).

    axis: {0/’index’, 1/’columns’}, defaults to 0. The axis to
concatenate along.

    join: {‘inner’, ‘outer’}, defaults to ‘outer’. How to 
handle indexes on other axis(es).

    ignore_index: boolean, defaults to False. If True, do not 
use the index values along the concatenation axis. The resulting 
axis will be labeled 0, ..., n - 1. 
'''
# Create two new DataFrames using two dictionaries
sample_data1 = {
    'item': ['cookie', 'brownie', 'slice of cake', 'slice of cheesecake', 'slice of pie'],
    'price': [2.50, 3.50, 4.75, 4.75, 5.00]
}
sample_data1 = pd.DataFrame(sample_data1)
sample_data2 = {
    'item': ['scoop of chocolate ice cream', 'scoop of vanilla ice cream', 'scoop of strawberry ice cream', 'scoop of cookie dough ice cream'],
    'price': [3.00, 2.95, 3.05, 3.25],
}
sample_data2 = pd.DataFrame(sample_data2)
# Concatenate two DataFrames which both contain 'item' and 'price' columns only
sample_concat = pd.concat([sample_data1, sample_data2])
print('Concatenation of a bakery and an ice cream parlor menus:')
print(sample_concat)
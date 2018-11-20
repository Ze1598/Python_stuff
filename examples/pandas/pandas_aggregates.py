'''
This second file focuses on data aggregation,
namely aggregate functions, grouping table columns
and pivot tables.
'''

import pandas as pd
import numpy as np

# This will be the sample data to be used
shoes = pd.read_csv('shoe_orders.csv')
# Print the first 5 rows
print(shoes.head())
print()



# Calculating Column/Row statistics
'''
    There are a handful of common functions very
useful to calculate statistical values like
mean, standard deviation, median, etc. across
a single column or row.

    To call these methods, usually the following
syntax is used:
DataFrame.desired_column_row.desired_method()
'''
'''
Common methods to use:
    mean()-     Arithmetic mean
    std()-      Standard Deviation
    median()-   Median
    max()-      Maximum value in column/row
    min()-      Minimum value in column/row
    count()-    Number of values in column/row
    nunique()-  Number of unique values in column
    unique()-   List of unique values in column
'''

print('Most expensive shoes:', shoes['price'].max())
print('Cheapest shoes:', shoes['price'].min())
print('Average price:', shoes['price'].mean())
print('List of available shoe types:', shoes['shoe_type'].unique())
print('Number of unique client IDs:', shoes['id'].nunique())
print()
print()


# Aggregate functions
'''
    After computing statistics about the given data we may
want to group specific parts of the dataset, such as names
and grades or clients and order price.
    For the effect, the groupby() method is used.
    The general syntax for its use looks like this:
DataFrame.groupby('column1').column2.measurement() 
where
    "column1" is the column that we want to group by (e.g. group by client)
    "column2" is the column that we want to perform a measurement on 
(e.g. get the average of the data in the column)
    "measurement" is the measurement function we want to apply (mean, median, etc.)
'''
'''
DataFrame.groupby(by=None, as_index=True, sort=True)

    by: the columns of the DataFrame to be grouped.

    as_index: boolean, defaults to True. If True, the
grouped columns will be used as index.

    sort: boolean, defaults to True. If True, will sort
the rows; if False rows' order stays as is.
'''

# Group the dataset by 'shoe_type' and 'shoe_material', calculating the mean\
# for the 'price's of 'shoe_type' + 'shoe_material' combinations
# Don't sort the rows and print just the first 5 rows. The last column is also\
# renamed
print('Shoe orders grouped by shoe type and shoe material, with the average price per combination')
print(shoes.\
    groupby(by=['shoe_type', 'shoe_material'], sort=False, as_index=False)['price']\
    .mean()\
    .rename(columns=
        {'shoe_type':'shoe_type',
        'shoe_material':'shoe_material',
        'price':'mean_price'
        }
    ).head()
)
print()

# We can also combine groupby() with lambda
print('Shoe orders grouped by shoe material, with the 75th percentile of prices')
print(shoes.\
    groupby(by='shoe_material', sort=True)['price']\
    .apply(lambda x: np.percentile(x, 75))\
    .reset_index()
    .head()
)
print()
print()



# DataFrame.pivot()
'''
    Reshape data in a DataFrame, by adjusting which is displayed
as columns, as indexes and the values to populate the table, that
is, create a Pivot Table
'''
'''
DataFrame.pivot(index=None, columns=None, values=None)

    index: string or object. Column name to use as the index column.
If None is given, uses existing index.

    columns: string or object. Column name whose values will be used
to create columns for the Pivot Table.

    values: string or object. Column name to use for populating 
the Pivot Table's values. If not specified, all remaining columns 
will be used and the result will have hierarchically indexed columns.

If a column you want to use as index contains duplicate values, use
.pivot_table() instead, passing it the same arguments.

You can also use pd.pivot(), passing the name of the target DataFrame
as the first argument.
'''

shoes_pivot = shoes.pivot_table(
    index='shoe_type', 
    columns='shoe_material', 
    values='price'
)
print('Pivot table with shoe types as index, shoe material as columns and prices as values')
print(shoes_pivot.stack())



# DataFrame.melt()
'''
    “Unpivots” a DataFrame, optionally leaving identifier variables
set.

    This function is useful to massage a DataFrame into a format
where one or more columns are identifier variables (id_vars), while
all other columns, considered measured variables (value_vars), are 
“unpivoted” to the row axis, leaving just two non-identifier columns, 
‘variable’ and ‘value’.
'''
'''
DataFrame.melt(id_vars=None, value_vars=None, var_name=None, value_name='value')

    id_vars: tuple, list, or array. Column(s) to use as identifier
variables.

    value_vars: tuple, list, or array. Column(s) to unpivot. If
not specified, uses all columns that are not set as id_vars.

    var_name: scalar. Name to use for the "variable" column. If
None, it uses frame.columns.name or "variable".

    value_name: scalar, defaults to "value". Name to use for
the "value" column.

You can also use pd.melt(), passing the name of the target DataFrame
as the first argument.
'''

# We use pd.melt() to keep shoes_pivot unchanged
shoes_unpivot = pd.melt(
    shoes_pivot, 
    id_vars=['shoe_type'], 
    value_vars=['fabric', 'faux_leather', 'leather']
)
print('"Unpivoted" shoe types\' pivot table')
print(shoes_unpivot)
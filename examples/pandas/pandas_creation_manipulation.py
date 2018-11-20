'''
This first file focuses on creation of DataFrames,
handling .csv files, accessing data in DFs via row
and/or column, adding new content to DFs and editing
said data
'''

import pandas as pd
import numpy as np

# pandas.Dataframe()
'''
    The DataFrame() constructor creates a DataFrame object. These are 
two-dimensional size-mutable, potentially heterogeneous tabular 
data structure with labeled axes (rows and columns).
    Rows are zero-indexed and colums are sorted alphabetically.

    At its simplest, a single dictionary can be passed to the
constructor, where each key in a key-value pair is a string and
the values lists. These lists must all be of the same size (length), 
otherwise a ValueError exception will be raised, that is, all 
columns must have the same number of rows.
'''
'''
pd.DataFrame(data=None, index=None, columns=None, dtype=None)

    data: numpy ndarray (structured or homogeneous), dict, or DataFrame.
dict can contain, arrays, constants, or list-like objects.

    index: Index or array-like. Index to use for resulting frame. 
Will default to np.arange(n) if no indexing information is part of input 
data and no index provided.

    columns: Index or array-like. Column labels to use for resulting frame. 
Will default to np.arange(n) if no column labels are provided.

    dtype: dtype, defaults to None. The data type to be forced. Only a 
single dtype is allowed. If None, infer the data type to use.
'''

df1_data = {
  'Product ID': [1, 2, 3, 4],
  'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
  'Color': ['blue', 'green', '', 'black']
}
df1 = pd.DataFrame(data=df1_data)
print('DataFrame 1:\n', df1)
print()
# Passing a list to the "index" kwarg, we make it so the DataFrame's\
# indexes are the ones included in the list
df1_v2 = pd.DataFrame(data=df1_data, index=[10,20,30,40])
print('DataFrame 1 V2:\n', df1_v2)
print()
# Now that we have a created a list of lists where each nested list is a\
# row of data from the original DataFrame, using it to create a new DataFrame\
# will not include labeled colums. Thus, we can pass a list of strings to the\
# "columns" kwargs so that the column labels are customized. In this case, by\
# default, the indexes for each nested list would be used as column labels
df1_v3 = pd.DataFrame(data=[[df1_data[key][i] for key in df1_data] for i in range(4)], 
                    index=[i for i in range(5, 21, 5)], 
                    columns=['Product ID', 'Product Name', 'Color'])
print('DataFrame 1 V3:\n', df1_v3)
print()
print()



# DataFrame.to_csv()
'''
    Write a DataFrame to a .csv (comma-sepparated values) file.
    Works similarly to file i/o methods in standard Python, thus,
at its simplest, this method can be used just as
DataFrame.to_csv(example_file.csv). If a file path is not given,
the .csv will be created in the current working directory.
'''
'''
DataFrame.to_csv(path_or_buf=None, sep=', ', na_rep='', float_format=None,
columns=None, header=True, index=True, index_label=None, mode='w',
encoding=None)
    
    path_or_buf: string. The name for the file or a file path.

    sep: 1-character string, defaults to ','. Character separating values
in the file (should be a comma, since it's a csv file).
    
    na_rep: string, defaults to empty string (''). String to be used in place
of missing data.
    
    float_format: string, defaults to None. Format string for floating 
point numbers.
    
    columns: sequence. A sequence with the labels of columns
to be written to the file.
    
    header: boolean or list of strings, defaults to True. If False, headers
column headings won't be written to the file. If a list of strings is given,
it must be of the same length as the number of columns in the DataFrame, and
these strings will be used as labels for the columns.
    
    index: boolean, defaults to True. If False, row indexes won't be written
to the file.
    
    index_label: string, sequence or False; defaults to None. If False the index
column won't be written to the file; if a string is given it will be used as the
label for the row column; if a sequence is given, its items will be prepended
to the column headings to be written to the file.
    
    mode: string, defaults to 'w'. The file modes used in standard Python I/O
operations.
    
    encoding: string, defaults to 'utf-8'. The enconding to be used for the
writing operation.
'''
# Writes the df1_v3 DataFrame to a .csv file called "test_csv". It is written\
# without the index column
df1_v3.to_csv('write_csv_test.csv', index=False)
# Other examples
'''
Write the DataFrame using slashes (/) instead of commas, and without the\
column headings
df1_v3.to_csv('test_csv.csv', sep="/", header=False)

Write the DataFrame including only the "Product ID" and "Product Name" columns
df1_v3.to_csv('test_csv.csv', columns=["Product ID", "Product Name"])
'''



# pandas.read_csv()
'''
    Read a .csv file into DataFrame.
    At its simplest, simply call pandas.read_csv('csv_file.csv').
'''
'''
pandas.read_csv(filepath_or_buffer, header='infer', names=None, index_col=None,
dtype=None, nrows=None, na_values=None)

    filepath_or_buffer: string. A file name or file path to a .csv file.

    header: int. The row number to be used as the column headings and, consequently,
the start of the data. Defaults to using the first line of the file and it zero-indexed.

    names: array-like, defaults to None. List of column names to use. If the file 
contains no header row, then you should explicitly pass header=None.

    index_col: int or False, defaults to None. If False, a column for the row labels
won't be used; if an integer is given, that row's contents will be used in the column
for rows' labeling. Passing an integer is zero-indexed.

    dtype: Type name or dict where each pair is of the type column_name: datatype, 
defaults to None. Data type for data or columns. E.g. 
dtype={‘col1’: np.float64, ‘col2’: np.int32}.

    nrows: int, defaults to None. Number of rows of the file to read. Useful for 
reading pieces of large files

    na_filter: boolean, defaults to True. Detect missing value markers (empty strings 
and the value of na_values). In data without any NAs, passing na_filter=False can 
improve the performance of reading a large file.
'''
# Create a DataFrame using the file "write_csv_test.csv". Passing the value False for\
# the na_filter kwarg, we make it so missing values aren't read (such as empty strings)
df_read = pd.read_csv('write_csv_test.csv', na_filter=False)
print('Read CSV to DataFrame:\n', df_read)
print()
print()



# DataFrame.head()
'''
    Returns, by default, the first 5 rows of a DataFrame.
'''
'''
DataFrame.head(n=5)

    n: int, defaults to 5. The number of rows to return.
'''
print('First 2 rows of DataFrame 1:\n', df1.head(n=2))
print()
print()



# DataFrame.info()
'''
    Returns statistics regarding a DataFrame. Includes the
type of the object (DataFrame), Number of rows (not
counting the row for column headings), Number of
Columns (not counting column for row labels), 
Summary of data types in each column, Data types used
in the DataFrame and, lastly, memory usage.
    At its simplest, just call DataFrame.info() without
passing any argument and all these statistics will be
returned.
    Note: this method doesn't need to be printed because it
returns None and outputs automatically the contents.
'''
'''
DataFrame.info(verbose=None)

    verbose: boolean. If False, it includes a count
of used columns, along with the label of the first and last
columns instead of a detailed count of objects per column; if
True, includes all statistics mentioned.
'''
df1.info()
print()



# DataFrame.describe()
'''
    Generates descriptive statistics about numerical columns in
a DataFrames or a Series.
    Signature call:
    DataFrame.describe()
which creates a DataFrame/Series with summary statistics such as

            quantity_bought
    count    4.000000
    mean     2.500000
    std      1.290994
    min      1.000000
    25%      1.750000
    50%      2.500000
    75%      3.250000
    max      4.000000

   For DataFrames with mixed datatypes, the default is to return
only an analysis of numeric columns. If the DataFrame consists
only of of object and categorical data then the default is to
return an analysis of both the object and categorical columns.
To force an analysis of all datatypes, creating a union of 
attributes, call DataFrame.describe(include='all').
    Example:

            Color  Product ID Product Name
    count      4    4.000000            4
    unique     4         NaN            2
    top     blue         NaN      t-shirt
    freq       1         NaN            2
    mean     NaN    2.500000          NaN
    std      NaN    1.290994          NaN
    min      NaN    1.000000          NaN
    25%      NaN    1.750000          NaN
    50%      NaN    2.500000          NaN
    75%      NaN    3.250000          NaN
    max      NaN    4.000000          NaN
'''
'''
    DataFrame.describe(percentiles=None, include=None, exclude=None)

    percentiles: list-like of numbers, defaults to [.25, .5, .75].
The percentiles to include in the output. Should be passed as
floats between 0 and 1.

    include: ‘all’, list-like of dtypes or None (default). A white 
list of data types to include in the result. Ignored for Series.

    exclude: list-like of dtypes or None (default). A black list of
data types to omit from the result. Ignored for Series.
'''
'''
    Passable datatypes values for include and exclude:
    
    numpy.number: limits the result to numeric types.
    
    numpy.object: limits the result to object columns.

    'category': selects pandas categorical columns.
    
    Strings can also be used in the style of select_dtypes 
(e.g. df.describe(include=['O'])). 
'''
print('Dataframe 1 data description:\n', df1.describe())
print()
print('Dataframe 1 complete data description:\n', df1.describe(include='all'))
print()
print('Dataframe 1 data description for objects:\n', df1.describe(include=np.object))
print()
print('Dataframe 1 data description for objects and numbers:\n', df1.describe(include=[np.object, np.number]))
print()
print()



# Selecting single columns
'''
    If we want to access the full contents of a single column, there
are two ways for the effect: 
        treat the dataframe as a dictionary (e.g., with a DF called 
'customers' where we want to access the column 'names', simply use 
the syntax customers['names'])
        if the column name fullfils the rules for a variable name in
Python, we can use that column name as an attribute for the DF and call
it that way (using the same example we could use customers.name).
    We can then create a list or an array of these values, otherwise it
will create a Series (sort of a "minimized" DataFrame), including only 
the values along with the row indexes. It will also include at the end 
the name of the column and its datatype.

Example output:
0     blue
1    green
2         
3    black
Name: Color, dtype: object
'''
print('Dataframe 1 "Color" column contents:\n', df1.Color)
# Alternatively, use df1['Color']
print()
print()


# Selecting multiple columns
'''
    To select multiple columns of a DataFrame use dictionary notation
but with the desired columns wrapped by double brackets. This
produces a new DataFrame.
    e.g. To select the columns "last_name" and "email" from a customers
DataFrame, use the syntax customers[["last_name", "email"]].
'''
print('Dataframe 1 "Product ID" and "Product Name" columns contents:\n', df1[['Product ID', 'Product Name']])
print()
print()



# Selecting rows (DataFrame.iloc)
'''
    To select a row from a DataFrame call iloc on it, passing
an integer or a list/array of integers. DataFrames are zero-indexed,
so passing it a single integer n to .iloc will return the (n+1)th row.
    e.g. Given a customers DataFrame, if we call customers.iloc[2] it
will return its third row.
    Since this indexing works just list indexing, to get multiple rows
(a DataFrame slice if you will), we can use the syntax .iloc[start, stop, step],
where it will return all rows from start up to stop, exclusive, stepping step
rows at a time.
    e.g., to return all the even rows from the customers DataFrame starting at the
second row, use customers.iloc[2::2].
    Note: selecting a single row produces a Series, while selecting multiple rows
produces a new DataFrame.
'''
print('DataFrame 1\'s second row:\n', df1.iloc[1])
print()
print('DataFrame 1\'s odd rows:\n', df1.iloc[1::2])
print()
print()



# Select rows with logic
'''
    We can select rows based on logic that is, if particular values
on the row are bigger than, smaller than, equal to, etc.
    For example, if we have a DataFrame people with personal 
information about various people and we want to select only rows 
of people younger than 30, we can use the syntax 
people[people.Age < 30].
    It is also possible to combine conditions as long as each condition
is parenthesized. Note that the boolean operator or is represented as
"|" and the boolean operator and is represented as "&".
'''
print('DataFrame 1 rows with "Color" "blue:\n', df1[df1.Color == 'blue'])
print()
print('DataFrame 1 rows with "Product Name" "t-shirt" and "Product ID" lower than 3:\n',\
df1[(df1['Product Name'] == 't-shirt') & (df1['Product ID'] < 3)])
print()
print()



# DataFrame.reset_index())
'''
    Reset the indexes for a DataFrame.
'''
'''
DataFrame.reset_index(drop=False, inplace=False)

    drop: boolean, defaults to False. If False
the old indexes will be moved into a new colum labeled
"Index", with the DataFrame's indexes being reseted; if
True, the DataFrame's indexes will be updated, leaving the
rest of the data intact.

    inplace: boolean, defaults to False. If True, it will
modify the current DataFrame; if False, it will create a new
DataFrame with reset indexes.
'''
# Select only the odd rows from df1
df1_odds = df1.iloc[1::2]
# Reset df1_odds' indexes, dropping the old indexes and modifying\
# the existing DF, that is, we are not creating a new DF
df1_odds.reset_index(drop=True, inplace=True)
print('DataFrame 1\'s odd rows with reset indexes:\n', df1_odds)
print()
print()



# Get a list of a DF's indexes
'''
    To get a list of all the DataFrame's indexes, simply call
DataFrame.index and something like  
RangeIndex(start=start_value, stop=stop_value, step=step_value)
will be returned. Then, construct a list by passing that
to the list constructor (list()).
'''
# Get a list with all the indexes of df1
# In essence, this is list(RangeIndex(start=0, stop=4, step=1))
df1_indexes = list(df1.index)
print('DataFrame 1\'s indexes:\n', df1_indexes)
# Now the df1's rows could be easily shuffled with
# df1 = df1.reindex(np.random.permutation(df1_indexes))



# Add new columns to a DataFrame
'''
    To add a new column to a DataFrame, simply use dictionary notation
once again, assigning the to new column a list of length equal to the
length of the columns in the DataFrame.
    If only one value will be used across the whole column simply
assign the new column to the value (e.g. eg_df['new_column'] = 'Tuesday').
    We can also add new columns by applying operations to already existing
columns. Simply assign the new column to the operation you wish to apply
to already existing columns.
'''
'''
    For example, given the following DataFrame (let's call it clothes)
        Color  Product ID Product Name
    0   blue           1      t-shirt
    1  green           2      t-shirt
    2                  3        skirt
    3  black           4        skirt
to add a "Quantity" column we could use the following line of code:
clothes['Quantity'] = [2, 3, 1, 9]
so now the DataFrame looks like this:
        Color  Product ID Product Name  Quantity
    0   blue           1      t-shirt         2
    1  green           2      t-shirt         3
    2                  3        skirt         1
    3  black           4        skirt         9

    Let's say each piece of clothing cost 2.5. If we want
to create a column called "Paid", where holds the price paid
by the customer in each row dependant on the quantity bought,
we could use
clothes['Paid'] = clothes['Quantity'] * 2.5
The result would be this:
        Color  Product ID Product Name  Quantity  Price p/ Unit  Paid
    0   blue           1      t-shirt         2            2.5   5.0
    1  green           2      t-shirt         3            2.5   7.5
    2                  3        skirt         1            2.5   2.5
    3  black           4        skirt         9            2.5  22.5
'''
# df1_v4 starts by being a complete copy of df1
df1_v4 = df1[:]
# Add a 'Quantity' column
df1_v4['Quantity'] = [2, 3, 1, 9]
# Add a 'Price p/ Unit' column, where all rows hold the value 2.5
df1_v4['Price p/ Unit'] = 2.5
# Add a 'Paid' column, which is the the price a customer paid\
# for each purchase (row)
df1_v4['Paid'] = df1_v4['Quantity'] * df1_v4['Price p/ Unit']
print('DataFrame 1 with new columns added:\n', df1_v4)
print()
print()



# DataFrame.append()
'''
    To add (append) new rows to a DataFrame we use the
DatafFrame.append() method. It functions similarly to
lists' append() method, instead here we are appending
other DataFrames, Series, etc. to a DataFrame.
    This method returns a DataFrame, that is, it doesn't
append to a DataFrame inplace.
'''
'''
DataFrame.append(other, ignore_index=False, verify_integrity=False)
    
    other: DataFrame, Series/dict-like object, or a list containing
these datatypes. The data to append.

    ignore_index: boolean, defaults to False. If True, do not use
the index labels from the appended data.

    verify_integrity: boolean, defaults to False. If True, raise
a ValueError exception when creating indexes for duplicate rows.
'''
append_data = pd.DataFrame({'Product ID': [list(df1_v4.index)[-1]+2],
                            'Product Name': ['shorts'], 
                            'Color': ['yellow'], 
                            'Quantity': [3], 
                            'Price p/ Unit': [5.0],
                            'Paid': [15.0]})
df1_v4 = df1_v4.append(append_data, ignore_index=True)
print('DataFrame 1 with a new row appended:\n', df1_v4)
print()
print()



# DataFrame.apply()
'''
    This function applies a given function along the axis
of a DataFrame.
'''
'''
DataFrame.apply(func, axis=0)

    func: The function to be applied.

    axis: {0 or ‘index’, 1 or ‘columns’}, defaults to 0-
If 0 or ‘index’, the function is applied to each column; If 
1 or ‘columns’, the function is applied to each row.
'''
# Makes all values in the 'Product Name' column uppercase
df1_v4['Product Name'] = df1_v4['Product Name'].apply(str.upper)
# Creates a column 'Comment' based on the values of the 'Quantity'\
# column. If the quantity is bigger than 5 the comment will be\
# "Bought a lot", else if bigger than 2 it is "Moderate Purchase",\
# else the comment is "Bought a few"
df1_v4['Comment'] = df1_v4['Quantity'].apply(lambda x: 'Bought a lot' if x > 5 else 'Moderate Purchase' if  x > 2 else 'Bought a few')
# Create a column 'Full Name' which is just the concatenation of the\
# color and name of the product of each row.
df1_v4['Full Name'] = df1_v4.apply(
    lambda row: row['Color'].upper() + ' ' + row['Product Name'],
    axis=1
)
print('DataFrame 1 with functions applied:\n', df1_v4)
print()
print()



# Change column headings/labels
'''
    To change all the column headings in a DataFrame
simply assign DataFrame.columns to a list of strings to
be used as the new labels. This list must be of length
equal to the number of existing columns.
'''

# DataFrame.rename()
'''
Rename the axis of the DataFrame.
'''
'''
DataFrame.rename(mapper=None, index=None, columns=None, axis=None, inplace=False)

    mapper: A mapping object with contents of the type 
label_to_change: new label or a function to be applied to the
labels. The affected axis needs to be specified with the "axis" kwarg.

    index: Same as mapper, but without the need to specify the axis.

    columns: Same as mapper, but without the need to specify the axis.

    axis: {0 or ‘index’, 1 or ‘columns’}, defaults to 'index'. The axis to
be the target of modifications.

    inplace: boolean, defaults to False. If True, modifies the existing
DataFrame; if False creates a new DataFrame.
'''
df1.rename(
    {'Color': 'Color',
    'Product ID': 'Prod ID',
    'Product Name': 'Prod Name'
    },
    axis=1,
    inplace=True
)
print('DataFrame 1 with modified column headings:\n', df1)
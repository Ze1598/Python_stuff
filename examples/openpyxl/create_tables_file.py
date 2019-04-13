import openpyxl
# Convert column addresses
from openpyxl.utils import get_column_letter, column_index_from_string
# Create tables
from openpyxl.worksheet.table import Table, TableStyleInfo
import re
import datetime
import calendar

TABLES_ROWS = [6, 5, 3, 3, 5, 5, 4, 3, 5, 8, 5]

TABLE_TITLES = [
	"Workforce",
	"Type of Worker",
	"Compensation",
	"Type of Employment Contract",
	"Education Status",
	"Retention Status",
	"Productivity",
	"Location",
	"Department",
	"Category",
	"Nationality"
]

TABLE_ROW_VALUES = [

]

MONTHS = [
	"January",
	"February",
	"March",
	"April",
	"May",
	"June",
	"July",
	"August",
	"September",
	"October",
	"November",
	"December"
]

def create_table_range (num_rows, num_months, cell_origin):
	'''
	Create the range representation for a single new Excel table.

	Parameters
	----------

	Returns
	-------
	'''

	# We need enough columns for: name of the indicator, a column per month\
	# and an extra one to account for the starting column
	last_column  = get_column_letter(1 + num_months)
	start_row = str(cell_origin)
	last_row = str(cell_origin + num_rows - 1)
	# The starting column will always be the first one ("A")
	return f"A{start_row}:{last_column}{last_row}"

# Helper function to extract the row from a cell address
def get_row (cell):
	return re.split("(\d+)", cell)[1]

# Helper function to extract the column from a cell address
def get_column (cell):
	return re.split("(\d+)", cell)[0]

def create_new_table (tab_range, tab_name):
	'''
	Create a new Excel table object with given its range and name.

	Parameters
	----------

	Returns
	-------
	'''

	# Create a style for the table
	new_tab_style = TableStyleInfo(
		name="TableStyleLight15",
		showFirstColumn=False,
		showLastColumn=False,
		showRowStripes=True,
		showColumnStripes=False
	)

	# Create a new Excel table object
	new_tab_obj = Table(
		displayName="_".join( tab_name.split() ),
		ref=tab_range
	)

	# Set the created style as the style for the new table
	new_tab_obj.tableStyleInfo = new_tab_style

	return new_tab_obj


if __name__ == "__main__":
	# Create a new empty workbook
	wb = openpyxl.Workbook()
	# Move to the active worksheet a.k.a. the first one
	ws = wb.active
	ws.title = "HR Metrics"

	# Dictionary with the starting index of each year of activity in the list\
	# of month headers
	month_headers_years = {"2018":4}
	# The last four months correspond to the four months of activity in 2018
	month_headers = MONTHS[8:]
	# Get the numeric representation of the current month (1-12)
	current_month = datetime.date.today().month
	# The first month of 2019 will be at this index
	month_headers_years["2019"] = len(MONTHS[:current_month])
	# Append the passed months of 2019 to the list of month headers
	month_headers.extend(MONTHS[:current_month])

	# List of the ranges for each table
	tables_ranges = []
	# The first table will be put at the "A3" cell
	cell_origin_row = 3
	# Create the ranges for each table
	for i in range( len(TABLES_ROWS) ):
		# Find the range for the new table
		table_range = create_table_range(TABLES_ROWS[i], len(month_headers), cell_origin_row)
		
		# Add the new range to the list of table ranges
		tables_ranges.append(table_range)
		
		# Set the title of the table, i.e., the text in the cell above the table
		ws.cell(row=cell_origin_row-1, column=1).value = f"{i+1}. {TABLE_TITLES[i]}"
		
		# Set the headers for each table
		# Loop through the columns of the table
		last_col = column_index_from_string( get_column( table_range.split(":")[1] ) )
		# The header for the first column is always "Indicator"
		ws.cell(row=cell_origin_row, column=1).value = "Indicator"
		for i in range(2, last_col+1):
				ws.cell(row=cell_origin_row, column=i).value = month_headers[i-2]

		# Update the next table to start 3 rows below where the last table ended
		cell_origin_row = int( get_row( table_range.split(":")[1] ) ) + 3

	# List of Excel table objects
	table_objs = []
	# Create the Excel table objects
	for i in range( len(TABLES_ROWS) ):
		table_objs.append( create_new_table(tables_ranges[i], TABLE_TITLES[i]) )

	# Insert the tables in the workbook
	for i in range( len(tables_ranges) ):
		ws.add_table(table_objs[i])

	# In the first row, merge cells to cover the months of each respective year
	# Get a sorted list of the years of activity
	years_headers = sorted(month_headers_years.keys())
	# The first merge will start at the second column
	merge_start_col = 2
	# Loop through said list to write in the first row of the worksheet and\
	# then merge the cells for the header to cover all the months of that\
	# year
	for year in years_headers:
		# First write the year to the first cell of the to-be merged cells
		ws.cell(row=1, column=merge_start_col).value = year

		# If this is the last year, then the header will span from the\
		# current column up to the last column of the tables		
		if years_headers.index(year) == ( len(years_headers)-1 ):
			merge_end_col = get_column_letter(last_col)
		
		# Otherwise, the header will span the space between the current\
		# column up to the one of the last month of that year
		else:
			year_length = month_headers_years[ str( int(year) + 1 ) ]
			merge_end_col = get_column_letter( merge_start_col + year_length - 1 )
		
		# Create the string with the merge range
		merge_range = f"{get_column_letter(merge_start_col)}1:{merge_end_col}1"
		# Merge the desired cells
		ws.merge_cells(merge_range)
		# The next year's banner will be as many columns away from the\
		# first cell of the current year as this year has months of\
		# activity
		merge_start_col += month_headers_years[year]
		

	# Finally, create and save the file
	wb.save("test_excel.xlsx")
import openpyxl
# Convert column addresses
from openpyxl.utils import get_column_letter, column_index_from_string
# Create tables
from openpyxl.worksheet.table import Table, TableStyleInfo
# Regular expressions for extracting column and row values from cell addresses
import re

# print("Available tables:", len(ws._tables))

# print("Table name:", target_table.displayName)
# print("Table type:", target_table.tableType)
# print("Table range:", target_table.ref)

# Helper function to extract the column from a cell address
def get_column (cell):
	return re.split("(\d+)", cell)[0]

# Helper function to extract the row from a cell address
def get_row (cell):
	return re.split("(\d+)", cell)[1]


def get_table_range (og_table_range):
	# Get starting address
	start = og_table_range.split(":")[0]
	# Get ending address
	end = og_table_range.split(":")[1]

	# Get the starting column of the table
	start_col = int( column_index_from_string(get_column(start)) )
	# Get the ending column of the table
	end_col = int ( column_index_from_string(get_column(end)) )
	# Get the starting row of the table
	start_row = int( get_row(start) )
	# Get the ending row of the table
	end_row = int( get_row(end) )

	# Starting column of the new table ("A" column)
	first_col = 1
	# Ending column of the new table
	last_col = int(end_col) - int(start_col) + 1
	# Starting row of the new column (first row)
	first_row = 1
	# Ending row of the new table
	last_row = int(end_row) - int(first_row) + 1

	# Now create the string for the table's range
	final_range = f"{get_column_letter(first_col)}{first_row}:{get_column_letter(last_col)}{last_row}"
	# print(final_range)

	return final_range



if __name__ == "__main__":

	# Load the workbook
	wb = openpyxl.load_workbook("test_ws.xlsx")
	# Choose the worksheet "Sheet1"
	ws = wb.get_sheet_by_name("Sheet1")
	# The target table is the first one
	target_table = ws._tables[0]

	# Access the range of data of the table. Then, scrape the first and last\
	# columns, as well as the first and last rows
	first_column = get_column(target_table.ref.split(":")[0])
	last_column = get_column(target_table.ref.split(":")[1])
	first_row = get_row(target_table.ref.split(":")[0])
	last_row = get_row(target_table.ref.split(":")[1])

	# print("First column:", first_column)
	# print("Last column:", last_column)
	# print("First row:", first_row)
	# print("Last row:", last_row)

	# Get all the columns in the target table and print the name of each
	# columns = target_table.tableColumns
	# print("Column names:")
	# for col in columns:
		# print("\t", col.name)

	# List to hold lists of rows; represents the new table
	new_table = []
	# Loop through the cells in the table to print their contents
	# Loop through the rows
	for row in range(int(first_row), int(last_row)+1):
		# List to contain the values for the current row
		temp_row = []
		# Loop through the columns
		for col in range( int(column_index_from_string(first_column)), int(column_index_from_string(last_column))+1 ):
			# print(ws.cell(row=row, column=col).value)
			# Append the value of the current cell to the temporary row
			temp_row.append(ws.cell(row=row, column=col).value)
		
		# Append the created row to the table
		new_table.append(temp_row)

	# Create a new worksheet
	wb.create_sheet("MyTestSheet")
	# Create the string with the range for the new table
	new_table_range = get_table_range(target_table.ref)

	# First we add the data to the worksheet, and then we set that range of\
	# data to be a table

	# Append the rows of data from the new table list to the newly-created\
	# worksheet
	for row in new_table:
		wb.get_sheet_by_name("MyTestSheet").append(row)
	
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
		displayName="myTable",
		ref=new_table_range
	)
	# Set the created style as the style for the new table
	new_tab_obj.tableStyleInfo = new_tab_style
	# Add the table object to the new worksheet
	wb.get_sheet_by_name("MyTestSheet").add_table(new_tab_obj)
	# Save the file
	wb.save("test_ws.xlsx")



'''
sheet.cell(row=val, column=val).value
sheet.max_row
sheet.max_column
ws.cell(row=row, column=col).row
ws.cell(row=row, column=col).column

'''
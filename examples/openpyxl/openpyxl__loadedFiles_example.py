'''
File that goes over basic operations with the openpyxl module: a
module for working with Excel files (.xlsx) and LibreOffice Calc
(.xls), that is, workbook files.
This file goes over the basic operations performed with these files,
without touching any writing to the files.
'''

import openpyxl
# Used to pretty-print the information written to the output file
import pprint 

# Input
# -----------------------------------------------------------------
# book(load) a worksheet file (we'll use an Excel file in this\
# case)
wb = openpyxl.load_workbook("openpyxl_sample.xlsx")
# -----------------------------------------------------------------


# Get sheets
# -----------------------------------------------------------------
# Get a list with the names of each sheet in the file
wb_sheets = wb.get_sheet_names()
# Get the sheet with name "Sheet1"
single_sheet = wb.get_sheet_by_name("Sheet1")
# Print the title of the sheet
print(single_sheet.title)
# Gets the sheet currently open in the file
active_sheet = wb.active
print(active_sheet)
print()
# -----------------------------------------------------------------


# Get cells
# -----------------------------------------------------------------
# Print the cell located at A1 in the "Sheet1" sheet
a1_cell = single_sheet["A1"]
print(a1_cell)
# Actually print the value saved in the cell (properly converted to a\
# Python datatype)
print(a1_cell.value)
# Print the coordinates of the A1 cell
print(f"`a1_cell` is located at row {a1_cell.row} and column {a1_cell.column}, that is, {a1_cell.coordinate}.")
# Print the value of another cell (cell located at B1)
# This time we access a cell by calling the `cell()` method and pass the\
# the desired coordinate as row and column values
print(single_sheet.cell(row=1, column=2).value)
print()
# -----------------------------------------------------------------


# Access rows and columns
# -----------------------------------------------------------------
# Print the values saved in all the rows of the second column (B)
print("Values saved in the second column:")
# Loop through all the rows in the second column and print the values found
# Use the `max_row` attribute to find the index of the last row in this sheet
for i in range(1, single_sheet.max_row+1):
	print(f"Row {i}, Value {single_sheet.cell(row=i, column=2).value}")
print()
# Print the number of columns found in the current sheet by using the\
# `max_column` attribute
print(f"{single_sheet.title} has {single_sheet.max_column} columns.")
print()

# Extract the first three rows, including columns A through C
extract_rows = tuple(single_sheet["A1":"C3"])
# Each item corresponds to a single row, that is, a single item contains\
# all the cells of that row
print(extract_rows)
print("Loop through rows 1 through 3, including columns A through C.")
for row_of_cell_objs in extract_rows:
	for cell_obj in row_of_cell_objs:
		print(cell_obj.coordinate, cell_obj.value)
	print('--- END OF ROW ---')
print()
# We can loop through all the columns in a given row by with dictionary syntax
# Loop through the cells in the first row column (column B)
for cell_obj in single_sheet[1]:
	print(cell_obj.value)
print()
# -----------------------------------------------------------------


# Convert between integer and alphabetic representation of columns
# -----------------------------------------------------------------
# Because a workbook can have many columns, the when it reachs the 27th\
# it needs to start using two letters to represent the column. Thus, we\
# can use `get_column_letter()` method to input the integer representation\
# of a column and get the alphabetic representation returned
print("get_column_letter(27) =>", openpyxl.utils.get_column_letter(27))
print("get_column_letter(900) =>", openpyxl.utils.get_column_letter(900))
# The exact operation, that is, get the integer representation given the\
# alphabetic counterpart, is done via the `column_index_from_string()` method
print("column_index_from_string(AA) =>", openpyxl.utils.column_index_from_string("AA"))
print("column_index_from_string(AHP) =>", openpyxl.utils.column_index_from_string("AHP"))
print()
# -----------------------------------------------------------------

# Load an Excel file, extract data and save it in a new Python file
# -----------------------------------------------------------------
wb = openpyxl.load_workbook("censuspopdata.xlsx")
sheet = wb.get_sheet_by_name("Population by Census Tract")
# Dictionary to hold the extracted data in the format:
# county_data[state][county]["tracts"]
# county_data[state][county]["pop"]
county_data = {}

# Loop through all the rows in the file
for row in range(2, sheet.max_row+1):
	# Get the state, county and population count for the current row
	state = sheet["B"+str(row)].value
	county = sheet["C"+str(row)].value
	pop = sheet["D"+str(row)].value

	# To make sure a key for the current state exists in the dictionary,\
	# create the key-value pair `county_data[state] = {}`
	county_data.setdefault(state, {})
	# Create default values as well for the values of the current `state`\
	# key, so that the `state` key holds a dictionary of the type:
	# county_data[state][county]["tracts"]
	# county_data[state][county]["pop"]
	county_data[state].setdefault( county, {"tracts":0, "pop":0} )

	# Since each row represents a census tract, increment the `tracts` key
	county_data[state][county]["tracts"] += 1
	# While we are in the same row, that is, the same county, add up the\
	# population amounts found
	county_data[state][county]["pop"] += int(pop)

# Now write the extracted data to a Python file
with open("openpyxl_sample_output_file.py", "w") as f:
	f.write("all_data = " + pprint.pformat(county_data))

# -----------------------------------------------------------------
'''
File that goes over basic operations with the openpyxl module: a
module for working with Excel files (.xlsx) and LibreOffice Calc
(.xls), that is, workbook files.
This file goes over some operations in the context of writing directly
to these files / creating new workbook files.
'''

import openpyxl
from openpyxl.styles import Font

# Create a new workbook with some sheets
# -----------------------------------------------------------------
# Create a Workbook object to represent a new workbook file (it contains\
# an empty "Sheet" sheet by default)
wb = openpyxl.Workbook()

sheet = wb.active
# Update the title of the active (and only) sheet
sheet.title = "My Sheet"
# Create a new sheet
wb.create_sheet("My Sheet (2)")
# Create a new sheet and place it in between the two already existing sheets\
# (that is, it will be the second sheet in order)
# Note: this index is zero-based
wb.create_sheet(index=1, title="Middle Sheet")
# Print the names of all the existing sheets
print(wb.get_sheet_names())
# Remove the "Middle Sheet" sheet
wb.remove_sheet(wb.get_sheet_by_name("Middle Sheet"))
print(wb.get_sheet_names())

# Actually save the workbook as an Excel file
wb.save("openpyxl_createdFile_example.xlsx")
# -----------------------------------------------------------------


# Write values to cells
# -----------------------------------------------------------------
wb = openpyxl.load_workbook("openpyxl_sample.xlsx")
# Pick the "My Sheet" sheet
work_sheet = wb.get_sheet_by_name("Sheet1")
# Write a string to the A1 cell
# work_sheet["A1"] = "Hello World!"
# Create a dictionary with where the values are the new values for the\
# cells in the B column with the corresponding keys
update_values = {
	"Apples": 12,
	"Cherries": 150,
	"Bananas": 75
}
# Loop through the second column and update the value of the third column\
# if the value in the second column matches one of the keys in the dictionary
for i in range(1, work_sheet.max_row+1):
	# Get the current cell
	curr_cell = work_sheet.cell(row=i, column=2)
	# If the value of the current cell is a key in the dictionary, then update\
	# the value of that row in the third (C) column
	if curr_cell.value in update_values:
		work_sheet.cell(row=i, column=3).value = update_values[curr_cell.value]
# -----------------------------------------------------------------


# Work with fonts
# -----------------------------------------------------------------
# Make an object for the font using size 11 and italic style. It's also possible\
# to pass it the kwargs `name` for the font family and `bold` to bold the text
ital_font = Font(size=11, italic=True)
# Italicize all the rows in the first (A) column
for i in range(1, work_sheet.max_row+1):
	work_sheet.cell(row=i, column=1).font = ital_font
# -----------------------------------------------------------------


# Use formulas in cell values
# -----------------------------------------------------------------
# We'll use the first empty row
target_row = work_sheet.max_row+1

# Create a condition just to prevent the duplication of the row when this\
# script is run more than once
if work_sheet.cell(row=target_row-1, column=2).value == "Strawberries":
	# Create the cell that holds the "Total:" text
	total_text = work_sheet.cell(row=target_row, column=2)
	# Write the value of the cell
	total_text.value = "Total:"
	# Change its font
	total_text.font = Font(size=11, bold=True)

	# Create the cell that holds the actual sum
	total_value = work_sheet.cell(row=target_row, column=3)
	# Start of the range of cells for the SUM function
	start = work_sheet.cell(row=1, column=3).coordinate
	# End of the range of cells for the SUM function
	end = work_sheet.cell(row=target_row-1, column=3).coordinate
	# Write the value of the cell (the SUM function)
	total_value.value = f"=SUM({start}:{end})"
# -----------------------------------------------------------------


# Change row and column heigh and width
# -----------------------------------------------------------------
# Change the height of the totals row
	work_sheet.row_dimensions[target_row].height = 70
# Change the width of the first (A) column
	work_sheet.column_dimensions["A"].width = 35
# -----------------------------------------------------------------


# Merge and unmerge cells
# -----------------------------------------------------------------
# Unmerge the given cells
# work_sheet.unmerge_cells("B9:C11")

# Populate the rows 9 through 11 and the columns B and C so that we can\
# then merge all the involved cells
# for i in range(3):
# 	curr_cell = work_sheet.cell(row=9+i, column=2)
# 	curr_cell.value = "X"
# 	curr_cell = work_sheet.cell(row=9+i, column=3)
# 	curr_cell.value = "Y"
# Now merge all these six cells
# work_sheet.merge_cells("B9:C11")
# -----------------------------------------------------------------


# Create freeze panes (rows that overlay the screen at all times)
# -----------------------------------------------------------------
'''
freeze_panes setting				Rows and columns frozen

sheet.freeze_panes = 'A2'			Row 1

sheet.freeze_panes = 'B1'			Column A

sheet.freeze_panes = 'C1'			Columns A and B

sheet.freeze_panes = 'C2'			Row 1 and columns A and B

sheet.freeze_panes = 'A1' or 		No frozen panes
sheet.freeze_panes = None
'''

# The first row will be a freeze pane
# panes = work_sheet.freeze_panes = "A2"
work_sheet.freeze_panes = None
# -----------------------------------------------------------------


# Charts (pie chart example)
# -----------------------------------------------------------------
# The reference data for the chart will be found in the third column
data = openpyxl.chart.Reference(work_sheet, min_col=3, min_row=1, max_col=3, max_row=7)
# The reference labels for the chart will be found in the second column
labels = openpyxl.chart.Reference(work_sheet, min_col=2, min_row=1, max_col=2, max_row=7)

# Create the pie chart
chart_obj = openpyxl.chart.PieChart()
# Set the chart's title
chart_obj.title = "Sample Pie Chart"
# Add the data
chart_obj.add_data(data)
# Add the categories/labels
chart_obj.set_categories(labels)
# Draw the chart at E3
work_sheet.add_chart(chart_obj, "E3")
# -----------------------------------------------------------------


# Save the changes to the file
wb.save("openpyxl_sample.xlsx")
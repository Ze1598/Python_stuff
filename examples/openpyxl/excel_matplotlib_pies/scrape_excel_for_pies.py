import openpyxl # Scrape Excel documents
from matplotlib import pyplot as plt # Plot pie charts


def extract_answer_freqs (target_columns):
	'''
	Returns a dictionary of the type columnHeader-listOfAnswersFrequencies,
	where the list contains the frequencies of each reply in the corresponding
	column. The functions extracts frequencies from the columns included in
	`target_columns`.

	Parameters
	----------
	target_columns : list
		A list of strings where each string is the letter representation
		of a target column.

	Returns
	-------
	table : dict
		A dictionary with pairs of the type
		columnHeader-listOfAnswersFrequencies.
	'''

	# Dictionary to be returned with the results
	table = {}
	# We will always start at the second row of each column
	row_ind = 2

	# Loop through the target columns
	for col in target_columns:
		# Integer representation of the current column's index
		curr_col = openpyxl.utils.column_index_from_string(col)
		# Value of the first row of the current column
		col_name = ws.cell(row=1, column=curr_col).value
		# If the column header contains the word "scale", then the values vary\
		# between 1 and 10 inclusive, thus we need 10 indices in the list, one\
		# to count the frequency of each answer; if the header does not contain\
		# "scale", then apply the same logic, except this time only for 5 answers
		if "scale" in col_name.lower():
			table[col_name] = [0 for x in range(10)]
		else:
			table[col_name] = [0 for x in range(5)]

		# Get the values from the current row and the next one
		curr_row = ws.cell(row=row_ind, column=curr_col).value
		next_row = ws.cell(row=row_ind+1, column=curr_col).value
		# While either the current or the next row is not empty, keep\
		# extracting data from the column
		while (curr_row != None) or (next_row != None):
			# Append the value to the list holding the values contained in the\
			# current column
			# table[col_name].append(ws.cell(row=row_ind, column=curr_col).value)
			table[col_name][curr_row-1] += 1
			# Move to the next row
			row_ind += 1
			# Update which rows are the current and the next rows
			curr_row = next_row
			next_row = ws.cell(row=row_ind+1, column=curr_col).value

		# Start back at the first row of the next column
		row_ind = 2

	return table



def plot_pie_charts (freqs_table):
	'''
	Plot pie charts for the lists saved as values in the input dictionary
	and then save a .png file for said chart.

	Parameters
	----------
	freqs_table : dict
		A dictionary with pairs of the type
		columnHeader-listOfAnswersFrequencies.

	Returns
	-------
	None
	'''
	
	for question in freqs_table:
		# Create a new empty 8x5 inches figure
		plt.figure(figsize=(8,5))
		# fig, ax = plt.subplots(figsize=(8, 5), subplot_kw=dict(aspect="equal"))
		# The list of data to be plotted
		chart_data = freqs_table[question]
		# The labels for each wedge
		chart_labels = [i+1 for i in range(len(freqs_table[question]))]
		# Plot the pie chart
		# Wedge percentages will have a single decimal place
		# https://matplotlib.org/users/text_props.html -> for text options
		plt.pie(chart_data, labels=chart_labels, autopct='%0.1f%%', textprops=dict(color="w", weight="bold"))
		# The title is the question saved as a key in the dictionary
		plt.title(question)
		# Adjust the axis
		plt.axis('equal')
		# Insert a legend, which uses the defined labels and is located in\
		# the upper left corner
		plt.legend(chart_labels, loc="upper left")
		# Save the figure as a .png file
		plt.savefig(question+".png", format="png")
		# plt.show()



if __name__ == "__main__":
	# Load the workbook
	wb = openpyxl.load_workbook("sampleExcel.xlsx")
	# Focus on the target worksheet
	ws = wb.get_sheet_by_name("Sheet1")

	# Target the following columns
	target_columns = ["B", "C", "D", "E"]
	# Save the extracted frequencies
	extracted_frequencies = extract_answer_freqs(target_columns)
	# Plot a pie chart for each question and save the chart as a .png
	plot_pie_charts(extracted_frequencies)
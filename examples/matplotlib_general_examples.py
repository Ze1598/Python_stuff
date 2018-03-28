# Matplotlib general practice
from matplotlib import pyplot as plt
import numpy as np

'''First graph'''
# Data for the first graph
past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]
# Start by creating a Figure object, of width 10 and height 8
plt.figure(figsize=(10,8))
# Plot a bar chart, with error bars of capsize 5
plt.bar([x for x in range(len(past_years_averages))], past_years_averages, yerr=error, capsize=5)
# Limit the range of the x-axis to -0.5 to 6.5
plt.xlim(-0.5, 6.5)
# Limit the range of the y-axis to 70 to 95
plt.ylim(70, 95)
# Create an Axis object
ax = plt.subplot()
# Set the x-axis ticks to be the integers in the range of 0 to the length of 'years'
ax.set_xticks(range(len(years)))
# Label the x-axis ticks to be the values in the 'years' list
ax.set_xticklabels(years)
# Title the graph and label the axis
plt.title("Final Exam Averages")
plt.xlabel("Year")
plt.ylabel("Test Average")
# Save the figure to a .png image
plt.savefig("first_exercise.png")
# Show the plotted graph
plt.show()


'''Second graph'''
# Data for the second graph
unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]
# Function to create lists with the x-axis values for the datasets
def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]
# Create a list with the x-axis values for the first dataset's values
school_a_x = create_x(2, 0.8, 1, len(unit_topics))
# Create a list with the x-axis values for the second dataset's values
school_b_x = create_x(2, 1.6, 1, len(unit_topics))
# Create a Figure object of width 10 and heigh 8
fig = plt.figure(figsize=(10,8))
# Create an Axis object
ax = plt.subplot()
# Plot the bar graphs for both datasets
plt.bar(school_a_x, middle_school_a)
plt.bar(school_b_x, middle_school_b)
# Calculate the middle values for each pair of bars
middle_x = [((school_a_x[i]+school_b_x[i])/2) for i in range(len(school_a_x))]
# Set the x-ticks to use the values of the 'middle_x' list
ax.set_xticks(middle_x)
# Set the x-ticks labels to use the values from the 'unit-topics' list
ax.set_xticklabels(unit_topics)
# Create a legend for the graph
ax.legend(['Middle School A', 'Middle School B'])
# Title the graph and label the axis
plt.title('Test Averages on Different Units')
plt.xlabel('Unit')
plt.ylabel('Test Average')
# Save the figure to a .png image
plt.savefig('second_exercise.png')
# Show the finalized graphs
plt.show()


'''Third graph'''
# Data for the third graph
unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]
x = range(5)
# Create the stacks for each grade
c_bottom = np.add(As, Bs)
d_bottom = np.add(c_bottom, Cs)
f_bottom = np.add(d_bottom, Ds)
# Create a Figure object
fig = plt.figure(figsize=(10,8))
# Plot each grade by stacking each new plot on top of the previous one
plt.bar(x, As)
plt.bar(x, Bs, bottom=As)
plt.bar(x, Cs, bottom=c_bottom)
plt.bar(x, Ds, bottom=d_bottom)
plt.bar(x, Fs, bottom=f_bottom)
# Create an Axis object
ax = plt.subplot()
# Set the x-ticks to be the values in the range of 0 to the length of the 'unit_topics' list
ax.set_xticks(range(len(unit_topics)))
# Set the x-ticks to be labeled using the values in 'unit_topics'
ax.set_xticklabels(unit_topics)
# Title the graph and label the axis
plt.title('Grade distribution')
plt.xlabel('Unit')
plt.ylabel('Number of Students')
# Save the graph to a .png image
plt.savefig('third_exercise.png')
# Show the graph
plt.show()


'''Fourth graph'''
# Data for the fourth graph
exam_scores1 = [62.58, 67.63, 81.37, 52.53, 62.98, 72.15, 59.05, 73.85, 97.24, 76.81, 89.34, 74.44, 68.52, 85.13, 90.75, 70.29, 75.62, 85.38, 77.82, 98.31, 79.08, 61.72, 71.33, 80.77, 80.31, 78.16, 61.15, 64.99, 72.67, 78.94]
exam_scores2 = [72.38, 71.28, 79.24, 83.86, 84.42, 79.38, 75.51, 76.63, 81.48,78.81,79.23,74.38,79.27,81.07,75.42,90.35,82.93,86.74,81.33,95.1,86.57,83.66,85.58,81.87,92.14,72.15,91.64,74.21,89.04,76.54,81.9,96.5,80.05,74.77,72.26,73.23,92.6,66.22,70.09,77.2]
# Create a Figure object of width 10 and height 8
fig = plt.figure(figsize=(10,8))
# Plot a normed histogram for exam_scores1, with 12 bins
plt.hist(exam_scores1, bins=12, histtype='step', linewidth=2, normed=True)
# Plot a normed histogram for exam_scores2, with 12 bins
plt.hist(exam_scores2, bins=12, histtype='step', linewidth=2, normed=True)
# Legend the graph
plt.legend(["1st Yr Teaching", "2nd Yr Teaching"])
# Title the graph and label the axis
plt.title('Final Exam Score Distribution')
plt.xlabel('Percentage')
plt.ylabel('Frequency')
# Save the graph to a .png image
plt.savefig('fourth_exercise.png')
# Show the graph
plt.show()


'''Fifth graph'''
# Data for the fifth graph
unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
num_hardest_reported = [1, 3, 10, 15, 1]
# Create a Figure object
plt.figure(figsize=(10,8))
# Plot the graph, using the values in the 'unit_topics' list to label each slice. Show the slice's percentages rounded to the nearest integer
plt.pie(num_hardest_reported, labels=unit_topics, autopct="%d%%")
# Equalize the axis
plt.axis('equal')
# Title the graph
plt.title('Hardest Topics')
# Save the graph to a .png image
plt.savefig('fifth_exercise.png')
# Show the graph
plt.show()


'''Sixth graph'''
# Data for the sixth graph
hours_reported =[3, 2.5, 2.75, 2.5, 2.75, 3.0, 3.5, 3.25, 3.25,  3.5, 3.5, 3.75, 3.75,4, 4.0, 3.75,  4.0, 4.25, 4.25, 4.5, 4.5, 5.0, 5.25, 5, 5.25, 5.5, 5.5, 5.75, 5.25, 4.75]
exam_scores = [52.53, 59.05, 61.15, 61.72, 62.58, 62.98, 64.99, 67.63, 68.52, 70.29, 71.33, 72.15, 72.67, 73.85, 74.44, 75.62, 76.81, 77.82, 78.16, 78.94, 79.08, 80.31, 80.77, 81.37, 85.13, 85.38, 89.34, 90.75, 97.24, 98.31]
# Define the upper and lower bounds for the filled area
hours_lower_bound = [i*0.8 for i in hours_reported]
hours_upper_bound = [i*1.2 for i in hours_reported]
# Make your graph here
# Create a Figure object
fig = plt.figure(figsize=(10,8))
# Plot 'exam_scores' vs. 'hours_reported'
plt.plot(exam_scores, hours_reported, linewidth=2)
# Fill the area between the lower and upper bounds, with an alpha value of 0.2
plt.fill_between(exam_scores, hours_lower_bound, hours_upper_bound, alpha=0.2)
# Title the graph and label the axis
plt.title('Time spent studying vs final exam scores')
plt.xlabel('Score')
plt.ylabel('Hours studying (self-reported)')
# Save the graph to a .png image
plt.savefig('sixth_exercise.png')
# Show the plot
plt.show()

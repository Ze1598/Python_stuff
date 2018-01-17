#exam statistics
#print elements of a list
#print sum of elements of a list
#print average of the elements of a list
#print variance of the elements of a list
#print standard variation of the elements of a list

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    avrg = sum_of_grades / float(len(grades))
    return avrg
    
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    return variance / len(scores)


def grades_std_deviation(variance):
    return variance ** 0.5

variance = grades_variance(grades)

print(print_grades(grades))
print(grades_sum(grades))
print(grades_average(grades))
print(grades_variance(grades))
print(grades_std_deviation(variance))
    
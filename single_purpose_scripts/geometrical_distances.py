'''
This file presents functions to calculate the Euclidean,
Manhatttan and Hamming distances between two lists of length N.
'''

def euclidean_distance(pt1, pt2):
    '''
    Calculate the distance between two points using the
    Euclidean distance.

    Scipy method: scipy.spatial.distance.euclidean

    Formula: square_root((a1-b1)**2 + (a2-b2)**2 + ... + (an-bn)**2)
    '''

    # The distance between the two points
    distance = 0

    # Loop through the lists to calculate the squared differences\
    # between each dimension
    for i in range(len(pt1)):
        distance += (pt1[i] - pt2[i]) ** 2
    
    print(f'Euclidean Distance for {pt1}, {pt2}:\n\t{distance ** 0.5}')
    # Return the square root value of the distance
    return distance ** 0.5

euclidean_distance([1, 2], [4, 0])
euclidean_distance([5, 4, 3], [1, 7, 9])



def manhattan_distance(pt1, pt2):
    '''
    Calculate the distance between two points using the
    Manhattan distance.

    Scipy method: scipy.spatial.distance.cityblock

    Formula: |a1-b1| + |a2-b2| + ... + |an-bn|
    '''

    # The distance between the two points
    distance = 0

    # Loop through the lists to calculate the absolute difference\
    # between each dimension
    for i in range(len(pt1)):
        distance += abs(pt1[i] - pt2[i])
    
    print(f'Manhattan Distance for {pt1}, {pt2}:\n\t{distance}')
    return distance

manhattan_distance([1, 2], [4, 0])
manhattan_distance([5, 4, 3], [1, 7, 9])



def hamming_distance(pt1, pt2):
    '''
    Calculate the distance between two points using the
    Hamming Distance.

    Scipy method: scipy.spatial.distance.hamming
    Note: the Scipy method returns a float between 0
    and 1, as a resulting of dividing the distance
    by the number of dimensions of the lists.

    For each dimension that does not have the same value
    in both points, increment the distance by 1.
    '''

    # The distance between the two points
    distance = 0
    
    # Loop through the lists to check which dimensions\
    # (indexes) don't have the same value for both lists
    for i in range(len(pt1)):
        # If the lists have different values for the current\
        # dimension (index), increment the distance by 1
        if pt1[i] != pt2[i]:
            distance += 1
    
    print(f'Hamming Distance for {pt1}, {pt2}:\n\t{distance}')
    # scipy.spatial.distance.hamming would return\
    # `distance / len(pt1)`
    return distance

hamming_distance([1,2], [1,100])
hamming_distance([5, 4, 9], [1, 7, 9])
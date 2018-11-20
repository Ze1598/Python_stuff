# A se can be created using the built-in function\
# and passing it an iterable
set_ = [1,2,3,4,5]
set_ = set(set_)
set_ = (1,2,3,4,5)
set_ = set(set_)

# Or the set can be created directly
set_ = {1,2,3,4,5}

# To create an empty set, use the built-in function\
# without passing it arguments
set_ = set()

# --------------------------------------------------------------

# Sets don't allow duplicates
set_ = {1,2,1,3,4,4,5} # {1,2,3,4,5}

# --------------------------------------------------------------

# To add a new item to the set, use the .add() method
set_ = {1,2,3,4,5}
set_.add(6) # {1,2,3,4,5,6}

# To add multiple items to the set, use the .update() method\
# by passing it an iterable such as a list
set_ = {1,2,3,4,5}
set_.update([6,7,8,9,10]) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# You can also update a set with multiple objects at the\
# same time, including other sets
set_.update([11,12], {13,14}) 
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}

# --------------------------------------------------------------

# To remove an item from a set use the .remove() method
set_ = {1,2,3,4,5}
set_.remove(5) # {1, 2, 3, 4}

# If you use .discard() instead of .remove(), it has the advantage\
# that this way it won't raise a KeyError exception if you try to\
# remove an item that is not present in the set
set_ = {1,2,3,4,5}
set_.discard(6) # {1,2,3,4,5}

# --------------------------------------------------------------

# To obtain the common values between sets, use the .intersection() method
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}
# s4 has the common values between s1 and s2
s4 = s1.intersection(s2) # {2, 3}
# s5 has the common values between s1, s2 and s3
s5 = s1.intersection(s2, s3) # {3}

# --------------------------------------------------------------

# To obtain the values a given set has and other sets don't, use the\
# .difference() method
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}
# From the values in s1, only 1 is not present in s2
s4 = s1.difference(s2) # {1}
# From the values in s1, only 1 is not present in both s2 and s3
s5 = s1.difference(s2, s3) # {1}
# To obtain all the unique values between sets, use the\
# .symmetric_difference() method
s6 = s1.symmetric_difference(s2) # {1, 4}

# --------------------------------------------------------------

# Sets also support set comprehension
set_ = {i for i in range(1,6)}
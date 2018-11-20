import pickle
import io

'''
The following types can be pickled:
    None, True, and False
    integers, floating point numbers, complex numbers
    strings, bytes, bytearrays
    tuples, lists, sets, and dictionaries containing only picklable objects
    functions defined at the top level of a module
    built-in functions defined at the top level of a module
    classes that are defined at the top level of a module
'''

# A dictionary with random types of supported data for pickle
data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': set([None, True, False])
}


# Create a file to contain the pickled data
# Remember the data is saved as bytes
with open('pickle_example_data.pickle', 'wb') as f:
    # Pickle the "data" dictionary using the highest protocol available
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)


# Now depickle (read) the pickled data from the created file
with open('pickle_example_data.pickle', 'rb') as f:
    # The protocol version used is detected automatically, so we do\
    # not have to specify it
    data = pickle.load(f)
    print(data)
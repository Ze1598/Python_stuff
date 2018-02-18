import os
from contextlib import contextmanager

#The decorator removes the need to create separate __enter__() and __exit__() methods
@contextmanager
def change_dir(directory):
    #Use a try statement in case any exceptions are raised
    try:
        #Save the current directory in a variable
        cwd = os.getcwd()
        #Then change directories to the input directory
        os.chdir(directory)
        yield
    finally:
        #After the with statements have been executed, change back to the original directory
        os.chdir(cwd)

#The first line executes the code inside 'change_dir' up to the yield statement
with change_dir('sample_dir1'):
    #Then this code is executed, and after that, the code inside the finally statement is executed
    print(os.listdir())

#The first line executes the code inside 'change_dir' up to the yield statement
with change_dir('sample_dir2'):
    #Then this code is executed, and after that, the code inside the finally statement is executed
    print(os.listdir())
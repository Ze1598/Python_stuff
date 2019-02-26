# https://realpython.com/documenting-python-code/#commenting-vs-documenting-code
# Docstring conventions are described within PEP 257.

'''
    Multi-lined docstrings are used to further elaborate on the 
object beyond the summary. 
    All multi-lined docstrings have the following parts:

    A one-line summary line;
    A blank line proceeding the summary;
    Any further elaboration for the docstring;
    Another blank line.
'''

# Example:
"""This is the summary line

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""

# Notice the blank line above. Code should continue on this line.

# --------------------------------------------------------------------------------

# Class docstrings

'''
    Class Docstrings are created for the class itself, as 
well as any class methods. The docstrings are placed 
immediately following the class or class method indented 
by one level:
'''
class SimpleClass:
    """Class docstrings go here."""

    def say_hello(self, name: str):
        """Class method docstrings go here."""

        print(f'Hello {name}')

'''
    Class docstrings should contain the following
information:
    A brief summary of its purpose and behavior;
    Any public methods, along with a brief description;
    Any class properties (attributes);
    Anything related to the interface for subclassers, if 
the class is intended to be subclassed.
    
    
    The class constructor parameters should be documented 
within the __init__ class method docstring. Individual 
methods should be documented using their individual 
docstrings. Class method docstrings should contain the
following:
    A brief description of what the method is and what it’s
used for;
    Any arguments (both required and optional) that are
passed including keyword arguments;
    Label any arguments that are considered optional or
have a default value;
    Any side effects that occur when executing the method;
    Any exceptions that are raised;
    Any restrictions on when the method can be called;
'''

# Example:

class Animal:
    """
    A class used to represent an Animal

    ...

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

    says_str = "A {name} says {sound}"

    def __init__(self, name, sound, num_legs):
        """
        Parameters
        ----------
        name : str
            The name of the animal
        sound : str
            The sound the animal makes
        num_legs : int, optional
            The number of legs the animal (default is 4)
        """

        self.name = name
        self.sound = sound
        self.num_legs = num_legs

    def says(self, sound=None):
        """Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used.

        Parameters
        ----------
        sound : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """

        if self.sound is None and sound is None:
            raise NotImplementedError("Silent Animals are not supported!")

        out_sound = self.sound if sound is None else sound
        print(self.says_str.format(name=self.name, sound=out_sound))


# --------------------------------------------------------------------------------------

# Package docstrings

'''
    Package docstrings should be placed at the top of the package’s 
__init__.py file. This docstring should list the modules and 
sub-packages that are exported by the package.

    Module docstrings are placed at the top of the file even before 
any imports. Module docstrings should include the following:
    A brief description of the module and its purpose;
    A list of any classes, exception, functions, and 
any other objects exported by the module.

    The docstring for a module function should include the 
same items as a class method:
    A brief description of what the function is and what it’s 
used for;
    Any arguments (both required and optional) that are passed 
including keyword arguments;
    Label any arguments that are considered optional;
    Any side effects that occur when executing the function;
    Any exceptions that are raised;
    Any restrictions on when the function can be called;
'''

# --------------------------------------------------------------------------------------

# Script docstrings

'''
    Scripts are considered to be single file executables run 
from the console. Docstrings for scripts are placed at the 
top of the file and should be documented well enough for 
users to be able to have a sufficient understanding of how 
to use the script.

    Any custom or third-party imports should be listed within 
the docstrings to allow users to know which packages may be 
required for running the script.
'''

# Example:

"""Spreadsheet Column Printer

This script allows the user to print to the console all columns in the
spreadsheet. It is assumed that the first row of the spreadsheet is the
location of the columns.

This tool accepts comma separated value files (.csv) as well as excel
(.xls, .xlsx) files.

This script requires that `pandas` be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions:

    * get_spreadsheet_cols - returns the column headers of the file
    * main - the main function of the script
"""

import argparse

import pandas as pd


def get_spreadsheet_cols(file_loc, print_cols=False):
    """Gets and prints the spreadsheet's header columns

    Parameters
    ----------
    file_loc : str
        The file location of the spreadsheet
    print_cols : bool, optional
        A flag used to print the columns to the console (default is
        False)

    Returns
    -------
    list
        a list of strings used that are the header columns
    """

    file_data = pd.read_excel(file_loc)
    col_headers = list(file_data.columns.values)

    if print_cols:
        print("\n".join(col_headers))

    return col_headers


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'intput_file',
        type=str,
        help="The spreadsheet file to pring the columns of"
    )
    args = parser.parse_args()
    get_spreadsheet_cols(args.input_file, print_cols=True)


if __name__ == "__main__":
    main()
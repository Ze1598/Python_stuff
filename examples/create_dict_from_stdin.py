'''The first line contains an integer, n, denoting the number of entries in the phone book.
Each of the n subsequent lines describes an entry in the form of 2 space-separated values on
a single line. The first value is the contact's name, and the second value is an 8-digit phone number.'''

from sys import stdin
#Dictionary to hold the contact-phone_number pairs
contacts = {}
#Read the first line, which is the number of pairs to be added to the dictionary
n = int(stdin.readline().strip())

#Read n-1 lines of input, that is, we read from the second line up to the nth line\
#And create the read contact-phone_number pair in the dictionary
for i in range(1, n+1):
    contact = stdin.readline().split()
    contacts[contact[0]] = contact[1]

#Now simply read the rest of the lines and test if they are present in the dicionary or not
query = stdin.readline().strip()
#Only run the loop while reading a line does not return an empty string (end of the input)
while query:
    if query in contacts:
        print('{}={}'.format(query, contacts[query]))
    else:
        print('Not found')
    query = stdin.readline().strip()
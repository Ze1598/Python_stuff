import re
import re_module_sampledata
#File with a single string full of data
#It contains the name, phone number, adress and e-mail of a lot of people
#Example:
'''Dave Martin
615-555-7164
173 Main St., Springfield RI 55924
davemartin@bogusemail.com'''

sample_data = re_module_sampledata.sample_data
#We could use the re.compile() method if we wanted to use our RE more than once,\
#but since that's not the case, we'll feed the RE direcly to the find method (.finditer())
#To simply obtain a list with all the results we could have used .findall() instead, but\
#the purpose of using .finditer() is so that we can also put the .start() and .end()\
#methods to use (the start and end indexes for each match)

#What we'll do is save each type of information from 'sample_data' to a different list: a list for\
#names, one for phone numbers, one for adresses and one for emails

names = []
#NEWLINE \ (upperletter \ 1+_letter_digit) \ SPACE \ (1+_letter_digit)
name_re = re.finditer(r'\n([A-Z]\w+)\s(\w+)', sample_data)
for match in name_re:
    #Don't append the newline characters
    names.append(sample_data[match.start():match.end()][1:])
print(names, '\n')

phones = []
#(3_digits) \ dash \ (3_digits) \ dash \ (4_digits)
phone_re = re.finditer(r'(\d{3})-(\d{3})-(\d{4})', sample_data)
for match in phone_re:
    phones.append(sample_data[match.start():match.end()])
print(phones,'\n')

adresses = []
#(3_digits) \ SPACE \ (1+_letter_digit \ SPACE \ 1+_letter_digit \ .,) \ SPACE \ ((azAZ-' OR Braavos) \ SPACE){repeat this group 1to3 times} \ SPACE
adress_re = re.finditer(r'''(\d{3})\s(\w+\s\w+\.,)\s([a-zA-z-'|Braavos‎]+\s){1,3}\d+''', sample_data)
for match in adress_re:
    adresses.append(sample_data[match.start():match.end()])
print(adresses, '\n')

emails = []
#(1+_digit_letter) \ at symbol \ (1+_digit_letter) \ period \ (1+_digit_letter) 
email_re = re.finditer(r'(\w+)@(\w+)\.(\w+)', sample_data)
for match in email_re:
    emails.append(sample_data[match.start():match.end()])
print(emails, '\n')

#Each list has 100 items
print(len(names), len(phones), len(adresses), len(emails))
# https://github.com/abenassi/Google-Search-API
from google import google

#Query to be made on google is used as a parameter as a string, along with the number of pages to be retrieved
search_ = google.search("reddit",1)
# print(search_, '\n')
# for i in search_:
#     print(i, '\n')

#Print the first item from the list of results
#Print the item itself, its type, and some properties: name, description and link
print('{}\n{}\n{}\n{}\n{}'.format(search_[0],type(search_[0]), search_[0].name, search_[0].description, search_[0].link))
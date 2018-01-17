#Basic tutorial for Beautiful Soup to deal with html source code

#Import the necessary modules
from bs4 import BeautifulSoup

#Open the source file containing html
with open('simple_bs4tutorial.html') as html_file:
    #Then create a BeautifulSoup object with the file, parsing it using lxml
    soup = BeautifulSoup(html_file, 'lxml')

#Indents the html code as it is in the source
print(soup.prettify(),'\n')

#Print the first instance of tags from the source file
print(soup.title)
print(soup.title.text,'\n') #just the text from this tag
print(soup.div)
print(soup.div.text) #just the text from this tag

#Find a specific instance of a tag
article = soup.find('div', class_='article')
print(article)
#Then access specific contents from that tag
headline = article.h2.a.text
print(headline)
summary = article.p.text
print(summary, '\n')


#Find all instances of a tag
for article in soup.find_all('div', class_= 'article'):
    #Then get the text of 'article'\s <a> tag
    headline = article.h2.a.text
    #Then get the text of 'article'\s <p> tag
    summary = article.p.text
    print(headline)
    print(summary,'\n')
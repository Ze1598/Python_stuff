#encrypts input


def representsint(s): #http://stackoverflow.com/questions/1265665/python-check-if-a-string-represents-an-int-without-using-try-except
    try: 
        int(s)
        return True
    except ValueError:
        return False


numbers = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26'] #list with numbers
letters = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #list with letters
symbols1 =['\\','|','!','"','@','#','£','$','§','%','€','&','/','{','(','[',')',']','=','}','?','\'','«','»','<','>','+','*','¨','`','´','º','ª','~','^',',',';','.',':','-','_']
symbols2 = symbols1[::-1]
zipp = list(zip(numbers, letters)) #zipped tupple of all the lists with items to be used for the encryption
# print('---', zipp) #debug
# print('---',symbols1)
# print(symbols2)
# print(len(symbols1))

user_input = input('Write the message to be encrypted:')
output = '' #string to be used as input
everything = [] #final list that will contain all the possible items that can be used for the encryption

for item1 in zipp:
    for item2 in item1:
        everything.append(item2)
# print('---', everything) #debug
#example ['1', 'a', '2', 'b', '3', 'c']

#encryption
for char in user_input: #iterate over the input string
    if char == ' ': #if char is just a space ' '
        output += ' '
   
    else: #if char is not a space ' '
        
        #if char is a number    
        if representsint(char) == True: #if char can be turned into an integer
            index = everything.index(char) #get the index of that char in the everything list
            output += everything[index + 1] #then add 1 to that index to get the corresponding letter
            output += ' '
        
        #if char is a letter
        elif representsint(char) == False and char in letters: #if char can't be turned into an integer
            index = everything.index(char) #get the index of that char in the everything list
            output += everything[index-1] #then subtract 1 to that index to get the corresponding number
            output += ' '
        
        #if char is a symbol
        elif char in symbols1:
            index = symbols1.index(char)
            output += symbols2[index]
            output += ' '
            
print('Here is your encrypted message:', output) #output the encryption

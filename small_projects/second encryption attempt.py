string = input('Insert string:')
encrypted = '' #will hold the encrypted result
decrypted = ''

encrypted += string[1::2] #get the odd-index characters
encrypted += string[::2] #get the even-index characters

# print('--1', len(string))
# prsint('--2', len(encrypted))

print(encrypted)

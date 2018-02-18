#Function to turn on the bit number 'n' (counting from the right) of 'number'

def flip_bit(number, n):
    #Create a binary number (the "mask") that only has one bit turned on: the one at the\
    #wanted position
    mask = (0b1 << (n-1))
    #Use XOR to turn on that bit in the input number; then save it to a new variable
    result = number ^ mask
    return bin(result)
    
print(flip_bit(0b10, 4)) #0b1010
print(flip_bit(0b1010, 3)) #0b1110
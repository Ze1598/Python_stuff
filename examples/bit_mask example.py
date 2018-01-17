def flip_bit(number, n):
    mask = (0b0 << (n-1))
    result = number ^ mask
    return bin(result)
    
print(flip_bit(0b10, 4))
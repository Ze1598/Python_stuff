#practice

#is x an even number

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

#is x an integer

def is_int(x):
    if (x-round(x)) != 0:
        return False
    else:
        return True

#sum digits of an integer x

def digit_sum(n):
    result = 0
    for char in str(n):
        result += int(char)
    return result


#factorial(x)

def factorial(x):
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)

#is x a prime number

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2,x):
            if x % n == 0:
                return False
        return True

#reverse word -> drow

def reverse(text):
    y=""
    for i in text:
        y=i+y
    return y

#remove vowels from a word

def anti_vowel(text):
    result = ''
    for char in text:
        if char not in "aeiouAEIOU":
            result += char
    return result

#simple scrable

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
    points = 0
    for char in word.lower():
        points += score[char]
    return points

#censor a word in a text

def censor(text, word):
    split_text = text.split() 
    for n in split_text: 
        if n == word:
            wposition = split_text.index(word)
            n = "*" * len(n)
            split_text[wposition] = n
            joined_text = " ".join(split_text)
    return joined_text

#count as many times a specific item occurs in input by user

def count(sequence,item):
    found = 0
    for x in sequence:
        if x == item:
            found += 1
    return found

#remove odd numbers from a list of numbers

def purify(x):
    result = []
    for item in x:
        if item % 2 == 0:
            result.append(item)
    return result

#product of the elements of a list of numbers

def product(x):
    total = 1
    for element in x:
        total *= element
    return total

#remove duplicates from a list

def remove_duplicates(x):
    final_list = []
    for item in x:
        if item not in final_list:
            final_list.append(item)
    return final_list

#median of a list of numbers

def median(x):
    result = 0
    x = sorted(x)
    for item in x:
        if len(x) % 2 == 0:
            result = (x[len(x)/2] + x[(len(x)/2)-1]) / 2.0
        else:
            result = x[len(x)/2]
    return result
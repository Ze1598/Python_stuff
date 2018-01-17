#This script rotates the input string by starting from the last character in the string, and putting it in the beginning of a new empty string. 
#It picks one character at a time, starting at the last character of the initial string and finishing by picking the first character of said the initial string.
#Example using "abcde" as input: "e" => "de" => "cde" => "bcde" => "abcde"

def rotate_string(string):
    #Counter to keep the loop running, and used at the same time to access each letter of the input
    counter = 0
    #Final string to be returned
    new_string = ''
    #Main code of the script to execute the intended task
    #Runs while the 'counter' variable is smaller than the length of the input string
    while counter < len(string):
        #To pick a letter, reverse the string and then using the value of 'counter', pick a character, starting, in effect, from the last character of the string
        letter = string[::-1][counter]
        # print('letter =>', letter)
        new_string = letter + new_string
        # print('new_string =>', new_string)
        #Before finishing the loop increment 'counter' by 1
        counter += 1
    return new_string

print('rotate_string(\'w3resource\') =>', rotate_string('w3resource'))
print('rotate_string(\'A3$9,8+\') =>', rotate_string('A3$9,8+'))
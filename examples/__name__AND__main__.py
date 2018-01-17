def plusOne(x):
    return x+1

#No matter if the file is being executed or imported the code up to the conditional statement below will be executed
#However, if the file is being imported by another file then the code inside the conditional statement won't be executed
#If you are simply running the file itself, then even the code inside the conditional statement will run

#tl;dr the code below a 'if __name__ == '__main__'' will only be executed if the file itself is being run
if __name__ == '__main__':
    print(plusOne(1))
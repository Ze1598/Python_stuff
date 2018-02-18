import os, time

print('Clearing screen in two seconds!')
#Sleep for two seconds so the previous print isn't cleared immediately
time.sleep(2)
#Then clear the screen in the command line using the cls command
os.system('cls')
#After clearing, print a new statement
print('I\'m back.')
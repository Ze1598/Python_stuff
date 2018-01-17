f = open("text.txt", "w") 
f.write("Hello World!" + "\n") 
f.write("Hello World!!" + "\n") 
f.write("Hello World!!!" + "\n") 
f.close() 

my_file = open("text.txt", "r") 

print(my_file.readline()) 
print(my_file.readline()) 
print(my_file.readline()) 

my_file.close()
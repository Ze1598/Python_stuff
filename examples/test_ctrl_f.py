#Look for a specific string in a file
with open("test_ctrl_f_sourcefile.txt", 'r') as f:
    #Each element in this list corresponds to a line in the file
    file_lines = list(f)
    print(file_lines)
    #String to look for in each line
    look_for = 'python'
    #Counter to keep of track of what line is being read; starts on line 1
    line_count = 1
    #List to keep track of what lines contained an instance of 'look_for'
    look_forInstances = []
    for line in file_lines:
        #If 'look_for' is in 'line', count it as one instance
        if look_for in line:
            print(f'Found an instance of "{look_for}" on line {line_count}.')
            #Append the number of the line to the 'line_count' to know on which lines there was an instance of it
            look_forInstances.append(line_count)
        line_count += 1
    else:
        #Final print statement with the total of instances and on what lines there was an instance
        print(f'\nFound {len(look_forInstances)} instances of "{look_for}" on lines {look_forInstances}.')
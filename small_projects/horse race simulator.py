#This program creates a simulation of a horse race. This is done via a While loop that is executed until at least 1 horse has crossed the finish line. 
#If only 1 horse crossed the finish line then that horse is the winner; else if multiple horses cross the finish line in the same instance of the loops, the horse that was closest to the finish line in the previous instance of the loop then that horse is the winner
#In this case each horse runs a random ammount between 70 and 150, with the full lenght of the race being 1000; these values can be safely modified with no worries of causing bugs; and in the future it is quite simple to modify each horse to have a different range of possible movement in each loop instance
#The program was created with having 6 horses participatin, though this number could be modified easily
#This program was quite limited to the fact of it not running in real time, so problems like "if multiple horses just crossed the finish line which one wins?" appeared, and I tried to come up with best solution (with the help of a colleague)

from random import randint
# from sys import exit

x = 70 #minimum value of movement of a horse in a loop instance; this value can be changed anytime with no worries of creating bugs
y = 150 #maximum value of movement of a horse in a loop instance; this value can be changed anytime with no worries of creating bugs
race_length = 1000 #length of the race; this value can be changed anytime with no worries of creating bugs
finish = False #False while no horses cross the finish line
raced_values = [] #holds how much each horse moved in the current loop instance; this is resetted at the end of each instance
num_horses = 6
raced_previous_values = [0,0,0,0,0,0] #the total length each horse ran 
winner_indices = [] #indices of the multiple horses that crossed the finish line
min_diff = 10 #just a variable to hold the indice of the winner horse in case multiple horses cross the finish line in the same instance of the loop (the winner with the shortest difference between its previous position and its current position is declared the winner)
diff_list = [] #list to hold all the differences between last and second-last positions of each horse (each of the multiple that had cross the finish in line in the same instance of the loop)

while finish == False:
    #The logic is the same for the 6 horses in the race:
    #Randomize the how much Horse N will move in this instance of the loop
    #Then to the length ran by the 1st horse, in this case, add the value it ran in this instance of the loop
    #The list raced_values which contains how much each horse ran in the current instance of the loop is resetted at the end of each instance
    raced_values.append(randint(x,y))
    raced_previous_values[0] += raced_values[len(raced_values)-1]
    
    raced_values.append(randint(x,y))
    raced_previous_values[1] += raced_values[len(raced_values)-1]
    
    raced_values.append(randint(x,y))
    raced_previous_values[2] += raced_values[len(raced_values)-1]
    
    raced_values.append(randint(x,y))
    raced_previous_values[3] += raced_values[len(raced_values)-1]
    
    raced_values.append(randint(x,y))
    raced_previous_values[4] += raced_values[len(raced_values)-1]
    
    raced_values.append(randint(x,y))
    raced_previous_values[5] += raced_values[len(raced_values)-1]
    
    #if at least a horse crossed the finish line
    if max(raced_previous_values) >= race_length:
        # print('Values for this loop:', raced_values)
        # print('Ran length:', raced_previous_values)
        over_finish_count = 0 #this counter variable counts how many horses crossed the finish line; only applied to the horses that crossed the finish line in the current instance of the loop
        
        #loop to determine how many horses crossed the finish line
        for value in raced_previous_values:
            if value > race_length:
                over_finish_count += 1
        
        #if multiple horses crossed the finish line in the same instance of the loop, then add the pair 'horse index'-'total length ran by horse' of each of those horses to the list winner_indices; so the ones that didn't cross the line are ignored
        if over_finish_count > 1:
            for i in raced_previous_values:
                if i > race_length:
                    winner_indices.append((i, raced_previous_values.index(i)))
            # print('Indices:', winner_indices)
            
            #loop through the pairs of winner_indices to see which horse has the shortest Difference 
            #the Difference is the difference between the horses total ran length and how much it ran in this instance of the loop; this way we can see which horse was closest to the finish line before any horse crossing it, then that horse is declared the winner
            for i in winner_indices:
                # print('i[1]:',i[1])
                diff = raced_previous_values[i[1]] - raced_values[i[1]]
                # print('raced_previous_values[i[1]]:',raced_previous_values[i[1]], 'raced_values[i[1]]:',raced_values[i[1]], 'diff:',diff)
                if len(diff_list) == 0:
                    min_diff = i[1]
                elif diff < min(diff_list):
                    # print('Got here')
                    min_diff = i[1]
                    # print('Min diff:',min_diff)
                diff_list.append(diff)
            # print('Min diff:',min_diff)
            # exit(0) #debug
            print('The winner is Horse', min_diff + 1) #final output
            finish = True #this terminates the loop normally

        else:
            winner_index = raced_previous_values.index(max(raced_previous_values))
            print('The winner is Horse', winner_index + 1) #final output
            finish = True #this terminates the loop normally
           
            
    else:
        # print('Keep going')
        raced_values = [] #reset the raced_values list which holds how much each horse moved in this loop instance
        # print(raced_previous_values)
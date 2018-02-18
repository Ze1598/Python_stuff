class Node:
    '''Class to create each Node object'''
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    '''Class to create linked lists with methods to insert and output them'''
    def display(self,cargo):
        '''Outputs each node in the linked list'''
        current = cargo
        while current:
            print(current.data,end=' ')
            current = current.next
    def insert(self,cargo,data): 
        '''Inserts nodes in the linked list'''
        #If the present cargo is None then assign it to be a new Node
        if cargo is None:
            cargo = Node(data)
        #If cargo is not None (that is, it is already refering to a Node) then
        else:
            curr = cargo
            #Loop through the linked list to reach the list's tail
            while curr.next:
                curr = curr.next
            #Then we can assign the next node in the list to point to a newly created Node
            curr.next = Node(data)
        return cargo

#Receive a first integer that denotes how many nodes will be inserted
mylist= Solution()
T=int(input())
#Initialize the 'cargo' as None; 'cargo' is an item of data contained in the node
cargo=None
#Create a loop to receive 'T' nodes as input
for i in range(T):
    #'data' is an integer
    data=int(input())
    #Create the node for the linked list
    cargo=mylist.insert(cargo,data)    
#Output the linked list
mylist.display(cargo)
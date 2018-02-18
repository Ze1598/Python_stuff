
class Node:
    '''Creates a node for the tree, with a left and right children.

    Attributes:
        right_child (int): The right child of the node; bigger than the node.
        left_child (int): The left child of the node; smaller than the node.
        val (int): The value of the node
    '''
    
    def __init__(self, val):
        '''The class constructor.

        Args:
            val (int): The value of the node to be created.
        '''

        self.val = val
        self.left_child = None
        self.right_child = None
    
    def get_child(self):
        '''Gets a list with the node's child(ren).
        
        Args:
            None.
        
        Returns:
            children (list): A list containing the node's child(ren).
        '''

        children = []
        if self.left_child != None:
            children.append(self.left_child)
        if self.right_child != None:
            children.append(self.right_child)
        
        return children

class BinarySearchTree:
    '''Creates a Binary Search Tree.

    Attributes:
        root (int): The root of the Tree.
    '''
    def __init__(self):
        '''The class constructor. Sets the Tree's root to None.

        Args:
            None
        '''

        self.root = None
    
    def insert(self, value):
        '''Inserts a new node in the tree.

        Args:
            value (int): The value of the new node.
        
        Returns:
            None.
        '''

        #If the tree doesn't have a root yet, make this value the tree's root
        if self.root == None:
            self.root = Node(value)
        
        #If the tree already has a root
        else:
            #We looking for a place to insert the new value at the root
            current_node = self.root

            #Run this loop while we can find a node that is higher bigger or smaller than the given value
            #When that node is found, break out of the loop
            while True:
                #If the value is smaller than the current node
                if value < current_node.val:
                    #If the current node doesn't have a left child, make this value the left child
                    if current_node.left_child == None:
                        current_node.left_child = Node(value)
                    #If the current node already has a left child, the current node will now be that left child
                    else:
                        current_node = current_node.left_child
                
                #If the value is bigger than the current node
                elif value > current_node.val:
                    #If the current node doesn't have a right child, make this value the right child
                    if current_node.right_child == None:
                        current_node.right_child = Node(value)
                    #If the current node already has a right child, the current node will now be that right child
                    else:
                        current_node = current_node.right_child

                #We can't find nodes that are bigger are smaller than the given value                
                else:
                    #Break out of the loop
                    break
    
    def get_tree(self):
        '''Gets a string with all of the tree's nodes.

        Args:
            None.

        Returns:
            (str): A string containing all the values in the tree.
        '''

        #The root is located in level 0 (height = 0)
        self.root.level = 0
        #A list with nodes we still haven't searched
        nodes_to_search = [self.root]
        #A list to contains the values found in the tree
        tree_contents = []
        #The level we are currently searching at; we start at the root
        current_level = self.root.level

        #Run the loop while there's nodes to search (len(nodes_to_search) > 0)
        while nodes_to_search:
            #The current node will always be the first node contained in the nodes_to_search list
            current_node = nodes_to_search.pop(0)

            #If the level of the current node is bigger than the current level, increment current_level by 1
            if current_node.level > current_level:
                current_level += 1
                #Also append a newline character to the tree for easier output formatting at the end
                tree_contents.append("\n")

            #Add the current node's value to the tree (the space is added to facilitate output)
            tree_contents.append(str(current_node.val) + " ")

            #If the current node has a left child, that child's level will be the current level + 1
            #Add that child to the list of nodes to be searched
            if current_node.left_child != None:
                current_node.left_child.level = current_level + 1
                nodes_to_search.append(current_node.left_child)
            
            #If the current node has a right child, that child's level will be the current level + 1
            #Add that child to the list of nodes to be searched
            if current_node.right_child != None:
                current_node.right_child.level = current_level + 1
                nodes_to_search.append(current_node.right_child)

        return "".join(tree_contents)


bst_values = [3, 5, 2, 1, 4, 6, 7]
bst = BinarySearchTree()
for num in bst_values:
    bst.insert(num)
print(bst.get_tree())
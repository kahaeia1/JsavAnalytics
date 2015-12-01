from Trace import Trace
import numpy as np

class TreeTrace(Trace):
    """Handels the traces related to the tree data structure"""

    def __init__(self, file_name):
        self.file_name = file_name      
        super(TreeTrace, self).__init__(self.file_name)

    def __testing__(self):
        print "Hello"

    def testing(self):
        print "Hello"

     #======================================================================================
    def preorder_traversal(self, node):        
        
        if node['v'] == '':
            return
        try:
            self.tree_array[self.state_number][self.node_number] = node['v']
            self.node_number += 1
            if node['left']['v']:
                self.preorder_traversal(node['left'])
            if node['right']['v']:
                self.preorder_traversal(node['right'])
        except IndexError as e:
            print '[Exception] in preorder traversal:\n' + e.message   

    #======================================================================================
    def inorder_traversal(self, node):
        
        if node['v'] == '':
            return

        try:            
            if node['left']['v']:
                self.inorder_traversal(node['left'])
            #print str(node['v'])
            self.tree_array[self.state_number][self.node_number] = node['v']
            self.node_number += 1
            if node['right']['v']:
                self.inorder_traversal(node['right'])  
        except IndexError as e:
            print '[Exception] in inorder traversal:\n' + e.message   
    
    def postorder_traversal(self, node):
        if node['v'] == '':
            return

        try:
            if node['left']['v']:
                self.postorder_traversal(node['left'])
            if node['right']['v']:
                self.postorder_traversal(node['right'])
            self.tree_array[self.state_number][self.node_number] = node['v']
            self.node_number += 1
            #print str(node['v'])
        except IndexError as e:
            print '[Exception] in preorder traversal:\n' + e.message   

    def run_tree_traversal(self, traversal_type):
        self.state_number = 0
        self.node_number = 0
        self.tree_array = np.zeros((len(self.states['answer']), len(self.states['answer']) - 2)) # -2 is because the first state doesn't have any node and the last state is repeated

        for state in self.states['answer']:
            if traversal_type == 'preorder':
                self.preorder_traversal(state)
            elif traversal_type == 'postorder':
                self.postorder_traversal(state)
            elif traversal_type == 'inorder':
                self.inorder_traversal(state)            
            self.state_number += 1
            self.node_number = 0
            #print '---'
        return self.tree_array

    def run_inorder_traversal(self):
        for state in self.states['answer']:
            self.inorder_traversal(state)
            print '---'

    def run_postorder_traversal(self):
        for state in self.states['answer']:
            self.postorder_traversal(state)
            #print '---'



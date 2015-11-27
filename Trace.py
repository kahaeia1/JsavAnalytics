import sys
from State import State
from pprint import pprint
import numpy as np

class Trace(object):
    """This class handles traces that has been collected from the students"""

    def __init__(self, file_name):
        global states        
        states = State().getStates(file_name)

    def print_states(self):
        #print 'in print states'  
        i = 0      
        for state in states['answer']:
            i += 1
            print 'state' + str(i) + ': ' + str(state) + '\n------------------\n'

    #======================================================================================
    def preorder_traversal(self, node):        
        
        if node['v'] == '':
            return
        try:
            tree_array[self.state_number][self.node_number] = node['v']
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
            tree_array[self.state_number][self.node_number] = node['v']
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
            tree_array[self.state_number][self.node_number] = node['v']
            self.node_number += 1
            #print str(node['v'])
        except IndexError as e:
            print '[Exception] in preorder traversal:\n' + e.message   

    def run_tree_traversal(self, traversal_type):
        self.state_number = 0
        self.node_number = 0
        global tree_array
        tree_array = np.zeros((len(states['answer']), len(states['answer']) - 2)) # -2 is because the first state doesn't have any node and the last state is repeated

        for state in states['answer']:
            if traversal_type == 'preorder':
                self.preorder_traversal(state)
            elif traversal_type == 'postorder':
                self.postorder_traversal(state)
            elif traversal_type == 'inorder':
                self.inorder_traversal(state)            
            self.state_number += 1
            self.node_number = 0
            #print '---'
        return tree_array

    def run_inorder_traversal(self):
        for state in states['answer']:
            self.inorder_traversal(state)
            print '---'

    def run_postorder_traversal(self):
        for state in states['answer']:
            self.postorder_traversal(state)
            #print '---'

    def print_array(self, printable_arr, traversal_type):
        print '\n'

        if traversal_type == 'preorder':
            array_description = 'Preorder traversal of all states: \n'
        elif traversal_type == 'inorder':            
            array_description = 'Inorder traversal of all states: \n'
        elif traversal_type == 'postorder':
            array_description = 'Postorder traversal of all states: \n'
        print array_description
        print printable_arr
        print '\n'



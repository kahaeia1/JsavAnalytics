import sys
from State import State
from pprint import pprint

class Trace(object):
    """Handles traces that has been collected from the students"""

    def __init__(self, file_name):
        self.file_name = file_name        
        self.states = State().getStates(self.file_name)

    def print_states(self):
        #print 'in print states'  
        i = 0      
        for state in self.states['answer']:
            i += 1
            print 'state' + str(i) + ': ' + str(state) + '\n------------------\n'

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



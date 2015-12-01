import unittest
from Trace import Trace
from State import State
import numpy as np

class TestTraces(unittest.TestCase):
    file_name = 'TraceSample.json'
    global trace
    global states
    trace = Trace(file_name)
    states = State().getStates(file_name)

    def test_preorder_traversal_expected_result(self):
        
        test_tree_arr = trace.run_tree_traversal('preorder')
        np.testing.assert_array_equal(test_tree_arr[[len(states['answer'])-1][0]], [19, 36, 25, 34, 80, 53, 48, 60, 96, 81])      

    def test_inorder_traversal_expected_result(self):
        
        test_tree_arr = trace.run_tree_traversal('inorder')
        np.testing.assert_array_equal(test_tree_arr[[len(states['answer'])-1][0]], [19, 25, 34, 36, 48, 53, 60, 80, 81, 96])      

    def test_postorder_traversal_expected_result(self):
        
        test_tree_arr = trace.run_tree_traversal('postorder')
        np.testing.assert_array_equal(test_tree_arr[[len(states['answer'])-1][0]], [34, 25, 48, 60, 53, 81, 96, 80, 36, 19])     

if __name__ == '__main__':
    unittest.main()
  
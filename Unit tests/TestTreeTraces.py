﻿import unittest
from TreeTrace import TreeTrace
from State import State
import numpy as np

class TestTreeTraces(unittest.TestCase):
    file_name = 'JsonSampleFiles/TreeTraceSample.json'
    global tree_trace
    tree_trace = TreeTrace(file_name)

    def test_preorder_traversal_expected_result(self):

        test_tree_arr = tree_trace.run_tree_traversal('preorder')
        np.testing.assert_array_equal(test_tree_arr[[len(tree_trace.states['answer'])-1][0]], [19, 36, 25, 34, 80, 53, 48, 60, 96, 81])      

    def test_inorder_traversal_expected_result(self):
        
        test_tree_arr = tree_trace.run_tree_traversal('inorder')
        np.testing.assert_array_equal(test_tree_arr[[len(tree_trace.states['answer'])-1][0]], [19, 25, 34, 36, 48, 53, 60, 80, 81, 96])      

    def test_postorder_traversal_expected_result(self):
        
        test_tree_arr = tree_trace.run_tree_traversal('postorder')
        np.testing.assert_array_equal(test_tree_arr[[len(tree_trace.states['answer'])-1][0]], [34, 25, 48, 60, 53, 81, 96, 80, 36, 19])     

if __name__ == '__main__':
    unittest.main()
  
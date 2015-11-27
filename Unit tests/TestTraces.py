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

    #def test_A(self):
    #    self.fail("Not implemented")

    def test_preorder_traversal_expected_result(self):

        test_tree_array = trace.run_tree_traversal('preorder')
        np.assert_array_equal(test_tree_array[[len(states['answer'])-1][0]], [19, 36, 25, 34, 80, 53, 48, 60, 96, 81])       # [19, 36, 25, 34, 80, 53, 48, 60, 96, 81]

    def test_preorder_traversal_unexpeted_result(self):

        test_tree_array = trace.run_tree_traversal('preorder')
        np.allclose(test_tree_array[[len(states['answer'])-1][0] ], [0, 36, 25, 34, 80, 53, 48, 60, 96, 81])       # [19, 36, 25, 34, 80, 53, 48, 60, 96, 81]

if __name__ == '__main__':
    unittest.main()

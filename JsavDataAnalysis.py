from State import State
from Trace import Trace

file_name = 'TraceSample.json'
state = State()
trace = Trace(file_name)

tree_array = trace.run_tree_traversal('preorder')
trace.print_array(tree_array, 'preorder')

state.plot_last_trace(tree_array)

from State import State
from TreeTrace import TreeTrace

file_name = 'JsonSampleFiles/TreeTraceSample.json'
state = State()
treeTrace = TreeTrace(file_name)

tree_array = treeTrace.run_tree_traversal('postorder')
treeTrace.print_array(tree_array, 'postorder')

#state.plot_last_trace(tree_array)

# A demo for using and visualing Graphs in python
# It depends on `graphviz` package for doing so.

from graphviz import Digraph


dot: Digraph = Digraph(name='test', comment='Graph Visualization')
dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the wise')
dot.node('L', 'Sir Lancelot the brave')

dot.edges(['AB', 'BL'])
dot.edge('A', 'L', label='AL')

# View the output
dot.view()

# Saves this in dot format
# dot.save(filename='/tmp/test.gv')

# Saves in the specific format
# dot.render(filename='/tmp/test', format='png')

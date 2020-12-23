The primary purpose of this program is to determine the local Whitehead graphs of train track maps. The program is built to accept train track maps as compositions of folds, and allows for reapplying sequences of folds with permutations on the edge names.



Throughout this program, a switch of case indicates a reversal of orientation.
Example: 'A' is the edge 'a' traversed in reverse.

MAKE EDGE MAPS

Given a sequence of edge maps on a graph, format each edge map as (for example),
['a', 'ae'] to indicate that 'a' is mapped to 'ae'.
Put all such edge maps into a list, where the first element in the list is the first element to be done. Henceforth, call this list "maps."

Let edge_names be the list of all edges in the graph in lower case. For example,
edge_names = ['a','b','c','d','e']

In the event that the same sequence of edge maps must be applied again to the graph, but for a permutation on the edge names, let "perm" indicate permutation, where perm should be formatted as follows:
[ ['a','b','c'], ['c','a','b'] ] indicates that 'a' maps to 'c',
                                                'b' maps to 'a', and
                                                'c' maps to 'b'.
This will also (implicitly) additionally indicate that
                                                'A' maps to 'C',
                                                'B' maps to 'A', and
                                                'C' maps to 'B'.

Specify in "order" how many times the permutation should be applied and the graph maps performed.
	** order is an optional parameter. By default, order is the order of the permutation.

Then, to determine edge maps, run
edge_map.get_loop_edge_map(edge_names, maps, perm, order = None)

Do note: this edge map will be output as a dictionary, not a list.


MAKE DIRECTION MAPS

Given an edge map (edge_maps), as a dictionary, get direction maps by running
direction_map.dir_from_edge_maps(edge_maps)

Given edge_names (as a list), map, perm, and optionally order, as specified in section "Make Edge Maps," get direction maps by running
direction_map.get_loop_dir_map(edge_names, maps, perm, order = None)


LOCAL WHITEHEAD GRAPHS

Given edge maps (edge_maps) as a dictionary, get the local Whitehead graph by running
local_whitehead.get_whitehead(edge_maps)


EDGE MAPS AND WHITEHEAD GRAPHS TO LATEX

Given an edge map (loop) as a dictionary, output LaTeX code to format it nicely by running
tex.tex_graph_map(loop)

Given a local Whitehead graph (as output by the local_whitehead module), output LaTeX code to format it nicely by running
tex.tex_turns_taken(turns)
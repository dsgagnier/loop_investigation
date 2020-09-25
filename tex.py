def tex_graph_map(loop):
    '''Given a graph map in the form of a dictionary (where the keys are edges and the
    values are images), this function turns the dictionary into text formatted with LaTeX.
    '''
    s = ""
    for key in loop:
        s += "$" + key + "\\mapsto "
        for edge in loop[key]:
            if edge.isupper():
                s += "\\bar{" + edge.lower() + "}"
            else:
                s += edge
        s += "$\n\n"
    return s

if __name__ == "__main__":
    import edge_map as em
    edge_names = ['a','b','c','d','e']
    maps = [['c','cA'],
            ['b','bc'],
            ['c','cb'],
            ['d','Cd']]
    perm = [['a','b','c','d','e'], ['d','e','a','b','C']]
    loop = em.get_loop_edge_map(edge_names, maps, perm, 10)

    map_tex = tex_graph_map(loop)
    print(map_tex)

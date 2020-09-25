def bar_cap(char):
    '''Given a character, if it's a capital letter, this function returns the character in
    lower case formatted with an overline in LaTeX. Otherwise, this function returns the
    character.
    '''
    s = char
    if char.isupper():
        s = "\\bar{" + char.lower() + "}"
    return s

def tex_graph_map(loop):
    '''Given a graph map in the form of a dictionary (where the keys are edges and the
    values are images), this function turns the dictionary into text formatted with LaTeX.
    '''
    s = ""
    for key in loop:
        s += "$" + key + "\\mapsto "
        for edge in loop[key]:
            s += bar_cap(edge)
        s += "$\n\n"
    return s

def tex_turns_taken(turns):
    '''Given a set of turns taken eventually (as a list of 2-element lists), this function
    turns that list into text formatted with LaTeX.
    '''
    s = "\\{"
    for turn in turns:
        s += "\\{" + bar_cap(turn[0]) + "," + bar_cap(turn[1]) + "\\},"
    s = s[:-1] + "\\}"
    return s

if __name__ == "__main__":
    import edge_map as em
    import local_whitehead as wh
    edge_names = ['a','b','c','d','e']
    maps = [['c','cA'],
            ['b','bc'],
            ['c','cb'],
            ['d','Cd']]
    perm = [['a','b','c','d','e'], ['d','e','a','b','C']]
    loop = em.get_loop_edge_map(edge_names, maps, perm, 10)

    map_tex = tex_graph_map(loop)
    print(map_tex)

    edge_names = ['a','b','c','d','e']
    maps = [['c','cA'],
            ['b','bc'],
            ['c','cb'],
            ['d','Cd']]
    perm = [['a','b','c','d','e'], ['d','e','a','b','C']]
    edge_maps = em.get_loop_edge_map(edge_names, maps, perm, 10)
    wh1 = wh.get_whitehead(edge_maps)
    
    wh_tex = tex_turns_taken(wh1)
    print(wh_tex)
    

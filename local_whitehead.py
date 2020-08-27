import direction_map as dm

def turns_from_path(path):
    '''Given a path, this function returns a list of the turns taken by the path. For
    example, "abc" -> [['A','b'],['B','c']]
    '''
    turns = []
    i = 0
    while i < len(path) - 1:
        turn = [path[i].swapcase(), path[i + 1]]
        turn.sort()
        if turn not in turns:
            turns.append(turn)
        i += 1
    return turns

def get_whitehead(edge_maps):
    '''This function returns the local whitehead graph of the map edge_maps.'''
    recent_turns = []
    all_turns = []
    dir_map = dm.dir_from_edge_maps(edge_maps)

    for key in edge_maps:
        turns = turns_from_path(edge_maps[key])
        for turn in turns:
            if turn not in recent_turns:
                recent_turns.append(turn)
    all_turns.extend(recent_turns)

    while recent_turns != []:
        new = dm.dir_map_to_turn_list(dir_map, recent_turns)
        recent_turns = []
        for turn in new:
            if turn not in all_turns:
                all_turns.append(turn)
                if turn not in recent_turns:
                    recent_turns.append(turn)
    return all_turns
        

if __name__ == "__main__":
    import edge_map as em

    # test turns_from_path()
    print(turns_from_path("aaaaaaa"))
    print(turns_from_path("abcabcAbCa"))

    # test get_whitehead()
    edge_names = ['a','b','c','d','e']
    maps = [['c','cA'],
            ['b','bc'],
            ['c','cb'],
            ['d','Cd']]
    perm = [['a','b','c','d','e'], ['d','e','a','b','C']]
    edge_maps = em.get_loop_edge_map(edge_names, maps, perm, 10)
    wh1 = get_whitehead(edge_maps)

    del maps[0]
    maps.append(['a','aD'])
    edge_maps = em.get_loop_edge_map(edge_names, maps, perm, 10)
    wh2 = get_whitehead(edge_maps)

    del maps[0]
    maps.append(['e','ea'])
    edge_maps = em.get_loop_edge_map(edge_names, maps, perm, 10)
    wh3 = get_whitehead(edge_maps)

    del maps[0]
    maps.append(['a','ae'])
    edge_maps = em.get_loop_edge_map(edge_names, maps, perm, 10)
    wh4 = get_whitehead(edge_maps)
    

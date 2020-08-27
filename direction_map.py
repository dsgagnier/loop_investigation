import edge_map as em

def apply_direction_map(edge, image, direction):
    '''Given a direction (a character), this function returns the first character of image
    if direction is the same as edge. This function returns the last character of image with
    its case swapped if the direction is the same as edge.swapcase(). Otherwise, this
    function returns direction.
    '''
    if direction == edge:
        return image[0]
    elif direction == edge.swapcase():
        return image[-1].swapcase()
    else:
        return direction

def dir_from_edge_maps(edge_maps):
    '''Given a dict representing where each edge (key) goes under a map, this function
    returns the corresponding direction map.

    For example, {"a", "def"} -> {"a": "d", "A": "F"}
    '''
    dir_maps = {}
    for key in edge_maps:
        dir_maps[key] = edge_maps[key][0]
        dir_maps[key.swapcase()] = edge_maps[key][-1].swapcase()
    return dir_maps

def get_loop_dir_map(edge_names, maps, perm, order = None):
    '''Given a list of edge names, this function applies edge maps to each of them. Then,
    it applies perm to the maps and applies the maps again. This process is repeated order
    times. The function returns the resulting direction maps.
    '''
    return dir_from_edge_maps(em.get_loop_edge_map(edge_names, maps, perm, order))

def dir_map_to_turn_list(dir_map, turn_list):
    '''Given a direction map (dict) containing all directions (forwards and backwards) and
    a list of turns, this function applies the direction maps to each turn and returns a
    new list of turns.

    Each individual turn will be sorted, but the list of turns will not. Duplicates will
    not be removed.
    '''
    i = 0
    new = []
    while i < len(turn_list):
        to_add = [dir_map[turn_list[i][0]], dir_map[turn_list[i][1]]]
        to_add.sort()
        new.append(to_add)
        i += 1
    return new

if __name__ == "__main__":
    #test apply_direction_map():
    print(apply_direction_map('a','erv','e'))
    print(apply_direction_map('a','erv','a'))
    print(apply_direction_map('a','erv','A'))

    # test get_loop_dir_map and dir_from_edge_maps
    edge_names = ['a','b','c','d','e']
    maps = [['c','cA'],
            ['b','bc'],
            ['c','cb'],
            ['d','Cd']]
    perm = [['a','b','c','d','e'], ['d','e','a','b','C']]
    loop = get_loop_dir_map(edge_names, maps, perm, 10)
    for key in loop:
        print(f"{key} -> {loop[key]}")
    

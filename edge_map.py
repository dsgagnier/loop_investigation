import permutations as p

def reverse(s):
    '''Reverses a string.'''
    return s[::-1]

def apply_edge_map(edge, image, path):
    '''Given a string path, this function replaces all instances of edge (a character) with
    image, and replaces all instaces of edge.swapcase() with image in reverse swapcased.
    '''
    new_path = ""
    other_image = reverse(image).swapcase()
    for char in path:
        if char == edge:
            new_path += image
        elif char == edge.swapcase():
            new_path += other_image
        else:
            new_path += char
    return new_path

def get_loop_edge_map(edge_names, maps, perm, order = None):
    '''Given a list of edge names, this function applies the edge maps in maps to each
    of them. Then, it applies perm to the maps and applies the maps again. This process
    is repeated order times.

    Note, an element of maps is formatted as in the example: ['a','ae'] indicates that 'a'
    is mapped to 'ae'.
    '''
    loop_map = {}
    for edge in edge_names:
        loop_map[edge] = edge

    if order is None:
        order = p.get_order(perm)

    i = 0
    while i < order:
        m = 0
        while m < len(maps):
            for key in loop_map:
                loop_map[key] = apply_edge_map(maps[m][0], maps[m][1], loop_map[key])
            maps[m][0] = p.apply_permutation(perm, maps[m][0])
            maps[m][1] = p.apply_permutation(perm, maps[m][1])
            m += 1
        i += 1
    return loop_map

if __name__ == "__main__":
    # test reverse():
    print(reverse("Hi! Please reverse me."))

    # test apply_edge_map():
    print(apply_edge_map("e", "ae", "aejfjEjeoE"))

    # test get_loop_edge_map
    edge_names = ['a','b','c','d','e']
    maps = [['c','cA'],
            ['b','bc'],
            ['c','cb'],
            ['d','Cd']]
    perm = [['a','b','c','d','e'], ['d','e','a','b','C']]
    loop = get_loop_edge_map(edge_names, maps, perm, 3)
    for key in loop:
        print(f"{key} -> {loop[key]}")

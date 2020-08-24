'''For the purposes of this program, a permutation will be represented by a
list of lists as in the example below:
[ ['a','b','c'], ['c','a','b'] ] indicates that 'a' maps to 'c',
                                                'b' maps to 'a', and
                                                'c' maps to 'b'.
This will also (implicitly) additionally indicate that
                                                'A' maps to 'C',
                                                'B' maps to 'A', and
                                                'C' maps to 'B'.
'''

def apply_permutation(perm, s):
    '''This function applies the permuation perm to the string s. This function will also
    work on a list of characters, but will still return a string.'''
    new_s = ""
    for char in s:
        try:
            ind = perm[0].index(char)
            new_s += perm[1][ind]
        except:
            ind = perm[0].index(char.swapcase())
            new_s += perm[1][ind].swapcase()
    return new_s

def get_order(perm):
    '''Returns the order of the permutation.'''
    return

if __name__ == "__main__":
    # test apply_permutation
    print(apply_permutation([['a','b','c'],['c', 'a', 'b']], "abcc"))
            
            

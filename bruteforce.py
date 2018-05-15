import string
from itertools import permutations
from time import time
from scipy.special import perm

def bruteforce(password, max_nchar=8, possible_char=None, lazy=False):
    """Brute-force string

    Parameters
    ----------
    password : string
        Actual password
    max_nchar : int
        Maximum number of characters in passwords
    possible_char : string
        List of possible characters (e.g. 'abcdefghijklmnop...')

    Return
    ------
    bruteforce_password : string
        Brute-forced password
    """
    if possible_char is None:
        # All digits + upper/lower case ASCII letters + punctuation
        # Same as possible_char = string.printable[:-5]
        possible_char = string.digits + string.ascii_letters + \
                        string.punctuation

    nperm = sum([perm(len(possible_char), l) for l in
                                            range(1, max_nchar+1)])
    print('Max password length: %d' % max_nchar)
    print('Number of possible char: %d' % len(possible_char))
    print('Computing %.1e possible combinations' % nperm)
    
    if lazy:
        return None
      
    for l in range(1, max_nchar+1):
        print("%d char" % l)
        generator = permutations(possible_char, int(l))
        for p in generator:
            if ''.join(p) == password:
                print('Password:', ''.join(p))
                return ''.join(p)

# EXAMPLE
start = time()
bruteforce('PasS1')
end = time()
print('Total time: %.2f seconds' % (end - start))
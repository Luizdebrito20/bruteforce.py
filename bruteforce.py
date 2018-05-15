import string
from itertools import product
from time import time
from scipy.special import perm

def bruteforce(password, max_nchar=8, possible_char=None):
    """Brute-force string

    Parameters
    ----------
    password : string
        Password to-be-found
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
     
    for l in range(1, max_nchar+1):
        print("%d char" % l)
        generator = product(possible_char, int(l))
        for p in generator:
            if ''.join(p) == password:
                print('Password:', ''.join(p))
                return ''.join(p)

# EXAMPLE
start = time()
bruteforce('PasS1')
end = time()
print('Total time: %.2f seconds' % (end - start))
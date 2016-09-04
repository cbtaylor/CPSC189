#Lecture 01
#Solutions - Part 2

#****Data of arbitrary size****

#Try the following in the 'iPython Console' window:
#loi = []
#loi
#loi = [3] + loi
#loi

#loi = [3, 4, 5, -5, 3]
#loi[0]
#loi[4]
#loi[5]       #produces IndexError (last index is 4)

#loi[-1]
#loi[-2]

#Slicing operations (produce a NEW list):

#loi[1:4]
#loi[3:]
#loi[::2]



# List of X is one of:
# - []
# - [X] + List of X
# interp. a list of elements of type X

# Note that the above data definition is so commonly used that we
# use the special notation (listof X) to refer to it.

L0 = []
L1 = [3]
L2 = [5, 6, -3]

#def fn_for_lox(lox):
#    if lox == []:
#        return ...
#    else:
#        return ...lox[0] ...fn_for_lox(lox[1:])



# ****Functions that operate on data of arbitrary size****

# Example: design a function that determines if a list of integers
# contains a particular integer.

def contains(loi, si):
    """
    (listof int), int -> bool

    Determines if loi contains si

    >>> contains([], 4)
    False

    >>> contains([3, 4, 5], 4)
    True

    >>> contains([3, -4, 5], 4)
    False
    """
    #return False                                     #<--- STUB
    #if loi == []:                                    #<--- TEMPLATE
        #return ...
    #else:
        #return ...loi[0] ...contains(loi[1:], si)
    if loi == []:
        return False
    else:
        return loi[0] == si or contains(loi[1:], si)



# EXERCISE: design a function that consumes a list of integers and
# that determines how many of the integers are negative.

def count_neg(loi):
    """
    (listof int) -> int

    Determines how many entries in loi are negative

    >>> count_neg([])
    0

    >>> count_neg([3, 4, 5])
    0

    >>> count_neg([3, -4, 0, -6])
    2
    """
    if loi == []:
        return 0
    else:
        if loi[0] < 0:
            return 1 + count_neg(loi[1:])
        else:
            return count_neg(loi[1:])

#_________________________________________

# Consider the following data definitions:

# Word is str
# interp. a word in an essay

W1 = 'the'
W2 = 'a'
W3 = 'essay'

#fn_for_word(w):
#    ...w


# Example: design a function that consumes a list of Words and that
# produces a list of those words that start with a vowel.

# Hint: add (listof Word) to the data definition above and then draw
# the reference arrows on the data definitions.  You'll see that
# (listof Word) has a reference to Word.  Keep this in mind when
# you generate the template for your function. 

def words_starting_with_vowel(low):
    """
    (listof Word) -> (listof Word)

    Produces a list of words in low that start with a vowel

    >>> words_starting_with_vowel([])
    []

    >>> words_starting_with_vowel(['abcde'])
    ['abcde']

    >>> words_starting_with_vowel(['bcdef'])
    []

    >>> words_starting_with_vowel(['abc', 'def', 'efg', 'fgh'])
    ['abc', 'efg']
    """
#    return []                                           <--- STUB
#
#    if low == []:                                       <--- TEMPLATE
#        return ...
#    else:
#        return ...fn_for_word(low[0]) ...words_starting_with_vowel(low[1:])
#                  ^^^^^^ note the call to this helper - why is it there???

    if low == []:
        return []
    else:
        if starts_with_vowel(low[0]):
            return [low[0]] + words_starting_with_vowel(low[1:])
        else:
            return words_starting_with_vowel(low[1:])


def starts_with_vowel(w):
    """
    Word -> bool

    Determine if w starts with a vowel

    >>> starts_with_vowel('abc')
    True

    >>> starts_with_vowel('efg')
    True

    >>> starts_with_vowel('ijk')
    True

    >>> starts_with_vowel('opq')
    True

    >>> starts_with_vowel('uvw')
    True

    >>> starts_with_vowel('xyz')
    False
    """
    #return False                                        #<--- STUB
    #return ...w                                         #<--- TEMPLATE
    return w[0] == 'a' or w[0] == 'e' or w[0] == 'i' \
           or w[0] == 'o' or w[0] == 'u'

# As was pointed out in class today, an alternate implementation
# for the body of this function is to use Python's 'in' operator

#    return w[0] in "aeiou"
    
# In this context, the in operation produces true if w[0] is found
# in the string "aeiou"

# Make sure tests run when this module is run
if __name__=='__main__':
    import doctest
    EPS = 1.0e-6
    print(doctest.testmod(verbose=False))


# CPSC 189: Lecture 03 Starter File

# From recursion to iteration...
# In today's lecture we investigate how to design functions using loops...

# Consider the following function from Lecture 02:

#def sum_positive(loi0):
#    """
#    (listof int) -> int
#
#    Produces the sum of the positive integers in loi
#
#    >>> sum_positive([])
#    0
#
#    >>> sum_positive([5, -4, 3])
#    8
#    """
#    def sum_positive_acc(loi, acc):
#        """
#        Accumulator: acc is int
#
#        Invariant: acc represents the sum of the positive integers in loi0
#        prior to loi[0]
#
#        sum_positive_acc([5, -4, 3], 0)
#        sum_positive_acc([-4, 3], 5)
#        sum_positive_acc([3], 5)
#        sum_positive_acc([], 8)
#        """
#        if loi == []:
#            return acc
#        else:
#            if loi[0] > 0:
#                return sum_positive_acc(loi[1:], loi[0] + acc)
#            else:
#                return sum_positive_acc(loi[1:], acc)
#
#    return sum_positive_acc(loi0, 0)

# We start by re-designing this function using a loop...

def sum_positive(loi):
    """
    (listof int) -> int

    Produces the sum of loi

    >>> sum_positive([])
    0

    >>> sum_positive([5, -4, 3])
    8
    
    Accumulator: acc is int

    Invariant: acc is the sum of the positive integers processed so far

    Example: sum_positive([5, -4, 3])
    Processed so far       Accumulator
    []                     0
    [5]                    5
    [5, -4]                5
    [5, -4, 3]             8
    """
    acc = 0
    
    for num in loi:
        if num > 0:
            acc += num
            
    return acc


#_____________________________________

# Problem 1: complete the design of the following function using a loop

def average_lon(lon):
    """
    (nelistof Real) -> float

    Determines the average of a non-empty list of numbers

    >>> exp = 2.0
    >>> act = average_lon([2.0])
    >>> abs(exp - act) < EPS * exp
    True

    >>> exp = 3.0
    >>> act = average_lon([2.0, 4.5, 2.5])
    >>> abs(exp - act) < EPS * exp
    True

    >>> exp = 3.5
    >>> act = average_lon([2, 4, 3, 5])
    >>> abs(exp - act) < EPS * exp
    True
    
    Accumulator: sum is float, count is int
    
    Invariant: sum is the sum of elements seen so far
               count is the number of elements seen so far

    Example: processed so far   sum     count
             [2.0, 4.5, 2.5]    0.0     0
             [4.5, 2.5]         2.0     1
             [2.5]              6.5     2
             []                 9.0     3
    
    """
    sum = 0.0
    count = 0
    for num in lon:
        sum += num
        count += 1
    return sum / count



#_____________________________________

# Problem 2: Design a function that consumes a list of string and produces
# a list of the lengths of those strings

def str_lengths(los):
    """
    (listof str) -> (listof int)

    Produces a list of the lengths of a list of strings

    >>> str_lengths([])
    []

    >>> str_lengths([''])
    [0]

    >>> str_lengths(['123'])
    [3]

    >>> str_lengths(['1', '12', '123'])
    [1, 2, 3]

    Accumulator: lolos is (listof int)

    Invariant: lolos is a list of the lengths of the strings in los

    Example: processed so far     lolos
             ['1', '12', '123']   []
             ['12', '123']        [1]
             ['123']              [1, 2]
             []                   [1, 2, 3]
    
    """
#    lolos = []
#    
#    for s in los:
#        lolos = lolos + [len(s)]
#    
#    return lolos

    return [len(s) for s in los]


#_____________________________________

# Problem 3: Design a function that consumes two lists of pressures (same length)
# and a tolerance (a Real) and produces a list of pairs (tuples) of
# pressures whose difference in absolute value is greater than the tolerance.

def pressure_diff(lop1, lop2, tol):
    """
    (listof Real), (listof Real), Real -> (listof (Real, Real))

    >>> pressure_diff([], [], 0.001)
    []

    >>> pressure_diff([0.4], [0.40001], 0.0001)
    []

    >>> pressure_diff([0.4], [0.39998], 0.00001)
    [(0.4, 0.39998)]

    >>> pressure_diff([0.4, 0.5, 0.6, 0.7], [0.395, 0.489, 0.605, 0.711], 0.01)
    [(0.5, 0.489), (0.7, 0.711)]

    Accumulator:  lopet is (listof tuples)
    
    Invariant: lopet is a list of tuples of pressures whose diff exceeeds tolerance
    
    Example: processed so far                 lopet
             [1, 2, 3], [2, 8, 6], 2          []
             [2, 3], [8, 6] 2                 []
             [3], [6] 2                       [(2, 8)]
             [], [] 2                         [(2, 8), (3, 6)]
    
    """
#    lopet = []
    
#    for i in range(len(lop1)):
#        if abs(lop1[i] - lop2[i]) > tol:
#            lopet = lopet + [(lop1[i], lop2[i])]
#    
#    return lopet
    
#    for t in zip(lop1, lop2):
#        if abs(t[0] - t[1]) > tol:
#            lopet = lopet + [t]
#    return lopet

#    return [t for t in zip(lop1, lop2) if abs(t[0] - t[1]) > tol]
    
    return [(p1, p2) for (p1, p2) in zip(lop1, lop2) if abs(p1 - p2) > tol]

#_____________________________________

# Problem 5: Design a function that consumes two non-empty lists of temperatures
# of the same length and that produces true if, for every pair of temperatures,
# the temperature in the first list is greater than the corresponding
# temperature in the second list.  Use a list comprehension so that the body
# of the function consists of a single line of code!

def temperatures_greater(nelot1, nelot2):
    """
    (nelistof Real), (nelistof Real) -> boolean

    >>> temperatures_greater([5], [6])
    False

    >>> temperatures_greater([6.1], [5.3])
    True

    >>> temperatures_greater([4.9, 6.1, 7.0], [4.1, 5.0, 6.4])
    True

    >>> temperatures_greater([5.1, 6.2, 7.0], [6.0, 6.2, 7.8])
    False
    """
#    flag = True
#    
#    for t in zip(nelot1, nelot2):
#        flag = True and t[0] > t[1]
#        
#    return flag
        
#    return not False in [t[0] > t[1] for t in zip(nelot1, nelot2)]
    
    return all([x > y for (x, y) in zip(nelot1, nelot2)])


#_____________________________________

# Make sure doctests run when script is run

if __name__ == '__main__':
    import doctest
    EPS = 1.0e-9  # for testing equality on floats
    print(doctest.testmod(verbose=False))



# Lecture 01

# Functions in Python

# Example 0: Here's a function that returns the largest of two numbers

def maximum(num1, num2):
    """
    Real, Real -> Real

    Consumes two numbers and produces the largest of them.

    >>> maximum(3, 1)
    3

    >>> maximum(1.1, 3.3)
    3.3

    >>> maximum(-2.1, -2.1)
    -2.1
    """

    if (num1 > num2):
        return num1
    else:
        return num2


#****Functions that operate on atomic data****

# Example: design a function that consumes a time t in seconds and
# produces the position of a particle in metres at that time according to
# the formula: s = 5 t + (1/2) a t^2  (where a = 9.81 m/s^2 is the acceleration
# due to gravity).

GRAV_ACCEL = 9.81

def particle_posn(time):
    """
    Real -> Real
    
    Produces the position of a particle at given time
    
    >>> particle_posn(0)
    0.0
    
    >>> act = particle_posn(1)
    >>> exp = 9.905
    >>> abs(act - exp) < EPS * exp
    True
    
    >>> act = particle_posn(2)
    >>> exp = 29.62
    >>> abs(act - exp) < EPS * exp
    True
    
    """
    #return 0.0  #stub
    #return ...time  #template
    return 5.0 * time + 0.5 * GRAV_ACCEL * time ** 2


#_______________________________________________

# ****Compound data

# Course is dict(name=str, enrolment=int)
# interp. a course with a name and a number of students enrolled

CRS1 = dict(name='CPSC 189', enrolment=35)
CRS2 = dict(name='ENGL 100', enrolment=121)

#def fn_for_course(c):
#    return ... c['name'] ... c['enrolment']


# ****Functions that operate on compound data****

# Example: design a function that consumes a course and determines
# if the course has sufficiently high enrolment to run.  Assume that a
# minimum enrolment of 30 students is required.

MIN_ENROL = 30

def can_run(crs):
    """
    Course -> bool
    
    Produces true if course can run
    
    >>> c1 = dict(name='ENGL 100', enrolment=5)
    >>> can_run(c1)
    False
    
    >>> c1['enrolment'] = 29
    >>> can_run(c1)
    False
    
    >>> c1['enrolment'] = 30
    >>> can_run(c1)
    True
    
    >>> c1['enrolment'] = 40
    >>> can_run(c1)
    True
    
    """
#    return False #stub
    return crs['enrolment'] >= MIN_ENROL

# Example: design a function that consumes a course and a number
# of students and that adds the given number of students to the course.
# Note: this function *mutates* the given course - it does not produce
# a new course!

def enrol_students(crs, num):
    """
    Course, int -> NoneType
    
    Effect: adds num students to crs
    
    >>> c1 = dict(name='ENGL 100', enrolment=5)
    >>> enrol_students(c1, 5)
    >>> c1 == dict(name='ENGL 100', enrolment=10)
    True
    """
    
#    return None #stub
    crs['enrolment'] = crs['enrolment'] + num
    
    
#______________________________________


#****Data of arbitrary size****



# ****Functions that operate on data of arbitrary size****

# Example: design a function that determines if a list of integers
# contains a particular integer.

def contains(loi, si):
    """
    (listof int) int -> bool
    
    Determines if loi contains si
    
    >>> contains([], 4)
    False
    
    >>> contains([3, 4, 5], 4)
    True
    
    >>> contains([3, 4, 5], 2)
    False
    """
    #return False #stub
    
    if loi == []:
        return False
    else:
        return si == loi[0] or contains(loi[1:], si)
    
# EXERCISE: design a function that consumes a list of integers and
# that determines how many of the integers are negative.

def negatives(loi):
    """
    (listof int) -> int
    
    Produces the number of negatives in the list
    
    >>> negatives([])
    0
    
    >>> negatives([1, 2, 3])
    0
    
    >>> negatives([3, -4, 5, -6, 7])
    2
    """
    #return 0 #stub
    
    if loi == []:
        return 0
    elif loi[0] < 0:
        return 1 + negatives(loi[1:])
    else:
        return negatives(loi[1:])

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
  
    >>> words_starting_with_vowel(['abc', 'def', 'efg', 'fgh'])
    ['abc', 'efg']

    >>> words_starting_with_vowel(['bcc', 'vff'])
    []
    
    """
    #return [] #stub
#    if low == []:
#        return ...
#    else:
#        return ... fn_for_word(low[0]) ...words_starting_with_vowel(low[1:])
    
    if low == []:
        return []
    else:
       if starts_with_vowel(low[0]):
           return [low[0]] + words_starting_with_vowel(low[1:])
       else:
           return words_starting_with_vowel(low[1:])

def starts_with_vowel(word):
    """
    Word -> bool
    
    Produces True if word starts with a vowel
    
    >>> starts_with_vowel('abc')
    True

    >>> starts_with_vowel('ebc')
    True

    >>> starts_with_vowel('ibc')
    True

    >>> starts_with_vowel('obc')
    True

    >>> starts_with_vowel('ubc')
    True

    >>> starts_with_vowel('hbc')
    False
    """
    return word[0] in 'aeiou'

# Make sure tests run when this module is run
if __name__=='__main__':
    import doctest
    EPS = 1.0e-6
    print(doctest.testmod(verbose=False))
    
    
    
    
    
    
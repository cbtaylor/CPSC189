# Lecture 01

# While reading through these notes you should make reference to the
# How to Design Functions (HtDF) and How to Design Data Definitions (HtDDD)
# pages on the course website.

# Try out the following in the "iPython Console" window:
#2 + 3
#5 * 4
#5 / 2
#5 // 2
#5.0 / 2.0

#type(2)
#type(2.0)
#type(2.)

# We see that 2 is of type 'int' while 2.0 (or simply 2.) is of type 'float'
#
# The rule is that if an algebraic operation is performed on
# arguments of type 'int', the result will be of type 'int', *except* for 
# division, in which case a float is produced.
# 
# However, if at least one argument is of type 'float' the result will be a
# 'float'.
#
# Note that if we wish to perform integer division, we can use the // operator.
# This can be used to divide one integer by another and produces an integer 
# result - this operator rounds down, hence, 5 // 2 produces 2 and not 3.
# Similarly, -5 // 2 produces -3 (because we round DOWN).


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

#***
# Note that the type Real encompasses int and float. In other words, an int
# is a Real and so is a float.  We can therefore call this function passing
# any combination of int and float as arguments.
#***


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
    
    >>> act = particle_posn(2.1)
    >>> exp = 32.13105
    >>> abs(act - exp) < EPS * exp
    True
    """
    #return 0.0   #stub
    #return ...time  #template
    return 5.0 * time + 1 / 2 * GRAV_ACCEL * time ** 2.0
    
#***
# Note that in the example above, and in those that follow, I've left the
# stub and template in place but this is just for your reference only.
# Normally, the stub is replaced by the template which in turn is replaced
# by the function body.
#***

#_______________________________________________

# ****Compound data

# Course is dict(name=str, enrolment=int)
# interp. a course with a name and a number of students enrolled

CRS1 = dict(name='CPSC 189', enrolment=35)
CRS2 = dict(name='ENGL 100', enrolment=121)

#def fn_for_course(c):
#    return ...c['name'] ...c['enrolment']


# Try the following in the 'iPython Console' window:
#crs = dict(name='CPSC 189', enrolment=35)

# We have accessors...
#crs['name']
#crs['enrolment']

# ...and mutators...
#crs['name'] = 'CPSC 110'
#crs['name']
#crs['enrolment'] = crs['enrolment'] + 100
#crs['enrolment']


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
    #return False  #stub
    #return ...crs['name'] ...crs['enrolment']  #template
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
    #return None  #stub
    #return ...crs['name'] ...crs['enrolment']  #template
    crs['enrolment'] = crs['enrolment'] + num



# Make sure tests run when this module is run
if __name__=='__main__':
    import doctest
    EPS = 1.0e-6
    print(doctest.testmod(verbose=False))

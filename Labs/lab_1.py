# Lab 01 Starter

# **********
# Exercise 1:
# Design a function named starwrap that consumes a string and produces 
# a string wrapped with 3 asterisks on either side.

# Hint: review the following section of the Python tutorial:
# http://docs.python.org/3.3/tutorial/introduction.html#strings
# and look for an operation that will be useful.

def starwrap(s):
    """
    String -> String
    
    Generate a new string with *** before and after a given string
    
    >>> starwrap('')
    '******'
    
    >>> starwrap('hello')
    '***hello***'
    """
    
    return '***' + s + '***'


# **********
# Exercise 2: Design a function miles2kms that consumes a distance in miles 
# and produces the equivalent distance in kilometers.  Use a conversion factor 
# of 1.6 kms per mile.  Do not assume that distances are measured to the 
# nearest mile or nearest kilometer. 

KMS_PER_MILE = 1.6

def miles2kms(d):
    """
    Real -> Real
    
    Produce the distance in km given the distance in miles
    
    >>> miles2kms(0)
    0.0
    
    >>> act = miles2kms(1)
    >>> exp = 1.6
    >>> abs(act - exp) <  DELTA * exp
    True
    
    >>> act = miles2kms(5.27)
    >>> exp = 8.432
    >>> abs(act - exp) < DELTA * exp
    True
    """
    return d * KMS_PER_MILE


# **********
# Exercise 3: Consider the following DD:

# LightState is one of:
# - 'red'
# - 'yellow'
# - 'green'
# interp. the colour of a traffic light

# <examples not needed for this kind of data>

# Complete the DD by providing a template for a function operating on a
# LightState.  Hint: consult the HtDDD recipe page.  What kind of data
# are we dealing with?

#def fn_for_ls(ls):
#    if ls == 'red':
#        return ...
#    elif ls == 'yellow':
#        return ...
#    elif ls == 'green':
#        return ...

# Design a function named change_light that consumes a LightState and produces
# the LightState that is next in sequence (red changes to yellow changes to
# green changes to red...)

def change_light(ls):
    """
    LightState -> LightState
    
    Produce the next LightState given the currrent LightState
    
    >>> change_light('red')
    'green'
    
    >>> change_light('yellow')
    'red'
    
    >>> change_light('green')
    'yellow'
    """
    if ls == 'red':
        return 'green'
    elif ls == 'yellow':
        return 'red'
    elif ls == 'green':
        return 'yellow'


# **********
# Exercise 4:
# Consider the following data definitions for Posn, Direction and Robot...

# Posn is dict(x=int, y=int)
# interp. the (x, y) coordinates of a point in the xy-plane

P1 = dict(x=5, y=20)
P2 = dict(x=-10, y=15)
P3 = dict(x=0, y=10)
P4 = dict(x=-1, y=1)

# Complete the DD by providing the template for a function operating on a Posn

#def fn_for_posn(p):
#    return ...p['x'] ...p['y']


# Direction is one of:
# - 'N'
# - 'S'
# - 'E'
# - 'W'

# <examples not needed for this kind of data>

# Complete the DD by providing a template for a function operating on a
# Direction.  Hint: consult the HtDDD recipe page.  What kind of data
# are we dealing with?

#def fn_for_dir(d):
#    if d == 'N':
#        return ...
#    elif d == 'S':
#        return ...
#    elif d == 'E':
#        return ...
#    elif d == 'W':
#        return ...


# Robot is dict(p=Posn, d=Direction)
# interp. a robot at position p heading in direction d

R1 = dict(p=P1, d='N')
R2 = dict(p=P2, d='E')
R3 = dict(p=P3, d='S')
R4 = dict(p=P4, d='W')

# Complete the DD by providing a template for a function operating on a Robot
# Hint: base your template on the Direction rather than the Posn

#def fn_for_robot(r):
#    if r['d'] == 'N':
#        return ...fn_for_posn(r['p']) ...fn_for_dir(r['d'])
#    elif r['d'] == 'S':
#        return ...fn_for_posn(r['p']) ...fn_for_dir(r['d'])
#    elif r['d'] == 'E':
#        return ...fn_for_posn(r['p']) ...fn_for_dir(r['d'])
#    elif r['d'] == 'W':
#        return ...fn_for_posn(r['p']) ...fn_for_dir(r['d'])


# Design a function named move that consumes a Robot and *mutates* that robot 
# by moving it 1 unit in whatever direction it is currently pointing. 

def move(r):
    """
    Robot -> NoneType
    
    Mutates a robot by updating the position by moving it one unit
    
    >>> move(R1)
    >>> exp = {'p': {'x': 5, 'y': 21}, 'd': 'N'}
    >>> R1 == exp
    True
    
    >>> move(R2)
    >>> exp = {'p': {'x': -9, 'y': 15}, 'd': 'E'}
    >>> R2 == exp
    True
    
    >>> move(R3)
    >>> exp = {'p': {'x': 0, 'y': 9}, 'd': 'S'}
    >>> R3 == exp
    True
    
    >>> move(R4)
    >>> exp = {'p': {'x': -2, 'y': 1}, 'd': 'W'}
    >>> R4 == exp
    True
    """

    if r['d'] == 'N':
        r['p']['y'] += 1
    elif r['d'] == 'S':
        r['p']['y'] -= 1
    elif r['d'] == 'E':
        r['p']['x'] += 1
    elif r['d'] == 'W':
        r['p']['x'] -= 1


# The remaining exercises are related to the problem of managing a
# fund-raising drive. Groups of people can form a fund-raising team
# and collect donations.  As manager, you will be interested in answering
# questions like: Which team has the largest amount donated?  Which team
# has the largest number of donations? We assume that amounts donated are
# always an integer number of dollars.

# **********
# Exercise 5: consider the following data definition...

# Donation is dict(name=str, amount=int)
# interp. a donation with name of the donor and the amount donated

D1 = dict(name='arjun', amount=45)
D2 = dict(name='sally', amount=53)
D3 = dict(name='joe', amount=10)

#def fn_for_dntn(d):
#    ...d['name'] ...d['amount']
    

# Design a function using natural recursion that consumes a list of 
# donations and produces the total amount donated.

def total_donated(lod):
    """
    (listof Donation) -> Integer
    
    Produce the total amount donated given a list of donations
    
    >>> total_donated([])
    0
    
    >>> total_donated([D1, D2, D3])
    108
    """
    if lod == []:
        return 0
    else:
        return lod[0]['amount'] + total_donated(lod[1:])


# **********
# Exercise 6: Consider the following data definition...

# Participant is dict(name=str, donations=(listof Donation))
# interp. a participant with a name and list of donations received 

PT1 = dict(name='alireza', donations=[])
PT2 = dict(name='sally', donations=[D1])
PT3 = dict(name='pat', donations=[D1, D2])
PT4 = dict(name='kelvin', donations=[D1, D2, D3])

#def fn_for_participant(p):
#    ...p['name'] ...fn_for_lod(p['donations'])

# Design a function using natural recursion that consumes a list of 
# participant and produces the total amount of donations received. 

def total_received(lop):
    """
    (listof Participant) -> Real
    
    Produce the total amount received given a list of participants
    
    >>> total_received([])
    0
    
    >>> total_received([PT1, PT2, PT3, PT4])
    251
    """
    if lop == []:
        return 0
    else:
        return total_donated(lop[0]['donations']) + total_received(lop[1:])



# **********
# Exercise 7: Consider the following data definition...

# Team is dict(name=str, lop=(listof Participant))
# interp. a team with a name and list of participants

T1 = dict(name='Team Rally', lop=[])
T2 = dict(name='Survivors', lop=[PT1])
T3 = dict(name='Moms United!', lop=[PT1, PT2])
T4 = dict(name='Tragic Collectors', lop=[PT1, PT2, PT3])
T5 = dict(name='Hockey Dads', lop=[PT1, PT2, PT3, PT4])

#def fn_for_team(t):
#    ...t['name'] ...fn_for_lop(t['lop'])

# Now suppose that a draw prize is available for teams that consist of 2 or
# 3 members only. Design a function using natural recursion that consumes 
# a list of teams and produces a list of the names of those teams that are 
# eligible for the draw prize. 
#
# Hint: the built-in function len will be useful in this exercise;  
# see: http://docs.python.org/library/functions.html

def eligible(lot):
    """
    (listof Team) -> (listof str)
    
    Produce a list of team names of teams that consist of 2 or 3 members only
    
    >>> eligible([])
    []
    
    >>> eligible([T1, T2, T3, T4, T5])
    ['Moms United!', 'Tragic Collectors']
    """
    if lot == []:
        return []
    else:
        if 1 < len(lot[0]['lop']) < 4:
            return [lot[0]['name']] + eligible(lot[1:])
        else:
            return eligible(lot[1:])



# Automatically run doctests whenever this script is run 
# (but not when it is imported)

if __name__=='__main__':
    import doctest
    DELTA = 1.0e-6   # for testing
    print(doctest.testmod(verbose=False))
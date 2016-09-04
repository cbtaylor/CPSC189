# Lab 01 - Partial Solutions

# **********
# Exercise 4:
# Consider the following data definitions for Posn, Direction and Robot...

# Posn is dict(x=int, y=int)
# interp. the (x, y) coordinates of a point in the xy-plane

P1 = dict(x=5, y=2)
P2 = dict(x=-10, y=15)


# Complete the DD by providing the template for a function operating on a Posn

#def fn_for_posn(p):
#    ...p['x'] ...p['y']



# Direction is one of:
# - 'N'
# - 'S'
# - 'E'
# - 'W'

# <examples not needed for this kind of data>

# Complete the DD by providing a template for a function operating on a
# Direction.  Hint: consult the HtDDD recipe page.  What kind of data
# are we dealing with?

#def fn_for_direction(d):
#    if d == 'N':
#        ...
#    elif d == 'S':
#        ...
#    elif d == 'E':
#        ...
#    elif d == 'W':
#        ...



# Robot is dict(p=Posn, d=Direction)
# interp. a robot at position p heading in direction d

R1 = dict(p=P1, d='N')
R2 = dict(p=P2, d='E')

# Complete the DD by providing a template for a function operating on a Robot

#def fn_for_robot(r):
#    ...fn_for_posn(r['p']) ...fn_for_direction(r['d'])  



# Design a function named move that consumes a Robot and *mutates* that robot by moving it 1 unit in
# whatever direction it is currently pointing.

def move(r):
    """
    Robot -> NoneType
    
    Effect: moves robot 1 unit in whatever direction it is facing
    
    >>> R = dict(p=dict(x=5, y=2), d='N')
    >>> move(R)
    >>> R == dict(p=dict(x=5,y=3), d='N')
    True
    
    >>> R = dict(p=dict(x=5, y=2), d='S')
    >>> move(R)
    >>> R == dict(p=dict(x=5,y=1), d='S')
    True
    
    >>> R = dict(p=dict(x=5, y=2), d='E')
    >>> move(R)
    >>> R == dict(p=dict(x=6,y=2), d='E')
    True
    
    >>> R = dict(p=dict(x=5, y=2), d='W')
    >>> move(R)
    >>> R == dict(p=dict(x=4,y=2), d='W')
    True
    """
    move_posn(r['p'], r['d'])
    return None                 #optional
       

def move_posn(p, d):
    """
    Posn, Direction -> NoneType
    
    Effect: moves position one unit in direction specified by d
    
    >>> P = dict(x=5,y=2)
    >>> move_posn(P,'N')
    >>> dict(x=5, y=3) == P
    True
    
    >>> P = dict(x=5,y=2)
    >>> move_posn(P,'S')
    >>> P == dict(x=5, y=1)
    True
    
    >>> P = dict(x=5,y=2)
    >>> move_posn(P,'E')
    >>> P == dict(x=6, y=2)
    True
    
    >>> P = dict(x=5,y=2)
    >>> move_posn(P,'W')
    >>> P == dict(x=4, y=2)
    True
    """
    if d == 'N':
        p['y'] = p['y'] + 1
    elif d == 'S':
        p['y'] = p['y'] - 1
    elif d =='E':
        p['x'] = p['x'] + 1
    elif d == 'W':
        p['x'] = p['x'] - 1
    return None                 #optional 
    
    
# Note: it could be argued that the helper move_posn is
# somewhat redundant given that the move function simply
# pulls apart the compound data and then passes both
# parts on as parameters to move_posn.  Here's an alternative
# design that doesn't make use of a helper.
#
# Notice that it *does* use two local variables named p and d 
# to help improve readability. Note that:
#    
# p = r['p']            # assign the robot's position to p
# p['y'] = p['y'] + 1   # increase y coord of robot's position by 1
#
# is easier to read than:
#    
# r['p']['y'] = r['p']['y'] + 1  # increase y coord of robot's position by 1
#    
# Also note that this version of the function is called move_robot 
# rather than move, as it needs to have a unique name within this file. 
# Alternatively, we could just comment out the version above and use
# the same name.

def move_robot(r):
    """
    Robot -> NoneType
    
    Effect: moves robot 1 unit in whatever direction it is facing
    
    >>> R = dict(p=dict(x=5, y=2), d='N')
    >>> move_robot(R)
    >>> R == dict(p=dict(x=5,y=3), d='N')
    True
    
    >>> R = dict(p=dict(x=5, y=2), d='S')
    >>> move_robot(R)
    >>> R == dict(p=dict(x=5,y=1), d='S')
    True
    
    >>> R = dict(p=dict(x=5, y=2), d='E')
    >>> move_robot(R)
    >>> R == dict(p=dict(x=6,y=2), d='E')
    True
    
    >>> R = dict(p=dict(x=5, y=2), d='W')
    >>> move_robot(R)
    >>> R == dict(p=dict(x=4,y=2), d='W')
    True
    """
    p = r['p']
    d = r['d']
    if d == 'N':
        p['y'] = p['y'] + 1
    elif d == 'S':
        p['y'] = p['y'] - 1
    elif d =='E':
        p['x'] = p['x'] + 1
    elif d == 'W':
        p['x'] = p['x'] - 1
    return None                 #optional


# **********
# Exercise 5: Consider the following data definition...

# Donation is dict(name=str, amount=int)
# interp. a donation with name of the donor and the amount donated
D1 = dict(name='arjun', amount=45)
D2 = dict(name='sally', amount=53)
D3 = dict(name='joe', amount=10)

# Complete the DD by providing a template for a function operating on a Donation

#def fn_for_dntn(d):
#    ...d['name'] ...d['amount']

def total_donated(lod):
    """
    (listof Donation) -> int
    
    Produces total donations in lod

    >>> total_donated([])
    0
    >>> total_donated([D1])
    45
    >>> total_donated([D1, D2])
    98
    
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


def total_donations_lop(lop):
    """
    (listof Participant) -> int
    
    Produces the total amount of donations collected by participants in lop
    
    >>> total_donations_lop([])
    0
    >>> total_donations_lop([PT2])
    45
    >>> total_donations_lop([PT1, PT2, PT3])
    143
    """
    if lop == []:
        return 0
    else:
        return total_donated_participant(lop[0]) + total_donations_lop(lop[1:])


def total_donated_participant(p):
    """
    Participant -> int
    
    Produces total amount of donations for partipant p
    
    >>> total_donated_participant(PT1)
    0
    >>> total_donated_participant(PT3)
    98
    """
    return total_donated(p['donations'])

# The function total_donated was designed in Exercise 5. 


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
# Hint: the built-in function len will again be useful in this exercise.

def eligible_teams(lot):
    """
    (listof Team) -> (listof str)
    
    Produces list of names of teams in lot that are eligible.
    
    >>> eligible_teams([])
    []
    >>> eligible_teams([T2])
    []
    >>> eligible_teams([T3])
    ['Moms United!']
    >>> eligible_teams([T1, T2, T3, T4, T5])
    ['Moms United!', 'Tragic Collectors']
    """
    if lot == []:
        return []
    else:
        if is_eligible_team(lot[0]):
            return [lot[0]['name']] + eligible_teams(lot[1:])
        else:
            return eligible_teams(lot[1:])
            
                                 
def is_eligible_team(t):
    """
    Team -> bool
    
    Determines if team is eligible
    
    >>> is_eligible_team(T2)
    False
    >>> is_eligible_team(T3)
    True
    >>> is_eligible_team(T4)
    True
    >>> is_eligible_team(T5)
    False
    """
    return is_eligible_lop(t['lop'])


def is_eligible_lop(lop):
    """
    (listof Participant) -> bool
    
    Determines if list of participants has length 2 or 3
    
    >>> is_eligible_lop([])
    False
    
    >>> is_eligible_lop([PT1])
    False

    >>> is_eligible_lop([PT1, PT2])
    True
    
    >>> is_eligible_lop([PT1, PT2, PT3])
    True
    
    >>> is_eligible_lop([PT1, PT2, PT3, PT4])
    False
    """
    team_len = len(lop)
    return team_len == 2 or team_len == 3


# Automatically run doctests whenever this script is run 
# (but not when it is imported)

if __name__=='__main__':
    import doctest
    DELTA = 1.0e-6   # for testing
    print( doctest.testmod(verbose=False) )
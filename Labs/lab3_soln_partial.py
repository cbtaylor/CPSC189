# CPSC 189, Lab 03 - File I/O

import os
from io import StringIO

# Global assumptions: files have expected number of header rows and
# data in file is separated by specified delimiter.  There is at least one
# row of data in the file. There could be rows that contain only
# whitespace (spaces or tabs or newlines).

# The following function from lecture is provided for use in this lab:

def skip_rows(f, num_rows):
    """
    file, int -> NoneType

    Effect: skips over next num_rows rows in file

    >>> test_file = StringIO('row1\\n row2\\n row3\\n row4\\n')
    >>> skip_rows(test_file, 3)
    >>> test_file.readline()
    ' row4\\n'
    """
    for row in range(num_rows):
        f.readline()

# In the questions that follow, we assume that we are working
# with Environment Canada data in the file yvr_2011.csv (or a similarly
# formatted file) which we assume is in the same directory as this Python
# source file.


#____________________________________________________________________________
# Q0. The files that we are working with in this lab are formatted in
# such a way that there are multiple data points on each line of the file.
# In many of the exercises that follow, we will want to extract a
# data point from a particular column.  We will therefore begin by
# designing a function to perform this task.

def item_in_col(line, col, delim=None):
    """
    str, int, str -> float

    Produces the float at the given column in line.
    Assume: the first column is column 0
    Requires: line is a string containing numbers separated by delim

    >>> item_in_col('0.0, 1.1, 2.2, 3.3, 4.4, 5.5', 4, ',')
    4.4
    >>> item_in_col('0.0 1.1 2.2 3.3 4.4 5.5', 3)
    3.3
    """
    data = line.split(delim)
    return float(data[col])


#____________________________________________________________________________
# Q4. Design a function that produces a file that contains only the data
# stored in a specified column of the Environment Canada csv file.  The data
# must be written one value per row in the output file with no additional
# characters.

# Note: tests are not required for this function (it's a bit messy)

def write_col(inf, outf, col, delim=None, nhr=0):
    """
    file, file, int, str, int -> NoneType

    Effect: writes to file outf data from column col of inf
    All header rows from inf are ignored and not written to outf.

    >>> file_data = 'H1\\nH2\\nH3\\n0.0 1.0 2.0 3.0\\n   \\n'
    >>> test_infile = StringIO(file_data)
    >>> test_outfile = StringIO()
    >>> write_col(test_infile, test_outfile, 2, nhr=3)
    >>> test_outfile.getvalue()
    '2.0\\n'

    >>> file_data = 'H1\\nH2\\nH3\\n0.0 1.0 2.0 3.0\\n'  \
                                   '   \\n4.0 5.0 6.0 7.0\\n  \\n'
    >>> test_infile = StringIO(file_data)
    >>> test_outfile = StringIO()
    >>> write_col(test_infile, test_outfile, 2, nhr=3)
    >>> test_outfile.getvalue()
    '2.0\\n6.0\\n'

    """
    skip_rows(inf, nhr)

    for line in inf:
        if line.strip() != '':
            outf.write(str(item_in_col(line, col, delim)) + '\n')

# Q4b) Make a call to your function from the Python Shell so that data
# from column 5 in yvr_2011.csv is written to the file yvr_2011_5.txt.

# Make a note of the call that you make to your function so that it
# can be checked by your TA:

#with open('yvr_2011.csv', 'U') as inf:
    #with open(yvr_2011_5.txt, 'w') as outf:
        #write_col(inf, outf, 5, ',', 24)

# Check that the file was created containing the expected data.

#____________________________________________________________________________
# Q5. Design a function that consumes a file that contains a table
# of numbers with at least one row of data and at least one number per row.  

# Your function must produce a list of all the numbers in the file
# in the order in which they appear in the file, reading left to right
# and top-down.  Study the provided tests carefully before continuing. 
#
# Your solution must make use of a list comprehension. However, you may want 
# to start by designing a solution using a loop and then refactoring the code 
# to use a list comprehension.

def file_to_lon(f, delim=None, nhr=0):
    """
    file, str, int -> (listof Real)
    
    Produces a list of the numbers read from f
    
    >>> file_data = 'H1\\nH2\\nH3\\n0.0 1.0 2.0 3.0\\n'  \
                                   '   \\n4.0 5.0 6.0 7.0\\n  \\n'
    >>> test_file = StringIO(file_data)
    >>> act = file_to_lon(test_file, nhr=3)
    >>> exp = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    >>> act == exp
    True
    
    >>> file_data = 'H1\\nH2\\nH3\\n0.0, 1.0, 2.0\\n'  \
                                   '   \\n3.0, 4.0, 5.0\\n  \\n'
    >>> test_file = StringIO(file_data)
    >>> act = file_to_lon(test_file, ',', 3)
    >>> exp = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    >>> act == exp
    True
    """
    skip_rows(f, nhr)
    return [float(num) for line in f if line.strip() != '' for num in line.split(delim)]

# Q5b) Make a call to your function from the Python Shell and produce a list of
# the numbers found in the file heightData.txt

# Make a note of the call that you make to your function so that it
# can be checked by your TA:

#with open('heightData.txt', 'U') as inf:
#    print(file_to_lon(inf, '#', 1))

# Check that the list printed on the console contains the expected data:
#
# [0.12435, 0.25235, 0.52935, 0.45245, 
#  0.22553, 0.26323, 0.41983, 0.89098, 
#  0.23523, 0.28375, 0.22385, 0.32898, 
#  0.35354, 0.13523, 0.12323, 0.23557, 
#  0.42525, 0.09728, 0.09283, 0.18753, 
#  0.23529, 0.00234, 0.10938, 0.39223, 
#  0.12415, 0.00034, 0.49029, 0.23423]


#____________________________________________________________________________
# Q6. Design a function that consumes a file that contains a table
# of numbers with at least one row of data and at least one number per row.   

# Your function must produce a list of lists of numbers.  Each list within
# the list of list of numbers must contain the numbers found on a single
# row of the file, in the order in which they appear on that row. Study
# the provided tests carefully before continuing. 
#
# Your solution must make use of a list comprehension. However, you may want 
# to start by designing a solution using a loop and then refactoring the code 
# to use a list comprehension.

def file_to_lolon(f, delim=None, nhr=0):
    """
    file, str, int -> (listof (listof Real))
    
    Produces a list of list of numbers read from f, one list per row of numbers
    
    >>> file_data = 'H1\\nH2\\nH3\\n0.0 1.0 2.0 3.0\\n'  \
                                   '   \\n4.0 5.0 6.0 7.0\\n  \\n'
    >>> test_file = StringIO(file_data)
    >>> act = file_to_lolon(test_file, nhr=3)
    >>> exp = [[0.0, 1.0, 2.0, 3.0], [4.0, 5.0, 6.0, 7.0]]
    >>> act == exp
    True
    
    >>> file_data = 'H1\\nH2\\nH3\\n0.0, 1.0, 2.0\\n'  \
                                   '   \\n3.0, 4.0, 5.0\\n  \\n'
    >>> test_file = StringIO(file_data)
    >>> act = file_to_lolon(test_file, ',', 3)
    >>> exp = [[0.0, 1.0, 2.0], [3.0, 4.0, 5.0]]
    >>> act == exp
    True
    """
    skip_rows(f, nhr)
    return [[float(num) for num in line.split(delim)] for line in f if line.strip() != '']

# Q6b) Make a call to your function from the Python Shell and produce a list of
# the numbers found in the file heightData.txt

# Make a note of the call that you make to your function so that it
# can be checked by your TA:

#with open('heightData.txt', 'U') as inf:
#    print(file_to_lolon(inf, '#', 1))

# Check that the list printed on the console contains the expected data:
#
# [[0.12435, 0.25235, 0.52935, 0.45245], 
#  [0.22553, 0.26323, 0.41983, 0.89098], 
#  [0.23523, 0.28375, 0.22385, 0.32898], 
#  [0.35354, 0.13523, 0.12323, 0.23557], 
#  [0.42525, 0.09728, 0.09283, 0.18753], 
#  [0.23529, 0.00234, 0.10938, 0.39223], 
#  [0.12415, 0.00034, 0.49029, 0.23423]]

#____________________________________________________________________________
# Q7a. Design a function that consumes a file containing only text and
# produces a tuple (#para, #sentence, #word) where #para is the number
# of paragraphs, #sentence is the number of sentences and #word is
# the number of words found in the document.

# We make the following simplifying assumptions:
# - we can determine the number of paragraphs by counting the number
#   of blank lines as there is always a single blank line between
#   paragraphs and a single blank line at the end of the file
# - we can determine the number of sentences by counting the number
#   of words that have a period at the end
# - words are separated by one or more spaces

# Data Definition

# TextAnalysis is (p_count=int, s_count=int, w_count=int)
# interp. the number of paragraphs, sentences and words in text

A1 = (10, 42, 225)
A2 = (1, 5, 56)

#def fn_for_text_analysis(t):
#    ...t[0] ...t[1] ...t[2]
    


def analyze_text(f):
    """
    file -> TextAnalysis
    
    Produces a text analysis of the text in file f.
    
    >>> test_file = StringIO('')
    >>> analyze_text(test_file)
    (0, 0, 0)
    
    >>> test_file = StringIO('One para, one sentence, six words.\\n  \\n')
    >>> analyze_text(test_file)
    (1, 1, 6)
    
    >>> test_file = StringIO('One para, two sentence. Second sentence.\\n  \\n')
    >>> analyze_text(test_file)
    (1, 2, 6)
    
    >>> test_file = StringIO('First para, first sentence, 6 words.\\n \\n' \
                             'Second para, second sentence, 6 words.\\n \\n' \
                             'Third para, third sentence, 6 words.\\n \\n')
    >>> analyze_text(test_file)
    (3, 3, 18)
    """
    p_count = 0
    s_count = 0
    w_count = 0
    
    for line in f:
        if line.strip() == '':
            p_count += 1
        else:
            s_count += count_sentences(line)
            w_count += count_words(line)
            
    return (p_count, s_count, w_count)


def count_sentences(line):
    """
    str -> int
    
    Produces number of sentence endings line.
    
    >>> count_sentences('')
    0
    >>> count_sentences('One. Two words. Three more words.')
    3
    """
    s_count = 0
    
    words = line.split()
    for word in words:
        if word.endswith('.'):
            s_count += 1
            
    return s_count


def count_words(line):
    """
    str -> int
    
    Produces number of words in line
    
    >>> count_words('')
    0
    
    >>> count_words('a ab abc, "def": end.')
    5
    """
    return len(line.split())

    
# Q7b) Make a call to your analyze_text function and analyze the text in the file
# lorumIpsum.txt (this text is brought to you courtesy of http://www.lipsum.com/)


# Make a note of the call that you make to your function so that it
# can be checked by your TA:

# Expected output: (100, 1113, 9033)


#____________________________________________________________________________

# Make sure doctests run whenever this module is run.

if __name__=='__main__':
    import doctest
    EPS = 1.0e-6
    print(doctest.testmod(verbose=False))

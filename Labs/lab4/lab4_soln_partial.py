# CPSC 189, Lab 04 - File I/O - Partial Solutions

import matplotlib.pyplot as pyplt
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

# In the questions that follow, we assume that we are working
# with Environment Canada data in the file yvr_2011.csv (or a similarly
# formatted file) which we assume is in the same directory as this Python
# source file.

# Be sure to account for the fact that there may be empty lines in the file.

#____________________________________________________________________________

# Q3. Design a function that uses the matplotlib library to generate a graph 
# of the mean daily temperature for each day of the year.  Use the
# number of days since the start of the year as the independent variable.
# Label both axes and give your chart the title:
#    Mean Daily Temperature: <name of file f>
# So, if f is the file named 'yvr_2011.csv' then the title of your chart will
# be:
#    Mean Daily Temperature: yvr_2011.csv
#
# Save your chart as a .png file named yvr_2011.png

# Hint: you will need to skim through the documentation for matplotlib.pyplot
# http://matplotlib.sourceforge.net/api/pyplot_api.html
# to find functions that allow you to specify labels, set tick marks and
# save a plot to a file.

def plot_mdt(f, delim=None, nhr=0):
    """
    file, str, int -> NoneType

    Effect: generates plot of mean temperature against day of year for data
    in file f
    <Can't test this one.>
    """
    skip_rows(f, nhr)

    data = col_2_list(f, 9, delim)
    
    name, ext = os.path.splitext(f.name)
        
    pyplt.plot(data, 'g-')
    pyplt.title('Daily Mean temperature: ' + f.name)
    pyplt.ylabel('Mean temperature (C)')
    pyplt.xlabel('Day of year')
    pyplt.xticks(range(0, len(data), 30))
    pyplt.xlim(0, 365)
    pyplt.savefig(name + '.png', dpi=300)
    
    
def col_2_list(f, col, delim=None):
    """
    file, int, str -> (listof Real)
    
    Produces a list containing all the data in the specified column of f
    
    Requires: data is separated by delim; there are at least col columns
    of data (counting from zero)
    
    >>> test_file = StringIO('1 2 3\\n4 5 6\\n7 8 9\\n')
    >>> col_2_list(test_file, 2)
    [3.0, 6.0, 9.0]
    >>> test_file = StringIO('1.1, 2.2, 3.3\\n4.4, 5.5, 6.6\\n7.7, 8.8, 9.9\\n')
    >>> col_2_list(test_file, 0, ',')
    [1.1, 4.4, 7.7]
    """
    return [item_in_col(line, col, delim) for line in f if line.split() != '']


# Q3b. Make a call to your function from the Python Shell and verify that
#     the required file has been produced and contains the expected plot.

# Make a note of the call that you make to your function so that it
# can be checked by your TA:

# with open('yvr_2011.csv', 'U') as f:
#     plot_mdt(f, ',', 24)

# Check that the file was created containing the expected data.



#____________________________________________________________________________

# Q4. Design a function that walks the directory EnvCanData and produces
# a plot of the mean daily temperature for every .csv file found in that
# directory or any of its subdirectories.  The plot must be saved to
# a .png file having the same name as the .csv file.  Be on the lookout for
# operations on data of arbitrary size and design helpers to process this
# data.  Note that all the .csv files have the same format as
# yvr_2011.csv.
#
# Hint: you will need to make a call to pyplt.cla() to clear one plot
# before generating the next.  Otherwise, successive plots will be added
# to the same set of axes.

def plot_mdt_dir(rdir, delim=None, nhr=0):
    """
    str, str, int -> NoneType

    Effect: generates plot of mean temperature against day of year for data
    in each .csv file found in rdir or any of its subdirectories.
    """
    for root, lodn, lofn in os.walk(rdir):
        plot_mdt_lofn(root, lofn, delim, nhr)


def plot_mdt_lofn(root, lofn, delim, nhr):
    """
    str, (listof str), str, int -> NoneType

    Effect: generates plot of mean temperature against day of year for data
    in each .csv file found in lofn.
    """
    for fn in lofn:
        name, ext = os.path.splitext(fn)
        if ext == '.csv':
            with open(os.path.join(root, fn), 'U') as f:
                pyplt.cla()
                plot_mdt(f, delim, nhr)


#Q4b. Make a call to your function from the Python Shell and verify
#     that the required files containing the plots have been produced.

# Make a note of the call that you make to your function so that it
# can be checked by your TA:

# plot_mdt_dir('EnvCanData', ',', 24)



#____________________________________________________________________________

# Make sure doctests run whenever this module is run.

if __name__=='__main__':
    import doctest
    EPS = 1.0e-9
    print(doctest.testmod(verbose=False))

# \file files.py
# Python file library


#===============================================================================
# Content:            
#===============================================================================

#def skip_blanks(file, blanks=_DEF_BLANKS):
""" 
\param file: the file to clean of commentaries and blanks characters.
\param blanks: (string) array of blank expressions (i.e. " \t\n")

Given file:
1) Remove all the blank lines.
2) Return a 'generator object' the rest of the lines.
"""


# def skip_comments(file, comments=_DEF_COMMENTS):
""" 
\param file: the file to clean of commentaries.
\param comments: list (strings) of possible comment characters.

Given file:
1) Remove all the comment lines. (Lines beginning with 'comments')
2) Return a 'generator object' the rest of the lines.
"""

#def skip_blanks_and_comments(file, blanks=_DEF_BLANKS, comments=_DEF_COMMENTS):
"""
\param file: the file to clean of commentaries and blanks characters.
\param blanks: (string) array of blank expressions (i.e. " \t\n")
\param comments: list (strings) of possible comment characters.

Given file:
1) Remove all the blank lines.
2) Remove all the comment lines.
3) Return a 'generator object' the rest of the lines.
"""

            
#===============================================================================
# constants
#===============================================================================

# _EXAMPLE_FILE = "data/errors.data"
_DEF_BLANKS = " \t\n"
_DEF_COMMENTS = ["#"]
            
#===============================================================================

def skip_blanks(file, blanks=_DEF_BLANKS):
    """ 
    \param file: the file to clean of commentaries and blanks characters.
    \param blanks: (string) array of blank expressions (i.e. " \t\n")
    
    Given file:
    1) Remove all the blank lines.
    2) Return a 'generator object' the rest of the lines.
    """
    assert(type(blanks) is str)
    assert(len(blanks)>0)

    for line in file:
        yield line.strip(blanks)

#-------------------------------------------------------------------------------

def skip_comments(file, comments=_DEF_COMMENTS):
    """ 
    \param file: the file to clean of commentaries.
    \param comments: list (strings) of possible comment characters.

    Given file:
    1) Remove all the comment lines. (Lines beginning with 'comments')
    2) Return a 'generator object' the rest of the lines.
    """
    assert(not file.closed)
    assert(type(comments) is list)
    assert(len(comments>0))
    
    if len(comments > 1):
        _skip_comments_multiple(file, comments)
    else:
        _skip_comments_single(file, comments)

#-------------------------------------------------------------------------------

def skip_blanks_and_comments(file, blanks=_DEF_BLANKS, comments=_DEF_COMMENTS):
    """
    \param file: the file to clean of commentaries and blanks characters.
    \param comments: list (strings) of possible comment characters.
    \param blanks: (string) array of blank expressions (i.e. " \t\n")

    Given file:
    1) Remove all the blank lines.
    2) Remove all the comment lines.
    3) Return a 'generator object' the rest of the lines.
    """
    assert(not file.closed)
    assert(type(comments) is list)
    assert(len(comments>0))
    assert(type(blanks) is str)
    assert(len(blanks)>0)
    
    if len(comments > 1):
        _skip_blanks_and_comments_multiple(file, comments, blanks)
    else:
        _skip_blanks_and_comments_single(file, comments, blanks)

#-------------------------------------------------------------------------------

 

#===============================================================================
# Private 
#===============================================================================


def _skip_comments_single(file, comments):
    """ 
    \param file: the file to clean of commentaries.
    \param comments: a comment character as a string (i.e. '#').
    Given file:
    1) Remove all the comment lines.
    2) Return a 'generator object' the rest of the lines.
    """
    assert(not file.closed)
    assert(type(comments) is list)
    assert(len(comments==1))
    assert(type(comments[0]) is str)
    
    # assert(len(comments.split() <= 1)
    for line in file:
        if not line.strip().startswith(comments[0]):
            yield line

#-------------------------------------------------------------------------------

def _skip_comments_multiple(file, comments):
    """ 
    \param file: the file to clean of commentaries.
    \param comments: list (strings) of comment characters: i.e. ['#', '%', '//']

    Given file:
    1) Remove all the comment lines.
    2) Return a 'generator object' the rest of the lines.
    Info: 
    """
    assert(not file.closed)
    assert(type(comments) is list)
    assert(len(comments)>1)
        
    for line in file:
        valid_line=True
        # for comment_value in comments.split():  #strings
        for comment_value in comments:
            assert(type(comment_value) is str)
            if line.strip().startswith(comment_value):
                valid_line=False
                break
        if valid_line:
            yield line
            
#-------------------------------------------------------------------------------

def _skip_blanks_and_comments_single(file, comments, blanks):
    """ 
    \param file: the file to clean of commentaries.
    \param comments: a comment character as a string (i.e. '#').
    \param blanks: (string) array of blank expressions (i.e. " \t\n")

    Given file:
    1) Remove all the comment lines.
    2) Return a 'generator object' the rest of the lines.
    """

    assert(not file.closed)
    assert(type(comments) is list)
    assert(len(comments==1))
    assert(type(comments[0]) is str)
    assert(type(blanks) is str)
    assert(len(blanks)>0)
    
    for line in file:
        line = line.strip(blanks)
        if(not line.strip().startswith(comments[0])) and (not len(line) is 0):
            yield line

#-------------------------------------------------------------------------------

def _skip_blanks_and_comments_multiple(file, comments, blanks):
    """
    \param file: the file to clean of commentaries and blanks characters.
    \param comments: list (strings) of possible comment characters.
    \param blanks: (string) array of blank expressions (i.e. " \t\n")

    Given file:
    1) Remove all the blank lines.
    2) Remove all the comment lines.
    3) Return a 'generator object' the rest of the lines.
    """

    assert(not file.closed)
    assert(type(comments) is list)
    assert(len(comments)>1)
    assert(type(blanks) is str)
    assert(len(blanks)>0)

    for line in file:
        line = line.strip(blanks)
        valid_line=True
        if(len(line) is 0):
            continue
        for comment_value in comments:
            assert(type(comment_value) is str)
            if line.strip().startswith(comment_value):
                valid_line=False
                break
            if valid_line:
                yield line
           
#===============================================================================

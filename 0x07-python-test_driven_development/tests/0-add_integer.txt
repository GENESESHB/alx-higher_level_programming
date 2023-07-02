>>> add_integer = __import__('0-add_integer').add_integer

    ---- Check that the file is executable ----
    >>> import os
    >>> os.access('0-add_integer.py', os.X_OK)
    True

    ---- Check for the documentation of the module ----
    >>> len(__import__("0-add_integer").__doc__) > 10
    True

    ---- Check for the documentation of the function ----
    >>> len(__import__("0-add_integer").add_integer.__doc__) > 10
    True

    ---- Check for pep8 style ----
    >>> os.popen("pep8 0-add_integer.py").read()
    ''

    ---- Check for a newline at the end of the file ----
    >>> os.popen("cat -e 0-add_integer.py | tail -1").read()[-1]
    '\n'

    ---- Check for the file has a shebang ----
    >>> os.popen("cat 0-add_integer.py | head -1").read()
    '#!/usr/bin/python3\n'

    ---- Check that the README file exists ----
    >>> cwd = os.getcwd()
    >>> check_readme = cwd + '/README.md'
    >>> os.path.exists(check_readme)
    True


    #-------------------------- Tests from 0-main.py --------------------------#

    ### Both ints.
    >>> add_integer(1, 2)
    3

    ### One negative
    >>> add_integer(100, -2)
    98

    ### Only one int.
    >>> add_integer(2)
    100

    ### One float.
    >>> add_integer(100.3, -2)
    98

    ### Str in (b) argument.
    >>> add_integer(4, "School")
    Traceback (most recent call last):
    ...
    TypeError: b must be an integer

    ### None
    >>> add_integer(None)
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer

    #------------------ Mixed Correct cases, int, float ------------------#

    ### int + float
    >>> add_integer(3, 3.5)
    6

    ### float + int
    >>> add_integer(3.2, 3)
    6

    ### int + -float
    >>> add_integer(3, -3.2)
    0

    ### -float + int
    >>> add_integer(-3.9, 3)
    0

    ### float + -int
    >>> add_integer(3.2, -3)
    0

    ### -int + float
    >>> add_integer(-3, 3.2)
    0

    ### -int + -float
    >>> add_integer(-3, -3.5)
    -6

    ### Only one int.
    >>> add_integer(2)
    100

    ### float + float
    >>> add_integer(3.9, 3.5)
    6

    ### -int + -int
    >>> add_integer(-3, -3)
    -6

    #--------------------------| Incorrect cases |--------------------------#

    #------------------------- Not Correct Types -------------------------#

    ### Complex type
    >>> add_integer(3j)
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer

    ### Boolean type
    >>> add_integer(True, 1)
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer

    ### Too large of a number.
    >>> add_integer(1, 10e+1000)
    Traceback (most recent call last):
    ...
    OverflowError: cannot convert float infinity to integer

    >>> add_integer(1, (10e+1000 / 10e+1000))
    Traceback (most recent call last):
    ...
    ValueError: cannot convert float NaN to integer

    ### Two Floats.
    >>> add_integer(100.3, -100.3)
    0

    ### Str in (a) argument.
    >>> add_integer("C was fun", -100.3)
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer

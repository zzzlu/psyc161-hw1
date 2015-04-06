"""Module for estimation of factorial (Homework #1)

Note:  this is just a skeleton for you to work with.  But it already
       has some "bugs" you need to catch and fix.
"""

from nose.tools import assert_equal


def factorial_recursive(n):
    # TODO Define your logic for factorial here
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
    pass  # does nothing


def factorial(n):
    f = 1
    while n > 1:
        f = f*n
        n -= 1
    return f


def test_factorial():
    assert_equal(factorial_recursive(1), 1)
    # TODO: add more
    assert_equal(factorial_recursive(2), 2)
    assert_equal(factorial_recursive(6), 720)
    assert_equal(factorial(1), 1)
    # TODO: add more
    assert_equal(factorial(2), 2)
    assert_equal(factorial(6), 720)


if __name__ == '__main__':
    # This is a way to determine either file was "executed", so if it was
    # imported (by e.g. nose) as a library, we should not run code
    # below

    nconditions = raw_input("Please enter number of conditions: ")
    norders = factorial_recursive(int(nconditions))
    print("Number of possible trial orders: " + str(norders))
    import time

    start_time = time.clock()
    factorial(6)
    recursive_running_time = time.clock() - start_time
    print "running non-recursive factorial is ", recursive_running_time, "seconds"

    start_time = time.clock()
    factorial_recursive(6)
    non_recursive_running_time = time.clock() - start_time
    print "running recursive factorial is ", non_recursive_running_time, "seconds"

    print "time difference between running recursive and non_recursive factorial function is ", \
        recursive_running_time - non_recursive_running_time

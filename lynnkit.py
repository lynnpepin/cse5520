def fib(nn: int) -> int:
    '''Returns the nth value in the fibonacci sequence

    :param nn: The index of the value to generate for the fibonacci sequence
    :type nn: int
    
    :raises ValueError: for values < 0
    :raises TypeError:  for non-int input

    :returns: The (nn)th value of the fibonacci sequence
    :rtype: int

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(10)
    55
    >>> fib(-1)
    Traceback (most recent call last):
    ...
    TypeError: Fibonacci sequence can not be evaluated on negative index
    >>> fib(3.1)
    Traceback (most recent call last):
    ...
    TypeError: Fibonacci sequence can only be indexed over integers
    
    '''
    if not type(nn) is int:
        raise TypeError("Fibonacci sequence can only be indexed over integers")
    if nn < 0:
        raise TypeError("Fibonacci sequence can not be evaluated on negative index")
    vals = [0, 1]
    for ii in range(0, nn):
        vals[ii%2] += vals[(ii+1)%2]
    
    return vals[nn%2]


def fibgen():
    """Provides a generator yielding the  fibonacci sequence
    
    :yields: int
    :returns: An iterator which yields the i-th value of the Fibonacci sequence
        for each i-th call of next() on an instance of fibgen
    :rtype: Iterator[int]

    >>> f = fibgen()
    >>> next(f)
    0
    >>> next(f)
    1
    >>> next(f)
    1
    >>> next(f)
    2
    >>> next(f)
    3
    """
    
    vals = [0, 1]
    ii = 0
    while True:
        yield vals[ii%2]
        vals[ii%2] += vals[(ii+1)%2]
        ii += 1
    

def _fib2(nn: int) -> int:
    # for bytecode comparison
    a = 0
    b = 1
    if nn == 0:
        return 0
    if nn == 1:
        return 1
    else:
        for _ in range(0, nn-1):
            s = a + b
            a, b = b, a
            b = s
        
        return s

def binsearch(func, vv = 0.025, x_l = -100, x_r = 100, eps=0.00001):
    '''
    Search for a float input xx such that func(xx) = vv,
    where func(xx) increases as x does,
    and where x_l <= xx <= x_r
    
    :param :
    :type :
    :param :
    :type :
    :param :
    :type :
    '''
    v_l = func(x_l)
    v_r = func(x_r)
    
    x_m = (x_l + x_r)/2
    v_m = func(x_m)
    
    while abs(v_m - vv) >= eps:
        if v_m < vv:
            x_l = x_m
        elif v_m > vv:
            x_r = x_m
        else:
            print("weird, this shouldn't be possible")
            return x_m
            
        v_l = func(x_l)
        v_r = func(x_r)
        x_m = (x_l + x_r)/2
        v_m = func(x_m)
    
    return x_m


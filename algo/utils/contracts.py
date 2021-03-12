"""
Definition Imported from
https://wiki.python.org/moin/PythonDecoratorLibrary#Pre-.2FPost-Conditions
"""
__all__ = ['precondition', 'postcondition', 'conditions']

DEFAULT_ON = True


def precondition(precondition, use_conditions=DEFAULT_ON):
    return conditions(precondition, None, use_conditions)


def postcondition(postcondition, use_conditions=DEFAULT_ON):
    return conditions(None, postcondition, use_conditions)


class conditions(object):
    __slots__ = ('__precondition', '__postcondition')

    def __init__(self, pre, post, use_conditions=DEFAULT_ON):
        if not use_conditions:
            pre, post = None, None

        self.__precondition = pre
        self.__postcondition = post

    def __call__(self, function):
        # combine recursive wrappers (@precondition + @postcondition == @conditions)
        pres = set((self.__precondition,))
        posts = set((self.__postcondition,))

        # unwrap function, collect distinct pre-/post conditions
        while type(function) is FunctionWrapper:
            pres.add(function._pre)
            posts.add(function._post)
            function = function._func

        # filter out None conditions and build pairs of pre- and postconditions
        conditions = map(None, filter(None, pres), filter(None, posts))

        # add a wrapper for each pair (note that 'conditions' may be empty)
        for pre, post in conditions:
            function = FunctionWrapper(pre, post, function)

        return function


class FunctionWrapper(object):
    def __init__(self, precondition, postcondition, function):
        self._pre = precondition
        self._post = postcondition
        self._func = function

    def __call__(self, *args, **kwargs):
        precondition = self._pre
        postcondition = self._post

        if precondition:
            precondition(*args, **kwargs)
        result = self._func(*args, **kwargs)
        if postcondition:
            postcondition(result, *args, **kwargs)
        return result


def __test():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    __test()

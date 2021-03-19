"""
Definition Imported from
https://wiki.python.org/moin/PythonDecoratorLibrary#Pre-.2FPost-Conditions
"""

import functools
import logging as log

# For preconditions prefer using individual asserts
# For postcondition use the decorator

__all__ = ['postcondition', 'condition']  # 'precondition',

# Ignoring precondition for now
# Using assert statements for now

# def precondition(predicate):
#     """
#     PreCondition decorator
#     """
#     log.debug("Creating a precondition for %s", predicate)
#     return condition(pre_predicate=predicate)


def postcondition(predicate):
    """
    PostCondition decorator
    """
    log.debug("Creating a postcondition for %s", predicate)
    return condition(post_predicate=predicate)


def condition(pre_predicate=None, post_predicate=None):
    """
    condition decorator
    """
    def decorator(func):
        # presever name, docstring, etc
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # NOTE: no self
            if pre_predicate is not None:
                log.debug("Calling precondition for %s", str(func))
                assert pre_predicate(*args, **kwargs)

            # call original function or method
            log.debug("Calling function %s", str(func))
            result = func(*args, **kwargs)

            if post_predicate is not None:
                log.debug("Calling postcondition for %s", str(func))
                assert post_predicate(result)

            return result
        return wrapper
    return decorator

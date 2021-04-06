# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

import logging as log
import time

from algo.egg_dropping import egg_dropping


class TestEggDropping:
    """
    A Test Suite for egg_dropping
    """

    def test_empty(self):
        # assert egg_dropping(2, 6) == 3
        start = time.process_time()
        assert egg_dropping(4, 1000) == 13
        end = time.process_time()
        log.info('Took %s to complete egg dropping', (end - start))

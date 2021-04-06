# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

import logging as log
import time

from algo.egg_dropping_lc import Solution


class TestEggDropping:
    """
    A Test Suite for egg_dropping
    """

    def test_empty(self):
        # assert egg_dropping(2, 6) == 3
        s = Solution()
        start = time.process_time()
        assert s.superEggDrop(4, 5000) == 19
        end = time.process_time()
        log.info('Took %s to complete egg dropping', (end - start))

    # def test_empty(self):
    #     # assert egg_dropping(2, 6) == 3
    #     start = time.process_time()
    #     assert superEggDropR(4, 2000) == 16
    #     end = time.process_time()
    #     log.info('Took %s to complete egg dropping', (end - start))

    # def test_empty(self):
    #     # assert egg_dropping(2, 6) == 3
    #     start = time.process_time()
    #     assert egg_dropping(4, 2000) == 16
    #     end = time.process_time()
    #     log.info('Took %s to complete egg dropping', (end - start))

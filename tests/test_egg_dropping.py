# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

import logging as log
import time

from algo.egg_dropping_lc import egg_dropping as eg


class TestEggDropping:  # pylint: disable=too-few-public-methods
    """
    A Test Suite for egg_dropping
    """

    def test_samples(self):
        start = time.process_time()
        assert eg(2, 2) == 2
        assert eg(2, 6) == 3
        assert eg(4, 2000) == 16
        assert eg(4, 5000) == 19
        end = time.process_time()
        log.info('Took %s to complete egg dropping', (end - start))

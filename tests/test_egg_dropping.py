# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

import logging as log
import time

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

import pytest

from algo.egg_dropping import egg_dropping as eg
from algo.egg_dropping_optimized import egg_dropping as ego


class TestEggDropping:  # pylint: disable=too-few-public-methods
    """
    A Test Suite for egg_dropping
    """

    @pytest.mark.skip(reason="Takes 70 seconds to complete")
    def test_original(self):
        start = time.process_time()
        assert eg(2, 2) == 2
        assert eg(2, 6) == 3
        assert eg(4, 2000) == 16
        assert eg(4, 5000) == 19
        end = time.process_time()
        log.info('Took %s to complete egg dropping', (end - start))

    def test_optimized(self):
        start = time.process_time()
        assert ego(2, 2) == 2
        assert ego(2, 6) == 3
        assert ego(4, 2000) == 16
        assert ego(4, 5000) == 19
        end = time.process_time()
        log.info('Took %s to complete egg dropping', (end - start))

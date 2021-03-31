"""
You are a movie star. Given a list of possible movies that you can
act in 2021, find the subset which maximizes your earnings, given that
every movie will fetch you the same amount irrespective of its duration.
The condition, you cannot take up a new movie, without completing the
current movie.
"""

from typing import NamedTuple, List

import logging as log
log.basicConfig(level=log.INFO)

__all__ = ['find_maximum_subset']


class Movie(NamedTuple):
    """
    Movie data type
    """
    name: str
    start: int
    end: int


def find_maximum_subset(movies: List[Movie]) -> List[Movie]:
    """
    Given a list of movies, find the subset which maximizes
    profit, as per the given condition.

    Idea: Choose the movie that ends first. This way the actor
    gets more time to choose the rest of the movies
    """
    # Sort the movies, based on the end date (ascending order)
    movies = sorted(movies, key=lambda movie: movie.end)
    log.debug(movies)

    # begin is the first day when I am free
    begin, result = 1, []

    # reduce this list without any collision
    # resolving towards the movie that ends first
    for m in movies:
        # check if the input is really valid
        # can be turned off if required
        assert m.start <= m.end

        # if start is after (or equal to) begin
        if m.start >= begin:
            result.append(m)
            # the new begin is one day after this movie ends
            begin = m.end + 1

    return result

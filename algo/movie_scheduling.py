"""
You are a movie star. Given a list of possible movies that you can
act in 2021, find the subset which maximizes your earnings, given that
every movie will fetch you the same amount irrespective of its duration.
The condition, you cannot take up a new movie, without completing the
current movie.
"""

from typing import NamedTuple, List


class Movie(NamedTuple):
    """Movie data type"""
    name: str
    start: int
    end: int


def find_maximum_subset(movies: List[Movie]) -> List[Movie]:
    """
    Given a list of movies, find the subset which maximizes
    profit, as per the given condition.

    Idea: Chose the movie that ends first. This way the actor
    gets more time to chose the rest of the movies
    """
    # Sort the movies, based on the end date (ascending order)
    # movies = sorted(movies)

    # reduce this list without any collision
    # resolving towards the movie that ends first

    return movies

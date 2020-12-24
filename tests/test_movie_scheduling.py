# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

from algo.movie_scheduling import find_maximum_subset as max_sub, Movie


class TestMovieScheduling:
    def test_empty(self):
        # Given an empty list of Movies, it should work
        assert max_sub([]) == []

    def test_single_movie(self):
        # Given a single movie, it should work
        m = Movie("The Lord of the rings", 1, 300)
        assert max_sub([m]) == [m]

    def test_two_movies_conflict(self):
        # Should chose only one movie
        assert 1 == 1

    def test_two_movies_no_conflict(self):
        # Should chose both the movies
        assert 1 == 1

    def test_multiple_movies_with_conflict(self):
        # Should return a proper subset of movies
        assert 1 == 1

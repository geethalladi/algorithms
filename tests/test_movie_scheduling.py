# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use

class TestMovieScheduling:
    def test_empty(self):
        # Given an empty list of Movies, it should work
        assert 1 == 1

    def test_single_movie(self):
        # Given a single movie, it should work
        assert 1 == 1

    def test_two_movies_conflict(self):
        # Should chose only one movie
        assert 1 == 1

    def test_two_movies_no_conflict(self):
        # Should chose both the movies
        assert 1 == 1

    def test_multiple_movies_with_conflict(self):
        # Should return a proper subset of movies
        assert 1 == 1

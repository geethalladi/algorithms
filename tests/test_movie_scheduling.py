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
        m1 = Movie("LOTR", 1, 300)
        m2 = Movie("Matrix", 1, 200)
        assert max_sub([m1, m2]) == [m2]

    def test_two_movies_no_conflict(self):
        # Should chose both the movies
        m1 = Movie("LOTR", 1, 200)
        m2 = Movie("Matrix", 201, 300)
        assert max_sub([m1, m2]) == [m1, m2]

    def test_multiple_movies_with_conflict(self):
        # Should return a proper subset of movies

        m1 = Movie("The Lord of the rings", 1, 200)
        m2 = Movie("The Matrix", 30, 150)
        m3 = Movie("Twelve Angry Men", 40, 100)
        m4 = Movie("Harry Potter", 130, 250)
        m5 = Movie("You only live twice", 140, 200)
        m6 = Movie("Hitchhickers guide to the galaxy", 240, 270)
        m7 = Movie("Batman", 300, 350)
        m8 = Movie("X Men", 260, 360)

        assert max_sub([m1, m2, m3, m4, m5, m6, m7, m8]) == [m3, m5, m6, m7]

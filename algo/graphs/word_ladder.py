"""
Solve the word ladder problem
"""
from typing import Sequence

from algo.graphs.igraph import IGraph
from algo.graphs.graph import Graph

from algo.utils.contracts import precondition, postcondition


class WordLadder:
    """
    An ADT to solve the word ladder problem
    """

    words_file: str
    words: Sequence[str]
    graph: IGraph

    @precondition(lambda _s, l, _f='': l >= 3)
    def __init__(self, word_length: int = 4, words_file: str = ''):
        self.word_length = word_length
        self.words_file = words_file

        if self.is_valid_file(self.words_file):
            self.words = self.__get_words()
            self.__construct(self.words_file)
            self.add_words(self.__get_words())

    @classmethod
    def is_valid_file(cls, file: str):
        """
        Check if the file is indeed valid
        """
        return len(file) > 0

    def __get_words(self) -> Sequence[str]:
        """
        Populate the words from the contents of the file
        """
        return [self.words_file]

    def __construct(self, name: str):
        """
        Construct an undirected graph of words
        which differ in a single character
        """
        self.graph = Graph(name, directed=False)

    def add_words(self, words: Sequence[str]):
        """
        Add the words and construt the graph
        """
        self.words = words
        self.__construct(self.words_file or 'test_graph')

    @postcondition(lambda x: len(x) >= 0)
    def solution(self, start: str, end: str) -> Sequence[str]:
        """
        Find the solution between the start word and the end word
        """
        return [start, end]

#!/usr/bin/env python3
# coding: utf-8

from typing import FrozenSet
from typing import Generic
from typing import Tuple
from typing import TypeVar
from typing_extensions import Protocol

import parsing

from parsing import ling
from parsing import math

A = TypeVar('A')
L = TypeVar('L')


class Parser(Generic[A, L]):
    def parse(self, sentence: 'ling.Sentence[A]') -> 'parsing.Graph[A, L]':
        pass


class State(Generic[A, L]):
    @staticmethod
    def initial(sentence: 'ling.Sentence[A]') -> 'State[A, L]':
        def create_token(x: Tuple[int, 'ling.Word[A]']) -> 'ling.Token[A]':
            word, index = x
            return ling.Token(index, word)

        token_root: 'ling.Token[A]' = ling.Token(ling.Root, 0)

        return State(
            tuple([token_root]), tuple(map(create_token, enumerate(sentence))),
            frozenset())

    def __init__(self, stack: Tuple['ling.Token[A]', ...],
                 queue: Tuple['ling.Token[A]', ...],
                 edges: FrozenSet['parsing.Edge[A, L]']) -> None:
        self.__stack = stack
        self.__queue = queue
        self.__edges = edges

    @property
    def stack(self) -> Tuple['ling.Token[A]', ...]:
        return self.__stack

    @property
    def queue(self) -> Tuple['ling.Token[A]', ...]:
        return self.__queue

    @property
    def arcs(self) -> FrozenSet['parsing.Edge[A, L]']:
        return self.__edges

    @property
    def is_terminal(self) -> bool:
        return len(self.__queue) == 0

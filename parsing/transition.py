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
    def parse(
        self,
        sentence: 'ling.Sentence[A]'
    ) -> 'parsing.DependencyGraph[A, L]':
        pass


class State(Generic[A, L]):
    def __init__(
        self,
        stack: Tuple['ling.Token[A]', ...],
        queue: Tuple['ling.Token[A]', ...],
        arcs: FrozenSet['math.DirectedEdge[ling.Token[A], L]']
    ) -> None:
        self.__stack = stack
        self.__queue = queue
        self.__arcs = arcs

    @property
    def stack(self) -> Tuple['ling.Token[A]', ...]:
        return self.__stack

    @property
    def queue(self) -> Tuple['ling.Token[A]', ...]:
        return self.__queue

    @property
    def arcs(self) -> FrozenSet['math.DirectedEdge[ling.Token[A], L]']:
        return self.__arcs

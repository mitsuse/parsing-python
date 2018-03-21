#!/usr/bin/env python3
# coding: utf-8

from typing import FrozenSet
from typing import Generic
from typing import Tuple
from typing import TypeVar
from typing_extensions import Protocol

import parsing 


A = TypeVar('A')
L = TypeVar('L')


class Parser(Generic[A, L]):
    def parse(
        self,
        sentence: Tuple[parsing.Word[A], ...]
    ) -> parsing.DirectedGraph[parsing.Token[A], L]:
        pass


class State(Generic[A, L]):
    def __init__(
        self,
        stack: Tuple[parsing.Token[A], ...],
        queue: Tuple[parsing.Token[A], ...],
        arcs: FrozenSet[parsing.DirectedEdge[parsing.Token[A], L]]
    ) -> None:
        self.stack = stack
        self.queue = queue
        self.arcs = arcs

#!/usr/bin/env python3
# coding: utf-8

from typing import FrozenSet
from typing import Generic
from typing import TypeVar
from typing_extensions import Protocol


V = TypeVar('V')
L = TypeVar('L')


class DirectedGraph(Protocol[V, L]):
    def vertices(self) -> FrozenSet[V]: ...
    def edges(self) -> FrozenSet['DirectedEdge[V, L]']: ...


class DirectedEdge(Generic[V, L]):
    def __init__(self, start: V, end: V, label: L) -> None:
        self.__start = start
        self.__end = end
        self.__label = label

    @property
    def start(self) -> V:
        return self.__start

    @property
    def end(self) -> V:
        return self.__end

    @property
    def label(self) -> L:
        return self.__label

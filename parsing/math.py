#!/usr/bin/env python3
# coding: utf-8

from typing import FrozenSet
from typing import Generic
from typing import TypeVar

V = TypeVar('V')
L = TypeVar('L')


class DirectedGraph(Generic[V, L]):
    def __init__(self, vertices: FrozenSet['V'],
                 edges: FrozenSet['DirectedEdge[V, L]']) -> None:
        self.__verticies = vertices
        self.__edges = edges

    @property
    def vertices(self) -> FrozenSet[V]:
        return self.__verticies

    @property
    def edges(self) -> FrozenSet['DirectedEdge[V, L]']:
        return self.__edges


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

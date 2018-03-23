#!/usr/bin/env python3
# coding: utf-8

from typing import FrozenSet
from typing import Generic
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union
from typing_extensions import Protocol


A = TypeVar('A')
V = TypeVar('V')
L = TypeVar('L')


class Word(Generic[A]):
    def __init__(self, surfcace: str, attributes: A) -> None:
        self.__surface = surfcace
        self.__attributes = attributes

    @property
    def surface(self) -> str:
        return self.__surface

    @property
    def attributes(self) -> A:
        return self.__attributes


def word(surface: str) -> 'Word[None]':
    return Word(surface, None)


Sentence = Tuple['Word[A]', ...]


class Root: pass


class Terminal: pass


Symbol = Union[Type[Root], Type[Terminal], Word[A]]


class Token(Generic[A]):
    def __init__(self, symbol: 'Symbol[A]', index: int) -> None:
        self.__symbol = symbol
        self.__index = index

    @property
    def symbol(self) -> 'Symbol[A]':
        return self.__symbol

    @property
    def index(self) -> int:
        return self.__index


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


DependencyGraph = DirectedGraph['Token[A]', L]


class Parser(Protocol[A, L]):
    def parse(self, sentence: 'Sentence[A]') -> DependencyGraph[A, L]: ...

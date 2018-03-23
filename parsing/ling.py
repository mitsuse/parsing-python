#!/usr/bin/env python3
# coding: utf-8

from typing import Generic
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union


A = TypeVar('A')


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

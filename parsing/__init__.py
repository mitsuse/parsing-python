#!/usr/bin/env python3
# coding: utf-8

from typing import Generic
from typing import TypeVar


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


def word(surface: str) -> Word[None]:
    return Word(surface, None)


class Token(Generic[A]):
    def __init__(self, word: Word[A], index: int) -> None:
        self.__word = word
        self.__index = index

    @property
    def word(self) -> Word[A]:
        return self.__word

    @property
    def index(self) -> int:
        return self.__index

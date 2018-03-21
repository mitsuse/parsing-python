#!/usr/bin/env python3
# coding: utf-8

from typing import List
from typing import NewType
from typing import TypeVar

from typing_extensions import Protocol


class Word(Protocol):
    def surface(self) -> str:
        raise NotImplementedError()

#!/usr/bin/env python3
# coding: utf-8

from typing import Generic
from typing import TypeVar
from typing_extensions import Protocol

from parsing import ling
from parsing import math


A = TypeVar('A')
L = TypeVar('L')


DependencyGraph = math.DirectedGraph['ling.Token[A]', L]


class Parser(Protocol[A, L]):
    def parse(self, sentence: 'ling.Sentence[A]') -> DependencyGraph[A, L]: ...

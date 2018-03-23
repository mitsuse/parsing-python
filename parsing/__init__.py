#!/usr/bin/env python3
# coding: utf-8

from typing import Generic
from typing import TypeVar
from typing_extensions import Protocol

from parsing.ling import Sentence
from parsing.ling import Token
from parsing.math import DirectedEdge
from parsing.math import DirectedGraph


A = TypeVar('A')
V = TypeVar('V')
L = TypeVar('L')


DependencyGraph = DirectedGraph['Token[A]', L]


class Parser(Protocol[A, L]):
    def parse(self, sentence: 'Sentence[A]') -> DependencyGraph[A, L]: ...

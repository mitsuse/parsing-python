#!/usr/bin/env python3

from typing import TypeVar
from typing_extensions import Protocol

I = TypeVar('I', contravariant=True)
L = TypeVar('L', covariant=True)


class Classifier(Protocol[I, L]):
    def classify(self, instance: 'I') -> 'L':
        ...

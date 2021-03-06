#!/usr/bin/env python3 -tt
"""
File: observable.h
------------------
This file defines an abstract superclass named <code>Observable</code> that
allows objects to store lists of observers, which are other objects that are
notified when some part of the state of the observable object changes.
This is an example of the classic Observer/Observable design pattern.
"""
from abc import abstractmethod as _abstractmethod

class Observable():
    def __init__(self):
        self.observers = []

    def add_observer(self, obs):
        if obs not in self.observers:
            self.observers.append(obs)

    def notify_observers(self, *args, **kwargs):
        for obs in self.observers:
            obs.update(self, *args, **kwargs)

    def remove_observer(self, obs):
        if obs in self.observers:
            self.observers.remove(obs)

class Observer():
    @_abstractmethod
    def update(self, obs, *args, **kwargs):
        pass

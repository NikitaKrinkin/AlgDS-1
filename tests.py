import pytest
from lab import CircularDeque

def test_init():
    dq = CircularDeque(3, True)

def test_init_er_1():
    dq = CircularDeque(-3, True)

def test_init_er_2():
    dq = CircularDeque('123', True)

def test_init_er_3():
    dq = CircularDeque(12, 12)

def test_push_front():
    dq = CircularDeque(3, True)
    dq.push_front(14)

def test_push_back():
    dq = CircularDeque(3, True)
    dq.push_back(14)

def test_push_front_er_1():
    dq = CircularDeque(3, True)
    dq.push_front('sas')

def test_push_front_er_2():
    dq = CircularDeque(3, False)
    dq.push_front(12)
    dq.push_front(13)
    dq.push_front(15)
    dq.push_front(14)

def test_pop_front():
    dq = CircularDeque(3, False)
    dq.front()

def test_resize():
    dq = CircularDeque(3, False)
    dq.push_front(12)
    dq.push_front(13)
    dq.push_front(15)
    dq.resize(5)

def test_resize_er_1():
    dq = CircularDeque(3, False)
    dq.push_front(12)
    dq.push_front(13)
    dq.push_front(15)
    dq.resize(-5)

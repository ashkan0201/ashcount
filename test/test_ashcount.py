import os
import sys

path = os.path.join(os.getcwd(), "src")

sys.path.append(path)
from ashcount import counter , py_counter

def tset_counter1():
    assert counter.line_counter(path="text_test.txt") == 4

def tset_counter2():
    assert counter.counting_main_lines(path="text_test.txt") == 2

def tset_counter3():
    assert counter.word_count(path="text_test.txt") == 11

def test_py_counter1():
    assert py_counter.python_line_count(path="python_test.py") == 8

def test_py_counter2():
    assert py_counter.python_comment_count(path="python_test.py") == 2

def test_py_counter3():
    assert py_counter.pure_python_code(path="python_test.py") == 3

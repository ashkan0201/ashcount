import os
import sys

path = os.path.join(os.getcwd(), "src")

sys.path.append(path)

from module.ashcount import counter , py_counter

def tset_counter1():
    assert counter.line_counter(path="./test/text_test.txt") == 4

def tset_counter2():
    assert counter.counting_main_lines(path="./test/text_test.txt") == 2

def tset_counter3():
    assert counter.word_count(path="./test/text_test.txt") == 11

def tset_counter4():
    assert py_counter.python_line_count(path="./test/python_test.py") == 8

def tset_counter5():
    assert py_counter.python_comment_count(path="./test/python_test.py") == 2

def tset_counter6():
    assert py_counter.pure_python_code(path="./test/python_test.py") == 3

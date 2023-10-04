import os
import sys

path = os.path.join(os.getcwd(), "src")

sys.path.append(path)

from module.ashcount import counter , py_counter

def tset_counter1():
    assert counter.line_counter(path="./src/t_t.txt") == 4

def tset_counter2():
    assert counter.counting_main_lines(path="./src/t_t.txt") == 2

def tset_counter3():
    assert counter.word_count(path="./src/t_t.txt") == 11

def tset_counter4():
    assert py_counter.python_line_count(path="./src/p_t.py") == 8

def tset_counter5():
    assert py_counter.python_comment_count(path="./src/p_t.py") == 2

def tset_counter6():
    assert py_counter.pure_python_code(path="./src/p_t.py") == 3

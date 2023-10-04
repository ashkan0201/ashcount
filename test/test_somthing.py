import os
import sys

path = os.path.join(os.getcwd(), "src")

sys.path.append(path)

from module.ashcount import counter , py_counter

def test_counter1():
    assert counter.line_counter("./Testing_Files/Temp.txt") == 4

def test_counter2():
    assert counter.counting_main_lines(path="./Testing_Files/Temp.txt") == 2

def test_counter3():
    assert counter.word_count(path="./Testing_Files/Temp.txt") == 11

def test_counter4():
    assert py_counter.python_line_count(path="./Testing_Files/Temp.py") == 8

def test_counter5():
    assert py_counter.python_comment_count(path="./Testing_Files/Temp.py") == 2

def test_counter6():
    assert py_counter.pure_python_code(path="./Testing_Files/Temp.py") == 3

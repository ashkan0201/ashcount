import os
import sys

path = os.path.join(os.getcwd(), "src")

sys.path.append(path)

from module.ashcount import counter , py_counter

def tset_counter1():
    assert counter.line_counter(path="./Testing_Files/Temp.txt") == 4

# def tset_counter2():
#     assert counter.counting_main_lines(path="./Testing_Files/Temp.txt") == 2

# def tset_counter3():
#     assert counter.word_count(path="./Testing_Files/Temp.txt") == 11

# def tset_py_counter4():
#     assert py_counter.python_line_count(path="./Testing_Files/Temp.py") == 8

# def tset_py_counter4():
#     assert py_counter.python_comment_count(path="./Testing_Files/Temp.py") == 2

# def tset_py_counter4():
#     assert py_counter.pure_python_code(path="./Testing_Files/Temp.py") == 3

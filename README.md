
# ashcount

**This package helps you to get some information from the files.**

- Find the number of lines in a file
- Find the number of original lines in a file
- Find the word count of a file
- Find the number of codes in a Python file
- Find the net code count of a Python file
- Find the number of comments in a Python file

You can find the above items using this package.

## How to use modules
It is very easy to use modules, now we will give some examples.
The output will be a number in all modes.

First, we import the `counter` from `ashcount`
```python
from ashcount import counter
```

The files you use for it must have their addresses to avoid problems!
```python
Txt_file_address = 'example.txt'
Python_file_address = 'example.py'
```

For example, to find the number of `lines` in a `txt` file.
```python
print(counter.line_counter(path=Txt_file_address))
```

To get the number of `main lines` of a `txt` file.

In this section, we do not consider `lines` that are empty or only have extra spaces.
```python
print(counter.counting_main_lines(path=Txt_file_address))
```

To find the number of `words` in a `txt` file.
```python
print(counter.word_count(path=Txt_file_address))
```

For the part where you want to work with `Python` files, you must import `py_counter` from `ashcount`.
```python
from ashcount import py_counter
```

And also to find the number of `codes` in a `python` file.
```python
print(py_counter.python_line_count(path=Python_file_address))
```

To find the net number of `codes` in a `Python` file.

In this section, we do not consider `comments` and `lines` that do not have any code, and we will give you the net number of a code.
```python
print(py_counter.pure_python_code(path=Python_file_address))
```

And finally, to find the number of `comments` in a `Python` file.
```python
print(py_counter.python_comment_count(path=Python_file_address))
```

## Ways of communication

Contact me in case of problems.

- ashkan02011@gmail.com
- [github](https://github.com/ashkan0201)


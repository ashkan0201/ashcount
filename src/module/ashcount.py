"""
A set of things that can be done with files.
For example, 
* Finding the number of lines in a file
* Find the number of words
* Find the net code count of a Python file
* And ...
"""

class counter:
    def __init__(self) -> None:
        pass

    def line_counter(path:str) -> int:
        """       
        Be sure to enter an address that exists!
        Counts all the lines of a file.
        """
        with open(path, "r") as file:
            data = file.readlines()
        if "\n" in data[-1]:
            return len(data) + 1
        else:
            return len(data)

    def counting_main_lines(path:str) -> int:
        """
        Be sure to enter an address that exists!
        Counts all main lines.
        """
        with open(path, "r") as file:
            data1 = file.readlines()
        data2= []
        index1 = 0
        index2 = 0
        for everything in data1:
            if everything == "\n":
                index1 += 1
        for everything in data1:
            if "\n" in everything:
                data2.append(everything.replace("\n",""))
            else:
                data2.append(everything)
        for everything in data2:
            if everything.isspace():
                index2 += 1
        return len(data1) - index1 - index2

    def word_count(path:str) -> int:
        """
        Be sure to enter an address that exists!
        Counts all the words of a file.
        """
        with open(path, "r") as file:
            data = file.read()
        data = data.replace(" ", "\n")
        data = data.split("\n")
        index = 0
        for everything in data:
            if everything == "":
                index += 1
        return len(data) - index

class py_counter:
    def __init__(self) -> None:
        pass

    def python_line_count(path:str) -> int:
        """
        Be sure to enter an address that exists!
        Count all lines of a Python file.
        """
        with open(path, "r") as file:
            data = file.readlines()
        if "\n" in data[-1]:
            return len(data) + 1
        else:
            return len(data)

    def python_comment_count(path:str) -> int:
        """
        Be sure to enter an address that exists!
        Counts the commits of a Python file.
        """
        with open(path, "r") as file:
            data = file.readlines()
        index1 = 0
        index2 = 0
        for everything in data:
            if "#" in everything:
                index1 += 1
            elif  '"""' in  everything:
                index2 += 1
        if index2 != 0:
            index2 = index2 // 2
        return index1 + index2
    
    def pure_python_code(path:str) -> int:
        """
        Be sure to enter an address that exists!
        Counts the main lines of code.
        """
        with open(path, 'r') as file:
            lines = file.readlines()
        index = 0
        in_multiline_comment = False
        for line in lines:
            stripped_line = line.strip()
            if not in_multiline_comment and stripped_line and not stripped_line.startswith('#') and not stripped_line.startswith('"""'):
                index += 1
            if '"""' in line:
                in_multiline_comment = not in_multiline_comment
        return index

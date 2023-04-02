# code_to_python.py

import re

def convert_line(line):
    if line.startswith("memory"):
        return line.replace(" = ", " = \"") + "\""
    elif line.startswith("def"):
        return "def " + line[4:]
    elif line.startswith("for"):
        return "    for " + line[4:]
    elif line.startswith("return"):
        return "    return " + line[7:]
    else:
        return None

def code_to_python(input_file, output_file):
    with open(input_file, "r") as code_file, open(output_file, "w") as py_file:
        for line in code_file:
            if line.startswith("#"):
                py_file.write(line)
            else:
                converted_line = convert_line(line.strip())
                if converted_line:
                    py_file.write(converted_line + "\n")

if __name__ == "__main__":
    input_file = "brain.CODE"
    output_file = "brain.py"
    code_to_python(input_file, output_file)

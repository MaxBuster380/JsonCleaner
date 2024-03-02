import sys
import re
import json

INDENTATION_STRING = "\t"

############################## READ COMMAND ##############################

command_arguments = sys.argv
if (len(command_arguments) != 2):
    raise Exception("Invalid argument count : expected 1")

file_name = command_arguments[1]

if (file_name[-5:len(file_name)] != ".json"):
    raise Exception("\""+file_name+"\" is not a JSON file.")

############################### READ FILE ################################

file = open(file_name, 'r')
text = file.read()
file.close()

try:
    json.loads(text)
except Exception:
    raise Exception("Invalid JSON format.")

def new_line(indentation : int) -> str:
    return "\n" + INDENTATION_STRING * indentation

res = ""

ignore_next_character = False
in_string = False
indentation = 0
for i in range(len(text)):
    char = text[i]
    if (i < len(text)-1):
        next_char = text[i+1]

    if (ignore_next_character):
        ignore_next_character = False
        continue

    if (not in_string and re.match(r"\s", char) != None):
        continue

    if (char == '"'):
        in_string = not in_string

    if (char == '\\' and in_string):
        ignore_next_character = True
        res += char
        continue

    if (in_string):
        res += char
        continue

    match char:
        
        case '{':
            if (next_char == '}'):
                ignore_next_character = True
                res += "{}"
            else:
                indentation += 1
                res += "{" + new_line(indentation)
        
        case '[':
            if (next_char == ']'):
                ignore_next_character = True
                res += "[]"
            else:
                indentation += 1
                res += "[" + new_line(indentation)
        
        case '}':
            indentation -= 1
            res += new_line(indentation) + "}"
        
        case ']':
            indentation -= 1
            res += new_line(indentation) + "]"

        case ',':
            res += "," + new_line(indentation)

        case ':':
            res += ": "
            
        case _:
            res += char

file = open(file_name, 'w')
text = file.write(res)
file.close()
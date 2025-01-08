#!/usr/bin/python3

import sys

# print(dir(sys))

print(sys.version)
print(sys.version_info)
# print(sys.modules)            # Modules that are imported in this function
# print(sys.path)               # Paths where all the libraries are imported from | sys.path is like env variable of python
sys.exit()                      # Exits the interpreter
print(f'Print after sys.exit')

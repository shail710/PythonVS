# need to import Path class from pathlib module
from pathlib import Path

# # ways of creating path
# # create absolute path for Windows
# Path("C:\\Users\\sshah3\\Pictures")
# # we can simplify above path using rawstring so that we don't need to use double \
# Path(r"C:\Users\sshah3\Pictures")
# # create absolute path for linux or mac
# Path("/usr/local/bin")
# # this is a path object which returns the current folder
# Path()
# # relative path
# Path('pythonstandardlib/__init__')
# # we can combine path with strings too
# Path() / 'pythonstandardlib' / '__init__'
# # we can get the home home directory of a current user
# Path.home()


path = Path('python_standard_lib/__init__.py')
print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
# over rides just the name of the file and returns the path
path = path.with_name('file.txt')
# returns the absolute path
print(path)
print(path.absolute())
# over rides the suffix
path = path.with_suffix('.py')
print(path)


# Output:
# True
# True
# False
# __init__.py
# __init__
# .py
# python_standard_lib
# python_standard_lib\file.txt
# c:\Users\sshah3\Desktop\Python\python_standard_lib\file.txt
# python_standard_lib\file.py

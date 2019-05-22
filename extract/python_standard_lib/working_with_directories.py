from pathlib import Path
path = Path('python_standard_lib')

# following are the basic method to remember
# print(path.exists())
# path.mkdir()
# path.rmdir()
# path.rename('')
# iterdir() returns generator object
print(path.iterdir())
# Output: <generator object Path.iterdir at 0x0000000004D9C1B0>


# we can iterate over directory and it will return the list of the files
for p in path.iterdir():
    print(p)
    # output of for loop
    # python_standard_lib\working_with_directories.py
    # python_standard_lib\working_with_paths.py
    # python_standard_lib\__init__.py

# we can use comprehension to get this path
paths = [p for p in path.iterdir()]
print(paths)
#Output: [WindowsPath('python_standard_lib/working_with_directories.py'), WindowsPath('python_standard_lib/working_with_paths.py'), WindowsPath('python_standard_lib/__init__.py')]

# Path class is a base path for WindowsPath class and PosixPath Class
# Posix and windows are standards used in unix and windows operating sys respectively

# we can get only the list of dir as well
paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)
#Output; [WindowsPath('python_standard_lib/sample_dir')]

# iterdir() has 2 limitations
# 1 --> we cannot search by pattern
# 2 --> it does not search recursively

# glob() is solution to above issues
# glob() also return generator object
py_files = [p for p in path.glob('*.py')]
print(py_files)
#Output: [WindowsPath('python_standard_lib/working_with_directories.py'), WindowsPath('python_standard_lib/working_with_paths.py'), WindowsPath('python_standard_lib/__init__.py')]


# but this glob() does not search recursively.
# we should change the pattern to path.glob("**/*.py")
# or we can use rglob()
py_files = [p for p in path.rglob("*.py")]
print(py_files)
# this will get all the *.py files from the path dir and all its child dir too
# Output:
# [WindowsPath('python_standard_lib/working_with_directories.py'),
#     WindowsPath('python_standard_lib/working_with_paths.py'),
#     WindowsPath('python_standard_lib/__init__.py'),
#     WindowsPath('python_standard_lib/sample_dir/sample.py'),
#     WindowsPath('python_standard_lib/sample_dir/__init__.py')]

from pathlib import Path
from time import ctime
import shutil
path = Path('python_standard_lib/__init__.py')
# #returns boolean if it exsists or not
# path.exists()
# #we can rename the file
# path.rename('')
# #delete the file
# path.unlink()

# returns stat_result object with all the details about the file
print(path.stat())
# Output:
# os.stat_result(st_mode=33206,
# st_ino=1970324837273689,
# st_dev=378002598, st_nlink=1, st_uid=0,
# st_gid=0, st_size=0,
# st_atime=1558546439, st_mtime=1558546443, st_ctime=1558546439)

# the time mentioned on above output is in seconds and calculated from the epic
# this is platform dependent
# for example, in unix epic time is 1st January 1970

# to get this time in human language, we need to import Ctime from time module

# following line will returnt he creation time of the file
print(ctime(path.stat().st_ctime))
# Output: Wed May 22 13:33:59 2019

print(path.read_text())
# Output: print('initiated')

# write methods are also available
# path.write_text('')
# we can copy a file using path objec

source = Path('python_standard_lib/__init__.py')
target = Path() / '__util__.py'

# to copy above file we need to read the text from the source and write it to the target

target.write_text(source.read_text())


# better way is to use shutil module
shutil.copy(source, target)

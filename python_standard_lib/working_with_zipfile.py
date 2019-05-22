from pathlib import Path
from zipfile import ZipFile

# ZipFile() will create a new zip file, 'w' will allow us to write the to the zipfile
# since we want to close the file after writing to it, we are using with keyword


# with ZipFile('zipfile.zip', 'w') as zip:
#     for path in Path('python_standard_lib').rglob('*.*'):
#         zip.write(path)


# namelist() will list out all the file names exsist in the zip file
with ZipFile('zipfile.zip') as zip:
    print(zip.namelist())
    # we can access the information of any file in the zipfile.
    info = zip.getinfo('python_standard_lib/working_with_directories.py')
    print(info.file_size)
    print(info.compress_size)
    # we can extract all files from the zip file as well
    zip.extractall('extract')
# output:
# ['python_standard_lib/working_with_directories.py',
#     'python_standard_lib/working_with_files.py',
#     'python_standard_lib/working_with_paths.py',
#     'python_standard_lib/working_with_zipfile.py',
#     'python_standard_lib/__init__.py',
#     'python_standard_lib/sample_dir/sample.py',
#     'python_standard_lib/sample_dir/__init__.py']
#      2238
#      2238

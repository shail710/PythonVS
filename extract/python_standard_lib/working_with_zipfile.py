from pathlib import Path
from zipfile import ZipFile

# ZipFile() will create a new zip file, 'w' will allow us to write the to the zipfile
# since we want to close the file after writing to it, we are using with keyword
with ZipFile('zipfile.zip', 'w') as zip:
    for path in Path('python_standard_lib').rglob('*.*'):
        zip.write(path)

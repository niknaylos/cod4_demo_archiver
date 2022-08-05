import re
from pathlib import Path as path
from datetime import date
import py7zr

cdate = date.today()
p1 = 'path/to/demos' + '/'
p = path(p1)
temp = 'path/to/move/demos' + '/'
arch_name = str(cdate) + '.7z'
output_folder = 'path/to/save/archives' + '/'
z = 1
while path(output_folder + arch_name).is_file():
    arch_name = str(cdate) + '_' + str(z) + '.7z'
    z += 1
p2 = path(temp)
for i in p.iterdir():
    if i.is_file():
        if re.fullmatch(r'\bdemo\d{4}', i.stem):
            path(p1 + i.stem + '.dm_1').rename(temp + i.stem + '.dm_1')

with py7zr.SevenZipFile(output_folder + arch_name, 'w') as archive:
    archive.writeall(temp, 'demos')
for i in p2.iterdir():
    if i.is_file():
        if re.fullmatch(r'\bdemo\d{4}', i.stem):
            rem_file = path(temp + i.stem + '.dm_1')
            rem_file.unlink()
print('Archiving is done')

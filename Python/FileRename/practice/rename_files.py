import os

os.chdir('/Users/juan/GIT/TIL/Python/FileRename/practice/dummy')

filenames = os.listdir('.')

for filename in filenames:
    # os.rename(filename, f'SAMSUNG_{filename}')
    new_filename = filename.replace('SAMSUNG_', 'SSAFY_')
    os.rename(filename, new_filename)
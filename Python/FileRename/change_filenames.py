import os

os.chdir('/Users/Juan/GIT/TIL/Python/FileRename')

filenames = os.listdir('.')

for filename in filenames:
    os.rename(filename, f'SAMSUNG_{filename}')
    # os.rename(filename, filename.replace('SAMSUNG_','SSAFY_'))
    # txt = os.path.splitext(filename)[-1].lower()
    # if txt == '.txt':
        # os.rename(filename, f'SAMSUNG_{filename}')
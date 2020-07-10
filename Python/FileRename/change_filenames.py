import os   # python으로 운영체제(operating system)에 접근하기 위한 모듈

os.chdir('/Users/Juan/GIT/TIL/Python/FileRename/dummy')   # 작업 경로 변경

filenames = os.listdir('.')    # 현재 경로('.')안에 있는 파일들을 리스트에 담기

for filename in filenames:
    os.rename(filename, f'SAMSUNG_{filename}')    # 모든 파일명 앞에 'SAMSUNG_' 추가
    # os.rename(filename, filename.replace('SAMSUNG_','SSAFY_'))    # SAMSUNG_ -> SSAFY_ 로 변경
    # txt = os.path.splitext(filename)[-1].lower()    # .txt 파일명만 'SAMSUNG_' 추가
    # if txt == '.txt':
        # os.rename(filename, f'SAMSUNG_{filename}')
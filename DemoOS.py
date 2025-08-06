# DemoOS.py
from os.path import *
from os import *
import glob
import os
import shutil


fName = "sample.txt " 
print(abspath(fName))
print(basename(r"c:\work\text.txt"))

if (exists(r"c:\python310\python.exe")):
    print(getsize(r"c:\python310\python.exe")) # 파일 크기
else:
    print("파일이 없음")


print("운영체제명:", name)
print("환경변수:", environ)
system("notepad.exe")  # 메모장 실행

print(glob.glob("*.py"))  # 현재 디렉토리의 모든 파이썬 파일 목록
for item in glob.glob("*.py"):
    print(item)

# 다운로드 폴더 경로
download_dir = r"C:\Users\student\Downloads"

# 이동할 폴더 경로
dest_dirs = {
    "images": ["*.jpg", "*.jpeg"],
    "data": ["*.csv", "*.xlsx"],
    "docs": ["*.txt", "*.doc", "*.pdf"],
    "archive": ["*.zip"]
}

# 폴더 생성
for folder in dest_dirs.keys():
    target_path = os.path.join(download_dir, folder)
    if not os.path.exists(target_path):
        os.makedirs(target_path)

# 파일 이동
for folder, patterns in dest_dirs.items():
    for pattern in patterns:
        files = glob.glob(os.path.join(download_dir, pattern))
        for file_path in files:
            file_name = os.path.basename(file_path)
            dest_path = os.path.join(download_dir, folder, file_name)
            shutil.move(file_path, dest_path)
            print(f"{file_name} → {folder}")



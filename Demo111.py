import os
import shutil
from pathlib import Path

# 다운로드 폴더 경로
download_dir = Path(r"C:\Users\student\Downloads")

# 이동할 폴더 경로 (다운로드 폴더 하단에 생성)
folders = {
    "images": ["*.jpg", "*.jpeg"],
    "data": ["*.csv", "*.xlsx"],
    "docs": ["*.txt", "*.doc", "*.pdf"],
    "archive": ["*.zip"]
}

# 폴더 생성
for folder in folders:
    target_path = download_dir / folder
    target_path.mkdir(exist_ok=True)

# 파일 이동
for folder, patterns in folders.items():
    target_path = download_dir / folder
    for pattern in patterns:
        for file_path in download_dir.glob(pattern):
            # 이미 분류 폴더에 있는 파일은 건너뜀
            if file_path.parent == target_path:
                continue
            try:
                shutil.move(str(file_path), str(target_path / file_path.name))
                print(f"{file_path.name} → {target_path}")
            except Exception as e:
                print(f"오류: {file_path.name} 이동 실패 - {e}")
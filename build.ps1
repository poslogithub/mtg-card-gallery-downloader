PyInstaller --onefile --icon "src\icon.ico" --version-file "src\file_version_info.txt" --noconfirm --clean "src\downloader.py"
Copy-Item -Path "src\readme.txt" -Destination "dist"
Copy-Item -Path "LICENSE" -Destination "dist"

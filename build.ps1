Remove-Item -Path dist\*
PyInstaller --onefile --icon "src\icon.ico" --version-file "src\file_version_info.txt" --noconfirm --clean "src\downloader_file.py"
Copy-Item -Path "*.url" -Destination "dist"
Copy-Item -Path "LICENSE" -Destination "dist"
Compress-Archive -Path "dist\*" -DestinationPath "dist\mtg-card-gallery-file-downloader.zip"

Remove-Item -Path dist\*
PyInstaller --onefile --icon "src\icon.ico" --version-file "src\file_version_info_downloader.txt" --noconfirm --clean "src\downloader.py"
Copy-Item -Path "*.url" -Destination "dist"
Copy-Item -Path "LICENSE" -Destination "dist"
Compress-Archive -Path "dist\*" -DestinationPath "dist\mtg-card-gallery-downloader.zip"

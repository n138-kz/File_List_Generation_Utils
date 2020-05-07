@echo off
"C:\Users\%Username%\AppData\Local\Programs\Python\Python38-32\Scripts\pyinstaller.exe" core.py -F --onefile --icon core.ico
timeout 1

rmdir /S /Q __pycache__
rmdir /S /Q build
del /S /Q *.spec
timeout 5

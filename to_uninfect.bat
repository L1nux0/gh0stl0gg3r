taskkill /f /im ".exe"
del /q C:\Users\Public\Libraries\updat.exe
reg delete HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run /v updat  /f
cls
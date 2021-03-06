import os
import time
from time import strftime, localtime


class Log:
    DEFAULT_DIR = os.path.dirname(__file__)
    DEFAULT_FILE = 'garpr.log'

    fileDir = ""
    fileName = ""
    path = ""
    f = None

    def __init__(self, fileDir, fileName):
        if fileDir:
            self.fileDir = fileDir
        else:
            self.fileDir = self.DEFAULT_DIR

        if fileName:
            self.fileName = fileName
        else:
            self.fileName = self.DEFAULT_FILE
        self.path = os.path.join(self.fileDir, self.fileName)

    def write(self, msg):
        self.f = open(self.path, 'a')
        logtime = str(time.strftime("%Y-%m-%d %H:%M:%S", localtime()))
        self.f.write(logtime + " | " + msg + "\n")
        self.f.close()

    #@staticmethod
    #def log(message):
    #    l = Log(None, None)
    #    l.write(message)

    @staticmethod
    def log(module, message):
        l = Log(None, None)
        if module is not None:
            l.write('['+module+'] '+message)
        else:
            l.write(message)
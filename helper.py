import sublime
import os
import hashlib
import sys

# read content from a file
def readFile(path):
    f = open(path, "r")
    content = f.read()
    f.close()
    return content

# write content to a file
def writeFile(path, content):
    f = open(path, "w+")
    f.write(content)
    f.close()

# check file extention
def checkFileExt(file,ext):
    ext1 = os.path.splitext(file)[1][1:]
    if ext1 == ext:
        return True
    else:
        return False

def md5(str):
    return hashlib.md5(str.encode(sys.getfilesystemencoding())).hexdigest()

def isST3():
    return sublime.version()[0] == '3'

class CollatedSettings:
    def __init__(self, name):
        self.global_settings = sublime.load_settings(name+".sublime-settings")
        # Per-project settings
        self.local_settings = sublime.active_window().active_view().settings().get(name)

    def get(self, key, default):
        return self.local_settings.get(key, self.global_settings.get(key, default))

def loadSettings(name):
    return CollatedSettings(name)

import shutil
import glob
import os
import subprocess

default_dir = ["DESKTOP", "DOWNLOAD", "TEMPLATES", "PUBLICSHARE", "DOCUMENTS", "MUSIC", "PICTURES", "VIDEOS"]

class Organizer:

    def __init__(self, directories=None):
        # Set self.directories only if a list is passed
        if isinstance(directories, list):
            self.directories = []
            for i in directories:
                if os.path.exists(i) and os.path.isdir(i):
                    self.directories.append(i)
        # Check if a list is passed and make an empty list if not
        elif isinstance(directories, type(None)):
            self.directories = []
        else:
            raise Exception("Error: `directories` must be a list")

        # Execute system command to get the paths for the default directories 
        for i in default_dir:
            output = subprocess.check_output(['xdg-user-dir', i])
            output = output.decode("utf-8").rstrip()
            self.directories.append(output)

        print(self.directories)

    def get_directory(self):
        pass

types = [
    {
        'directory': '/home/pi/Documents/',
        'extensions': ['.doc', '.docx', '.log', '.msg', '.odt', '.pages', '.rtf', '.tex', '.txt', '.wpd', '.wps'],
    },
    {
        'directory': '/home/pi/Music/',
        'extensions': ['.aif', '.aac', '.iff', '.m3u', '.m4a', '.mid', '.mp3', '.mpa', '.wav', '.wma'],
    },
    {'directory': '/home/pi/Videos/',
        'extensions': ['.3g2', '.3gp', '.asf', '.avi', '.flv', '.m4v', '.mov', '.mp4', '.mpg', '.rm', '.srt', '.swf', '.vob', '.wmv'],
    },
    {
        'directory': '/home/pi/Pictures/',
        'extensions': ['.3dm', '.3ds', '.max', '.obj', '.bmp', '.dds', '.gif', '.heic', '.jpg', '.png', '.psp', '.pspimage', '.tga', '.thm', '.tif', '.tiff', '.yuv', '.ai', '.eps', '.svg'],
    },
    {
        'directory': '/home/pi/Python/',
        'extensions': ['.egg-info', '.epp', '.oog', '.p', '.p4a', '.pickle', '.pil', '.pth', '.py', '.pyc', '.pyd', '.pyo', '.pyt', '.pyw', '.pyz', '.pyzw', '.rpy', '.ssdf', '.whl', '.yaml'],
    },
]

def move():
    for i in types:
        for file in glob.glob(f"/home/pi/Downloads/*{i['extensions']}"):
            shutil.move(file, i['directory'])
            # print(f'moved {file} to {document_dir}')


if __name__=='__main__':
    li = ["/home/tasos/projects/test/directory-organizer/test", "/home/tasos/downloads"]
    test = Organizer(li)

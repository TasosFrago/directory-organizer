import shutil
import glob
import os
import subprocess

# 'extensions': ['.egg-info', '.epp', '.oog', '.p', '.p4a', '.pickle', '.pil', '.pth', '.py', '.pyc', '.pyd', '.pyo', '.pyt', '.pyw', '.pyz', '.pyzw', '.rpy', '.ssdf', '.whl', '.yaml'],

default_dir = ["DOWNLOAD", "DOCUMENTS", "MUSIC", "PICTURES", "VIDEOS"]

class Organizer:

    def __init__(self, directories=None):
        # Default extensions for every direcory
        default_types = [
            {
                'name': 'DOCUMENTS',
                'directory': '',
                'extensions': ['.doc', '.docx', '.log', '.msg', '.odt', '.pages', '.rtf', '.tex', '.txt', '.wpd', '.wps'],
            },
            {
                'name': 'MUSIC',
                'directory': '',
                'extensions': ['.aif', '.aac', '.iff', '.m3u', '.m4a', '.mid', '.mp3', '.mpa', '.wav', '.wma'],
            },
            {
                'name': 'VIDEOS',
                'directory': '',
                'extensions': ['.3g2', '.3gp', '.asf', '.avi', '.flv', '.m4v', '.mov', '.mp4', '.mpg', '.rm', '.srt', '.swf', '.vob', '.wmv'],
            },
            {
                'name': 'PICTURES',
                'directory': '',
                'extensions': ['.3dm', '.3ds', '.max', '.obj', '.bmp', '.dds', '.gif', '.heic', '.jpg', '.png', '.psp', '.pspimage', '.tga', '.thm', '.tif', '.tiff', '.yuv', '.ai', '.eps', '.svg'],
            },
        ]
        # Find the xdg path for the default directories
        self.default_types = default_types
        for i in self.default_types:
            dir_path = subprocess.check_output(['xdg-user-dir', i['name']]) # Use system call to get the xdg dir path
            dir_path = dir_path.decode("utf-8").rstrip()
            i["directory"] = dir_path

    def get_directory(self):
        pass

    def initialize_config(self):
        with open("config.py", "w+") as config:
            config.write("""
extra_paths = [
    {
        'name': "",
        'directory': "",
        'extensions': "",
    }
]
""")


def move():
    for i in types:
        for file in glob.glob(f"/home/pi/Downloads/*{i['extensions']}"):
            shutil.move(file, i['directory'])
            # print(f'moved {file} to {document_dir}')


if __name__=='__main__':
    li = ["/home/tasos/projects/test/directory-organizer/test", "/home/tasos/downloads"]
    test = Organizer(li)

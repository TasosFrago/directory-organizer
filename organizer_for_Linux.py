import shutil
import glob
import os
import subprocess

homedir = os.path.expanduser("~")
configdir = os.path.join(homedir, ".config")

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
            dir_path = subprocess.check_output(['xdg-user-dir', i['name']]).decode("utf-8").rstrip() # Use system call to get the xdg dir path
            i["directory"] = dir_path

    def get_directory(self):
        pass

    def initialize_config(self):
        config_path = os.path.join(configdir, "directory_organizer")
        config_file = os.path.join(config_path, "config.py")
        config_proj_path = "config.py"
        if os.path.exists(os.path.join(config_path)):
            if os.path.isfile(config_file):
                print("Configuration file already exists")
            else:
                shutil.copyfile(config_proj_path, config_file)
        else:
            os.mkdir(config_path)
            shutil.copyfile(config_proj_path, config_file)


# def move():
#     for i in types:
#         for file in glob.glob(f"/home/pi/Downloads/*{i['extensions']}"):
#             shutil.move(file, i['directory'])
#             # print(f'moved {file} to {document_dir}')


if __name__=='__main__':
    li = ["/home/tasos/projects/test/directory-organizer/test", "/home/tasos/downloads"]
    test = Organizer(li)
    test.initialize_config()

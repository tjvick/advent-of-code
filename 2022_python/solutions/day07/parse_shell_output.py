import re

from solutions import helpers
from solutions.day07.file_system import Directory, File


def parse_shell_output(filename):
    strings = helpers.read_each_line_as_string(filename)

    root_dir = Directory(parent=None, name="/")
    pwd = root_dir

    for string in strings:
        print(string)
        if string.startswith("$"):
            cd_match = re.match(r'\$ cd (.+)', string)
            if cd_match:
                new_pwd = cd_match.group(1)
                if new_pwd == "..":
                    pwd = pwd.parent
                elif new_pwd == "/":
                    pwd = root_dir
                else:
                    pwd = pwd.find_child(new_pwd)
        else:
            dir_match = re.match('dir (.+)', string)
            if dir_match:
                dirname = dir_match.group(1)
                new_dir = Directory(parent=pwd, name=dirname)
                pwd.add_child(new_dir)
            else:
                file_match = re.match(r'(\d+) (.+)', string)
                filesize = int(file_match.group(1))
                filename = file_match.group(2)
                new_file = File(parent=pwd, name=filename, size=filesize)
                pwd.add_child(new_file)

    return root_dir
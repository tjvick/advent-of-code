import numpy as np

from solutions.day07.file_system import FileType, FileSystemNode
from solutions.day07.parse_shell_output import parse_shell_output

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

root_dir = parse_shell_output(filename)


def find_directory_sizes(file_system_node: FileSystemNode):
    dir_sizes = []

    def collect_directory_sizes(child):
        if child.type == FileType.DIRECTORY:
            dir_sizes.append(child.size())

    file_system_node.walk_and_execute(collect_directory_sizes)

    return dir_sizes


directory_sizes = find_directory_sizes(root_dir)

total_size = root_dir.size()
goal = 30000000 - 70000000 + total_size
first_directory_larger_than_goal = [x for x in sorted(directory_sizes) if x > goal][0]

print(first_directory_larger_than_goal)
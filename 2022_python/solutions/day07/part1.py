import numpy as np

from solutions.day07.file_system import FileType, FileSystemNode
from solutions.day07.parse_shell_output import parse_shell_output

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'`

root_dir = parse_shell_output(filename)


def find_directory_sizes(file_system_node: FileSystemNode):
    dir_sizes = []

    def collect_directory_sizes(child):
        if child.type == FileType.DIRECTORY:
            dir_sizes.append(child.size())

    file_system_node.walk_and_execute(collect_directory_sizes)

    return dir_sizes


directory_sizes = find_directory_sizes(root_dir)
small_directories = [size for size in directory_sizes if size <= 100000]
print(sum(small_directories))

from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional


class FileType(Enum):
    FILE = 1
    DIRECTORY = 2


class FileSystemNode(ABC):
    def __init__(self, parent, file_type: FileType, name, size: int = 0):
        self.children: List[FileSystemNode] = []
        self.parent: FileSystemNode = parent
        self.name: str = name
        self.type: FileType = file_type
        self._size = size

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def serialize(self):
        pass

    def walk_and_execute(self, executable):
        executable(self)
        for child in self.children:
            child.walk_and_execute(executable)


class File(FileSystemNode):
    def __init__(self, parent: FileSystemNode, name: str, size: int):
        super().__init__(parent, file_type=FileType.FILE, name=name, size=size)
        self._size = size

    def size(self):
        return self._size

    def serialize(self):
        return self._size


class Directory(FileSystemNode):
    def __init__(self, parent: Optional[FileSystemNode], name: str):
        super().__init__(parent, file_type=FileType.DIRECTORY, name=name, size=0)

    def size(self):
        return sum(child.size() for child in self.children)

    def serialize(self):
        return {child.name: child.serialize() for child in self.children}

    def add_child(self, child):
        self.children.append(child)

    def find_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
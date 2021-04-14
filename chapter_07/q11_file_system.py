from typing import Optional, Dict, Union


class FileSystemNode:
    def __init__(self, path, parent) -> None:
        self.path = path
        self.parent: Optional[FileSystemNode] = parent

    def _absolute_path(self, node):
        if not node.parent:
            return ""  # root node

        prefix = self._absolute_path(node.parent)
        return f"{prefix}/{node.path}"

    def __str__(self) -> str:
        suffix = "/" if isinstance(self, Directory) else ""
        return self._absolute_path(self) + suffix

    def __repr__(self) -> str:
        klass = self.__class__.__name__
        path = str(self)
        return f"{klass}({path})"


class Directory(FileSystemNode):
    def __init__(self, path, parent) -> None:
        super().__init__(path, parent)
        self.children: Dict[str, Union[Directory, File]] = {}


class File(FileSystemNode):
    def __init__(self, path, parent, data) -> None:
        super().__init__(path, parent)
        self.data = data


class FileSystem:
    def __init__(self) -> None:
        self._root = Directory("/", parent=None)
        self._pwd: Directory = self._root

    def pwd(self):
        print(self._pwd)

    def mkdir(self, path):
        if path in self._pwd.children:
            raise RuntimeError("File exists")

        new_dir = Directory(path, self._pwd)
        self._pwd.children[path] = new_dir

    def ls(self):
        for f in self._pwd.children.values():
            print(f)

    def cd(self, path):
        if path == "..":
            if not self._pwd.parent:
                return  # Already in root node

            self._pwd = self._pwd.parent
            return

        if path not in self._pwd.children:
            raise RuntimeError("Not found")

        self._pwd = self._pwd.children[path]

    def mkfile(self, path, contents):
        if path in self._pwd.children:
            raise RuntimeError("File exists")

        new_file = File(path, self._pwd, contents)
        self._pwd.children[path] = new_file

    def rm(self, path):
        # Assume file is at current directory
        if path not in self._pwd.children:
            return

        f = self._pwd.children[path]
        # If it's a dir and not empty, recurse
        if isinstance(f, Directory) and f.children:
            self.cd(f.path)
            for node in list(f.children.values()):
                self.rm(node.path)
            self.cd("..")

        del self._pwd.children[path]


fs = FileSystem()

fs.pwd()
fs.mkdir("dir1")
fs.ls()
fs.cd("dir1")
fs.pwd()
fs.mkfile("file.txt", "File contents")
fs.ls()
fs.rm("file.txt")
fs.mkdir("dir2")
fs.cd("dir2")
fs.mkfile("file_dir2.txt", "File contents")
fs.mkdir("dir3")
fs.cd("..")
fs.mkfile("file_dir1.txt", "File contents")
fs.cd("..")
fs.pwd()
fs.rm("dir1")
fs.ls()

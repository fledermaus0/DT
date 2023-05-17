import os

class FileInfo:
    def __init__(self, file_path):
        self.file_path = file_path
        self.exists = os.path.exists(file_path)
        self.extension = os.path.splitext(file_path)[1]
        self.remembered = False

        


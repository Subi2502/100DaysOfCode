#Implement a context manager for file handling.
print ("\nSubi - Day 42 of #100DaysOfCode\n") 
print("\nImplement a context manager for file handling.\n")

class FileManager:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

file_path = "example.txt"

with FileManager(file_path, 'w') as file:
    file.write("Hello, this is a test.")
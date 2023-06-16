import os

def print_directory_tree(path, prefix=''):
    if os.path.isfile(path):
        print(prefix + '|--', os.path.basename(path))
    elif os.path.isdir(path):
        print(prefix + '|--', os.path.basename(path) + '/')
        prefix += '|   '
        for filename in sorted(os.listdir(path)):
            print_directory_tree(os.path.join(path, filename), prefix)

# Ví dụ sử dụng:
path = "D:\HaiZuka\source"
path.replace("\\", "\\\\")

print_directory_tree(path)

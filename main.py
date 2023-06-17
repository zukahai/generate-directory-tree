import os

ignore = ['.git']
def print_directory_tree(path, prefix='', last_path = ''):
    if os.path.basename(path) in ignore:
        return
    if os.path.isfile(path):
        print(prefix + '|--', os.path.basename(path))
    elif os.path.isdir(path):
        print(prefix + '|--', os.path.basename(path) + '/')
        if os.path.basename(path) == last_path:
            sub_prefix = '   '
        else:
            sub_prefix =  '|   '
        for filename in sorted(os.listdir(path)):
            print_directory_tree(os.path.join(path, filename), prefix + sub_prefix, sorted(os.listdir(path))[-1])

# Ví dụ sử dụng:
path = "F:\CTDA\spring-mvc-starter-master\spring-mvc-starter-master"
path.replace("\\", "\\\\")

print_directory_tree(path, last_path=path.split("\\")[-1])

import os


def print_directory_tree(path, prefix='', last_path = '', ignore = ['.git', 'target']):
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
        list_files = sorted(os.listdir(path))
        # remove file in ignore
        list_files = [file for file in list_files if file not in ignore]
        for filename in list_files:
            print_directory_tree(os.path.join(path, filename), prefix + sub_prefix, list_files[-1], ignore)

# Ví dụ sử dụng:
path = "F:\CTDA\spring-mvc-starter-master\spring-mvc-starter-master"
path.replace("\\", "\\\\")

print_directory_tree(path, last_path=path.split("\\")[-1])

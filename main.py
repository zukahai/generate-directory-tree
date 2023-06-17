import os

def print_directory_tree(path, prefix='', last_path='', ignore=['.git', 'target'], result=''):
    print("Read file or directory: ", path)
    if os.path.basename(path) in ignore:
        return result
    line = '└──' if os.path.basename(path) == last_path else '├──'
    if os.path.isfile(path):
        result += prefix + line + os.path.basename(path) + '\n'
    elif os.path.isdir(path):
        result += prefix + line + os.path.basename(path) + '/\n'
        if os.path.basename(path) == last_path:
            sub_prefix = '    '
        else:
            sub_prefix = '|   '
        list_files = sorted(os.listdir(path))
        # remove files in ignore list
        list_files = [file for file in list_files if file not in ignore]
        for filename in list_files:
            result = print_directory_tree(os.path.join(path, filename), prefix + sub_prefix, list_files[-1], ignore, result)
    return result

# Ví dụ sử dụng:
# path = "F:\CTDA\spring-mvc-starter-master\spring-mvc-starter-master"
# path.replace("\\", "\\\\")
# path.replace("/", "\\\\")
# directory_tree = print_directory_tree(path, last_path=path.split("\\")[-1], ignore=['.git', 'target', '.settings', '.vscode', '.gitkeep'])
# print(directory_tree)
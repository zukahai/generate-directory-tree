import os

def print_directory_tree(path, prefix='', last_path='', ignore=['.git', 'target'], output_file=None):
    print("Read file or directory: ", path)
    if os.path.basename(path) in ignore:
        return
    line = '└─── ' if os.path.basename(path) == last_path else '├─── '
    if os.path.isfile(path):
        output_file.write(prefix + line + os.path.basename(path) + '\n')
    elif os.path.isdir(path):
        output_file.write(prefix + line + os.path.basename(path) + '\n')
        if os.path.basename(path) == last_path:
            sub_prefix = '    '
        else:
            sub_prefix = '|   '
        list_files = sorted(os.listdir(path))
        # remove files in ignore list
        list_files = [file for file in list_files if file not in ignore]
        for filename in list_files:
            print_directory_tree(os.path.join(path, filename), prefix + sub_prefix, list_files[-1], ignore, output_file)

def save_file(path, output_file):
    with open(output_file, 'w', encoding="utf-8") as output_file:
        print_directory_tree(path, ignore=['.git', 'target', '.settings', '.vscode', '.gitkeep', '__pycache__', '.demo'], output_file=output_file, last_path=os.path.basename(path))
# Ví dụ sử dụng:
# path = "F:\CTDA\spring-mvc-starter-master\spring-mvc-starter-master"
# output_filename = "output.txt"

# save_file(path, output_filename)

# print("Kết quả đã được lưu vào file:", output_filename)

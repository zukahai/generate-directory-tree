import os

def print_directory_tree(path, prefix='', last_path='', ignore=['.git', 'target'], output_file=None):
    if os.path.basename(path) in ignore:
        return
    if os.path.isfile(path):
        output_file.write(prefix + '|-- ' + os.path.basename(path) + '\n')
    elif os.path.isdir(path):
        output_file.write(prefix + '|-- ' + os.path.basename(path) + '/\n')
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
    with open(output_file, 'w') as output_file:
        print_directory_tree(path, ignore=['.git', 'target', '.settings', '.vscode', '.gitkeep'], output_file=output_file)
# Ví dụ sử dụng:
path = "F:\CTDA\spring-mvc-starter-master\spring-mvc-starter-master"
output_filename = "output.txt"

save_file(path, output_filename)

print("Kết quả đã được lưu vào file:", output_filename)

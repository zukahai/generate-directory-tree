from gitignore_parser import parse_gitignore
import os

def is_path_ignored(path_to_check, gitignore_file='ignore.txt'):
    gitignore = parse_gitignore(gitignore_file)

    print(gitignore)

    # Kiểm tra path_to_check lỗi
    # if not os.path.exists(path_to_check):
    #     return True

    # Kiểm tra đường dẫn trong gitignore
    return gitignore(path_to_check)

# Sử dụng hàm để kiểm tra đường dẫn
path = '.\\generate-directory-tree\\ignore.txt'
result = is_path_ignored(path)

if result:
    print("Đường dẫn bị bỏ qua bởi gitignore.")
else:
    print("Đường dẫn không bị bỏ qua bởi gitignore.")

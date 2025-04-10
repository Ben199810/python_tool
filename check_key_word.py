import os

RED = "\033[91m"  # ANSI 顏色碼：紅色
YELLOW = "\033[93m"  # ANSI 顏色碼：黃色
GREEN = "\033[92m"  # ANSI 顏色碼：綠色
BULE = "\033[94m"  # ANSI 顏色碼：藍色
RESET = "\033[0m"  # ANSI 顏色碼：重置顏色

def is_binary_file(file_path):
    """
    檢查檔案是否為二進位檔案
    :param file_path: 檔案路徑
    :return: 如果是二進位檔案則回傳 True，否則 False
    """
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(1024)
            if b'\0' in chunk:
                return True
    except Exception as e:
        print(f"無法檢查檔案是否為二進位檔案: {file_path}, 原因: {e}")
    return False

def find_keyword_in_docker(repo_paths, keyword):
    """
    遞迴檢查多個 repo 中所有檔案是否包含關鍵字
    :param repo_paths: 專案路徑列表
    :param keyword: 要搜尋的關鍵字
    """
    for repo_path in repo_paths:
        print(f"正在檢查 repo: {repo_path}")
        for root, dirs, files in os.walk(repo_path):
            for file in files:
                # 檢查與 Dockerfile 相關的檔案
                if "Dockerfile" in file or "docker" in file.lower():
                    file_path = os.path.join(root, file)
                    # 讀取檔案檢查關鍵字
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            if not is_binary_file(file_path):
                                content = f.read()
                                if keyword in content:
                                    print(f"找到關鍵字 '{keyword}' 在檔案: {file_path}")
                                    # 找到的關鍵字行
                                    lines = content.splitlines()
                                    for line in lines:
                                        if keyword in line:
                                            print(f"{YELLOW}行: {line}{RESET}")
                                else:
                                    print(f"關鍵字 '{keyword}' 不在檔案: {file_path}")
                            else:
                                print(f"跳過二進位檔案: {file_path}")
                    except UnicodeDecodeError as e:
                        print(f"無法讀取檔案: {file_path}, 原因: {e}")

def find_keyword_in_yaml(repo_paths, keyword):
    """
    遞迴檢查多個 repo 中所有檔案是否包含關鍵字
    :param repo_paths: 專案路徑列表
    :param keyword: 要搜尋的關鍵字
    """
    for repo_path in repo_paths:
        print(f"正在檢查 repo: {repo_path}")
        for root, dirs, files in os.walk(repo_path):
            for file in files:
                if file.endswith(".yaml") or file.endswith(".yml"):
                    file_path = os.path.join(root, file)
                    # 讀取檔案檢查關鍵字
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            if not is_binary_file(file_path):
                                content = f.read()
                                if keyword in content:
                                    print(f"{BULE}找到關鍵字 '{keyword}' 在檔案: {file_path}{RESET}")
                                    # 找到的關鍵字行
                                    lines = content.splitlines()
                                    for line in lines:
                                        if keyword in line:
                                            print(f"{YELLOW}行: {line}{RESET}")
                                else:
                                    print(f"關鍵字 '{keyword}' 不在檔案: {file_path}")
                            else:
                                print(f"跳過二進位檔案: {file_path}")
                    except UnicodeDecodeError as e:
                        print(f"無法讀取檔案: {file_path}, 原因: {e}")

if __name__ == "__main__":
    # 使用者可修改以下路徑與關鍵字
    repo_paths = [
      "repo_path",
    ]
    # 替換為你要搜尋的關鍵字
    keyword = "your_keyword"
    find_keyword_in_docker(repo_paths, keyword)
    find_keyword_in_yaml(repo_paths, keyword)

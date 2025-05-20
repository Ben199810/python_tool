import os

# 定義顏色常數
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

def replace_file_name(repo_paths, old_name, new_name):
    for repo_path in repo_paths:
        print(f"{BLUE}檢查目錄: {repo_path}{RESET}")
        # 只檢查一層子目錄
        try:
            for entry in os.scandir(repo_path):
                if entry.is_dir():
                    subdir = entry.path
                    for file in os.listdir(subdir):
                        if file == old_name:
                            old_path = os.path.join(subdir, file)
                            new_path = os.path.join(subdir, new_name)
                            try:
                                os.rename(old_path, new_path)
                                print(f"{GREEN}已將 {old_path} 重新命名為 {new_path}{RESET}")
                            except Exception as e:
                                print(f"{RED}重新命名失敗: {old_path}，原因: {e}{RESET}")
        except Exception as e:
            print(f"{RED}無法存取目錄: {repo_path}，原因: {e}{RESET}")

if __name__ == "__main__":
    repo_paths = [
        "/Users/bing-wei/Documents/swissknife/SRE/iac/projects",
    ]
    # 範例：將所有子目錄下名為 old.txt 的檔案改名為 new.txt
    replace_file_name(repo_paths, "terragrunt.hcl", "root.hcl")
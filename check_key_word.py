import os

RED = "\033[91m"  # ANSI 顏色碼：紅色
YELLOW = "\033[93m"  # ANSI 顏色碼：黃色
GREEN = "\033[92m"  # ANSI 顏色碼：綠色
BULE = "\033[94m"  # ANSI 顏色碼：藍色
RESET = "\033[0m"  # ANSI 顏色碼：重置顏色

# images 空陣列
images = []

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

def find_keyword_in_files(repo_paths, keyword, file_extensions=None, file_keywords=None):
  """
  遞迴檢查多個 repo 中所有檔案是否包含關鍵字
  :param repo_paths: 專案路徑列表
  :param keyword: 要搜尋的關鍵字
  :param file_extensions: 要篩選的檔案副檔名列表 (如 [".yaml", ".yml"])
  :param file_keywords: 要篩選的檔案名稱關鍵字列表 (如 ["Dockerfile", "docker"])
  """
  for repo_path in repo_paths:
    print(f"正在檢查 repo: {repo_path}")
    for root, dirs, files in os.walk(repo_path):
      for file in files:
        # 檢查檔案是否符合條件
        if (file_extensions and any(file.endswith(ext) for ext in file_extensions)) or (file_keywords and any(keyword in file for keyword in file_keywords)):
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
                      # line 取得 docker image
                      print(f"{YELLOW}找到關鍵字 '{keyword}' 在行: {line}{RESET}")
                      if "FROM" in line:
                        # 取得 docker image
                        image = line.split("FROM")[1].strip()
                        if image not in images:
                          images.append(image)
                          print(f"{GREEN}找到 docker image: {image}{RESET}")
                      elif "image:" in line:
                        # 取得 docker image
                        image = line.split("image:")[1].strip()
                        if image not in images:
                          images.append(image)
                          print(f"{GREEN}找到 docker image: {image}{RESET}")
                      elif "- docker push " in line:
                        # 取得 docker image
                        image = line.split("- docker push ")[1].strip()
                        if image not in images:
                          images.append(image)
                          print(f"{GREEN}找到 docker image: {image}{RESET}")
                else:
                  print(f"檔案: {file_path} 不包含關鍵字 '{keyword}'")
              else:
                print(f"跳過二進位檔案: {file_path}")
          except UnicodeDecodeError as e:
            print(f"無法讀取檔案: {file_path}, 原因: {e}")

if __name__ == "__main__":
  # 使用者可修改以下路徑與關鍵字
  repo_paths = [
    "/Users/bing-wei/Documents/swissknife/SRE/pid-cluster-yaml/bbin/outside",
    "/Users/bing-wei/Documents/swissknife/SRE/pid-cluster-yaml/bbgp/outside",
    "/Users/bing-wei/Documents/swissknife/SRE/images-build/PI"
    "/Users/bing-wei/Documents/swissknife/SRE/images-build/base",
    "/Users/bing-wei/Documents/swissknife/SRE/images-build/cicd",
    "/Users/bing-wei/Documents/swissknife/SRE/images-build/proxy-server",
    "/Users/bing-wei/Documents/swissknife/SRE/images-build/redis_auto_restart",
    "/Users/bing-wei/Documents/swissknife/SRE/images-build/runner",
  ]
  # 替換為你要搜尋的關鍵字
  keyword = "gcr.io/rd6-project"

  # 搜尋 Dockerfile 和相關檔案
  find_keyword_in_files(repo_paths, keyword, file_keywords=["Dockerfile", "docker"])

  # 搜尋 YAML 檔案
  find_keyword_in_files(repo_paths, keyword, file_extensions=[".yaml", ".yml"])

  print(f"{GREEN}找到的 docker image:{RESET}")
  for image in images:
    print(f"{GREEN}{image}{RESET}")

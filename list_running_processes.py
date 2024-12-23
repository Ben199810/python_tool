import psutil

def list_running_processes():
    for proc in psutil.process_iter(['pid', 'name', 'username']):
      try:
        info = proc.info
        pid = info['pid']
        name = info['name']
        user = info['username']
        # if 'php' in name.lower():
        #   print(f"PID: {pid}, 程式名稱: {name}, 使用者: {user}")
        print(f"PID: {pid}, 程式名稱: {name}, 使用者: {user}")
      except (psutil.NoSuchProcess, psutil.AccessDenied,):
        pass

if __name__ == "__main__":
  list_running_processes()
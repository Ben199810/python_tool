import psutil

# interval: 每次取得資料的間隔時間
def get_system_usage():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()

    # print(f"記憶體資訊: {memory}")
    print(f"CPU 使用率: {cpu}%")
    print(f"記憶體總量: {memory.total / (1024**3):.2f} GB")
    print(f"記憶體使用率: {memory.percent}%")

# 用來確保某些程式碼只有在直接執行該腳本時才會運行，而不是在該腳本被作為模組導入時運行。
if __name__ == "__main__":
    get_system_usage()
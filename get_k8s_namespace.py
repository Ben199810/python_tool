from kubernetes import client, config

def choose_namespace():
    # 載入預設的 kube config
    config.load_kube_config()

    # 建立 API 實例
    v1 = client.CoreV1Api()

    # 取得所有的 namespace
    namespaces = v1.list_namespace()
    print("Namespaces:")
    for i in namespaces.items:
        print(i.metadata.name)
    namespace = input("Choose a namespace: ")
    return namespace

if __name__ == "__main__":
    choose_namespace()
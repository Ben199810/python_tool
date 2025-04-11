import os

# 定義顏色常數
GREEN = "\033[92m"  # 綠色
YELLOW = "\033[93m"  # 黃色
BULE = "\033[94m"  # 藍色
RED = "\033[91m"  # 紅色
RESET = "\033[0m"  # 重置顏色

def docker_pull_images(images):
    """
    使用 docker pull 指令下載所有 docker image
    :param images: 要下載的 docker image 列表
    """
    for image in images:
        print(f"{GREEN}正在下載 docker image: {image}{RESET}")
        os.system(f"docker pull {image}")

def docker_tag_images(images, keyword, new_keyword):
    """
    使用 docker tag 指令標記所有 docker image
    :param images: 要標記的 docker image 列表
    """
    for image in images:
        if image.startswith(keyword):
            new_image = image.replace(keyword, new_keyword)
            print(f"{YELLOW}標記 docker image: {image}: 為 {new_image}{RESET}")
            os.system(f"docker tag {image} {new_image}")

def docker_push_images(images, keyword, new_keyword):
    """
    使用 docker push 指令上傳所有 docker image
    :param images: 要上傳的 docker image 列表
    """
    for image in images:
        if image.startswith(keyword):
            new_image = image.replace(keyword, new_keyword)
            print(f"{GREEN}正在上傳 docker image: {new_image}{RESET}")
            os.system(f"docker push {new_image}")
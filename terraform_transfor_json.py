import hcl2
import json

def hcl_to_json(hcl_file_path, json_file_path):
    # 讀取 HCL 文件內容
    with open(hcl_file_path, 'r') as hcl_file:
        # 將 HCL 文件內容轉換為 JSON 數據
        hcl_data = hcl2.load(hcl_file)
    # 將 JSON 數據寫入 JSON 文件
    with open(json_file_path, 'w') as json_file:
        json.dump(hcl_data, json_file, indent=2)

def get_forwarding_rules_and_ssl_certificates(json_file_path):
    # 讀取 JSON 文件內容
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        # 提取 forwarding_rules 各組 key 的 ssl_certificates
        forwarding_rules = data['inputs']['forwarding_rules']
        result = {}
        for key in forwarding_rules.keys():
            result[key] = forwarding_rules[key].get('ssl_certificates', [])
        return result

def add_ssl_certificates_list_to_json_file(json_file_path, ssl_certificates):
    # 讀取現有的 JSON 文件內容
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
    # 將 all SSL 證書 List 添加到現有的 JSON 數據中
    json_data['inputs']['ssl_certificates'] = ssl_certificates
    # 將更新後的 JSON 數據寫回文件
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)
    print(f"SSL certificates have been successfully written to {json_file_path}")

def remove_certificate_and_private_key(json_file_path):
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
    forwarding_rules = json_data['inputs']['forwarding_rules']
    for key in forwarding_rules.keys():
        ssl_certificates = forwarding_rules[key].get('ssl_certificates', [])
        for cert in ssl_certificates:
            cert.pop('certificate', None)
            cert.pop('private_key', None)
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=2)
    print(f"Certificate and private key have been successfully removed from {json_file_path}")

# def json_to_hcl(json_file_path, hcl_file_path):
#     with open(json_file_path, 'r') as json_file:
#         json_data = json.load(json_file)
    
#     hcl_data = hcl.dumps(json_data)
    
#     with open(hcl_file_path, 'w') as hcl_file:
#         hcl_file.write(hcl_data)

if __name__ == "__main__":
    hcl_file_path = 'terragrunt.hcl'
    json_file_path = 'terragrunt.json'
    hcl_to_json(hcl_file_path, json_file_path)
    forwarding_rules_and_ssl_certificates = get_forwarding_rules_and_ssl_certificates(json_file_path)
    all_ssl_certificates = []
    for key, ssl_certificates in forwarding_rules_and_ssl_certificates.items():
      all_ssl_certificates.extend(ssl_certificates)
    add_ssl_certificates_list_to_json_file(json_file_path, all_ssl_certificates)
    remove_certificate_and_private_key(json_file_path)
    # json_to_hcl(json_file_path, hcl_file_path)
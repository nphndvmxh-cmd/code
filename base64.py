import requests
import os

API_URL = "https://freecodingtools.org/api/obfuscate/python"

headers = {
    'Accept': '*/*',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://freecodingtools.org',
    'Referer': 'https://freecodingtools.org/tools/obfuscator/python',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

def obfuscate_file():
    filepath = input("Nhập đường dẫn file cần mã hóa: ").strip()

    if not os.path.isfile(filepath):
        print("❌ File không tồn tại!")
        return
import requests
import os

API_URL = "https://freecodingtools.org/api/obfuscate/python"

headers = {
    'Accept': '*/*',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://freecodingtools.org',
    'Referer': 'https://freecodingtools.org/tools/obfuscator/python',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

def obfuscate_file():
    filepath = input("Nhập đường dẫn file cần mã hóa: ").strip()

    if not os.path.isfile(filepath):
        print("❌ File không tồn tại!")
        return

    # Đọc nội dung python gốc
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    # Gửi nguyên code, không base64
    json_data = {
        "code": code
    }

    print("⏳ Đang obfuscate...")

    response = requests.post(API_URL, headers=headers, json=json_data)

    # Kiểm tra lỗi API
    if response.status_code != 200:
        print("❌ API trả lỗi:", response.text)
        return

    result = response.json()

    # Lấy nội dung obfuscate từ key 'output'
    obf = result.get("output")
    if not obf:
        print("❌ API không trả về output!")
        print(result)
        return

    # XÓA xuống dòng trước exec (như bạn yêu cầu)
    obf = obf.replace("\nexec", "exec")

    # Tạo tên file mới
    output_file = filepath.replace(".py", "_obf_clean.py")

    # Ghi file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(obf)

    print(f"✅ Obfuscate thành công! File output: {output_file}")


if __name__ == "__main__":
    print("=== Python Obfuscator Tool ===")
    obfuscate_file()

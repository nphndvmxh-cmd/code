import requests, sys
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os
import time
ban = """\033[1;32m
                                            ┳┓┏┓┳┳┓┏┏┓┳┓  ┳┓┏┓┳┳┓
                                            ┃┃┃┓┃┃┗┫┣ ┃┃  ┃┃┣┫┃┃┃
                                            ┛┗┗┛┗┛┗┛┗┛┛┗  ┛┗┛┗┛ ┗                   								
"""
for h in ban:
	sys.stdout.write(h)
	sys.stdout.flush()
	time.sleep(0.001)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Chọn nguồn
print("🪿 CHỌN NGUỒN:")
print("1. mèo đen")
print("2. mèo đen")
choice = input("\033[1;31m▶ NHẬP LỰA CHỌN: ").strip()

if choice == "1":
    base_url = "https://meoden.net/yan"
elif choice == "2":
    base_url = "https://meoden.net/kona"
else:
    print("🦈 ĐÙA NHAU À")
    exit()

input("Nhấn Enter để vào tool...")
clear_screen()

# Tạo thư mục lưu ảnh
output_dir = "converted_images"
os.makedirs(output_dir, exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

page = 1
img_count = 0

while True:
    url = f"{base_url}?page={page}"

    try:
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code == 404 or "Không tìm thấy" in resp.text:
            print("💤 HẾT TRANG RỒI")
            break
    except Exception as e:
        print(f"💤 LỖI TẢI TRANG: {url}: {e}")
        break

    soup = BeautifulSoup(resp.text, 'html.parser')
    img_tags = soup.find_all('img')

    if not img_tags:
        print("💤 KHÔNG THẤY ẢNH")
        break

    for img_tag in img_tags:
        img_src = img_tag.get("src")
        if not img_src:
            continue

        if img_src.startswith("//"):
            img_src = "https:" + img_src
        elif img_src.startswith("/"):
            img_src = base_url + img_src

        try:
            img_data = requests.get(img_src, headers=headers, timeout=10).content
            img_pil = Image.open(BytesIO(img_data))
            img_name = os.path.join(output_dir, f"meoden_{img_count+1}.jpg")
            img_pil.convert("RGB").save(img_name, "JPEG")
            print(f"🐕🐬 LƯU ẢNH: {img_name}")
            img_count += 1
        except Exception as e:
            print(f"😿 LỖI ẢNH {img_src}: {e}")

    page += 1
    time.sleep(1)

print(f"\n🏹 TỔNG TRANG ĐÃ TẢI: {img_count}")

import sys,os,time,subprocess
ban = """\033[1;32m                             
 ▄▄▄   ▄▄     ▄▄     ▄▄▄  ▄▄▄ 
 ███   ██    ████    ███  ███ 
 ██▀█  ██    ████    ████████ 
 ██ ██ ██   ██  ██   ██ ██ ██ 
 ██  █▄██   ██████   ██ ▀▀ ██ 
 ██   ███  ▄██  ██▄  ██    ██ 
 ▀▀   ▀▀▀  ▀▀    ▀▀  ▀▀    ▀▀                                                            
"""
def banner():
  os.system("cls" if os.name == "nt" else "clear")
  for h in ban:
    sys.stdout.write(h)
    sys.stdout.flush()
    time.sleep(0.001)
banner()
def encode_pyarmor():
    filename = input("[!] nhập tên file hoặc đường dẫn file cần mã hóa: ").strip()

    # Nếu chỉ nhập tên file, tự chuyển thành đường dẫn đầy đủ
    if not os.path.isabs(filename):
        filename = os.path.join(os.getcwd(), filename)

    # Kiểm tra file có tồn tại không
    if not os.path.isfile(filename):
        print("! file không tồn tại!")
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        return

    output_dir = "build"
    os.makedirs(output_dir, exist_ok=True)

    cmd = [
        "pyarmor", "gen",
        "-i", filename,
        "-O", output_dir
    ]

    print("\n>>đang mã hóa...")
    result = subprocess.run(cmd)

    if result.returncode == 0:
        print(f"đã lưu vào: {output_dir}")
    else:
        print("mã hóa thất bại !.")

def main():
    while True:
        print("\n===========PYARMOR===========")
        print("1. Encode PyArmor")
        print("0. Thoát")

        choice = input("Chọn chức năng: ").strip()

        if choice == "1":
            encode_pyarmor()
        elif choice == "0":
            break
        else:
            print("sai lựa chọn!")
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    main()

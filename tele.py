from telethon import TelegramClient
from pystyle import Colors, Colorate
import asyncio
import time
import sys
import os
from datetime import datetime
from time import sleep
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#đánh dấu bản quyền
ndp_tool="\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ="
#Config
def banner():
 banner = f"""
						██╗  ██╗███╗   ██╗
						██║  ██║████╗  ██║
						███████║██╔██╗ ██║
						██╔══██║██║╚██╗██║
						██║  ██║██║ ╚████║
						╚═╝  ╚═╝╚═╝  ╚═══╝
							TELE

"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)
os.system("cls" if os.name == "nt" else "clear")
banner()
# Tên tệp để lưu thông tin API
DATA_FILE = "teledata.txt"

# Hàm để lấy thông tin API từ người dùng hoặc tệp
def get_api_data():
	if os.path.exists(DATA_FILE):
		use_old_data = input("Bạn có muốn sử dụng dữ liệu cũ không? (Y/N): ").strip().lower()
		if use_old_data == 'y':
			with open(DATA_FILE, "r") as file:
				data = file.read().splitlines()
				if len(data) == 3:
					api_id, api_hash, phone_number = data
					os.system("cls" if os.name == "nt" else "clear")
					return api_id, api_hash, phone_number
				else:
					print("Tệp dữ liệu không hợp lệ, vui lòng nhập thông tin mới.")
		elif use_old_data != 'n':
			print("Lựa chọn không hợp lệ, vui lòng nhập thông tin mới.")

	# Nhập thông tin từ người dùng
	api_id = input("Nhập api_id telegram: ").strip()
	api_hash = input("Nhập api_hash telegram: ").strip()
	phone_number = input("Nhập số điện thoại (+mã vùng): ").strip()
	os.system("cls" if os.name == "nt" else "clear")

	# Lưu thông tin vào tệp
	with open(DATA_FILE, "w") as file:
		file.write(f"{api_id}\n{api_hash}\n{phone_number}")

	return api_id, api_hash, phone_number

# Hàm hiển thị tiến trình loading dưới dạng phần trăm
def show_loading_bar(total_time, elapsed_time):
	# Tính phần trăm tiến trình
	progress = elapsed_time / total_time
	percent = int(progress * 100)
	
	# Hiển thị phần trăm và ETA
	sys.stdout.write( f"\r[{percent}%] ETA {int(total_time - elapsed_time)}s")
	sys.stdout.flush()

# Hàm chính
async def main(client):
	# Lấy thông tin người dùng qua API
	user = await client.get_me()
	user_id = user.id
	full_name = user.first_name + (" " + user.last_name if user.last_name else "")
	username = user.username if user.username else "Không có username"

	# Hiển thị thông tin người dùng
	print(Colorate.Diagonal(Colors.green_to_red,"[<>]Thông tin tài khoản của bạn:"))
	print(Colorate.Diagonal(Colors.green_to_red,f"[🌸]ID: {user_id}"))
	print(Colorate.Diagonal(Colors.green_to_red,f"[🌸]Tên đầy đủ: {full_name}"))
	print(Colorate.Diagonal(Colors.green_to_red,f"[🌸]Username: {username}"))
	print(Colorate.Diagonal(Colors.green_to_red,"────────────────────────────────────────────────────────────"))

	# Lấy tất cả các cuộc trò chuyện
	dialogs = await client.get_dialogs(limit=None)

	# Lọc và hiển thị các nhóm và kênh mà người dùng tham gia
	groups_channels = []
	print(Colorate.Diagonal(Colors.green_to_red, "[<>]Danh sách các nhóm và kênh tham gia:"))
	for idx, dialog in enumerate(dialogs):
		if dialog.is_group or dialog.is_channel:
			groups_channels.append(dialog)
			print(Colorate.Diagonal(Colors.blue_to_purple, f"[{len(groups_channels)}]{dialog.name} (ID: {dialog.id}) "))

	# Yêu cầu người dùng chọn nhóm hoặc kênh
	group_channel_num = int(input(Colorate.Diagonal(Colors.red_to_white,"\nNhập số thứ tự nhóm/kênh bạn muốn tham gia: "))) - 1
	os.system("cls" if os.name == "nt" else "clear")

	if 0 <= group_channel_num < len(groups_channels):
		target_group_channel = groups_channels[group_channel_num]
		print(Colorate.Diagonal(Colors.green_to_cyan, f"\nĐang truy cập nhóm/kênh: {target_group_channel.name}"))

		# Lấy tin nhắn từ nhóm hoặc kênh đã chọn
		all_messages = []
		last_message_id = None

		while True:
			# Lấy 1000 tin nhắn mới nhất
			if last_message_id:
				messages = await client.get_messages(target_group_channel.id, limit=1000, max_id=last_message_id)
			else:
				messages = await client.get_messages(target_group_channel.id, limit=1000)

			if not messages:
				break

			all_messages.extend(messages)
			last_message_id = messages[-1].id

			print(Colorate.Diagonal(Colors.red_to_white, f"\nĐã lấy {len(messages)} tin nhắn. Tổng số tin nhắn đã lấy: {len(all_messages)}"))

			# Hiển thị nội dung tin nhắn cụ thể (toàn bộ nội dung)
			# for msg in messages:
			for index, msg in enumerate(messages, 1):
				sender = await msg.get_sender()
				for index, msg in enumerate(messages, 1):
					sender = await msg.get_sender()
					if sender:
						sender_name = sender.first_name if hasattr(sender, 'first_name') else (sender.title if hasattr(sender, 'title') else "Không xác định")
					else:
						sender_name = "Không xác định"
					msg_time = msg.date.strftime("%d-%m-%Y %H:%M:%S")
					msg_text = msg.text if msg.text else "(Không có nội dung)"
					print(f"[{len(all_messages) - len(messages) + index}] [{msg_time}] {sender_name}: {msg_text}\n")

				# if sender:
				# 	if hasattr(sender, 'first_name'):
				# 		sender_name = sender.first_name + (" " + sender.last_name if sender.last_name else "")
				# 	elif hasattr(sender, 'title'):
				# 		sender_name = sender.title
				# 	else:
				# 		sender_name = "người gửi không xác định"
				# else:
				# 	sender_name = "người gửi không xác định"
				# msg_time = msg.date.strftime("%d-%m-%Y %H:%M:%S")
				# msg_text = msg.text if msg.text else "(Không có nội dung)"


				# Hiển thị toàn bộ nội dung tin nhắn
				print(f"[{msg_time}] {sender_name}:")
				print(f"  {msg_text}")
				print("────────────────────────────────────────────────────────────────────────────────")

			# Dừng lại sau mỗi lần lấy 1000 tin nhắn
			print("\nĐã lấy xong 1000 tin nhắn, chờ 120 giây trước khi tiếp tục...")

			# Đếm thời gian chờ (120 giây) với thanh loading
			total_time = 120
			start_time = time.time()

			for i in range(total_time + 1):
				elapsed_time = time.time() - start_time
				show_loading_bar(total_time, elapsed_time)
				await asyncio.sleep(1)

			print("\nChờ xong, tiếp tục lấy tin nhắn...")

		print(f"\nĐã lấy tổng cộng {len(all_messages)} tin nhắn từ nhóm/kênh {target_group_channel.name}.")
	else:
		print("Số nhóm/kênh không hợp lệ.")

# Chạy client
if __name__ == "__main__":
	api_id, api_hash, phone_number = get_api_data()
	client = TelegramClient('session_name', api_id, api_hash)
	with client:
		client.loop.run_until_complete(main(client))

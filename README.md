# 🤖 BiOne Self-Bot — Auto Reply DM

> Self-bot Discord tự động trả lời tin nhắn DM trên tài khoản cũ, thông báo cho bạn bè / khách hàng rằng bạn đã chuyển sang tài khoản mới.
> The Discord self-bot automatically replies to DMs on your old account, notifying friends/clients that you've switched to a new account.

## ✨ Features

- 📩 Tự động trả lời khi có ai nhắn DM vào tài khoản cũ
- 👤 Mention tên người gửi trong tin nhắn phản hồi
- 🔗 Gửi kèm link tài khoản chính mới
- ⚡ Nhẹ, dễ chạy trên VPS hoặc máy cá nhân

- 📩 Automatically reply to DMs from your old account
- 👤 Mention the sender's name in the reply message
- 🔗 Include a link to your new main account
- ⚡ Lightweight, easy to run on VPS or personal computers

## 📁 Project Structure

```
BiOne-selfbot/
├── main.py              # File chính chạy bot
├── requirements.txt     # Các thư viện cần cài
├── .env                 # Token & config (không push lên GitHub!)
└── README.md            # Hướng dẫn sử dụng
```

## ⚙️ Setup

### 1. Clone repo

```bash
git clone https://github.com/BiOneIsDaBest/disscord_bionebot-selfbot.git
cd BiOne-selfbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Cấu hình `.env`

Tạo file `.env` trong thư mục gốc (⚠️ **không bao giờ push file này lên GitHub!**):

```env
TOKEN = your_discord_token_here
MAIN_ACCOUNT = <@your_discord_user_id>
```

Thay thế:
- `your_discord_token_here` → Token tài khoản Discord cũ của bạn
- `your_discord_user_id` → ID tài khoản Discord chính mới

### 4. Run the bot

```bash
python main.py
```

Nếu chạy thành công, bạn sẽ thấy:

```
✅ Đang chạy với acc: <tên_tài_khoản>
```

## 📸 Demo auto message

Khi ai đó nhắn DM vào tài khoản cũ, bot sẽ tự động gửi:

```
━━━━━━━━━━━━━━━━━━━━━━
📢  ALO ALO ACC BIONE ĐÃ VỀ RÒI
━━━━━━━━━━━━━━━━━━━━━━

Xin chào @người_gửi 👋

Tài khoản này hiện không còn được sử dụng.
Mọi liên hệ vui lòng nhắn tin đến tài khoản chính của mình:

➡️ Discord: @tài_khoản_chính

Cảm ơn anhem đã nhắn tin! 🙏
━━━━━━━━━━━━━━━━━━━━━━
🌐 This account is no longer active. Please reach out to my main account above!
🤖 Tin nhắn này được gửi tự động
```

## ⚠️ Important notes

- **Self-bot vi phạm ToS của Discord** — sử dụng trên tài khoản có nguy cơ bị ban. Hãy cân nhắc trước khi dùng!
- **Không chia sẻ token** — Token cho phép toàn quyền truy cập tài khoản. Giữ bí mật file `.env`
- Thêm `.env` vào `.gitignore` để tránh push nhầm

## 🛠️ System requirements

- Python 3.8+
- Thư viện: `discord.py-self`, `python-dotenv`

---

## 🛡️ Bản quyền

Bản quyền thuộc **BiOneIsDaBest**  
📌 Nếu mượn sử dụng hoặc chỉnh sửa, vui lòng **ghi rõ nguồn** hoặc liên hệ: [Discord: BiOneIsDaBest](https://discord.com/users/1146990393167200276)
# Hướng dẫn đẩy Locket Gold Bot lên Replit

## Tổng quan
Bot là ứng dụng **Telegram** — bạn truy cập trên điện thoại qua **ứng dụng Telegram**, không qua trình duyệt. Replit chỉ chạy bot 24/7 để nhận tin nhắn từ bạn.

---

## Bước 1: Tạo tài khoản Replit
1. Vào [replit.com](https://replit.com) → Đăng ký/Đăng nhập (dùng Google/GitHub).

---

## Bước 2: Import dự án lên Replit
1. **Replit** → **Create Repl** (hoặc nút **+**)
2. Chọn **Import from GitHub**
3. Dán URL repo (ví dụ: `https://github.com/username/Locket-Gold`)
4. Hoặc: **Upload folder** — kéo thả toàn bộ thư mục `Locket-Gold` vào.

---

## Bước 3: Cấu hình Secrets (biến môi trường)
1. Trong Replit, mở **Tools** (hoặc **Lock** icon) → **Secrets**
2. Thêm các key sau:

| Key | Value | Bắt buộc |
|-----|-------|----------|
| `BOT_TOKEN` | Token từ [@BotFather](https://t.me/BotFather) trên Telegram | Có |
| `NEXTDNS_KEY` | API key NextDNS (cho DNS Anti-Revoke) | Có* |

*\* Nếu không có `NEXTDNS_KEY`, một số tính năng DNS có thể báo lỗi.*

---

## Bước 4: Chạy bot
1. Nhấn nút **Run** (▶) trên Replit
2. Đợi cài dependency (Replit tự chạy `pip install -r requirements.txt`)
3. Thấy log `Bot is running... (1 workers)` là đã chạy ổn

---

## Bước 5: Truy cập trên điện thoại
1. Cài **Telegram** trên điện thoại
2. Tìm bot bằng username (ví dụ: `@YourBotName`)
3. Nhấn **Start** hoặc gửi `/start`
4. Dùng bot qua Telegram như bình thường

---

## Lưu ý quan trọng

### Replit miễn phí (Hacker Plan)
- Repl **tự sleep** sau ~1 giờ không tương tác với Replit
- Khi sleep, bot **tạm dừng** → không nhận tin nhắn
- **Cách wake bot**: Mở tab Replit trên trình duyệt → bot sẽ tự chạy lại
- Hoặc dùng dịch vụ “Always On” (Replit cần nâng cấp trả phí)

### Replit trả phí (Pro)
- Có tùy chọn **Always On** → bot chạy 24/7
- Phù hợp khi cần bot online liên tục

### Bảo mật
- Không commit file `.env` hoặc token vào GitHub
- Dùng **Secrets** trên Replit thay cho `.env`
- File `bot_data.db` (SQLite) được tạo tự động khi chạy

---

## Xử lý lỗi thường gặp

| Lỗi | Cách xử lý |
|-----|------------|
| `BOT_TOKEN` không tìm thấy | Kiểm tra Secrets đã thêm đúng tên `BOT_TOKEN` chưa |
| Bot không phản hồi | Repl có thể đang sleep → mở tab Replit để wake |
| `ModuleNotFoundError` | Chạy `pip install -r requirements.txt` trong Shell rồi Run lại |
| NextDNS Error | Kiểm tra `NEXTDNS_KEY` trong Secrets |

---

## Cấu trúc sau khi deploy
```
Locket-Gold/
├── main.py          # Entry point
├── app/
│   ├── bot.py       # Logic bot
│   ├── config.py    # Cấu hình
│   ├── database.py  # SQLite
│   └── services/    # Locket, NextDNS
├── requirements.txt # Dependencies
└── .replit          # Cấu hình chạy Replit
```
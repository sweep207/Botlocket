import asyncio
import threading
import uvicorn
from app.config import app
from app.bot import run_bot # Đảm bảo file bot.py có hàm run_bot()

def start_bot():
    try:
        run_bot()
    except Exception as e:
        print(f"Bot Error: {e}")

if __name__ == "__main__":
    # Chạy Bot trong một luồng (thread) riêng
    threading.Thread(target=start_bot, daemon=True).start()
    
    # Chạy FastAPI Web Server
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)

import uvicorn
from app.bot import run_bot
from app.config import app  # Import biến app từ file config
import threading

if __name__ == "__main__":
    # Chạy Bot Telegram ở một luồng riêng để không làm crash Web Server
    threading.Thread(target=run_bot, daemon=True).start()
    
    # Chạy Web Server FastAPI
    uvicorn.run(app, host="0.0.0.0", port=8080)

import asyncio
import os
import uvicorn
from app.config import app
from app.bot import run_bot # Đảm bảo file bot.py có hàm run_bot() xử lý async

async def main():
    # Lấy cổng từ biến môi trường của Railway
    port = int(os.environ.get("PORT", 8080))
    
    # Cấu hình Web Server
    config = uvicorn.Config(app, host="0.0.0.0", port=port)
    server = uvicorn.Server(config)

    # Chạy song song cả Web Server và Bot Telegram
    # Cần đảm bảo run_bot() là một coroutine (async def)
    await asyncio.gather(
        server.serve(),
        run_bot() 
    )

if __name__ == "__main__":
    asyncio.run(main())

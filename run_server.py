#!/usr/bin/env python3
"""
Script để chạy server API VSL
"""
import uvicorn
import os
import sys

# Add the project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

if __name__ == "__main__":
    print("🚀 Đang khởi động server API VSL...")
    print("📡 Server sẽ chạy tại: http://127.0.0.1:8000")
    print("📄 Website demo: file:///d:/self-study/AL4project/web/index.html")
    print("🛑 Nhấn Ctrl+C để dừng server")
    print("-" * 50)

    uvicorn.run(
        "app.vsl_api:app", host="127.0.0.1", port=8000, reload=True, log_level="info"
    )

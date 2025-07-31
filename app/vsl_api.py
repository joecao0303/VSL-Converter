from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from app.pos_tagger import POS_MAP
from app.convert2VSL import VietnameseToVSLConverter

app = FastAPI(
    title="Vietnamese to VSL Converter API",
    description="API để chuyển đổi câu tiếng Việt sang ngôn ngữ ký hiệu VSL",
    version="1.0.0",
)
converter = VietnameseToVSLConverter()

# Allow frontend on localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class InputText(BaseModel):
    text: str


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "VSL Converter API is running!",
        "status": "healthy",
        "version": "1.0.0",
        "endpoints": {"convert": "/convert (POST)", "docs": "/docs", "redoc": "/redoc"},
    }


@app.get("/health")
async def health_check():
    """Detailed health check"""
    try:
        # Test if converter is working
        test_result = converter.convert("Xin chào")
        return {
            "status": "healthy",
            "converter": "working",
            "test_conversion": test_result,
        }
    except Exception as e:
        return {"status": "error", "converter": "failed", "error": str(e)}


@app.post("/convert")
async def convert_text(payload: InputText):
    """Convert Vietnamese text to VSL gloss"""
    try:
        text = payload.text.strip()
        if not text:
            return {"error": "Text cannot be empty"}

        parsed = converter.parser.annotate(text)
        tokens = [
            f"{t['form']} - {POS_MAP.get(t['posTag'], t['posTag'])}" for t in parsed
        ]
        gloss = converter.convert(text)

        return {"input": text, "tokens": tokens, "gloss": gloss, "status": "success"}
    except Exception as e:
        return {"error": f"Conversion failed: {str(e)}", "status": "error"}

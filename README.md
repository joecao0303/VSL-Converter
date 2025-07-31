# VSL Converter - Vietnamese Sign Language

Ứng dụng web để chuyển đổi câu tiếng Việt sang ngôn ngữ ký hiệu VSL (Vietnamese Sign Language).

> **⚠️ QUAN TRỌNG:** Trước khi chạy ứng dụng, bạn phải download `VnCoreNLP-1.1.1.jar` và thư mục `models/` từ trang chính thức: https://github.com/vncorenlp/VnCoreNLP

## 🚀 Cài đặt và Thiết lập

### Bước 1: Download các file cần thiết

**Quan trọng:** Trước khi chạy ứng dụng, bạn cần download các file sau từ trang chính thức VnCoreNLP:

#### 1. Download VnCoreNLP JAR file
```bash
# Truy cập: https://github.com/vncorenlp/VnCoreNLP
# Download file: VnCoreNLP-1.1.1.jar
# Đặt file này vào thư mục gốc của project
```

#### 2. Download models folder
```bash
# Truy cập: https://github.com/vncorenlp/VnCoreNLP
# Download toàn bộ thư mục models/ 
# Đặt thư mục models/ vào thư mục gốc của project
```

**Cấu trúc thư mục sau khi download:**
```
VSL Converter/
├── VnCoreNLP-1.1.1.jar         # File JAR cần download
├── models/                      # Thư mục models cần download
│   ├── dep/
│   ├── ner/
│   ├── postagger/
│   └── wordsegmenter/
├── app/
├── web/
└── ...
```

### Bước 2: Cài đặt dependencies

## 🐛 Troubleshooting

**Local:**
- Đảm bảo Java đã cài đặt: `java -version`
- Kiểm tra Python: `python --version`
- Đảm bảo đã download VnCoreNLP-1.1.1.jar và thư mục models/
- Cài đặt dependencies: `pip install -r requirements.txt`

### Chạy local (Development)

**Yêu cầu:** 
- Python 3.11+, Java 11+
- VnCoreNLP-1.1.1.jar và thư mục models/ đã được download (xem Bước 1 ở trên)

```bash
# Tạo virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# hoặc
venv\Scripts\activate     # Windows

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy server
python run_server.py
```

**Truy cập:**
- Website: Mở file `web/index.html` trong trình duyệt
- API: http://localhost:8000

### � Cách 3: Chỉ chạy logic chuyển đổi

Nếu bạn chỉ muốn sử dụng logic chuyển đổi mà không cần web interface:

```python
from app.convert2VSL import VietnameseToVSLConverter

# Khởi tạo converter
converter = VietnameseToVSLConverter()

# Chuyển đổi câu
result = converter.convert("Tôi đang ăn cơm")
print(result)  # Output: "TÔI CƠM ĐANG ĂN"
```

## 🌐 Sử dụng website

Website có 3 tab chính:

- **🚀 Chuyển đổi:** Nhập câu tiếng Việt và xem kết quả VSL
- **🏷️ POS Tags:** Bảng định nghĩa các loại từ
- **📚 Nguyên lý VSL:** Giải thích cách chuyển đổi

## 📡 API Endpoints

### POST `/convert`
```bash
curl -X POST "http://localhost:8000/convert" \
     -H "Content-Type: application/json" \
     -d '{"text": "Tôi đang ăn cơm"}'
```

**Response:**
```json
{
  "input": "Tôi đang ăn cơm",
  "tokens": ["Tôi - PRON", "đang - PART", "ăn - VERB", "cơm - NOUN"],
  "gloss": "TÔI CƠM ĐANG ĂN",
  "status": "success"
}
```

### GET `/health`
Kiểm tra trạng thái API server

### GET `/docs`
Swagger UI documentation
## 🛠️ Cấu trúc project

```
AL4project/
├── app/                          # Logic ứng dụng
│   ├── vsl_api.py               # FastAPI server
│   ├── convert2VSL.py           # Logic chuyển đổi VSL
│   ├── pos_tagger.py            # POS tagging
│   └── Data/                    # Dữ liệu từ điển
│       ├── ASK_WORDS.txt        # Từ nghi vấn
│       └── NEG_WORDS.txt        # Từ phủ định
├── web/                         # Frontend
│   └── index.html               # Website interface
├── models/                      # VnCoreNLP models
├── docs/                        # Tài liệu
├── Dockerfile                   # Docker image config
├── docker-compose.yml           # Docker compose config
├── requirements.txt             # Python dependencies
├── nginx.conf                   # Nginx config (optional)
├── run_server.py                # Server startup script
└── VnCoreNLP-1.1.1.jar         # VnCoreNLP Java library
```

## ⚙️ Requirements

**Local Development:**
- Python 3.11+
- Java 11+ (cho VnCoreNLP)
- **VnCoreNLP-1.1.1.jar** (download từ https://github.com/vncorenlp/VnCoreNLP)
- **Thư mục models/** (download từ https://github.com/vncorenlp/VnCoreNLP)
- Dependencies trong `requirements.txt`


**Local:**
- Đảm bảo Java đã cài đặt: `java -version`
- Kiểm tra Python: `python --version`
- Cài đặt dependencies: `pip install -r requirements.txt`

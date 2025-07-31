# VSL Converter - Technical Documentation

## 📋 Chi tiết POS Tags và Dependency Labels

### POS Tags (Part-of-Speech)

#### Danh từ (Nouns)
- **N**: Danh từ thường (cơm, nước, sách)
- **Np**: Danh từ riêng (Hà Nội, Minh Quang, Việt Nam)
- **Nc**: Danh từ chỉ loại (cái, con, chiếc)
- **Nu**: Danh từ đơn vị (lít, mét, người)
- **Ny**: Danh từ viết tắt (TP.HCM, USA)
- **Nb**: Danh từ mượn (internet, smartphone)

#### Động từ (Verbs)
- **V**: Động từ thường (ăn, đi, làm, nói)
- **Vb**: Động từ mượn (download, update)

#### Tính từ và Trạng từ
- **A**: Tính từ (đẹp, tốt, cao, nhỏ)
- **R**: Trạng từ (nhanh, chậm, rất, cũng)

#### Đại từ và Từ chỉ định
- **P**: Đại từ (tôi, bạn, chúng ta, nó)
- **L**: Từ hạn định (những, các, một, mỗi)

#### Số từ và Giới từ
- **M**: Số từ (một, hai, nhiều, ít)
- **E**: Giới từ (ở, từ, với, tại, trong)

#### Liên từ
- **C**: Liên từ phụ thuộc (rằng, nếu, khi, vì)
- **Cc**: Liên từ đẳng lập (và, hoặc, nhưng, mà)

#### Khác
- **I**: Thán từ (ôi, ồ, ái, chà)
- **T**: Trợ từ (đã, rồi, sẽ, đang)
- **Y**: Ký hiệu (%, $, &, @)
- **Z**: Hình vị phụ thuộc (chẳng, chả)
- **X**: Không phân loại
- **CH**: Dấu câu (. , ! ? : ;)

### Dependency Labels

#### Quan hệ cơ bản
- **root**: Động từ chính của câu
- **sub**: Chủ ngữ
- **dob**: Tân ngữ trực tiếp
- **iob**: Tân ngữ gián tiếp
- **prd**: Vị ngữ

#### Quan hệ bổ nghĩa
- **amod**: Bổ nghĩa tính từ
- **nmod**: Bổ ngữ cho danh từ
- **vmod**: Bổ nghĩa động từ
- **pmod**: Bổ nghĩa của giới từ

#### Quan hệ đặc biệt
- **adv**: Trạng ngữ
- **det**: Từ hạn định
- **loc**: Chỉ nơi chốn
- **tmp**: Trạng ngữ thời gian
- **mnr**: Cách thức
- **dir**: Hướng
- **prp**: Mục đích

#### Quan hệ cú pháp
- **conj**: Liên từ
- **coord**: Từ điều phối
- **pob**: Tân ngữ của giới từ
- **punct**: Dấu câu
- **dep**: Nhãn mặc định

## 🔄 Quy trình chuyển đổi VSL

### Bước 1: Tokenization và POS Tagging
```python
# VnCoreNLP phân tích câu thành tokens với POS tags
sentence = "Tôi đang ăn cơm"
tokens = [
    {"form": "Tôi", "posTag": "P", "depLabel": "sub"},
    {"form": "đang", "posTag": "T", "depLabel": "vmod"},
    {"form": "ăn", "posTag": "V", "depLabel": "root"},
    {"form": "cơm", "posTag": "N", "depLabel": "dob"}
]
```

### Bước 2: Phân loại cấu trúc
```python
structure = {
    'S': ['Tôi'],           # Subject (Chủ ngữ)
    'V': ['đang', 'ăn'],    # Verb (Động từ)
    'O': ['cơm'],           # Object (Tân ngữ)
    'NUM': [],              # Number (Số từ)
    'TIME': [],             # Time (Thời gian)
    'ASK': [],              # Question (Câu hỏi)
    'NEG': [],              # Negation (Phủ định)
    'OTHER': []             # Other (Khác)
}
```

### Bước 3: Sắp xếp theo thứ tự VSL
```python
# Thứ tự VSL: TIME → S → O → NUM → V → OTHER → ASK → NEG
vsl_order = ['TIME', 'S', 'O', 'NUM', 'V', 'OTHER', 'ASK', 'NEG']
result = "TÔI CƠM ĐANG ĂN"
```

## 📊 Thống kê từ đặc biệt

### Từ nghi vấn (ASK_WORDS.txt)
- ai, gì, nào, đâu, khi, nào, như thế nào
- bao nhiêu, có...không, có phải...không
- tại sao, vì sao, làm sao

### Từ phủ định (NEG_WORDS.txt)
- không, chẳng, chả, chưa
- đừng, đừng có, đừng nên
- không thể, không được

## 🎨 Màu sắc POS Tags trong giao diện

| POS Type | Màu nền | Màu chữ | Mô tả |
|----------|---------|---------|-------|
| NOUN | Xanh nhạt | Xanh đậm | Danh từ |
| PROPN | Tím nhạt | Tím đậm | Danh từ riêng |
| VERB | Xanh lá nhạt | Xanh lá đậm | Động từ |
| ADJ | Cam nhạt | Cam đậm | Tính từ |
| ADV | Hồng nhạt | Hồng đậm | Trạng từ |
| PRON | Xanh lục nhạt | Xanh lục đậm | Đại từ |
| NUM | Xanh lá nhạt | Xanh lá đậm | Số từ |
| DET | Xanh tím nhạt | Xanh tím đậm | Từ hạn định |

## 🚀 API Endpoints chi tiết

### GET /
Health check endpoint trả về thông tin cơ bản về API.

### GET /health
Kiểm tra chi tiết trạng thái của converter và thực hiện test conversion.

### POST /convert
**Input:**
```json
{
  "text": "Câu tiếng Việt cần chuyển đổi"
}
```

**Output (Success):**
```json
{
  "input": "Tôi đang ăn cơm",
  "tokens": ["Tôi - PRON", "đang - PART", "ăn - VERB", "cơm - NOUN"],
  "gloss": "TÔI CƠM ĐANG ĂN",
  "status": "success"
}
```

**Output (Error):**
```json
{
  "error": "Conversion failed: Error message",
  "status": "error"
}
```

## 🔧 Cấu hình và Tùy chỉnh

### Thêm từ nghi vấn mới
Chỉnh sửa file `app/Data/ASK_WORDS.txt`:
```
ai
gì
nào
...
từ_mới
```

### Thêm từ phủ định mới
Chỉnh sửa file `app/Data/NEG_WORDS.txt`:
```
không
chẳng
chả
...
từ_phủ_định_mới
```

### Tùy chỉnh mapping POS
Chỉnh sửa file `app/pos_tagger.py`:
```python
POS_MAP = {
    'Np': 'PROPN',
    'N': 'NOUN',
    # Thêm mapping mới
    'Custom': 'CUSTOM_TYPE'
}
```

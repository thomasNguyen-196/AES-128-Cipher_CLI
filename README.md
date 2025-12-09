# AES-128 Cipher CLI Tool

## Giới thiệu

Công cụ dòng lệnh (CLI) cho việc mã hóa và giải mã văn bản bằng thuật toán AES-128 (Advanced Encryption Standard, 128-bit key). Dự án này được khởi tạo từ khung CLI refactor sẵn có, giúp bạn nhanh chóng thử nghiệm AES trên văn bản.

## Tính năng

- Mã hóa/giải mã văn bản sử dụng AES-128 (block 128 bit, key 128 bit).
- Hỗ trợ mode ECB (PKCS#7 padding) và CFB (không padding, xử lý chuỗi dài bất kỳ).
- CFB dùng IV 16 byte (32 hex hoặc 16 ký tự); nếu không nhập IV khi encrypt, chương trình tự sinh. Ciphertext CFB trả về IV và ciphertext tách biệt (hex).
- Nhập văn bản trực tiếp, từ stdin (pipe) hoặc từ file.
- Giao diện dòng lệnh thân thiện, có tùy chọn copy ra clipboard / lưu file.

## Yêu cầu

- Python 3.10+ (type hints dùng `|` syntax, trùng với `pyproject.toml`).
- Các thư viện giao diện tùy chọn: `pyfiglet`, `colorama`, `pyperclip` (nếu cài sẽ có banner/màu/copy clipboard).

## Cài đặt và chạy

1. Cài đặt (editable):
   ```bash
   pip install -e .
   ```
2. Chạy chương trình:
   ```bash
   aes
   ```
   (entry-point đã đổi sang lệnh `aes`; bạn có thể đổi lại tùy ý trong `pyproject.toml`).

## Ghi chú

- Đã triển khai AES-128 core với ECB/CFB; ciphertext/IV hiển thị dạng hex tách biệt. CFB decrypt yêu cầu IV nhập thủ công (hoặc dùng IV đã trả ở kết quả encrypt).
- Plaintext/key/IV có thể nhập dưới dạng text (UTF-8) hoặc hex (key/IV: 32 hex = 16 byte).

# Nhận diện thực thể trong văn bản tiếng Việt

## Giới thiệu
Dự án này sử dụng mô hình LSTM để nhận diện thực thể có tên (Named Entity Recognition - NER) trong văn bản tiếng Việt. Đây là một nhiệm vụ quan trọng trong xử lý ngôn ngữ tự nhiên (NLP), giúp trích xuất thông tin từ văn bản.

## Công nghệ sử dụng
- **LSTM (Long Short-Term Memory)**: Mạng nơ-ron hồi tiếp (RNN) mạnh mẽ cho các bài toán xử lý chuỗi.
- **TensorFlow/Keras**: Thư viện học sâu để xây dựng và huấn luyện mô hình.
- **Pandas & NumPy**: Xử lý dữ liệu đầu vào.

## Cách cài đặt và chạy dự án

### 1. Cài đặt môi trường
Trước tiên, cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

### 2. Huấn luyện mô hình
Dự án bao gồm tệp notebook `Code_LSTM.ipynb` chứa các bước huấn luyện mô hình. Để huấn luyện, chạy lệnh sau:
```bash
jupyter notebook Code_LSTM.ipynb
```

### 3. Dự đoán với mô hình đã huấn luyện
Chạy file notebook để thực hiện dự đoán trên dữ liệu mới:
```bash
jupyter notebook Code_LSTM.ipynb
```

## Cấu trúc thư mục
```
├── dataset/  # Chứa dữ liệu huấn luyện
├── Code_LSTM.ipynb  # Notebook huấn luyện và dự đoán
├── utils.py  # Các hàm hỗ trợ xử lý dữ liệu
├── __pycache__/  # Cache của Python
└── README.md  # Tài liệu hướng dẫn
```

## Đóng góp
Bạn có thể fork repository này và tạo pull request để đóng góp.

## Giấy phép
Dự án này được phát hành theo giấy phép MIT.


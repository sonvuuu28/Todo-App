Mini Todo App
Một ứng dụng Todo List siêu đơn giản được xây dựng bằng Python, MySQL và được đóng gói toàn bộ trong Docker để bạn có thể dễ dàng cài đặt, chạy và bàn giao cho người dùng.

🌟 Mục Tiêu Dự Án
Tính năng chính:

Thêm công việc: Cho phép người dùng thêm todo mới.

Xóa công việc: Xoá các công việc không cần thiết.

Đánh dấu hoàn thành: Cho phép đánh dấu (tick) công việc đã hoàn thành.

Mục đích:

Ôn tập và thực hành các lệnh Docker, sử dụng docker-compose để cấu hình môi trường phát triển và triển khai.

Tạo một ứng dụng nhỏ gọn, dễ duy trì và bàn giao.

🚀 Công Nghệ Sử Dụng
Python: Xử lý backend (Flask) cho API đơn giản.

MySQL: Cơ sở dữ liệu lưu trữ danh sách công việc.

Docker & Docker Compose: Đóng gói ứng dụng thành các container, đảm bảo tính nhất quán giữa các môi trường.

📁 Cấu Trúc Dự Án
less
Sao chép
Chỉnh sửa
mini_todo_app/
├── docker-compose.yml    # Định nghĩa các service: web (Python) và db (MySQL)
├── README.md             # Tài liệu hướng dẫn và mô tả dự án (bạn đang đọc đây)
└── app
    ├── Dockerfile        # Cách build image cho ứng dụng Python
    ├── requirements.txt  # Danh sách các package Python cần cài
    └── main.py           # Code chính của ứng dụng (Flask API)
🛠 Hướng Dẫn Cài Đặt & Chạy Ứng Dụng
1. Clone Repository
bash
Sao chép
Chỉnh sửa
git clone https://github.com/your_username/mini_todo_app.git
cd mini_todo_app
2. Khởi Động Ứng Dụng
Dùng Docker Compose để build và chạy toàn bộ ứng dụng:

bash
Sao chép
Chỉnh sửa
docker-compose up --build
web container: Chạy ứng dụng Python (Flask).

db container: Chạy MySQL.

3. Tạo Bảng CSDL
Nếu chưa sử dụng file init, hãy tạo bảng todos thủ công:

Kết nối vào container MySQL:

bash
Sao chép
Chỉnh sửa
docker exec -it mysql_todo mysql -u todo_user -p
(Nhập mật khẩu: todo_pass)

Trong MySQL shell, chọn database và tạo bảng:

sql
Sao chép
Chỉnh sửa
USE tododb;
CREATE TABLE todos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    completed BOOLEAN DEFAULT FALSE
);
4. Kiểm Tra Ứng Dụng
API Endpoints:

GET /todos: Lấy danh sách các công việc.

POST /todos: Thêm mới một công việc (cần JSON body: {"title": "Công việc cần làm"}).

DELETE /todos/<id>: Xoá một công việc theo ID.

PATCH /todos/<id>: (Nếu có) Đánh dấu hoàn thành / bỏ hoàn thành công việc.

Truy cập API qua: http://localhost:5000

📚 Một Số Lệnh Docker Thường Dùng
Build lại các container:

bash
Sao chép
Chỉnh sửa
docker-compose up --build
Kiểm tra logs:

bash
Sao chép
Chỉnh sửa
docker-compose logs -f
Dừng các container:

bash
Sao chép
Chỉnh sửa
docker-compose down
💡 Gợi Ý Mở Rộng
Giao diện người dùng: Tích hợp frontend bằng React/Vue để tạo giao diện trực quan.

Xử lý xác thực: Thêm cơ chế đăng nhập/đăng ký.

Thông báo: Thêm thông báo realtime khi có thay đổi công việc (có thể dùng WebSocket).

👨‍💻 Lời Kết
Dự án Mini Todo App không chỉ giúp bạn ôn tập kiến thức Docker mà còn là một ví dụ nhỏ về cách kết hợp Python và MySQL để tạo ra một ứng dụng web thực tế. Hãy cảm thấy tự do để fork, đóng góp và mở rộng thêm các tính năng theo ý bạn!

Happy Coding! 🚀
Bài Tập CNN với Bộ Dữ Liệu MNIST
Mô tả
Đây là bài thực hành áp dụng mạng nơ-ron tích chập (CNN) để phân loại ảnh chữ số viết tay từ tập dữ liệu MNIST. Bài tập gồm 4 câu hỏi yêu cầu điều chỉnh mô hình và quan sát sự thay đổi.

Các nội dung chính:

Câu 1: Thay đổi số lượng epoch.

Câu 2: Thêm một tầng tích chập thứ ba.

Câu 3: So sánh các learning rate khác nhau.

Câu 4: Vẽ feature map từ các tầng tích chập.

Cấu trúc thư mục
Tên file	Mô tả
MNIST_CNN.ipynb	Notebook chứa toàn bộ code, biểu đồ, kết quả và giải thích từng câu
README.md	Mô tả nội dung và hướng dẫn chạy bài tập

Hướng dẫn chạy
Cài đặt các thư viện cần thiết (nếu chưa cài):

bash
Sao chép
Chỉnh sửa
pip install torch torchvision matplotlib
Mở Jupyter Notebook:

bash
Sao chép
Chỉnh sửa
jupyter notebook MNIST_CNN.ipynb
Chạy lần lượt từng ô mã lệnh để quan sát kết quả và biểu đồ.

Chi tiết từng câu
Câu 1: Thay đổi số lượng epoch
Sửa số epoch từ 5 thành 10 trong vòng lặp huấn luyện.

Kết quả:

Độ chính xác trên tập test tăng nhẹ.

Biểu đồ loss giảm đều trong vài epoch đầu, sau đó chững lại.

Giải thích:
Số epoch lớn giúp mô hình học lâu hơn và có thể cải thiện độ chính xác, nhưng cũng có nguy cơ bị quá khớp (overfitting).

Câu 2: Thêm tầng tích chập conv3
Thêm tầng conv3 (Conv2d(32, 64, 3)) vào mô hình.

Cập nhật lại kiến trúc tầng fully connected fc1 phù hợp với kích thước đầu ra mới.

Kết quả:

Độ chính xác tăng rõ rệt so với mô hình ban đầu.

Giải thích:
Tầng tích chập thứ ba giúp mạng học được các đặc trưng phức tạp hơn, từ đó nâng cao khả năng phân loại.

Câu 3: Thử các learning rate khác nhau
Thử lần lượt learning_rate = 0.001, 0.01, 0.1.

Kết quả:

0.001: học chậm, loss giảm ít, độ chính xác thấp.

0.01: học ổn định, độ chính xác cao.

0.1: loss dao động mạnh, có thể không hội tụ.

Giải thích:
Learning rate quá nhỏ khiến mô hình học chậm, quá lớn làm mất ổn định; cần chọn mức vừa phải để hội tụ nhanh và chính xác.

Câu 4: Vẽ feature map từ conv1 và conv2
Chỉnh sửa hàm visualize_feature_map để hiển thị thêm 2 kênh đầu từ tầng conv2.

Kết quả:

Các feature map từ conv2 chi tiết hơn, mang tính trừu tượng cao hơn so với conv1.

Giải thích:
Tầng tích chập sau thường học các đặc trưng phức tạp hơn như đường cong, góc cạnh và cấu trúc vùng ảnh thay vì chỉ các cạnh đơn giản.



# Bài Lab: Thuật Toán Di Truyền (Genetic Algorithm)

## Mục tiêu

Bài lab giúp mình hiểu và áp dụng thuật toán di truyền (Genetic Algorithm - GA) để giải các bài toán tối ưu hóa. Cụ thể:

- Nắm được nguyên lý hoạt động của GA.
- Viết code áp dụng GA để tối ưu hàm một biến và nhiều biến.
- So sánh các phương pháp lựa chọn trong GA.
- Trực quan hóa quá trình tiến hóa và sự phân bố quần thể.
- Phân tích ảnh hưởng của các tham số như kích thước quần thể, tỉ lệ đột biến, lai ghép.

## Lý thuyết cơ bản

GA là thuật toán tối ưu dựa trên tiến hóa sinh học. Các bước chính:

1. Khởi tạo quần thể ngẫu nhiên.
2. Đánh giá độ thích nghi (fitness).
3. Lựa chọn cha mẹ (Tournament hoặc Roulette).
4. Lai ghép (crossover) để tạo cá thể con.
5. Đột biến (mutation) để duy trì đa dạng.
6. Lặp lại các bước trên qua nhiều thế hệ.

## Nội dung thực hành

### Ví dụ 1: Tối ưu hàm bậc hai

Tối đa hóa:
f(x) = -x^2 + 10x + 50, với x ∈ [0, 10]

less
Sao chép
Chỉnh sửa

Kỳ vọng: x → 5, f(x) → 75.

### Ví dụ 2: Tối ưu hàm hai biến

Tối thiểu hóa:
g(x, y) = x^2 + y^2, với x, y ∈ [-5, 5]

less
Sao chép
Chỉnh sửa

Kỳ vọng: (x, y) → (0, 0), g(x, y) → 0.

### Bài tập 1: Hàm sin + cos

Tối đa hóa:
h(x) = sin(x) + cos(x), x ∈ [0, 2π]

less
Sao chép
Chỉnh sửa

Làm 2 cách:
- Sử dụng số thực + tournament selection.
- Mã nhị phân + roulette selection.

Kỳ vọng: h(x) → √2 ≈ 1.4142 tại x ≈ π/4.

### Bài tập 2: Ảnh hưởng tham số

Thay đổi các giá trị:
- `pop_size`: 10, 50, 100
- `mutation_rate`: thấp/cao
- `crossover_rate`: thấp/cao

Quan sát tốc độ hội tụ và chất lượng lời giải.

### Bài tập 3: So sánh lựa chọn

So sánh:
- Tournament Selection
- Roulette Wheel Selection

Nhận xét ưu nhược điểm từng phương pháp.

### Bài tập 4: Trực quan hóa 3D

Tối ưu:
k(x, y, z) = x^2 + y^2 + z^2

less
Sao chép
Chỉnh sửa

Vẽ biểu đồ phân bố quần thể 3D theo từng thế hệ.


## Kết luận

Qua bài lab này, mình đã hiểu rõ hơn về GA và cách hoạt động của các thành phần như chọn lọc, lai ghép, đột biến. Bên cạnh đó, mình cũng thấy được vai trò của các tham số trong quá trình hội tụ, và biết cách sử dụng GA để giải các bài toán tối ưu một cách hiệu quả hơn.

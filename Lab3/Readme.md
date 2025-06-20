Mô tả bài toán
Bài toán N-Queens là một trong những bài toán kinh điển trong lĩnh vực trí tuệ nhân tạo, sử dụng thuật toán quay lui (backtracking) để tìm tất cả các cách đặt N quân hậu trên bàn cờ NxN sao cho không có quân hậu nào tấn công lẫn nhau.
Quy tắc tấn công của quân hậu:
Theo hàng ngang
Theo cột dọc
Theo đường chéo chính và phụ
Bài toán 4-Queens
Mục tiêu:
Tìm tất cả các cấu hình hợp lệ để đặt 4 quân hậu trên bàn cờ 4x4.
Kết quả:
Tổng số lời giải: 2
Ví dụ lời giải:
[1, 3, 0, 2]: tương đương với các quân hậu đặt tại vị trí (cột, hàng): [(1,0), (3,1), (0,2), (2,3)]
[2, 0, 3, 1]: tương đương với vị trí: [(2,0), (0,1), (3,2), (1,3)]
Bài toán 8-Queens
Mục tiêu:
Tìm tất cả các lời giải hợp lệ cho việc đặt 8 quân hậu trên bàn cờ 8x8.
Kết quả:
Tổng số lời giải: 92
Ví dụ 2 lời giải ngẫu nhiên:
[0, 6, 3, 5, 7, 1, 4, 2]
⇒ Vị trí (cột, hàng): [(0,0), (6,1), (3,2), (5,3), (7,4), (1,5), (4,6), (2,7)]
[7, 2, 0, 5, 1, 4, 6, 3]
⇒ Vị trí (cột, hàng): [(7,0), (2,1), (0,2), (5,3), (1,4), (4,5), (6,6), (3,7)]
Công nghệ sử dụng:
Ngôn ngữ: Python
Thư viện: numpy, random
Cấu trúc chương trình

# is_valid_state(state, num_queens): Kiểm tra trạng thái hiện tại có hợp lệ hay không.
# get_candidates(state, num_queens): Trả về các cột có thể đặt hậu tiếp theo.
# search(state, solutions, num_queens): Đệ quy/backtracking để tìm lời giải.
# solve(num_queens): Hàm chính để giải bài toán và trả về danh sách lời giải.
# print_board(solution): In bàn cờ từ lời giải.
▶Cách chạy chương trình
bash
python queens.py
Sau đó nhập số lượng quân hậu N = 4 hoặc N = 8.
Ghi chú:
Bài toán được triển khai với phương pháp backtracking để tối ưu tìm kiếm.
Cấu trúc state = [col_0, col_1, ..., col_n] đại diện cho vị trí cột của quân hậu ở mỗi hàng.

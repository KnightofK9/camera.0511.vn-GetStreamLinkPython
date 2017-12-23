# coding=utf-8
from Extractor import Extractor

extractor = Extractor()

# Nếu muốn check lại các url còn sống chạy hàm này
# extractor.check_all_avail_stream_file()

# Xem tất cả link stream của website camera.0511.vn
# print extractor.avail_list

# Lấy 1 random url dẫn đến link stream của website camera.0511.vn, url này dùng cho hàm cv2.VideoCapture(url)
print extractor.get_random_avail_stream_file()
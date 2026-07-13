chạy được trương trình bằng lệnh uvicorn main:app-reload
test được api trên swagger
kết nối được fast api với sql
database tên là student_db
bảng student:
id - int - khóa chính tự tăng
full_name - str 
class_name - str
email - str
phone_number - str
Bảng danh sách API
1.kiểm tra server - GET (Không truyền tham số, message trả về "API đang chạy" ,data là null) - endpoint: /
2.Lấy danh sách sinh viên - GET (Không truyền tham số, data trả về 1 mảng danh sách) endpoint: /students
3.Tìm kiếm sinh viên theo lớp - GET (nhận từ khóa class_name qua Querry parameter, data trả về danh sách sinh viên) endpoint: /students/search?class_name=....
4.lấy chi tiết sinh viên -GET (nhận id qua path parameter,nếu k thấy trả về status code:404 , error "Not found" và message:"không tìm thấy sinh viên") endpoint: /students/{student_id}
5.thêm sinh viên mới - POST(nhận dữ liệu qua request body, (pydatic model không kèm id).Khi thành công , trả về status code 201, data chứa thông tin sinh viên vừa tạo kèm id tự tăng) endpoint: /students
6.cập nhật sinh viên - PUT
7.xóa sinh viên - DELETE(nhận id qua path parameter và dữ liệu thay đổi qua request body.Nếu không tồn tại trả lỗi 404 và tương tự API 4) endpoint: /students/{student_id}
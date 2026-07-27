---
title: "Worklog Tuần 5"
date: 2026-07-13
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---


### Mục tiêu tuần 5:

* Thiết kế schema cơ sở dữ liệu cho phần dữ liệu cốt lõi của ứng dụng web.
* Khởi tạo cơ sở dữ liệu quan hệ được quản lý bằng Amazon RDS trong subnet private và kết nối an toàn với ứng dụng.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Thiết kế schema database (bảng, quan hệ) cho ứng dụng. | 13/07/2026 | 13/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - Tìm hiểu khái niệm Amazon RDS và khởi tạo RDS instance (MySQL/PostgreSQL) trong subnet private. | 14/07/2026 | 14/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - Giới hạn quyền truy cập database chỉ từ Security Group của app server. | 15/07/2026 | 15/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - Cấu hình thông tin đăng nhập database an toàn (biến môi trường hoặc AWS Secrets Manager) và kết nối ứng dụng với RDS. | 16/07/2026 | 16/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - Kiểm tra các thao tác thêm/đọc/sửa/xóa (CRUD) dữ liệu thông qua ứng dụng. | 17/07/2026 | 17/07/2026 | <https://cloudjourney.awsstudygroup.com/> |


### Kết quả đạt được tuần 5:

* Thiết kế và triển khai schema database 
* Khởi tạo RDS instance trong subnet private, chỉ truy cập được từ Security Group của ứng dụng.
* Kết nối thành công ứng dụng với RDS, kiểm tra các thao tác CRUD hoạt động đúng.

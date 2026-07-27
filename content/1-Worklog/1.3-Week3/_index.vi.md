---
title: "Worklog Tuần 3"
date: 2026-06-29
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---


### Mục tiêu tuần 3:

* Khởi tạo EC2 instance trong VPC đã tạo ở tuần 2 để chạy ứng dụng web.
* Deploy code ứng dụng viết local trong VSCode lên EC2 instance và kiểm tra chạy đúng.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Tìm hiểu khái niệm EC2 (instance types, AMI, EBS, Elastic IP). | 29/06/2026 | 29/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - Khởi tạo EC2 instance trong subnet public, gắn Security Group tầng web. | 30/06/2026 | 30/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - Kết nối SSH và cài đặt môi trường runtime (Python/Node.js) và reverse proxy (Nginx). | 01/07/2026 | 01/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - Deploy code ứng dụng từ VSCode local lên EC2 instance (qua Git hoặc `scp`). | 02/07/2026 | 02/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - Kiểm tra ứng dụng chạy bằng cách truy cập public IP/domain của instance. | 03/07/2026 | 03/07/2026 | <https://cloudjourney.awsstudygroup.com/> |


### Kết quả đạt được tuần 3:

* Khởi tạo và cấu hình thành công EC2 instance chạy Amazon Linux/Ubuntu trong subnet public.
* Cài đặt runtime cho ứng dụng và reverse proxy, cấu hình instance phục vụ ứng dụng qua port 80/443.
* Deploy ứng dụng từ môi trường VSCode local lên EC2 và xác nhận truy cập được từ trình duyệt.

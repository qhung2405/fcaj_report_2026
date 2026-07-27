---
title: "Worklog Tuần 4"
date: 2026-07-06
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---


### Mục tiêu tuần 4:

* Tạo và cấu hình S3 bucket để lưu trữ static assets và/hoặc file người dùng upload cho ứng dụng.
* Tích hợp code ứng dụng với S3 bằng AWS SDK để có thể upload/lấy file trực tiếp từ ứng dụng.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Tìm hiểu khái niệm Amazon S3 (bucket, object, phân quyền). | 06/07/2026 | 06/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - Tạo S3 bucket với cấu trúc tên và thư mục phù hợp. | 07/07/2026 | 07/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - Cấu hình bucket policy/IAM policy để chỉ ứng dụng (qua IAM role) mới có quyền ghi vào bucket. | 08/07/2026 | 08/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - Tích hợp AWS SDK (boto3/AWS SDK for JavaScript) vào ứng dụng để upload/download file. | 09/07/2026 | 09/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - Kiểm tra upload và lấy file thông qua ứng dụng. | 10/07/2026 | 10/07/2026 | <https://cloudjourney.awsstudygroup.com/> |


### Kết quả đạt được tuần 4:

* Tạo và cấu hình thành công S3 bucket để lưu static assets / file người dùng upload cho ứng dụng.
* Áp dụng bucket policy và IAM permission theo nguyên tắc quyền hạn tối thiểu để app server truy cập S3 an toàn.
* Tích hợp S3 vào code ứng dụng, kiểm tra chức năng upload/download hoạt động đầy đủ.

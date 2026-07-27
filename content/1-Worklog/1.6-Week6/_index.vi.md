---
title: "Worklog Tuần 6"
date: 2026-07-20
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---


### Mục tiêu tuần 6:

* Bổ sung bảng DynamoDB để lưu dữ liệu phi quan hệ phù hợp với ứng dụng.
* Thiết lập CloudWatch để giám sát EC2, RDS và ứng dụng, xác nhận toàn bộ nhóm dịch vụ AWS bắt buộc hoạt động cùng nhau.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Tìm hiểu khái niệm DynamoDB (partition key, sort key) và thiết kế bảng. | 20/07/2026 | 20/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - Tạo bảng DynamoDB và tích hợp vào ứng dụng bằng AWS SDK. | 21/07/2026 | 21/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - Tìm hiểu khái niệm CloudWatch và cài đặt/bật CloudWatch Agent trên EC2 instance. | 22/07/2026 | 22/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - Thiết lập log group CloudWatch và tạo alarm cho CPU, bộ nhớ, kết nối database. | 23/07/2026 | 23/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - Rà soát và xác nhận toàn bộ nhóm dịch vụ bắt buộc (IAM, VPC, EC2, S3, RDS, DynamoDB, CloudWatch, AWS CLI) hoạt động đồng bộ. | 24/07/2026 | 24/07/2026 | <https://cloudjourney.awsstudygroup.com/> |


### Kết quả đạt được tuần 6:

* Tạo và tích hợp thành công bảng DynamoDB xử lý **[loại dữ liệu]**, hoạt động song song với RDS cho dữ liệu quan hệ.
* Thiết lập giám sát CloudWatch: dashboard metric, log group cho log ứng dụng, và alarm cho các ngưỡng quan trọng (CPU, bộ nhớ, tỷ lệ lỗi).
* Xác nhận toàn bộ nhóm dịch vụ AWS bắt buộc (IAM, VPC, EC2, S3, RDS, DynamoDB, CloudWatch, AWS CLI) đã được cấu hình và hoạt động cùng nhau.

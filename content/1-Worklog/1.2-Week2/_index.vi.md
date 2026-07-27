---
title: "Worklog Tuần 2"
date: 2026-06-22
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---


### Mục tiêu tuần 2:

* Thiết kế kiến trúc mạng cho ứng dụng web: VPC, subnet, route table, Internet Gateway, NAT Gateway.
* Cấu hình Security Group để kiểm soát traffic giữa tầng web và tầng database.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Tìm hiểu khái niệm Amazon VPC (VPC, subnet, Availability Zone, route table). | 22/06/2026 | 22/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - Tạo custom VPC với subnet public và private trên nhiều Availability Zone. | 23/06/2026 | 23/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - Cấu hình Internet Gateway và route table cho subnet public. | 24/06/2026 | 24/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - Cấu hình NAT Gateway và route table cho subnet private. | 25/06/2026 | 25/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - Tạo Security Group cho tầng web và tầng database theo nguyên tắc quyền hạn tối thiểu. | 26/06/2026 | 26/06/2026 | <https://cloudjourney.awsstudygroup.com/> |


### Kết quả đạt được tuần 2:

* Thiết kế và khởi tạo thành công custom VPC với subnet public (cho máy chủ web/app) và subnet private (cho database).
* Cấu hình Internet Gateway và NAT Gateway để tài nguyên trong subnet private vẫn truy cập được internet mà không bị lộ ra ngoài.
* Tạo Security Group theo nguyên tắc quyền hạn tối thiểu (ví dụ: chỉ mở port 80/443 từ internet, chỉ cho phép port database từ Security Group của app server).

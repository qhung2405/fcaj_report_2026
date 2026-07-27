---
title : "Blog 1"
date : "2026-07-27"
weight : 1
chapter : false
pre : " <b> 3.1. </b> "
---

# GIỚI THIỆU AMAZON VPC REGIONAL NAT GATEWAY

AWS NAT Gateway là dịch vụ dịch địa chỉ mạng (NAT) được quản lý hoàn toàn, có tính sẵn sàng cao, giúp các tài nguyên trong private subnet có thể khởi tạo kết nối ra ngoài mà không cần địa chỉ IP công khai riêng. Vào tháng 11/2025, AWS công bố một chế độ hoạt động mới cho NAT Gateway: Regional NAT Gateway (RNAT) — cho phép một NAT Gateway duy nhất tự động mở rộng và thu hẹp phạm vi hoạt động qua nhiều Availability Zone (AZ) trong cùng một VPC, thay vì phải triển khai riêng lẻ theo từng AZ như trước.

![Blog 1]({{< relURL "images/image1.png" >}})

### Những điểm chính cần biết

- Trước đây, mỗi AZ cần một NAT Gateway riêng, đặt trong public subnet riêng, và phải lặp lại quy trình này mỗi khi mở rộng sang AZ mới.
- Regional NAT Gateway hoạt động ở cấp độ VPC thay vì cấp độ subnet/AZ, giúp giảm đáng kể số lượng thành phần cần quản lý.
- RNAT không yêu cầu phải có public subnet trong mọi AZ để lưu trú.
- Khi mở rộng sang AZ mới, người dùng có thể tái sử dụng cùng một route table và cùng một NAT Gateway ID thay vì tạo mới.
- RNAT tự động duy trì "zonal affinity" (ưu tiên định tuyến trong cùng AZ) để đảm bảo tính sẵn sàng cao trong khi vẫn đơn giản hóa kiến trúc.

Về bản chất, Regional NAT Gateway giải quyết một vấn đề vận hành thường gặp: việc phải nhân bản hạ tầng NAT theo từng AZ gây tốn kém thời gian cấu hình và làm phức tạp hệ thống route table. Với RNAT, đội ngũ hạ tầng chỉ cần quản lý một thực thể NAT Gateway duy nhất cho toàn VPC, giúp việc mở rộng quy mô ứng dụng sang nhiều AZ trở nên đơn giản và nhất quán hơn.

---

### Nguồn tham khảo

- [Introducing Amazon VPC Regional NAT Gateway – AWS Blog](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-amazon-vpc-regional-nat-gateway)
- [Amazon VPC NAT Gateway Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)

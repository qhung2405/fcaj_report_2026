---
title : "Blog 2"
date : "2026-07-27"
weight : 2
chapter : false
pre : " <b> 3.2. </b> "
---

# Nên tự quản lý bảo mật và mở rộng NAT Gateway thủ công, hay để RNAT tự động hóa?

Nếu bạn đang vận hành NAT Gateway theo cách truyền thống (zonal), rất có thể bạn đã quen với việc phải tự tay xử lý một loạt vấn đề đi kèm — và cách nào cũng khiến đội vận hành mất thêm công sức:

1. **Đặt NAT Gateway trong public subnet:**
   - Rủi ro bảo mật. Vì NAT Gateway bắt buộc phải nằm trong public subnet, các tổ chức có yêu cầu bảo mật cao luôn phải cẩn trọng để không vô tình triển khai tài nguyên nhạy cảm vào chung subnet đó.
2. **Tự quản lý cạn kiệt cổng (port exhaustion) và cấp IP thủ công:**
   - Khi lưu lượng tăng, bạn phải tự theo dõi số kết nối đồng thời và tự thêm Elastic IP khi gần chạm ngưỡng — dễ bị động nếu traffic tăng đột biến.
   - Việc tích hợp với VPC IPAM để cấp phát IP có kiểm soát cũng đòi hỏi cấu hình và theo dõi thủ công riêng.

---

## Bước ngoặt từ AWS: Regional NAT Gateway (RNAT) tự động hóa toàn bộ

Với RNAT, phần lớn những việc thủ công ở trên được AWS đảm nhận ở tầng hạ tầng, mang lại các lợi ích sau:

1. **Tăng cường bảo mật:**
   - Vì không cần public subnet để lưu trú NAT Gateway, các tổ chức có yêu cầu bảo mật cao có thể loại bỏ hoàn toàn nguy cơ vô tình triển khai tài nguyên nhạy cảm vào public subnet.
2. **Chống cạn kiệt cổng tự động:**
   - Mỗi địa chỉ IP gán cho RNAT hỗ trợ tối đa 55.000 kết nối đồng thời tới một đích duy nhất; khi gần đạt ngưỡng, RNAT tự động cấp thêm IP (tối đa 32 IP mỗi AZ) mà không cần can thiệp thủ công.
   - Việc mở rộng IP diễn ra khá linh hoạt: quá trình tăng thêm IP mất khoảng 5 phút và bắt đầu khi số kết nối vượt khoảng 40.000; ngược lại, khi số kết nối giảm xuống dưới 20.000 trong khoảng 1 giờ thì hệ thống mới thu hẹp lại — thiết kế theo hướng "mở rộng nhanh, thu hẹp chậm".
3. **Tích hợp sẵn với VPC IPAM, vẫn giữ quyền kiểm soát thủ công khi cần:**
   - RNAT có thể tự động lấy địa chỉ IP từ pool IPAM khi mở rộng sang AZ mới hoặc khi cần mở rộng do lưu lượng tăng, giúp việc cấp phát IP có kiểm soát và dễ dự đoán hơn.
   - Nếu muốn, người dùng vẫn có thể chọn chế độ manual để tự quản lý AZ và EIP thay vì để RNAT tự động hóa hoàn toàn.
4. **Giám sát và routing linh hoạt:**
   - RNAT phát ra các chỉ số (metrics) qua CloudWatch tương tự NAT Gateway zonal cho từng AZ, cùng các trường log bổ sung như resource-id, az-id để dễ dàng theo dõi.
   - Route table của RNAT cho phép chèn thêm AWS Network Firewall hoặc Gateway Load Balancer vào giữa private subnet và NAT Gateway để kiểm tra lưu lượng (traffic inspection) trước khi ra internet.


![Blog 2]({{< relURL "images/image2.png" >}})
---

### Nguồn tham khảo

- [Introducing Amazon VPC Regional NAT Gateway – AWS Blog](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-amazon-vpc-regional-nat-gateway)
- [Amazon VPC IP Address Manager (IPAM) Documentation](https://docs.aws.amazon.com/vpc/latest/ipam/how-it-works-ipam.html)
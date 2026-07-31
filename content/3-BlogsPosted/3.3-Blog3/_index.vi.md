---
title : "Blog 3"
date : "2026-07-27"
weight : 3
chapter : false
pre : " <b> 3.3. </b> "
---

# Nên để các service gọi trực tiếp lẫn nhau, hay chuyển sang kiến trúc hướng sự kiện với EventBridge?

Nếu hệ thống của bạn gồm nhiều service cần "biết" về sự kiện xảy ra ở nơi khác, từ trước đến nay thường chỉ có 2 cách tiếp cận — và cách nào cũng để lại gánh nặng vận hành:

1. **Gọi trực tiếp qua API giữa các service (tight coupling):**
   - Mỗi khi thêm một service mới cần nhận thông tin, bạn phải sửa lại logic gọi ở tất cả các nơi liên quan.
   - Nếu một service đích gặp sự cố hoặc phản hồi chậm, service gọi cũng bị ảnh hưởng theo, dễ gây hiệu ứng dây chuyền trong toàn hệ thống.
2. **Tự viết cron job hoặc script đồng bộ định kỳ:**
   - Giảm bớt sự phụ thuộc trực tiếp giữa các service...
   - Nhưng lại phải tự quản lý lịch chạy, dễ trùng lặp logic xử lý, và khó theo dõi toàn bộ luồng sự kiện của hệ thống khi số lượng service tăng lên.

---

## Bước ngoặt từ AWS: Amazon EventBridge

Để giải quyết bài toán này, AWS cung cấp Amazon EventBridge — dịch vụ serverless hoạt động ở cấp độ kiến trúc hướng sự kiện (event-driven), với các lợi ích:

1. **Với EventBridge bạn đã có thể:**
   - Tách rời hoàn toàn các service khỏi nhau: một service chỉ cần phát sự kiện, các service khác quan tâm sẽ tự đăng ký rule để nhận đúng loại sự kiện mình cần, không cần gọi trực tiếp lẫn nhau.
   - Thêm hoặc bớt một service trong hệ thống mà không ảnh hưởng tới các phần còn lại.
2. **EventBridge cung cấp hai cơ chế chính, mỗi cơ chế giải quyết một bài toán khác nhau:**
   - Event bus hoạt động như một bộ định tuyến trung tâm, nhận sự kiện từ nhiều nguồn (ứng dụng tự xây dựng, dịch vụ AWS, phần mềm bên thứ ba) và gửi đến nhiều đích khác nhau, có thể biến đổi (transform) dữ liệu trước khi gửi.
   - Pipes phù hợp cho tích hợp điểm-tới-điểm (point-to-point): mỗi pipe chỉ nhận sự kiện từ một nguồn duy nhất và gửi tới một đích duy nhất, nhưng hỗ trợ biến đổi và làm giàu (enrichment) dữ liệu ở mức nâng cao hơn.
   - Hai cơ chế này thường được dùng kết hợp: một pipe có thể nhận dữ liệu từ DynamoDB Stream rồi gửi vào event bus, sau đó event bus tiếp tục phân phối tới nhiều đích theo các rule đã cấu hình.
3. **Không còn cần tự viết cron job thủ công:**
   - EventBridge Scheduler là một trình lập lịch serverless cho phép tạo, chạy và quản lý tác vụ theo lịch (cron hoặc rate expression) hoặc chạy một lần, kèm khả năng cấu hình cửa sổ thời gian linh hoạt và giới hạn số lần thử lại — thay thế hoàn toàn cho việc tự quản lý cron job thủ công.

![Blog 3]({{< relURL "images/image3.png" >}})

<p style="font-size: 1rem; font-weight: normal;">
  <a href="https://www.facebook.com/share/p/18qszRmJAL/">Xem bài đăng trên AWS Study Group</a>
</p>

---

### Nguồn tham khảo

- [What Is Amazon EventBridge? – AWS Documentation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
- [Amazon EventBridge Event Buses – AWS Documentation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html)
- [Amazon EventBridge Pipes – AWS Documentation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html)
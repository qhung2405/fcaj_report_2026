---
title: "Event 1"
date: 2026-07-27
weight: 1
chapter: false
pre: " <b> 4.1. </b> "
---

# Bài thu hoạch: "AI Agentic Build Week"

### Mục Đích Của Sự Kiện

- Tạo sân khấu để các đội thắng giải hackathon trình bày sản phẩm AI-agentic mình đã xây dựng
- Chia sẻ kinh nghiệm thực tế về việc thiết kế và triển khai một giải pháp AI-agentic trên AWS trong thời gian rất gấp
- Giúp người tham dự tiếp cận nhiều bài toán, cách chọn kiến trúc và cách ước tính chi phí khác nhau cho hệ thống agentic
- Khuyến khích trao đổi kiến thức giữa các đội thi, mentor và khán giả

### Các đội trình bày

- **Đội 3KA – S.H.E.P.H.E.R.D.**: hệ thống giám sát đám đông và phát hiện nguy cơ tại sự kiện, kết hợp computer vision (YOLO + ByteTrack) với lớp agentic (Amazon SageMaker, Amazon Bedrock AgentCore, Strands Agent) và dashboard vận hành bằng React
- **Đội Plan V – SA Professional Native App**: trợ lý AI giúp Solution Architect chuyển yêu cầu ngôn ngữ tự nhiên thành bản nháp kiến trúc, sơ đồ AWS có thể chỉnh sửa, và ước tính chi phí AWS
- **Đội 9slide.vn – Signal Scout**: nền tảng phát hiện sớm các tín hiệu thay đổi chiến lược/tái cấu trúc của doanh nghiệp, xây dựng trên Amazon Bedrock, AgentCore, LangFuse và các công cụ theo dõi web như Apify/TinyFish

### Nội Dung Nổi Bật

#### Từ ý tưởng đến sản phẩm chạy được trong 24 giờ

Mỗi đội đều kể lại hành trình của mình: chọn track, lập nhóm, code liên tục 24 tiếng, rồi pitch trước ban giám khảo vào ngày demo. Các đội chia sẻ khá thẳng thắn về những khó khăn hậu trường — thức trắng đêm, debug đến sáng, và áp lực phải cho ra sản phẩm chạy được thật sự.

#### Thiết kế "lớp agentic" chứ không chỉ đơn thuần gọi model

Một điểm chung xuất hiện ở nhiều bài trình bày là việc tách riêng **agent giám sát/tự động** (liên tục theo dõi dữ liệu và chủ động cảnh báo) khỏi **copilot phục vụ người dùng** (trả lời câu hỏi bằng ngôn ngữ tự nhiên dựa trên dữ liệu thực tế). Mẫu thiết kế này xuất hiện cả ở hệ thống giám sát đám đông lẫn nền tảng phát hiện tín hiệu doanh nghiệp.

#### Kiến trúc và chi phí cũng là một phần của sản phẩm

Ngoài phần demo, các đội còn phải trình bày kiến trúc AWS thực tế và bảng chi phí (ví dụ: chi phí token Bedrock, AgentCore runtime, hosting, monitoring...). Có đội còn đưa ra thêm một phương án kiến trúc tối ưu chi phí hơn — cho thấy một sản phẩm "chạy được" và một sản phẩm "bền vững lâu dài" là hai chuyện khác nhau.

#### Công cụ có thể tăng tốc chính việc thiết kế kiến trúc

Một đội đã xây dựng một sản phẩm khá thú vị: trợ lý AI dành cho Solution Architect, có thể đọc yêu cầu, tự đề xuất phương án kiến trúc, và tự sinh sơ đồ AWS cùng ước tính chi phí — biến một công việc vốn mất vài ngày thành chỉ còn vài phút.

### Những Gì Học Được

#### Về team & quy trình làm việc

- Việc chuẩn bị kỹ (phạm vi rõ ràng, công cụ sẵn sàng, phân vai rõ, kịch bản demo được tập trước) mới thực sự giúp cả đội tập trung vào việc xây dựng sản phẩm, chứ không phải là "ăn gian".
- Một tính năng nhỏ nhưng hoàn thiện luôn tốt hơn một ý tưởng lớn nhưng dang dở, dù là khi chấm điểm hay trong công việc thực tế.

#### Về kỹ thuật

- Hệ thống AI-agentic hưởng lợi nhiều khi tách riêng trách nhiệm **giám sát/dự đoán** khỏi trách nhiệm **hội thoại/phục vụ người vận hành**.
- Việc ước tính chi phí và cân nhắc kiến trúc nên được tính đến ngay từ đầu, không phải là việc làm thêm sau cùng.
- Việc kết hợp computer vision, cloud inference và điều phối agentic hoàn toàn khả thi trong thời gian hackathon ngắn, miễn là giới hạn phạm vi hợp lý.

#### Về kỹ năng mềm

- Trình bày một sản phẩm kỹ thuật sao cho người không chuyên cũng hiểu được là một kỹ năng riêng, tách biệt với việc xây dựng sản phẩm đó.
- Những mối quan hệ và con người gặp được trong sự kiện có giá trị không kém gì kết quả cuộc thi.

### Ứng Dụng Vào Công Việc

- Cân nhắc áp dụng mô hình "agent giám sát + copilot" khi thiết kế các tính năng agentic cho project của mình
- Luôn kèm theo ước tính chi phí AWS sơ bộ mỗi khi đề xuất kiến trúc, thay vì chỉ nghĩ đến sau cùng
- Áp dụng bài học "giới hạn phạm vi nhỏ nhưng làm cho hoàn chỉnh" khi lên kế hoạch các mốc công việc của project
- Tìm hiểu thêm về AWS Bedrock AgentCore / Strands Agent như những thành phần nền tảng cho các tính năng dựa trên agent

### Trải nghiệm trong event

Tham gia **AI Agentic Build Week** giúp em thấy rõ cách các đội khác nhau cùng giải quyết một chủ đề lớn — AI-agentic trên AWS — nhưng theo những hướng sản phẩm rất khác nhau: từ an toàn đám đông, tình báo doanh nghiệp, đến công cụ hỗ trợ Solution Architect. Được nghe cả hành trình chứ không chỉ xem phần demo hoàn chỉnh giúp em cảm nhận rõ hơn nhiều những đánh đổi và công sức đằng sau mỗi sản phẩm, hơn là chỉ đọc mô tả.

#### Một số hình ảnh khi tham gia sự kiện
![Sự kiện AI Agentic Build Week]({{< relURL "images/event1.jpg" >}})

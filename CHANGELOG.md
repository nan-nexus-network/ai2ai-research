# Lịch Sử Phiên Bản (Changelog)

Tài liệu trong kho này được phiên bản theo [Semantic Versioning](https://semver.org/lang/vi/). Mỗi mục ghi theo thời gian UTC.

> **Lưu ý về phiên bản:** Phiên bản của *tài liệu* và của *mã nguồn* là **riêng biệt**. Tài liệu ở đây đi trước mã nguồn. Đó là chủ ý: tài liệu là đề xuất để phản biện, mã nguồn là thứ chứng minh.

## [Chưa phát hành]: Đang chuẩn bị v0.4.0

### Thêm
- Bộ dữ liệu `STANDARDS/` gồm 23 văn bản tiêu chuẩn và chính sách, ở định dạng CSV và JSON, mỗi dòng có trường `source_ref` truy vết về mục tham khảo.
- `PAPERS/ABSTRACT_EN.md`: tóm tắt tiếng Anh và 摘要中文.
- `MEDIA/ONE_PAGE_SUMMARY.md`: tóm tắt một trang cho báo chí.
- `scripts/validate_dataset.py` + workflow CI kiểm tra dữ liệu trên mọi lần push.
- Mẫu issue `citation_correction`: dành riêng cho việc chỉ ra lỗi trích dẫn.

### Đã biết
- Bộ dữ liệu chỉ gồm 23 văn bản đã được đối chiếu trong Phụ lục A của whitepaper. Chưa phải bản tra cứu đầy đủ của mọi tiêu chuẩn AI tồn tại trên thế giới.
- Bản dịch tiếng Anh và tiếng Trung là **bản tóm tắt**, không phải bản dịch đầy đủ. Khi có bản dịch chính thức, mục `PAPERS/` sẽ được bổ sung.

# Lịch Sử Phiên Bản (Changelog)

Tài liệu trong kho này được phiên bản theo [Semantic Versioning](https://semver.org/lang/vi/). Mỗi mục ghi theo thời gian UTC.

> **Lưu ý về phiên bản:** Phiên bản của *tài liệu* và của *mã nguồn* là **riêng biệt**. Tài liệu ở đây đi trước mã nguồn. Đó là chủ ý: tài liệu là đề xuất để phản biện, mã nguồn là thứ chứng minh.

## [Chưa phát hành]: Đang chuẩn bị v0.4.0

### Sửa (đợt rà soát dòng-by-dòng 22/10)

Sửa **17 lỗi** được phát hiện khi đọc từng dòng của `README.md`, `MEDIA/ONE_PAGE_SUMMARY.md`, `PAPERS/WHITEPAPER_VN_AI_BRIDGE.md`, `STANDARDS/standards.csv`, `PAPERS/ABSTRACT_EN.md` và `STANDARDS/standards.json`, cộng **1 lỗi phát hiện thêm** khi kiểm chứng lại.

- **Chính tả:** `Kết luốn`→`Kết luận` (README) · `dẫn dẫn`→`dẫn dắt` · `Đã đối chiểu`→`Đã đối chiếu` · `nghiin`→`nghin` · `Doi pha`→`Dot pha` · `thu manh`→`the manh` · `thu vien so`→`cong nghe thong tin, kinh te so` · `Tien deu`→`Tien de` · `khuc-vuc`→`khu-vuc` · `cong-boc`→`cong-bo` · `luat vuc`→`khu vuc` · chữ Hán `谦解`→`谅解` (JSON).
- **Câu lặp:** xoá câu *"NAN AI2AI cung cấp một sân chơi thực hành mở…"* bị lặp 2 lần liên tiếp trong whitepaper.
- **Mâu thuẫn nhà xuất bản:** báo cáo *Economic Impact Report* của Google do **Access Partnership** thực hiện, không phải NIC — sửa ở whitepaper lẫn bộ dữ liệu (`id` `NIC-GOOGLE-2024`→`ACCESS-GOOGLE-2024`).
- **Dịch sai cơ quan ban hành:** `Viện Hàn lâm Viễn thông`→`Cục Quản lý Không gian mạng Quốc gia Trung Quốc (CAC)` (đúng với `国家互联网信息办公室`).
- **Thuật ngữ GB/Z thống nhất:** GB/Z 185.1–185.7-2026 là **7 văn bản kỹ thuật chỉ dẫn chuẩn hoá quốc gia**, không phải "7 tiêu chuẩn quốc gia" theo nghĩa thông thường — sửa 6 chỗ để khớp đính chính đã có.
- **Claim lỗi thời (phát hiện thêm):** `ONE_PAGE_SUMMARY.md` và `ABSTRACT_EN.md` còn viết *"chữ ký Ed25519 chưa có"*, trong khi `v0.2` đã có biên nhận `nan-receipt/v1` **ký bởi bên thực thi** + cơ chế chống thực thi lặp tuần tự lẫn đồng thời. Đã cập nhật, **kèm giữ nguyên các hạn chế còn lại** (TOFU, chưa chống chối bỏ, chưa chống replay xuyên tiến trình, chưa có log minh bạch).
- **Khoảng trống 17 vs 23:** thêm ghi chú giải thích **17 mục đánh số + 6 văn bản dẫn chiếu trong thân bài = 23 dòng** của bộ dữ liệu; sửa "How to Cite" trỏ về kho `ai2ai-research` (bản dành cho báo chí và cơ quan) và bổ sung link kho research trong mục liên hệ.
- **Đồng bộ CSV ↔ JSON:** cả 23 dòng có cùng giá trị ở mọi trường; `source_ref` chuẩn hoá hoa chữ cái đầu.

### Bổ sung

- `validate_dataset.py` mở rộng: ngoài kiểm tra chéo `source_ref` với danh mục tham khảo, nay còn **kiểm tra số lượng văn bản nêu trong văn xu** phải khớp số dòng thật; allowlist `jurisdiction` sửa lỗi gõ `khuc-vuc`→`khu-vuc`.

### Thêm
- Bộ dữ liệu `STANDARDS/` gồm 23 văn bản tiêu chuẩn và chính sách, ở định dạng CSV và JSON, mỗi dòng có trường `source_ref` truy vết về mục tham khảo.
- `PAPERS/ABSTRACT_EN.md`: tóm tắt tiếng Anh và 摘要中文.
- `MEDIA/ONE_PAGE_SUMMARY.md`: tóm tắt một trang cho báo chí.
- `scripts/validate_dataset.py` + workflow CI kiểm tra dữ liệu trên mọi lần push.
- Mẫu issue `citation_correction`: dành riêng cho việc chỉ ra lỗi trích dẫn.

### Đã biết
- Bộ dữ liệu chỉ gồm 23 văn bản đã được đối chiếu trong Phụ lục A của whitepaper. Chưa phải bản tra cứu đầy đủ của mọi tiêu chuẩn AI tồn tại trên thế giới.
- Bản dịch tiếng Anh và tiếng Trung là **bản tóm tắt**, không phải bản dịch đầy đủ. Khi có bản dịch chính thức, mục `PAPERS/` sẽ được bổ sung.

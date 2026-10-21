# AI2AI Research: Tài liệu thảo luận mở về tầng giao thức liên vận AI

**Kho này dành cho: nhà báo, cơ quan nhà nước, và nhà nghiên cứu chính sách.** Nó chứa tài liệu thảo luận, bộ dữ liệu so sánh các tiêu chuẩn AI liên vận toàn cầu, và cách trích dẫn đúng.

> **Mã nguồn chạy được nằm ở kho khác:** [`nan-nexus-network/ai2ai-core`](https://github.com/nan-nexus-network/ai2ai-core): chạy demo trong 60 giây, 0 dependency.

---

## 1. Câu hỏi tài liệu này trả lời

> *"Nếu một quốc gia không đua xây siêu mô hình tỷ đô, liệu quốc gia đó có thể đóng vai trò nào có giá trị thực chất và bền vững trong chuỗi giá trị AI toàn cầu?"*

Câu trả lời được đề xuất: thử nghiệm vai trò **"Cầu nối Tham Chiếu AI" (AI Reference Bridge)**: một tầng dịch thuật trung lập giữa các hệ sinh thái AI đang phân mảnh.

## 2. Ba kết luận chính

**Kết luận 1: Khoảng trống là thật, và nó do chính các văn bản chính thức thừa nhận.**
MCP (Anthropic) giải quyết tốt bài toán AI kết nối công cụ. A2A (Google) định hình giao tiếp tác tử-tác tử. Nhưng A2A vẫn mang dấu ấn kiến trúc của một hệ sinh thái. Tài liệu của Trung Quốc tự nêu rằng MCP và A2A chưa đủ và cần chuẩn mới. Ba rào cản khi hai bên thuộc hệ sinh thái khác nhau giao dịch: khác cấu trúc gói tin và quản lý phiên; thiếu cơ chế dịch và kiểm tra quy tắc tuân thủ xuyên biên giới; thiếu biên nhận xác thực trung lập khi hai bên tranh chấp.

**Kết luận 2: Việt Nam có bốn thế mạnh, nhưng chúng không tồn tại độc lập.**
Dân số trẻ và làn sóng phát triển AI; thị trường xuất khẩu đa dạng; Tuyên bố Hà Nội về Hợp tác Số và định hướng "Connected Intelligence"; và các cam kết song phương, đa phương về AI. Khi được kết nối bởi một tầng giao thức mở, chúng tạo thành một chỉnh thể có sức mạnh cộng hưởng.

**Kết luốn 3: Chúng tôi đề xuất, không tuyên ngôn.**
Tài liệu này kết thúc bằng **mười hai câu hỏi mở** dành cho cộng đồng và chuyên gia thảo luận, và một **tiêu chí dừng lại**: nếu sau 12 tháng mà đề xuất này không được cộng đồng đón nhận hoặc chứng minh được giá trị thực tiễn, chúng tôi sẽ công khai dừng dự án để không lãng phí nguồn lực xã hội.

## 3. Trong kho này có gì

| Đường dẫn | Nội dung | Dành cho |
|:---|:---|:---|
| [`PAPERS/WHITEPAPER_VN_AI_BRIDGE.md`](PAPERS/WHITEPAPER_VN_AI_BRIDGE.md) | Tài liệu thảo luận đầy đủ (7 chương + phụ lục đối chiếu chính sách quốc tế) | Người đọc có thời gian |
| [`PAPERS/ABSTRACT_EN.md`](PAPERS/ABSTRACT_EN.md) | Tóm tắt tiếng Anh + 摘要中文, một trang | Báo chí quốc tế, đối tác tiếng Trung |
| [`STANDARDS/standards.csv`](STANDARDS/standards.csv) · [`.json`](STANDARDS/standards.json) | **Bộ dữ liệu so sánh 22 văn bản tiêu chuẩn/chính sách**, máy đọc được | Phân tích dữ liệu, báo cáo, công cụ |
| [`MEDIA/ONE_PAGE_SUMMARY.md`](MEDIA/ONE_PAGE_SUMMARY.md) | Tóm tắt một trang, sẵn sàng dùng | Báo chí, thư ngỏ |
| [`CHANGELOG.md`](CHANGELOG.md) | Lịch sử phiên bản tài liệu | Theo dõi |

**Bộ dữ liệu `STANDARDS/` là phần đặc thù.** Nó gom 22 văn bản (tiêu chuẩn kết nối tác tử, quy định quản trị AI, hiệp định thương mại, tuyên bố chính sách) vào một bảng có trường máy đọc được: ai ban hành, thẩm quyền nào, năm nào, lĩnh vực, trạng thái hiệu lực, và **vì sao nó liên quan đến khoảng trống liên vận**. Mỗi dòng đều có trường `source_ref` trỏ về mục tham khảo trong whitepaper, nên **mọi khẳng định đều truy vết được**.

## 4. Cách trích dẫn

```
NAN AI2AI-SI2SI (2026). Việt Nam như cầu nối trong nền kinh tế AI2AI:
Tài liệu thảo luận mở (v0.4-draft). GitHub:
https://github.com/nan-nexus-network/ai2ai-research
Giấy phép: CC BY 4.0
```

Cũng có [`CITATION.cff`](CITATION.cff) cho các công cụ trích dẫn tự động (Zotero, GitHub).

## 5. Cam kết

- **Không xin tiền, không gọi vốn, không phát hành token, không bán khóa học.**
- **Không đại diện cho cộng đồng AI Việt Nam.** Đây là một thử nghiệm độc lập ở quy mô nhỏ.
- **Đây là PoC.** Tài liệu này là luận điểm để phản biện, không phải kết luận đã kiểm chứng. Xem `ai2ai-core` để biết giới hạn kỹ thuật cụ thể.
- **Mọi trích dẫn pháp lý trong tài liệu đều có ngày và số hiệu** và được đối chiếu với bản gốc. Nếu bạn tìm thấy chỗ sai, hãy [mở issue](https://github.com/nan-nexus-network/ai2ai-research/issues/new/choose). Đó là lý do tài liệu này tồn tại.
- **Tài liệu này được biên tập với sự hỗ trợ của công cụ trí tuệ nhân tạo.** Việc dùng AI không làm thay đổi tính đúng của các luận điểm, và mọi trích dẫn đều phải tự kiểm chứng.

## 6. Liên hệ

- **Câu hỏi về tài liệu, phản biện, góp ý:** mở issue tại [ai2ai-research](https://github.com/nan-nexus-network/ai2ai-research/issues/new/choose)
- **Câu hỏi về mã nguồn:** mở issue tại [ai2ai-core](https://github.com/nan-nexus-network/ai2ai-core/issues/new/choose)
- **Báo cáo lỗ hổng bảo mật:** xem [SECURITY.md](https://github.com/nan-nexus-network/ai2ai-core/blob/main/SECURITY.md). Không mở issue công khai
- **Email:** `nan_ai2ai@proton.me`

---

## English summary

This repository holds the **open discussion paper** and a **machine-readable dataset of 22 international AI interoperability and AI-governance instruments**, for journalists, government agencies, and policy researchers.

**The question:** if a country does not compete to build billion-dollar foundation models, what role could it play that is genuinely valuable and sustainable in the global AI value chain? The proposed answer to test: a **neutral reference bridge layer** between fragmented AI ecosystems.

**Three findings.** (1) The gap is real and acknowledged in official documents themselves: MCP and A2A are not sufficient on their own, and three specific barriers block cross-ecosystem agent transactions. (2) Vietnam has four concrete advantages, but they are not independent. (3) This is a proposal for discussion, not a manifesto: the paper ends with twelve open questions and a published stopping criterion.

**Repository layout:** `PAPERS/` full paper (Vietnamese) and one-page abstract (English, Chinese); `STANDARDS/` the 22-instrument dataset in CSV and JSON, every row traceable to a numbered source; `MEDIA/` one-page summary; `CHANGELOG.md` version history.

**Commitments:** no funding sought, no token issued, no course sold; this does not represent the Vietnamese AI community; this is a proof of concept, and the paper is an argument to be challenged, not a verified conclusion; every legal citation carries a date and document number, and if you find an error, please open an issue.

Licence: **CC BY 4.0** (texts) · code in `ai2ai-core` is **Apache 2.0**.

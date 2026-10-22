# Tóm tắt một trang: NAN AI2AI

*Dành cho báo chí, thư ngỏ, và trao đổi với cơ quan. Bản đầy đủ: [`PAPERS/`](../PAPERS/). Bản tiếng Anh: [`ABSTRACT_EN.md`](../PAPERS/ABSTRACT_EN.md).*

---

## Dự án là gì

**NAN AI2AI-SI2SI** là một **khung tham chiếu mở** (Open Reference Framework) đang ở giai đoạn **PoC**, nhằm thử nghiệm giả thuyết: một lớp bằng chứng kỹ thuật **trung lập** có thể kết nối các hệ sinh thái AI đang phân mảnh, và trong đó Việt Nam có thể thử đóng vai trò trung lập.

## Câu hỏi

> *Nếu một quốc gia không đua xây siêu mô hình tỷ đô, liệu có thể đóng vai trò nào có giá trị thực chất và bền vững trong chuỗi giá trị AI toàn cầu?*

## Ba điều cần biết

**1. Khoảng trống là thật.** MCP kết nối AI với công cụ. A2A định hình giao tiếp tác tử-tác tử. Nhưng A2A vẫn mang dấu ấn kiến trúc của Google, và tài liệu chính thức của Trung Quốc (bộ văn bản kỹ thuật chỉ dẫn chuẩn hóa quốc gia GB/Z 185.1–185.7-2026 về kết nối tác tử AI) nói rõ MCP và A2A **chưa đủ**. Ba rào cản khi hai hệ sinh thái giao dịch: khác cấu trúc gói tin, thiếu cơ chế dịch và kiểm tra tuân thủ xuyên biên giới, thiếu biên nhận xác thực trung lập khi tranh chấp.

**2. Việt Nam có bốn thế mạnh, nhưng chúng không độc lập.** Dân số trẻ và làn sóng AI; thị trường xuất khẩu đa dạng; Tuyên bố Hà Nội về Hợp tác Số và định hướng "Connected Intelligence" (01/2026); các cam kết song phương và đa phương về AI. Kết nối bằng một tầng giao thức mở, chúng trở thành một chỉnh thể cộng hưởng.

**3. Đây là đề xuất, không phải tuyên ngôn.** Tài liệu kết thúc bằng **mười hai câu hỏi mở** và một **tiêu chí dừng lại**: nếu sau 12 tháng đề xuất này không được cộng đồng đón nhận hoặc chứng minh được giá trị thực tiễn, chúng tôi sẽ **công khai dừng dự án**.

## Ranh giới kỹ thuật (nói thẳng)

- Đây là **PoC cục bộ**, một tiến trình, dùng dữ liệu mô phỏng. **Không** dùng được trong production.
- Bộ lọc chuỗi tĩnh trong PoC **không phải** biện pháp bảo mật.
- Biên nhận SHA-256 trong bản PoC chỉ chứng minh **toàn vẹn dữ liệu**, **không** xác thực danh tính hay chống chối bỏ. *Cập nhật v0.2:* kho `ai2ai-core` đã có thêm biên nhận `nan-receipt/v1` **ký bằng Ed25519 bởi chính bên thực thi** (mỗi lần chạy đều kiểm chứng bằng vector chính thức RFC 8032), kèm cơ chế chống thực thi lặp cả tuần tự lẫn đồng thời. **Nhưng vẫn còn hạn chế lớn:** neo tin cậy hiện là TOFU (ghim khoá lần đầu), **chưa** có bằng chứng chống chối bỏ, **chưa** có chống replay xuyên tiến trình, **chưa** có log minh bạch công khai. Xem [ADR-002](https://github.com/nan-nexus-network/ai2ai-core/blob/main/docs/ADR_002_SIGNED_RECEIPT_AND_TRUST_MODEL.md) và [ADR-003](https://github.com/nan-nexus-network/ai2ai-core/blob/main/docs/ADR_003_ATOMIC_IN_FLIGHT_CLAIM.md)。
- **Chúng tôi không tuyên bố** đã xây dựng được một tiêu chuẩn quốc tế. Chúng tôi đề xuất một **lớp trung lập** và mời cộng đồng phản biện.

## Kèm theo

| | |
|:---|:---|
| **Tài liệu đầy đủ** | [`PAPERS/WHITEPAPER_VN_AI_BRIDGE.md`](../PAPERS/WHITEPAPER_VN_AI_BRIDGE.md): 7 chương + phụ lục đối chiếu chính sách quốc tế |
| **Tóm tắt EN / 中文** | [`PAPERS/ABSTRACT_EN.md`](../PAPERS/ABSTRACT_EN.md) |
| **Bộ dữ liệu 23 văn bản** | [`STANDARDS/`](https://github.com/nan-nexus-network/ai2ai-research/tree/main/STANDARDS): CSV + JSON, mỗi dòng truy vết được |
| **Mã nguồn chạy được** | [`ai2ai-core`](https://github.com/nan-nexus-network/ai2ai-core): demo 60 giây, 0 dependency |
| **Trang chủ 3 ngôn ngữ** | <https://nan-ai2ai.nexusasianetwork.workers.dev> |

## Cam kết

**Không xin tiền. Không gọi vốn. Không phát hành token. Không bán khóa học.** Không đại diện cho cộng đồng AI Việt Nam. Mọi mã nguồn đã mở theo Apache 2.0 sẽ **không bao giờ** bị rút lại.

## Liên hệ

`nan_ai2ai@proton.me` · [mở issue để phản biện](https://github.com/nan-nexus-network/ai2ai-research/issues/new/choose)

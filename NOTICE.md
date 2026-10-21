# NOTICE: Quan hệ giữa kho này và `ai2ai-core`

Kho `ai2ai-research` và kho `ai2ai-core` là **hai mặt của một sáng kiến**, tách theo đối tượng và theo giấy phép.

| | `ai2ai-research` (kho này) | `ai2ai-core` |
|:---|:---|:---|
| **Nội dung** | Tài liệu thảo luận, bộ dữ liệu chuẩn, tóm tắt báo chí | Mã nguồn PoC, kiểm thử, CI, trang chủ 3 ngôn ngữ |
| **Đối tượng** | Nhà báo, cơ quan nhà nước, nhà nghiên cứu chính sách | Kỹ sư, lập trình viên, người phản biện kỹ thuật |
| **Giấy phép** | CC BY 4.0 | Apache 2.0 (mã nguồn) + CC BY 4.0 (tài liệu) |
| **Trạng thái** | v0.4-draft | v0.1 (PoC) |

## Quan hệ nội bộ

- Tài liệu trong `PAPERS/` là **bản trích từ** `docs/WHITEPAPER_VN_AI_BRIDGE.md` của `ai2ai-core` (cùng một v0.4-draft, cùng nguồn trích dẫn).
- **Khi nội dung lệch nhau, `ai2ai-core` là bản quyết định**, vì đó là nơi mã nguồn và bộ kiểm thử cùng tồn tại.
- Mọi văn bản pháp lý và số liệu trong kho này **trỏ về bản gốc đã kiểm chứng** ở `ai2ai-core`. Không có phát biểu nào ở đây không có nguồn.

## Quy trình kiểm định trước khi công bố

Kho này được dựng theo đúng cổng kiểm định đã áp dụng cho `ai2ai-core`:

1. Quét PII, tài liệu nội bộ, secret và đường dẫn máy trên **toàn bộ lịch sử Git** (không chỉ cây hiện tại).
2. Kiểm tra blob trong toàn bộ object database, kể cả blob không còn reachable.
3. Chuẩn hoá danh tính tác giả về `NAN AI2AI <nan_ai2ai@proton.me>`.
4. Xác minh **tree hash** không đổi, tức nội dung file trước và sau khi chuẩn hoá là giống hệt.
5. Chạy `scripts/validate_dataset.py` trong CI trên mọi lần push.

### Vì sao CI không tự kiểm tra tên người thật

`scripts/validate_dataset.py` là **file công khai**. Nếu ta viết thẳng tên của
người thật vào danh sách cấm, ta sẽ **tự làm lộ chính dữ liệu cần bảo vệ**.
Vì vậy scanner công khai chỉ kiểm tra những thứ **có thể viết công khai mà vẫn
có tác dụng**: đường dẫn máy, tên tài liệu nội bộ, và định dạng secret.

Việc kiểm tra **ở mức tên người / tên pháp nhân** chạy cục bộ với một file
denylist **riêng tư, không commit**:

```bash
python scripts/validate_dataset.py --denylist /path/rieng/denylist.txt
```

File denylist chỉ ghi mỗi dòng một chuỗi cấm. Cơ chế này giữ cho CI công khai
sạch trong khi vẫn cho phép kiểm tra sâu trước mỗi lần phát hành.

Chi tiết phương pháp: [`ai2ai-core/PROCESS.md`](https://github.com/nan-nexus-network/ai2ai-core/blob/main/PROCESS.md).

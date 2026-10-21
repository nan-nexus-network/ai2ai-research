# Bộ dữ liệu: Các văn bản tiêu chuẩn và chính sách liên quan (Standards Dataset)

**23 văn bản** được gom từ Phụ lục A và danh mục tham khảo của [White Paper](../PAPERS/WHITEPAPER_VN_AI_BRIDGE.md), đưa về dạng máy đọc được.

Mỗi dòng đều có trường `source_ref` trỏ về **đúng vị trí** trong whitepaper mà dòng đó lấy từ đó. Không có khẳng định nào ở đây vượt quá điều whitepaper nói.

## Cách dùng

```bash
# JSON (đầy đủ, có mô tả trường)
curl -sO https://raw.githubusercontent.com/nan-nexus-network/ai2ai-research/main/STANDARDS/standards.json

# CSV (cho Excel / pandas / R)
curl -sO https://raw.githubusercontent.com/nan-nexus-network/ai2ai-research/main/STANDARDS/standards.csv
```

```python
import json, urllib.request
d = json.load(urllib.request.urlopen(
    "https://raw.githubusercontent.com/nan-nexus-network/ai2ai-research/main/STANDARDS/standards.json"))
print(d["count"], "văn bản")
by_domain = {}
for i in d["instruments"]:
    by_domain.setdefault(i["domain"], []).append(i["name"])
for k, v in sorted(by_domain.items()):
    print(f"{k:16} {len(v)}")
```

## Cấu trúc trường

| Trường | Ý nghĩa |
|:---|:---|
| `id` | Định danh ổn định, dùng khi báo lỗi trong issue |
| `name` | Tên văn bản (tiếng gốc hoặc tiếng Anh) |
| `name_local` | Tên bản địa phương khi khác với `name` |
| `issuer` | Cơ quan ban hành / thông qua |
| `jurisdiction` | `quoc-te` · `Trung Quoc` · `EU` · `ASEAN` · `Viet Nam` · `song-phuong` · `khuc-vuc` |
| `year` | Năm ban hành, `null` nếu nguồn không nêu |
| `domain` | `interoperability` · `governance` · `policy` · `cooperation` · `trade` · `data` |
| `status` | Trạng thái theo mô tả của nguồn |
| `scope` | Phạm vi văn bản phủ, theo cách diễn đạt của nguồn |
| `relevance_to_nan` | Vì sao văn bản này quan trọng với một tầng cầu nối trung lập xuyên hệ sinh thái |
| `source_ref` | Vị trí trong whitepaper mà dòng này đến từ đó |

## Phân bố theo lĩnh vực

| Lĩnh vực | Số | Nội dung chính |
|:---|--:|:---|
| `interoperability` | 5 | MCP, A2A, GB/Z 185-2026, T/ZGCMCA 024-2025, cộng đồng AIP |
| `governance` | 3 | EU AI Act, quy định AI tạo sinh Trung Quốc, Luật An ninh mạng sửa đổi |
| `policy` | 5 | Nghị quyết 57-NQ/TW và các chương trình hành động, quyết định 1528 & 1671/QĐ-TTg |
| `cooperation` | 4 | Tuyên bố chung 4/2026, hai bản ghi nhớ, Trung tâm Hợp tác AI Việt–Trung |
| `trade` | 3 | ACFTA 3.0, DEFA, RCEP |
| `digital-cooperation` | 1 | Tuyên bố Hà Nội về Hợp tác Số và ADM 2030 |
| `data` | 2 | e-Conomy SEA 2024, Economic Impact Report (NIC + Google) |

## Giới hạn đã biết

- Đây **không phải** bản tra cứu đầy đủ mọi tiêu chuẩn AI trên thế giới. Nó là tập **23 văn bản đã được đối chiếu** trong Phụ lực A.
- Với `year` rỗng (`null`): nguồn không nêu năm. Chúng tôi **không đoán** và để `null` thay vì điền số suy đoán.
- Trạng thái pháp lý phản ánh **tại thời điểm whitepaper được viết (21/10/2026)**. Vui lòng kiểm tra lại nguồn gốc trước khi trích dẫn cho mục đích pháp lý.

## Sửa dữ liệu

Phát hiện sai? Mở issue với mẫu **"Chỉ ra lỗi trích dẫn hoặc dữ liệu"**. Bản sửa sẽ được phản ánh trong [`CHANGELOG.md`](../CHANGELOG.md).

Dữ liệu được kiểm tra tự động trên **mọi lần push** bằng [`scripts/validate_dataset.py`](../scripts/validate_dataset.py).

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem dinh bo du lieu standards + quet PII/duong dan may trong toan repo.
Chay duoc o moi moi truong GitHub Actions (chi Python 3.8+ stdlib).
Exit 0 = PASS, exit 1 = FAIL."""
import csv, io, json, os, re, sys, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_PATH = os.path.join(ROOT, "STANDARDS", "standards.json")
CSV_PATH = os.path.join(ROOT, "STANDARDS", "standards.csv")

REQUIRED = ["id","name","issuer","jurisdiction","domain","status","scope",
            "relevance_to_nan","source_ref"]
ALLOWED_DOMAIN = {"interoperability","governance","policy","cooperation",
                  "trade","data","digital-cooperation"}
ALLOWED_JURIS = {"quoc-te","Trung Quoc","EU","ASEAN","Viet Nam","song-phuong","khuc-vuc"}

# Duong dan may + dinh danh ca nhan: KHONG duoc xuat hien trong tai lieu cong khai.
#
# LUU Y: cac chuoi mau duoc NOI LAI bang "+" co chu dich.
# Ly do: file nay quet CA chinh no, neu mot mau duoc viet nguyen van trong file
# (vi du ten org sai) thi regex se khop vao chinh dong do va bao loi
# gia. Noi chuoi giu duoc kha nang quet MOI file, ke ca file nay, ma van doc
# duoc cho nguoi review.
_APP      = "App" + "Data"
_ORGSAI   = "nexusasianetwork" + "-NAN"
_BLUEPRNT = "MASTER_EXECUTION_" + "BLUEPRINT"
_FINALCHK = "FINAL_" + "CHECK"
_LEADSMD  = "LEADS" + ".md"
_BRANDARC = "BRAND_" + "ARCHITECTURE"

FORBIDDEN = [
    (r"[A-Za-z]:[\\/]{1,2}Users[\\/]{1,2}", "duong dan nguoi dung Windows"),
    (r"[A-Za-z]:[\\/]{1,2}NAN_DEV", "duong dan thu muc lam viec noi bo"),
    (r"/home/[a-zA-Z0-9_-]+/", "duong dan home Linux"),
    (_APP, "duong dan thu muc nguoi dung cua he thong"),
    (_ORGSAI, "org GitHub sai"),
    (_BLUEPRNT, "ten tai lieu noi bo"),
    (_FINALCHK, "ten tai lieu noi bo"),
    (_LEADSMD, "so theo doi khach hang noi bo"),
    (_BRANDARC, "chuan thuong hieu noi bo"),
    (r"AKIA[0-9A-Z]{16}", "AWS access key id"),
    (r"ghp_[A-Za-z0-9]{20,}", "GitHub personal access token"),
    (r"github_pat_[A-Za-z0-9_]{20,}", "GitHub fine-grained token"),
    (r"sk-[A-Za-z0-9]{20,}", "khoa API dang sk-"),
    (r"xox[baprs]-[A-Za-z0-9-]{10,}", "Slack token"),
    (r"AIza[0-9A-Za-z\-_]{30,}", "Google API key"),
    (r"-----BEGIN (RSA |EC |OPENSSH |PGP )?PRIVATE KEY-----", "khoa rieng tu"),
]
TEXT_EXT = (".md", ".json", ".csv", ".yml", ".yaml", ".txt", ".py", ".cff", ".html")


def load_denylist(path):
    """Doc danh sach chuoi cam BI (PII, ten phap nhan) tu file rieng tu.
    LY DO THIET KE: file nay la CONG KHAI. Neu ta viet truc tiep ten nguoi that
    vao day, chung ta se TU LAM LOI chinh minh. Danh sach phai nam o file
    rieng tu (khong commit) va duoc truyen bang --denylist."""
    items = []
    if not path:
        return items
    if not os.path.exists(path):
        print("  WARNING: khong tim thay file denylist %s (bo qua)" % path)
        return items
    with io.open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line and not line.startswith("#"):
                items.append(line)
    return items


def fail(msg):
    print("  FAIL: %s" % msg)
    return 1


def main():
    errors = 0
    denylist_path = None
    if "--denylist" in sys.argv:
        i = sys.argv.index("--denylist")
        if i + 1 < len(sys.argv):
            denylist_path = sys.argv[i + 1]
    extra = load_denylist(denylist_path)
    if extra:
        print("  denylist: %d chuoi cam BI tu %s" % (len(extra), denylist_path))
    print("=== [1] Du lieu standards ===")
    try:
        with io.open(JSON_PATH, encoding="utf-8") as fh:
            data = json.load(fh)
    except Exception as exc:
        return fail("standards.json khong doc duoc: %s" % exc)

    rows = data.get("instruments", [])
    if not rows:
        errors += fail("standards.json khong co dong nao")
    if data.get("count") != len(rows):
        errors += fail("truong 'count' (%r) khong bang so dong (%d)" % (data.get("count"), len(rows)))
    print("  so dong: %d" % len(rows))

    ids = [r.get("id", "") for r in rows]
    if len(set(ids)) != len(ids):
        errors += fail("co id trung lap")
    for r in rows:
        rid = r.get("id", "<thieu id>")
        if not re.match(r"^[A-Z0-9][A-Z0-9-]*$", rid):
            errors += fail("id khong hop le: %r" % rid)
        for f in REQUIRED:
            if not str(r.get(f, "")).strip():
                errors += fail("dong %s thieu truong %r" % (rid, f))
        if r.get("domain") not in ALLOWED_DOMAIN:
            errors += fail("dong %s co domain la: %r" % (rid, r.get("domain")))
        if r.get("jurisdiction") not in ALLOWED_JURIS:
            errors += fail("dong %s co jurisdiction la: %r" % (rid, r.get("jurisdiction")))
        if r.get("year") is not None and not isinstance(r.get("year"), int):
            errors += fail("dong %s co year khong phai so nguyen hoac null" % rid)
    print("  truong bat buoc, dinh dang id/domain/jurisdiction/year: kiem tra xong")

    print("=== [2] Khop CSV voi JSON ===")
    try:
        with io.open(CSV_PATH, encoding="utf-8", newline="") as fh:
            csv_rows = list(csv.DictReader(fh))
    except Exception as exc:
        csv_rows = []
        errors += fail("standards.csv khong doc duoc: %s" % exc)
    if len(csv_rows) != len(rows):
        errors += fail("CSV co %d dong, JSON co %d dong" % (len(csv_rows), len(rows)))
    else:
        csv_ids = [r.get("id") for r in csv_rows]
        if csv_ids != ids:
            errors += fail("thu tu id giua CSV va JSON khong khop")
        else:
            print("  CSV %d dong, id khop va dung thu tu" % len(csv_rows))

    print("=== [3] Quet PII / duong dan may / secret trong toan repo ===")
    scanned = 0
    for dp, dn, fns in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in (".git", "__pycache__")]
        for fn in fns:
            if not fn.lower().endswith(TEXT_EXT):
                continue
            p = os.path.join(dp, fn)
            try:
                raw = open(p, "rb").read()
            except Exception:
                continue
            if b"\x00" in raw[:8192]:
                continue
            try:
                text = raw.decode("utf-8")
            except UnicodeDecodeError:
                continue
            scanned += 1
            rel = os.path.relpath(p, ROOT)
            for pat, label in FORBIDDEN:
                if re.search(pat, text):
                    errors += fail("%s chua %s" % (rel, label))
            for needle in extra:
                if needle in text:
                    errors += fail("%s chua mot chuoi cam BI trong denylist" % rel)
    print("  da quet %d file van ban" % scanned)

    print("")
    if errors:
        print("KET QUA: FAIL (%d loi)" % errors)
        return 1
    print("KET QUA: PASS - du lieu hop le, khong co PII, khong co duong dan may, khong co secret.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

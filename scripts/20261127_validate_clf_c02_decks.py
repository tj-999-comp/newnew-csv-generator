import csv
from pathlib import Path


EXPECTED = {
    "clf_c02_deck1_cloud_concepts.csv": 25,
    "clf_c02_deck2_shared_responsibility_iam_governance.csv": 25,
    "clf_c02_deck3_security_audit_compliance.csv": 25,
    "clf_c02_deck4_compute_storage.csv": 25,
    "clf_c02_deck5_database_network.csv": 20,
    "clf_c02_deck6_analytics_integration_ai_operations.csv": 20,
    "clf_c02_deck7_billing_pricing_support.csv": 20,
}


deck_dir = Path(__file__).resolve().parents[1] / "decks"
total = 0
for filename, expected_count in EXPECTED.items():
    path = deck_dir / filename
    raw = path.read_bytes()
    assert not raw.startswith(b"\xef\xbb\xbf"), f"BOM detected: {path}"
    assert b"\r" not in raw, f"Non-LF newline detected: {path}"
    text = raw.decode("utf-8")
    assert all(line.startswith('"') and line.endswith('"') for line in text.splitlines()), f"Unquoted line: {path}"
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle))
    assert rows[0] == ["問題", "解答", "解説"], f"Bad header: {path}"
    assert len(rows) - 1 == expected_count, f"Bad count: {path}"
    for line_number, row in enumerate(rows[1:], start=2):
        assert len(row) == 3, f"Bad column count: {path}:{line_number}"
        assert row[0].strip() and row[1].strip(), f"Blank required field: {path}:{line_number}"
        assert "\n" not in row[0] + row[1] + row[2], f"Embedded newline: {path}:{line_number}"
        assert "※" in row[2], f"Missing trap note: {path}:{line_number}"
    total += expected_count
    print(f"OK: {expected_count}問 ({path})")

assert total == 160, f"Bad total: {total}"
print(f"OK: 合計{total}問、全7デッキを正常に検証しました")

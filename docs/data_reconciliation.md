# Dataset Reconciliation — Actual CSVs vs Draft Chapter 3 (Table 2)

This note documents discrepancies between the dataset descriptions in the project
draft (Chapter 3, Table 2 / §3.3) and the **actual CSV files** shipped in
`Datasets/`. Per the supervisor's note (`Datasets/IMPORTANT NOTICE/The Concern.txt`),
the data is **kept as-is**; this document is the basis for correcting the draft text.

All facts below were verified directly from the CSV headers and row counts.

## Summary table

| DS | Draft Table 2 says | Actual CSV | Verdict |
|----|--------------------|-----------|---------|
| **D1** | Mendeley; raw first 1024 bytes (0–255); 1023 ransomware (25 families) + 1134 benign = 2157 | `Ransomware_headers.csv`: 1024 byte cols `0..1023` + `ID,filename,GR,family`; **2157 rows**; `GR` 1=1023 / 0=1134 | ✅ **Matches** |
| **D2** | "Raw sequential byte frequencies"; **1024 features**; ~1000+1000 (~2000); source **Manavi & Hamzeh (2021)** | `pe_headers.csv`: **127 byte cols `0..126`**; target `GR`; **6978 rows** (benign 3226 / mal 3752); folder source = **Oriola Kolawole** | ❌ **Mismatch**: feature count (127≠1024), sample count (~6978≠~2000), and source attribution |
| **D3** | "Engineered structural heuristics incl. SizeOfCode, SectionAlignment, **Shannon entropy**"; ~50–100 features; **binary** | `PE_Header.csv`: **52 parsed PE-header fields** + `SHA256` + `Type`; **29807 rows**; `Type` is **multiclass 0–6**; **no entropy column** | ❌ **Mismatch**: no entropy/engineered heuristics; multiclass (collapsed to binary in code); far larger N |
| **D4** | "Extracted **API/IAT** features: num_libraries, num_functions, ADVAPI32.dll…"; ~200–500 features; **balanced 2000** | `Malware-Benign.csv`: **78 parsed PE / optional-header / section-directory fields** + `Hash_md5_Name` + `Malware`; **19611 rows**; **imbalanced** (mal 14599 / benign 5012) | ❌ **Mismatch**: not API/IAT features; not balanced; far larger N |

## Additional findings

1. **D3 ≡ IMPORTANT NOTICE file.** `Datasets/IMPORTANT NOTICE/PE_Header.csv` is
   **byte-identical** to Dataset 3 (`md5 = 5b72fc4f7d04d9b5d6f891fd117da91d`). The
   "usability-10 Kaggle dataset" the student flagged is already present as D3.

2. **D3 and D4 share the same parsed PE-header schema** (`e_magic, e_cblp, …,
   ImageBase, …`). They are structurally very similar, which weakens the thesis's
   "four **structurally independent** datasets" claim. D1/D2 (raw bytes) remain
   distinct from D3/D4 (parsed fields).

3. **Scope vs. labels.** The title says *ransomware*, but D3's `Type` families
   (RedLineStealer, Downloader, RAT, BankingTrojan, SnakeKeyLogger, Spyware) and
   D4's `Malware` flag are **general malware, not ransomware**. Only **D1** (and
   D2) are genuine ransomware-vs-goodware. Project framing adopted:
   **malware-inclusive** — D1/D2 tagged `task=ransomware`, D3/D4 tagged
   `task=malware` in `config.py`; claims are scoped accordingly.

## Recommended draft corrections (Chapter 3, Table 2)

- **D2**: change "1024 raw byte features / ~2000 samples / Manavi & Hamzeh" →
  "127 raw byte-frequency features / 6,978 samples / Oriola Kolawole".
- **D3**: change "engineered structural heuristics incl. Shannon entropy / binary"
  → "52 parsed PE-header fields / 29,807 samples / originally multiclass (7 malware
  families incl. benign), collapsed to binary malware-vs-benign".
- **D4**: change "API/IAT-derived features / balanced 2000" → "78 parsed PE /
  optional-header / section-directory fields / 19,611 samples / imbalanced
  (74% malware)".
- Reframe the "structurally independent" claim as **two structural families** (raw
  bytes: D1/D2; parsed fields: D3/D4) rather than four fully independent sets.

_No data files were modified or replaced; this reconciliation is documentation only._
